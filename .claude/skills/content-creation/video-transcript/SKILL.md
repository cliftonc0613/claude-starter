---
name: video-transcript
description: Pulls a full text transcript from a YouTube URL, a Vimeo URL, or a local video/audio file. Use this whenever the user shares a video link or file path and wants the transcript, wants to know "what does this video say", wants to quote or summarize a video's spoken content, or wants to repurpose a video into an article/blog/social post. Triggers on requests like "get the transcript of this YouTube video", "what's said in this Vimeo clip", "pull the captions from this video", "transcribe this mp4/mov file", or "turn this video into a written article." Handles both platforms that have existing captions (fast) and videos that don't (falls back to local Whisper transcription).
---

# Video Transcript

Extracts a timestamped transcript from a YouTube URL, Vimeo URL, or local video/audio file
(mp4, mov, mp3, wav, m4a, etc.).

## Why this approach

Fetching the platform's own captions is dramatically faster and cheaper than transcribing audio
from scratch — most YouTube videos, and many Vimeo ones, already have auto-generated or
uploaded captions available. So the bundled script always tries captions first for URLs, and
only falls back to running Whisper locally (which reads the actual audio) when no captions
exist, or when the input is already a local file with no caption track to speak of.

## Requirements

- `ffmpeg` and `whisper` (openai-whisper) must be installed for the audio-transcription fallback
  and for any local file. Check with `which ffmpeg whisper`. If missing, install via
  `brew install ffmpeg openai-whisper` (macOS) and let the user know if brew isn't available.
- `yt-dlp` is needed for URLs (captions and audio download). The script auto-installs it via
  Homebrew if it's missing — no need to check for it yourself.

## How to run it

Call the bundled script with the URL or file path:

```bash
bash scripts/get_transcript.sh "<youtube-or-vimeo-url-or-file-path>" [output_dir] [whisper_model]
```

- `output_dir` defaults to the current directory — pass a real path (e.g. a scratchpad or the
  user's project folder) so output files land somewhere sensible. Each video gets its own
  subfolder inside `output_dir`, named after the video's slugified title, containing both output
  files — this keeps multiple transcripts from colliding or getting mixed up when processing
  several videos into the same output_dir.
- `whisper_model` defaults to `base`. Use `small` or `medium` when the user wants higher
  accuracy and is willing to wait longer; `base` is a good default for most spoken-word content
  (interviews, talks, game recaps). Only reach for `large` if the audio is noisy or heavily
  accented and `base`/`small` produced garbled output.

The script prints its progress to stderr (so you can see whether it found captions or fell back
to Whisper) and on success prints two lines at the end:

```
PLAIN:/path/to/output.txt
TIMESTAMPED:/path/to/output.timestamped.txt
```

Read the timestamped file if the user wants time references (e.g. "what do they say around the
5 minute mark"), or the plain file if they just want the flowing text (e.g. to summarize or feed
into an article draft).

## Handling multiple videos

If the user gives several URLs/files at once, run the script once per input — don't try to batch
them into a single call. Report back which ones used captions vs. Whisper, since Whisper runs
are much slower (roughly real-time to a few minutes per video depending on model size and
length), so the user isn't surprised by the wait on a long video.

## What can go wrong

- **Age-restricted, private, or region-locked videos**: yt-dlp will fail to download. Tell the
  user what happened rather than retrying blindly — some of these need cookies/login, which is
  out of scope for this skill unless the user provides them.
- **Non-English audio**: Whisper auto-detects language by default, which works well for most
  content. If the user wants a specific source language or a translated-to-English transcript,
  edit the whisper invocation to add `--language <code>` or `--task translate`.
- **Very long videos** (2+ hours): Whisper transcription can take a while even on `base`. Let the
  user know this before kicking it off if no captions were found, so they can decide whether to
  wait or try a smaller model.
