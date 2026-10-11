---
name: jev-chatgpt-visibility
description: Use when checking whether ChatGPT mentions or recommends a brand, measuring AI search visibility across buyer questions, finding which competitors ChatGPT sends people to, or finding AI answers a business should be in. Also use when someone wants Jev (TypeSafe's decision model) to read or classify ChatGPT answers.
---

# Jev ChatGPT visibility

## Overview

This skill fetches real ChatGPT answers for a list of buyer questions (DataForSEO's ChatGPT scraper, $0.004 per answer) and has **Jev** read every one. Jev is TypeSafe AI's decision model: it never writes text, it only picks from options you give it and returns probabilities. For each answer it decides:

- how the brand is treated: recommended, listed with others, only a source link, or not mentioned
- which business or website the reader gets sent to first (it can only pick names that appear in the answer)
- what kind of answer it is: local businesses, websites, specific offers, or general advice
- whether a business like this one would be a natural thing to recommend there

Plain Python does everything that needs no judgement, like the text search for the domain. That search is also the trust check: Jev's "mentioned or not" should match it on nearly every answer. The output is one HTML report.

## Before the first run

**Project keys:** In this repo the keys already live in the project-root `.env`. The scripts don't read that file, so load it into the environment first by running `set -a; source .env; set +a` from the repo root, then the script. Don't copy the keys elsewhere.

1. **Python packages.** Run `python -c "import requests"`. If it fails, run `pip install -r <this skill>/requirements.txt`.
2. **Keys.** It needs `OPENROUTER_API_KEY`, `DATAFORSEO_USERNAME` and `DATAFORSEO_PASSWORD`. It checks the environment, then `./jev-chatgpt/<domain>/.env`, then `~/.config/jev-seo/.env`, then `~/.config/jev-internal-links/.env`. If any key is missing, ask the user for it (openrouter.ai/keys, and the DataForSEO API login from https://app.dataforseo.com/?aff=182182) and save it to `~/.config/jev-seo/.env` with `chmod 600`. Never print a key.
3. **Brand and description.** Ask for the brand name as people write it, and one line on what the business is and who it serves. That line goes into every Jev question, so make it specific (for example "a property portal for the Aysén region of Chilean Patagonia", not "a real estate company").
4. **Prompts.** If the user has no prompts file, write 20 to 40 realistic buyer questions with them and save them to `prompts.txt`:
   - Seed them from the site's top Search Console queries when those are available, rewritten as questions a person would type into ChatGPT.
   - Mix "who should I use" questions (where a recommendation is possible) with a few general advice questions.
   - Group them by language and market with header lines. The location must be a DataForSEO location name:

     ```
     # es | Chile
     mejor corredora de propiedades en Coyhaique

     # en | United States
     best website to find property for sale in Chilean Patagonia
     ```

   **Show the list to the user and confirm it before running**, since each new prompt costs money.

## Run it

```bash
python <this skill>/scripts/run.py example.com --brand "Example Co" --about "one line on what the business is" --prompts prompts.txt
```

- Output goes to `./jev-chatgpt/<domain>/`. The report is `out/chatgpt-answers.html` and opens when the run finishes (`--no-open` to skip).
- It prints a cost estimate first and stops if it is over `--max-cost` (default $1). 40 prompts cost about $0.17.
- Prompts without a header use `--lang` (default `en`) and `--location` (default `United States`).
- ChatGPT answers and Jev answers are both cached, so a re-run with the same prompts costs nothing. Delete `data/ai_raw/` to fetch fresh answers.

## After the run

Give the user:
- mentioned in X of N answers, recommended in Y
- the top 3 "sent to first" names
- 3 to 5 answers from the gaps section, where they aren't mentioned but should plausibly be
- the trust check number (Jev versus the text search)
- the report path

## Calling Jev directly

Jev is **not** on the chat completions endpoint.

```
POST https://openrouter.ai/api/alpha/decisions
Authorization: Bearer $OPENROUTER_API_KEY
{"model": "~typesafe/jev-latest",
 "state": "<short plain-text context>",
 "questions": {
   "pick": {"type": "choice", "instructions": "...", "criteria": {"1": "...", "none": "..."}},
   "fits": {"type": "noul", "instructions": "<statement to rate true/false>"}}}
```

A choice returns `{choice, probabilities, confidence}` and a noul returns `{noul}`, a 0 to 1 probability. Set `JEV_MODEL=typesafe/jev-1.13` to pin a version when runs must be comparable.

## Common mistakes

- **Treating one run as the truth.** ChatGPT answers change from run to run and by location. Re-fetch before quoting a number, and compare runs, not single answers.
- **Leaning on the "you'd fit here" score.** In testing it came back high for almost every answer, so it barely separates good gaps from bad ones. Use it as a filter, not a ranking.
- **Presenting confidence as calibrated.** It is Jev's own estimate.
- **Putting numbers or long exports into the state.** Jev is weak at arithmetic and dates. Keep the state to one answer and do all counting in Python.
- **Running it on client data without checking TypeSafe's terms.** Jev's API terms are still early-access.
