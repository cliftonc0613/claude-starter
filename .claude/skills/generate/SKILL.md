---
name: generate
description: Generate images and videos via the Kie AI jobs API with cost-safe routing. Use whenever the user says /generate, generate image, generate video, create image, create a thumbnail, hero image, animate this, make a clip, or asks for any AI media generation for a client or project — even without naming a model. Also use when the user asks to open, show, or view the gallery, gallery wall, generations wall, or their generated images — that request just rebuilds and opens the gallery page, no generation. Routes image jobs to Nano Banana 2 (cheap draft-first) and video jobs to Kling 3.0 (quote cost and get approval before running). Saves every output flat into knowledge/generations/ with a JSON sidecar log.
---

# /generate

One command for AI media. Route the request, prep references, generate via the bundled script, log the result, refresh the gallery.

## Models

| Task | Default model | Recipe |
|---|---|---|
| Image (default / drafts) | `nano-banana-2` on Kie AI | `models/nano-banana-2.md` |
| Image (quality / fine ratios) | `nano-banana-pro` on Kie AI | `models/nano-banana-2.md` (constraints table covers both) |
| Video (default) | Kling 3.0 on Kie AI | `models/kling-3-0.md` |

Read the recipe file before every generation — it holds the exact request shape and gotchas. Kie AI is the only wired provider today; when a model isn't on Kie or a call fails hard, say so plainly and ask before trying anything else (fal.ai / WaveSpeed may be added later).

## The pipeline

1. **Route** — image or video? Draft or final? Pick the model from the table and read its recipe.
2. **Prep refs** — logos, faces, product shots, and style references live in `knowledge/generations/refs/`. Never describe a logo or a face in prompt text; a described logo comes back wrong every time. Pass the real file. If the user's request clearly needs a reference that isn't in `refs/`, stop and ask for the file before spending credits.
3. **Generate** — use `scripts/kie_task.py` (submit → wait split; see below). Run multiple generations one at a time to avoid rate limits.
4. **Log + gallery** — the script writes a sidecar `.json` beside every file automatically. After a batch finishes, run `scripts/build_gallery.py --open` to refresh the gallery wall and open it in the browser so the user sees the new work immediately.

## Output

- Every file saves FLAT into: `/Users/cliftoncanady/web-apps/_starter/knowledge/generations/`
- No subfolders — subfolders break the gallery and every future tool that reads the library. References are the one exception and live in `knowledge/generations/refs/`.
- Naming: `{project}_{description}_{timestamp}.{ext}` — the script handles this via `--name {project}_{description}`.

## Cost rules

These exist because video is the expensive lane (roughly $0.20–0.35/second — a 10s clip is $2–3.50) while draft images cost about a cent.

- **Quote before video.** Before any paid video run, state model, duration, resolution, and estimated dollars, then wait for an explicit go. Quoting alone is not approval. One approval = one run — a second take needs a second yes.
- **Draft cheap, finish pretty.** Iterate on `nano-banana-2` at 1K/2K. Only when the user picks a favourite, rerun that one prompt at 4K or on `nano-banana-pro`. Never burn quality-tier credits on throwaway drafts.
- **Real refs, never described** (see step 2 above).
- If the API returns 402 (insufficient credits), tell the user to top up at kie.ai — do not retry.

## Running the script

The Kie jobs API is async: `createTask` returns in seconds, but rendering takes 30s–several minutes. A single Bash call polling to completion gets killed by the 2-minute default timeout, so the script splits into resumable subcommands. Always use `python3`.

```bash
# 1. Submit (< 5s). Prints JSON with taskId.
python3 scripts/kie_task.py submit \
  --model nano-banana-2 \
  --input '{"prompt": "…", "aspect_ratio": "16:9", "resolution": "2K"}' \
  --name clientname_herodraft

# 2. Wait — invoke with Bash timeout: 600000. Polls, downloads, writes sidecar, exits 0.
python3 scripts/kie_task.py wait <taskId>
```

Exit code `3` from `wait` means "still generating, resumable" — call `wait <taskId>` again; no extra credits are spent. `status <taskId>` gives a quick non-downloading poll; `fetch <taskId>` recovers a finished task whose download was interrupted (result URLs expire in ~24h, so fetch promptly).

Local reference images must be uploaded to a public URL first — pass them with `--ref /path/to/file.png` (repeatable) and the script uploads via Kie's file endpoint and injects the URLs into `input.image_input`.

The API key is read from `KIE_API_KEY` in the environment or a `.env` file (repo root or `~/.kie/.env`). Never paste keys into code or logs.

## Sidecar log

Written automatically by the script beside every download, same basename + `.json`:

```json
{
  "model": "nano-banana-2",
  "prompt": "the full prompt sent to the API",
  "refs": ["refs/logo.png"],
  "params": {"aspect_ratio": "16:9", "resolution": "2K"},
  "created": "2026-08-01T12:00:00Z"
}
```

Same basename plus `.json` is the contract — that's how anyone recovers "what prompt made THIS?" three weeks later. Don't skip it, don't rename one without the other.

## Gallery wall

```bash
python3 scripts/build_gallery.py --open
```

Scans `knowledge/generations/` and rewrites `knowledge/generations/gallery.html` — a single-file masonry wall (newest first, hover-play videos, click-to-lightbox). Run it with `--open` as the last step of every generation batch — rebuild once per batch, not per file, so multi-image runs open the gallery a single time at the end. Omit `--open` only if the user asks not to have it pop up.

When the user just asks to **open/show the gallery** ("open the gallery wall", "show me my generations"), run this same command and nothing else — always rebuild before opening (it's instant) so the wall reflects any files added or deleted since last time.

## Adding a model later

One markdown file in `models/` per model: id, endpoint, request shape, sync/async, cost, gotchas (copy an existing recipe as the template). Then add a row to the Models table above. If a call ever returns "model not found", the id changed upstream — copy it fresh from kie.ai's model page into the recipe. That's the only maintenance this system needs.
