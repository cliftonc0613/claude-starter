# Nano Banana 2 / Nano Banana Pro (images)

Everyday image generation. Cheap, fast, strong with reference images. Default to `nano-banana-2` for drafts; use `nano-banana-pro` when the user needs fine-grained ratios (`4:5`, `2:3`) or PNG-by-default finals.

| Field | Value |
|---|---|
| Model ID | `nano-banana-2` (drafts) · `nano-banana-pro` (quality) |
| Provider | Kie AI |
| Method | Async — submit then poll (usually done in 30–90s) |
| Type | Image |
| API key | `.env` → `KIE_API_KEY` (Bearer auth) |
| Docs | https://kie.ai — Nano Banana model page |
| Cost | roughly $0.01–0.03 per draft image; a few cents more at 4K |

## Endpoint

```
POST https://api.kie.ai/api/v1/jobs/createTask
Authorization: Bearer {KIE_API_KEY}
```

## Request format

```json
{
  "model": "nano-banana-2",
  "input": {
    "prompt": "the full prompt",
    "image_input": ["https://public-url-of-reference.jpg"],
    "aspect_ratio": "16:9",
    "resolution": "2K",
    "output_format": "png"
  }
}
```

### Per-model constraints

| Field | `nano-banana-pro` | `nano-banana-2` |
|---|---|---|
| Prompt max | 10,000 chars | 20,000 chars |
| Reference images | up to 8 | up to 14 |
| Aspect ratios | `1:1` `2:3` `3:2` `3:4` `4:3` `4:5` `5:4` `9:16` `16:9` `21:9` `auto` | `1:1` `16:9` `9:16` `4:3` `3:4` `21:9` `auto` |
| Resolution | `1K` `2K` `4K` | `1K` `2K` `4K` |
| Default format | `png` | `jpg` |

`image_input` items must be **publicly fetchable URLs** — the generation service pulls them. The bundled `kie_task.py --ref` flag uploads local files for you via Kie's file endpoint.

## Response handling

`createTask` returns `data.taskId`. Poll `GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=…` until `data.state` is `success` or `fail`. On success, `data.resultJson` is a **JSON string** (parse it) containing `resultUrls` — download immediately, URLs expire in ~24h.

## Notes

- State machine: `waiting` → `queuing` → `generating` → `success`/`fail`. Ignore `progress` (only populated for sora models).
- `failCode` 501 = moderation — reframe the prompt, don't auto-retry. 500 = transient — one retry is fine.
- Draft at 1K/2K to save credits; reserve 4K for the user's picked favourite.
