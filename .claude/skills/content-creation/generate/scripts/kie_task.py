#!/usr/bin/env python3
"""Generic Kie AI jobs-API runner for the /generate skill.

Subcommands (resumable split so long renders survive Bash timeouts):
  credits              print remaining Kie AI account credit balance
  submit --model <id> --input '<json>' [--ref file ...] [--name base] [--out-dir dir]
  wait   <taskId>     poll until done, download, write sidecar log (exit 3 = still going, re-run)
  status <taskId>     one quick poll, no download
  fetch  <taskId>     download an already-finished task

State lives in ~/.kie/generate-tasks/<taskId>.json.
"""

import argparse
import json
import mimetypes
import os
import re
import sys
import time
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path

API_BASE = "https://api.kie.ai/api/v1/jobs"
UPLOAD_URL = "https://kieai.redpandaai.co/api/file-stream-upload"
# Portable: resolves to the current project's knowledge/generations folder,
# overridable with the GENERATIONS_DIR env var. Created on first save.
DEFAULT_OUT = os.environ.get("GENERATIONS_DIR") or str(Path.cwd() / "knowledge" / "generations")
STATE_DIR = Path.home() / ".kie" / "generate-tasks"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_api_key():
    key = os.environ.get("KIE_API_KEY")
    if key:
        return key.strip()
    for env in (Path.cwd() / ".env", Path.home() / ".kie" / ".env"):
        if env.is_file():
            for line in env.read_text().splitlines():
                m = re.match(r"\s*(?:export\s+)?KIE_API_KEY\s*=\s*['\"]?([^'\"\s]+)", line)
                if m:
                    return m.group(1)
    sys.exit("KIE_API_KEY not found in environment or any .env file")


def api(method, url, key, body=None, form=None):
    if form is not None:
        boundary = uuid.uuid4().hex
        parts = []
        for name, (filename, data, ctype) in form.items():
            head = f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"'
            head += f'; filename="{filename}"\r\nContent-Type: {ctype}' if filename else ""
            parts.append(head.encode() + b"\r\n\r\n" + (data if isinstance(data, bytes) else data.encode()) + b"\r\n")
        payload = b"".join(parts) + f"--{boundary}--\r\n".encode()
        headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
    else:
        payload = json.dumps(body).encode() if body is not None else None
        headers = {"Content-Type": "application/json"}
    headers["Authorization"] = f"Bearer {key}"
    req = urllib.request.Request(url, data=payload, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())


def state_path(task_id):
    return STATE_DIR / f"{task_id}.json"


def save_state(state):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = now_iso()
    state_path(state["taskId"]).write_text(json.dumps(state, indent=2))


def load_state(task_id):
    p = state_path(task_id)
    return json.loads(p.read_text()) if p.is_file() else {"taskId": task_id}


def upload_ref(path, key):
    p = Path(path).expanduser()
    if not p.is_file():
        sys.exit(f"reference file not found: {path}")
    ctype = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
    resp = api("POST", UPLOAD_URL, key, form={
        "file": (p.name, p.read_bytes(), ctype),
        "uploadPath": (None, "images/generate-refs", "text/plain"),
    })
    url = (resp.get("data") or {}).get("fileUrl")
    if not url:
        sys.exit(f"upload failed for {path}: {resp}")
    print(f"uploaded ref: {p.name} -> {url}", file=sys.stderr)
    return url


def cmd_submit(args):
    key = load_api_key()
    try:
        inp = json.loads(args.input)
    except json.JSONDecodeError as e:
        sys.exit(f"--input is not valid JSON: {e}")
    ref_urls = [upload_ref(r, key) for r in (args.ref or [])]
    if ref_urls:
        inp.setdefault("image_input", []).extend(ref_urls)
    resp = api("POST", f"{API_BASE}/createTask", key, body={"model": args.model, "input": inp})
    if resp.get("code") != 200:
        sys.exit(f"createTask failed: {resp}")
    task_id = resp["data"]["taskId"]
    save_state({
        "taskId": task_id, "model": args.model, "input": inp,
        "refs": args.ref or [], "name": args.name,
        "out_dir": str(Path(args.out_dir).expanduser()),
        "state": "submitted", "remote_urls": [], "local_files": [],
        "created_at": now_iso(),
    })
    print(json.dumps({"taskId": task_id, "state": "submitted"}))
    return 0


def poll(key, task_id):
    resp = api("GET", f"{API_BASE}/recordInfo?taskId={task_id}", key)
    return resp.get("data") or {}


def download_and_log(state, urls):
    out_dir = Path(state.get("out_dir") or DEFAULT_OUT)
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = int(time.time())
    base = state.get("name") or f"generate_{state['model'].replace('/', '-')}"
    saved = []
    for i, url in enumerate(urls):
        ext = Path(url.split("?")[0]).suffix or ".bin"
        suffix = f"_{i + 1}" if len(urls) > 1 else ""
        dest = out_dir / f"{base}{suffix}_{ts}{ext}"
        # Kie's result CDN 403s Python's default user-agent; send a browser-ish one.
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=300) as r:
            dest.write_bytes(r.read())
        sidecar = {
            "model": state["model"],
            "prompt": state.get("input", {}).get("prompt", ""),
            "refs": state.get("refs", []),
            "params": {k: v for k, v in state.get("input", {}).items() if k != "prompt"},
            "taskId": state["taskId"],
            "created": now_iso(),
        }
        dest.with_suffix(dest.suffix + ".json").write_text(json.dumps(sidecar, indent=2))
        saved.append(str(dest))
        print(f"saved: {dest}", file=sys.stderr)
    state.update(state="downloaded", remote_urls=urls, local_files=saved)
    save_state(state)
    print(json.dumps({"taskId": state["taskId"], "state": "downloaded", "files": saved}))


def finish_if_done(state, info):
    """Returns exit code, or None if still running."""
    s = info.get("state")
    if s == "success":
        urls = json.loads(info.get("resultJson") or "{}").get("resultUrls", [])
        if not urls:
            print(json.dumps({"taskId": state["taskId"], "state": "success", "error": "no resultUrls"}))
            return 1
        download_and_log(state, urls)
        return 0
    if s == "fail":
        state["state"] = "fail"
        save_state(state)
        print(json.dumps({"taskId": state["taskId"], "state": "fail",
                          "failCode": info.get("failCode"), "failMsg": info.get("failMsg")}))
        return 1
    return None


def cmd_wait(args):
    key = load_api_key()
    state = load_state(args.task_id)
    if state.get("state") == "downloaded":
        print(json.dumps({"taskId": args.task_id, "state": "downloaded", "files": state.get("local_files", [])}))
        return 0
    deadline = time.time() + args.timeout
    while time.time() < deadline:
        info = poll(key, args.task_id)
        state.setdefault("model", info.get("model") or "unknown")
        code = finish_if_done(state, info)
        if code is not None:
            return code
        state["state"] = info.get("state") or "generating"
        save_state(state)
        time.sleep(args.interval)
    print(json.dumps({"taskId": args.task_id, "state": state.get("state"), "resumable": True}))
    return 3


def cmd_status(args):
    info = poll(load_api_key(), args.task_id)
    print(json.dumps({"taskId": args.task_id, "state": info.get("state"),
                      "failCode": info.get("failCode"), "failMsg": info.get("failMsg")}))
    return 0


def cmd_credits(args):
    key = load_api_key()
    resp = api("GET", "https://api.kie.ai/api/v1/chat/credit", key)
    if resp.get("code") != 200:
        sys.exit(f"credit check failed: {resp}")
    print(json.dumps({"credits": resp.get("data")}))
    return 0


def cmd_fetch(args):
    key = load_api_key()
    state = load_state(args.task_id)
    info = poll(key, args.task_id)
    state.setdefault("model", info.get("model") or "unknown")
    code = finish_if_done(state, info)
    if code is None:
        print(json.dumps({"taskId": args.task_id, "state": info.get("state"), "resumable": True}))
        return 3
    return code


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("submit")
    s.add_argument("--model", required=True)
    s.add_argument("--input", required=True, help="JSON string for the model's input object")
    s.add_argument("--ref", action="append", help="local reference file, uploaded automatically (repeatable)")
    s.add_argument("--name", help="output basename: {project}_{description}")
    s.add_argument("--out-dir", default=DEFAULT_OUT)
    s.set_defaults(fn=cmd_submit)

    for name, fn, timeout in (("wait", cmd_wait, 540), ("status", cmd_status, 0), ("fetch", cmd_fetch, 0)):
        s = sub.add_parser(name)
        s.add_argument("task_id")
        if name == "wait":
            s.add_argument("--timeout", type=int, default=timeout)
            s.add_argument("--interval", type=int, default=10)
        s.set_defaults(fn=fn)

    sub.add_parser("credits").set_defaults(fn=cmd_credits)

    args = p.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
