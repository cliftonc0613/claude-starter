#!/usr/bin/env python3
"""Is ChatGPT recommending you? One command.

  python run.py example.com --brand "Example Co" --about "what the business is" --prompts prompts.txt

1. DataForSEO's ChatGPT scraper fetches a real ChatGPT answer for every prompt
   ($0.004 each). Raw answers are cached, so re-runs don't pay again.
2. Python does the checks that need no judgement: is your domain in the answer
   or its links, and which names did the answer mention.
3. Jev reads each answer: how are you treated, who does the reader get sent to
   first, what kind of answer is it, and should a business like yours be in it.
4. Plain rules turn Jev's probabilities into the report.

Output: ./jev-chatgpt/<domain>/out/chatgpt-answers.html (one file, no server)
"""
import argparse
import collections
import json
import os
import re
import statistics
import sys
import time
import webbrowser
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse

import requests

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from _env import load_keys, jev_model  # noqa: E402
from jev import Jev, stats  # noqa: E402

SCRAPER = "https://api.dataforseo.com/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced"
SCRAPER_COST = 0.004
JEV_COST = 0.0001

# ── the rulebook ──────────────────────────────────────────────
SHOULD_WIN = 0.85         # an answer we should plausibly be in

LANGS = {"en": "English", "es": "Spanish", "pt": "Portuguese", "fr": "French", "de": "German",
         "it": "Italian", "nl": "Dutch", "sv": "Swedish", "da": "Danish", "no": "Norwegian",
         "fi": "Finnish", "pl": "Polish", "ja": "Japanese"}


def bare(domain):
    d = domain.strip().lower()
    d = re.sub(r"^https?://", "", d).split("/")[0]
    return d.replace("www.", "")


def read_prompts(path, lang, location):
    """One prompt per line. '# es | Chile' starts a group (language | location)."""
    out, cur = [], (lang, location)
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            parts = [p.strip() for p in line.lstrip("#").split("|")]
            if len(parts) == 2 and parts[0] and parts[1]:
                cur = (parts[0].lower(), parts[1])
            continue
        out.append((line, cur[0], cur[1]))
    return out


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:80]


def raw_file(raw, prompt, lang, loc):
    return raw / f"{slug(prompt)}-{lang}-{slug(loc)}.json"


def fetch(job, raw):
    prompt, lang, loc = job
    f = raw_file(raw, prompt, lang, loc)
    if f.exists():
        return json.loads(f.read_text())
    body = {}
    for attempt in range(5):
        try:
            r = requests.post(SCRAPER, timeout=300,
                              auth=(os.environ["DATAFORSEO_USERNAME"], os.environ["DATAFORSEO_PASSWORD"]),
                              json=[{"keyword": prompt, "location_name": loc, "language_code": lang}])
            body = r.json()
        except Exception as e:
            body = {"status_message": str(e)[:200]}
        if body.get("tasks"):
            break
        print(f"  retry: {prompt[:40]} ({body.get('status_message')})")
        time.sleep(5 * (attempt + 1))
    t = (body.get("tasks") or [{}])[0]
    res = (t.get("result") or [{}])[0]
    d = {"prompt": prompt, "location": loc, "lang": lang, "cost": t.get("cost") or 0,
         "status": t.get("status_message"), "markdown": res.get("markdown") or "",
         "sources": res.get("sources") or [], "brand_entities": res.get("brand_entities") or []}
    if d["markdown"]:
        f.write_text(json.dumps(d, ensure_ascii=False, indent=1))
    return d


def domain(u):
    return urlparse(u or "").netloc.replace("www.", "")


def names_in(d):
    """Names the answer itself surfaced. Jev can only pick from a list we give it."""
    names = []
    for b in d["brand_entities"]:
        n = b.get("title") or b.get("name") or ""
        if n and n not in names:
            names.append(n)
    for s in d["sources"]:
        dm = domain(s.get("url"))
        if dm and dm not in names and "chatgpt" not in dm:
            names.append(dm)
    return names[:14]


def clean(md):
    md = re.sub(r"\(https?://[^)]+\)", "", md)      # drop link targets, keep link text
    return re.sub(r"\n{3,}", "\n\n", md).strip()


def build_state(d, brand, site, about):
    return "\n".join([
        f"WE ARE: {brand} ({site}), {about}",
        "", f'A USER ASKED CHATGPT: "{d["prompt"]}"', "",
        "CHATGPT ANSWERED:", clean(d["markdown"])[:4000], "",
        "SOURCES CHATGPT LINKED: " + ", ".join(sorted({domain(s.get("url")) for s in d["sources"]} - {""}))[:600],
    ])


def build_questions(names, brand, site, about):
    opts = {str(n): nm[:100] for n, nm in enumerate(names, 1)}
    opts["none"] = "The answer does not steer the reader to any specific business or website"
    return {
        "first_pick": {"type": "choice", "criteria": opts, "instructions":
                       "Which business or website does this answer steer the reader to first?"},
        "our_treatment": {"type": "choice", "instructions":
                          f"How does this answer treat {brand} ({site})?",
                          "criteria": {
                              "recommended": "Named as a good place to go, with endorsement",
                              "listed": "Named among other options, without endorsement",
                              "source_only": "Only used as a background source link",
                              "absent": "Not mentioned at all",
                          }},
        "answer_type": {"type": "choice", "instructions": "What kind of answer is this?",
                        "criteria": {
                            "agencies": "A list of local businesses or service providers",
                            "portals": "A list of websites, tools or platforms",
                            "listings": "Specific products, properties or offers",
                            "advice": "General advice or information, no businesses to choose",
                        }},
        "should_win": {"type": "noul", "instructions":
                       f"A business like this ({about}) would be a natural, genuinely useful "
                       "thing to recommend in this answer."},
    }


def short_brand(n):
    n = n.split("|")[0].strip()
    return re.sub(r"^www\.", "", n)


def place(loc):
    return ("the " + loc) if loc.startswith(("United", "Netherlands", "Philippines", "Czech")) else loc


def group_label(lang, loc):
    return f"{LANGS.get(lang, lang)}, asked from {place(loc)}"


def build_report(items, meta, out_dir):
    data_items = []
    for i in items:
        j = i["jev"]
        fp = j["first_pick"]["choice"]
        pick = "none" if fp == "none" else short_brand(i["names"][int(fp) - 1])
        probs = sorted(((short_brand(i["names"][int(k) - 1]) if k != "none" else "No one", v)
                        for k, v in j["first_pick"]["probabilities"].items()), key=lambda x: -x[1])
        data_items.append({
            "prompt": i["prompt"], "lang": i["lang"], "group": f"{i['lang']}|{i['location']}",
            "pick": pick, "pickConf": j["first_pick"]["confidence"], "pickProbs": probs[:4],
            "treat": j["our_treatment"]["choice"], "treatConf": j["our_treatment"]["confidence"],
            "type": j["answer_type"]["choice"], "win": j["should_win"]["noul"],
            "exact": i["we_appear_exact"], "ms": i["jev_ms"] or 0,
            "answer": i["answer"][:2400],
            "sources": sorted({s["domain"] for s in i["sources"] if s["domain"]})[:10],
        })
    groups = list(dict.fromkeys(r["group"] for r in data_items))
    counts = collections.Counter(r["group"] for r in data_items)
    glist = [[g, group_label(*g.split("|", 1))] for g in groups]
    parts = [f"{counts[g]} in {LANGS.get(g.split('|')[0], g.split('|')[0])} from {place(g.split('|', 1)[1])}"
             for g in groups]
    gtext = parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + " and " + parts[-1]

    picks = collections.Counter(r["pick"] for r in data_items if r["pick"] != "none")
    opp = [r for r in data_items if r["treat"] == "absent" and r["win"] >= SHOULD_WIN and r["type"] != "advice"]
    agree = sum((r["treat"] != "absent") == r["exact"] for r in data_items)
    n = len(data_items)
    payload = {"items": data_items, "picks": picks.most_common(8), "groups": glist,
               "opps": sorted(opp, key=lambda r: -r["win"]),
               "root": meta["site"].split(".")[0], "brand": meta["brand"],
               "rules": {"win": SHOULD_WIN}}
    appear = sum(r["treat"] != "absent" for r in data_items)
    rec = sum(r["treat"] == "recommended" for r in data_items)

    html = (HERE / "dashboard_template.html").read_text()
    fills = {"title": "ChatGPT Visibility Check", "domain": meta["site"], "model": meta["model"],
             "n": n, "appear": appear, "rec": rec, "groupsText": gtext, "brand": meta["brand"],
             "root": payload["root"], "oppN": len(opp), "winThr": f"{int(SHOULD_WIN * 100)}%",
             "agree": agree, "scraper": f"{meta['scraper_cost']:.2f}", "cost": f"{meta['jev_cost']:.4f}",
             "p50": int(statistics.median(r["ms"] for r in data_items)) if n else 0,
             "data": json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")}
    for k, v in fills.items():          # data goes last so its text is never re-scanned
        html = html.replace("[[" + k + "]]", str(v))
    out = out_dir / "chatgpt-answers.html"
    out.write_text(html)
    return out, {"answers": n, "mentioned": appear, "recommended": rec, "agree": agree,
                 "gaps": len(opp), "top_picks": picks.most_common(3)}


def main():
    ap = argparse.ArgumentParser(description="How does ChatGPT treat your brand? Read by Jev.")
    ap.add_argument("domain")
    ap.add_argument("--brand", required=True, help="Your business name as people write it")
    ap.add_argument("--about", required=True, help="One line: what the business is and who it serves")
    ap.add_argument("--prompts", required=True, help="Text file, one prompt per line")
    ap.add_argument("--lang", default="en", help="Default language code for prompts without a header")
    ap.add_argument("--location", default="United States", help="Default DataForSEO location_name")
    ap.add_argument("--max-cost", type=float, default=1.0)
    ap.add_argument("--no-open", action="store_true")
    args = ap.parse_args()

    site = bare(args.domain)
    work = Path.cwd() / "jev-chatgpt" / site
    raw, data, out = work / "data/ai_raw", work / "data", work / "out"
    for p in (raw, out):
        p.mkdir(parents=True, exist_ok=True)

    missing = load_keys(work)
    if missing:
        sys.exit("Missing keys: " + ", ".join(missing) +
                 ". Put them in ~/.config/jev-seo/.env (see README).")

    jobs = read_prompts(args.prompts, args.lang.lower(), args.location)
    if not jobs:
        sys.exit("No prompts found in " + args.prompts)
    new = sum(not raw_file(raw, *j).exists() for j in jobs)
    est = new * SCRAPER_COST + len(jobs) * JEV_COST
    print(f"{len(jobs)} prompts ({len(jobs) - new} already fetched). Estimated cost: ${est:.2f}")
    if est > args.max_cost:
        sys.exit(f"Estimate is over --max-cost ${args.max_cost:.2f}. Raise it to continue.")

    with ThreadPoolExecutor(3) as ex:
        answers = list(ex.map(lambda j: fetch(j, raw), jobs))
    ok = [a for a in answers if a["markdown"]]
    scraper_cost = sum(a.get("cost") or 0 for a in answers)
    print(f"{len(ok)}/{len(answers)} ChatGPT answers fetched")
    for a in answers:
        if not a["markdown"]:
            print(f"  no answer: {a['prompt']} ({a.get('status')})")

    model = jev_model()
    jev = Jev(model, work / "cache")

    def judge(a):
        names = names_in(a)
        return names, jev.decide(build_state(a, args.brand, site, args.about),
                                 build_questions(names, args.brand, site, args.about))

    with ThreadPoolExecutor(10) as ex:
        res = list(ex.map(judge, ok))
    root = site.split(".")[0]
    items = []
    for a, (names, r) in zip(ok, res):
        text = (a["markdown"] + " " + " ".join(s.get("url", "") for s in a["sources"])).lower()
        if not r.get("answers"):
            print(f"  Jev error on: {a['prompt']} ({r.get('error')})")
            continue
        items.append({
            "prompt": a["prompt"], "lang": a["lang"], "location": a["location"],
            "answer": a["markdown"], "names": names,
            "sources": [{"domain": domain(s.get("url")), "url": s.get("url"),
                         "title": s.get("title")} for s in a["sources"]],
            "we_appear_exact": root in text,       # Python: string match, no judgement
            "jev": r["answers"], "jev_ms": r.get("_ms"), "jev_usage": r.get("usage"),
        })
    (data / "ai_answers.json").write_text(json.dumps(
        {"model": model, "stats": stats, "scraper_cost": scraper_cost, "items": items},
        indent=1, ensure_ascii=False))

    report, summary = build_report(items, {"site": site, "brand": args.brand, "model": model,
                                           "scraper_cost": scraper_cost, "jev_cost": stats["cost"]}, out)
    print(f"\nJev: {stats['calls']} new calls, {stats['cached']} from cache, ${stats['cost']:.4f}")
    print(f"ChatGPT answers: ${scraper_cost:.3f} (cached answers count at their original fetch cost)")
    print(json.dumps(summary, ensure_ascii=False))
    print(f"Report: {report}")
    if not args.no_open:
        webbrowser.open(report.as_uri())


if __name__ == "__main__":
    main()
