# Kling 3.0 (video)

The sensible video default: good motion, fair price. Text-to-video and image-to-video (start frame).

| Field | Value |
|---|---|
| Model ID | `kling-3.0/video` — if the API says "model not found", the id changed upstream; copy it fresh from kie.ai's Kling page and update this file |
| Provider | Kie AI |
| Method | Async — submit then poll. Renders take several minutes; always use the resumable `wait` |
| Type | Video |
| API key | `.env` → `KIE_API_KEY` (Bearer auth) |
| Docs | https://kie.ai — Kling model page |
| Cost | roughly $0.20–0.35 per second. `std` = 720p, `pro` = 1080p. 3–15 second clips. A 10s clip ≈ $2–3.50 |

**Cost gate applies.** Before submitting, quote model, mode (std/pro), duration, and estimated dollars, and wait for an explicit go. One approval = one run.

## Endpoint

```
POST https://api.kie.ai/api/v1/jobs/createTask
Authorization: Bearer {KIE_API_KEY}
```

## Request format

```json
{
  "model": "kling-3.0/video",
  "input": {
    "prompt": "the full motion prompt",
    "image_input": ["https://public-url-of-start-frame.jpg"],
    "aspect_ratio": "16:9",
    "mode": "std",
    "duration": 5
  }
}
```

Field names for mode/duration follow Kie's Kling docs — if a 422 validation error comes back, open the model's page on kie.ai and check the current input schema before retrying (Kie occasionally renames input fields between Kling versions).

## Response handling

Same jobs API as images: `createTask` → `data.taskId`, poll `recordInfo` every 10–15s until `state` is `success`/`fail`, parse `resultJson` (a string) for `resultUrls`, download immediately (~24h expiry). The bundled `kie_task.py` handles all of this including the resumable poll.

## Notes

- Prefer image-to-video when a strong still already exists in the generations folder — motion from a good start frame beats text-only prompts.
- `std` 720p is fine for social; only quote `pro` 1080p when the user asks for hero-quality.
- Renders regularly exceed one `wait` window — exit code 3 is normal, just re-run `wait <taskId>`.
