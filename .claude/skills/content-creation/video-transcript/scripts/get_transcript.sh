#!/usr/bin/env bash
# get_transcript.sh — pull a timestamped transcript from a YouTube/Vimeo URL or a local video/audio file.
#
# Usage:
#   get_transcript.sh <url-or-file-path> [output_dir] [whisper_model]
#
# Strategy:
#   1. If input is a URL: try to fetch existing captions/subtitles via yt-dlp first (fast, free).
#   2. If no captions exist (or input is a local file): download/extract audio and run local
#      Whisper to transcribe it.
#
# Requires: yt-dlp, ffmpeg, whisper (openai-whisper). Installs yt-dlp via Homebrew if missing.
#
# Output: writes <slug>.txt (plain text) and <slug>.timestamped.txt (timestamped segments)
# to output_dir (default: current directory), and prints the paths at the end.

set -euo pipefail

INPUT="${1:?Usage: get_transcript.sh <url-or-file-path> [output_dir] [whisper_model]}"
OUTPUT_DIR="${2:-.}"
WHISPER_MODEL="${3:-base}"

mkdir -p "$OUTPUT_DIR"

is_url() {
  case "$1" in
    http://*|https://*) return 0 ;;
    *) return 1 ;;
  esac
}

ensure_yt_dlp() {
  if ! command -v yt-dlp >/dev/null 2>&1; then
    echo "yt-dlp not found — installing via Homebrew..." >&2
    if command -v brew >/dev/null 2>&1; then
      brew install yt-dlp >&2
    else
      echo "ERROR: Homebrew not found. Install yt-dlp manually: https://github.com/yt-dlp/yt-dlp#installation" >&2
      exit 1
    fi
  fi
}

# Converts a .vtt subtitle file to two outputs: plain text and a cleaned timestamped text file.
#
# YouTube's auto-generated VTT captions use a "rolling" format: each cue re-displays part of the
# previous cue's text plus a bit of new text (so the caption appears to scroll as you watch). A
# naive parse duplicates most of the transcript. To fix this, each cue's words are diffed against
# the previously kept cue: only the new suffix (words not already emitted) gets appended, keyed to
# that cue's timestamp. Manually uploaded (non-auto) captions don't roll, but the same diff logic
# is a no-op for them since there's no overlap to strip.
vtt_to_text() {
  local vtt="$1" plain_out="$2" ts_out="$3"
  python3 - "$vtt" "$plain_out" "$ts_out" <<'PYEOF'
import html, re, sys

vtt_path, plain_path, ts_path = sys.argv[1], sys.argv[2], sys.argv[3]
with open(vtt_path, encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

TIME_RE = re.compile(r"(\d{2}:\d{2}:\d{2})\.\d{3}\s*-->\s*(\d{2}:\d{2}:\d{2})\.\d{3}")
TAG_RE = re.compile(r"<[^>]+>")

raw_cues = []  # (timestamp, text)
current_time = None
current_lines = []

def flush():
    if current_time and current_lines:
        text = " ".join(current_lines).strip()
        text = TAG_RE.sub("", text)
        text = html.unescape(text)
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            raw_cues.append((current_time, text))

for line in lines:
    line = line.rstrip("\n")
    m = TIME_RE.search(line)
    if m:
        flush()
        current_time = m.group(1)
        current_lines = []
        continue
    if line.strip() and not line.strip().isdigit() and "WEBVTT" not in line and "-->" not in line:
        current_lines.append(line.strip())
flush()

def overlap_len(prev_words, cur_words):
    # Longest suffix of prev_words that matches a prefix of cur_words (rolling-caption overlap).
    max_k = min(len(prev_words), len(cur_words))
    for k in range(max_k, 0, -1):
        if prev_words[-k:] == cur_words[:k]:
            return k
    return 0

segments = []
prev_words = []
for t, text in raw_cues:
    cur_words = text.split()
    k = overlap_len(prev_words, cur_words)
    new_words = cur_words[k:]
    if new_words:
        segments.append((t, " ".join(new_words)))
    prev_words = cur_words

with open(ts_path, "w", encoding="utf-8") as f:
    for t, text in segments:
        f.write(f"[{t}] {text}\n")

with open(plain_path, "w", encoding="utf-8") as f:
    f.write(" ".join(text for _, text in segments))
    f.write("\n")

print(f"{len(segments)} segments", file=sys.stderr)
PYEOF
}

whisper_json_to_text() {
  local json="$1" plain_out="$2" ts_out="$3"
  python3 - "$json" "$plain_out" "$ts_out" <<'PYEOF'
import json, sys

json_path, plain_path, ts_path = sys.argv[1], sys.argv[2], sys.argv[3]
with open(json_path) as f:
    data = json.load(f)

def fmt(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

with open(ts_path, "w", encoding="utf-8") as f:
    for seg in data.get("segments", []):
        f.write(f"[{fmt(seg['start'])}] {seg['text'].strip()}\n")

with open(plain_path, "w", encoding="utf-8") as f:
    f.write(data.get("text", "").strip() + "\n")
PYEOF
}

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

if is_url "$INPUT"; then
  ensure_yt_dlp

  SLUG=$(yt-dlp --get-filename -o "%(title).80s" --restrict-filenames "$INPUT" 2>/dev/null || echo "video")
  VIDEO_DIR="$OUTPUT_DIR/${SLUG}"
  mkdir -p "$VIDEO_DIR"
  PLAIN_OUT="$VIDEO_DIR/${SLUG}.txt"
  TS_OUT="$VIDEO_DIR/${SLUG}.timestamped.txt"

  echo "Checking for existing captions..." >&2
  if yt-dlp --skip-download --write-auto-sub --write-sub --sub-langs "en.*,en" --sub-format vtt \
       -o "$TMP_DIR/%(title).80s.%(ext)s" --restrict-filenames "$INPUT" >&2; then
    VTT_FILE=$(find "$TMP_DIR" -name "*.vtt" | head -n1)
  else
    VTT_FILE=""
  fi

  if [[ -n "$VTT_FILE" && -f "$VTT_FILE" ]]; then
    echo "Found captions, converting to transcript..." >&2
    vtt_to_text "$VTT_FILE" "$PLAIN_OUT" "$TS_OUT"
  else
    echo "No captions available — downloading audio and transcribing with Whisper (model: $WHISPER_MODEL)..." >&2
    yt-dlp -x --audio-format mp3 -o "$TMP_DIR/audio.%(ext)s" --restrict-filenames "$INPUT" >&2
    AUDIO_FILE=$(find "$TMP_DIR" -name "audio.*" | head -n1)
    whisper "$AUDIO_FILE" --model "$WHISPER_MODEL" --output_format json --output_dir "$TMP_DIR" >&2
    JSON_FILE=$(find "$TMP_DIR" -name "*.json" | head -n1)
    whisper_json_to_text "$JSON_FILE" "$PLAIN_OUT" "$TS_OUT"
  fi
else
  # Local file
  if [[ ! -f "$INPUT" ]]; then
    echo "ERROR: file not found: $INPUT" >&2
    exit 1
  fi
  SLUG=$(basename "$INPUT" | sed 's/\.[^.]*$//' | tr -c 'a-zA-Z0-9_-' '_')
  VIDEO_DIR="$OUTPUT_DIR/${SLUG}"
  mkdir -p "$VIDEO_DIR"
  PLAIN_OUT="$VIDEO_DIR/${SLUG}.txt"
  TS_OUT="$VIDEO_DIR/${SLUG}.timestamped.txt"

  echo "Transcribing local file with Whisper (model: $WHISPER_MODEL)..." >&2
  whisper "$INPUT" --model "$WHISPER_MODEL" --output_format json --output_dir "$TMP_DIR" >&2
  JSON_FILE=$(find "$TMP_DIR" -name "*.json" | head -n1)
  whisper_json_to_text "$JSON_FILE" "$PLAIN_OUT" "$TS_OUT"
fi

echo "DONE"
echo "PLAIN:$PLAIN_OUT"
echo "TIMESTAMPED:$TS_OUT"
