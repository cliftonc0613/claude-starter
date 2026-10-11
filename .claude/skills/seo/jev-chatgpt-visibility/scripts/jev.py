"""Tiny Jev client: one POST per decision, cached by request hash (Jev is not
deterministic, so a cache keeps runs auditable and re-runs free), with cost
and real latency recorded per call."""
import hashlib
import json
import os
import random
import threading
import time
from pathlib import Path

import requests

URL = "https://openrouter.ai/api/alpha/decisions"

lock = threading.Lock()
stats = {"calls": 0, "cached": 0, "cost": 0.0, "in_tok": 0, "errors": 0}


class Jev:
    def __init__(self, model, cache_dir):
        self.model = model
        self.cache = Path(cache_dir)
        self.cache.mkdir(parents=True, exist_ok=True)

    def decide(self, state, questions, attempt=0):
        body = {"model": self.model, "state": state, "questions": questions}
        h = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()[:20]
        hit = self.cache / f"{h}.json"
        if hit.exists():
            with lock:
                stats["cached"] += 1
            return json.loads(hit.read_text())
        t0 = time.time()
        try:
            r = requests.post(URL, json=body, timeout=60, headers={
                "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}"})
            if r.status_code in (429, 500, 502, 503) and attempt < 5:
                time.sleep(2 ** attempt + random.random())
                return self.decide(state, questions, attempt + 1)
            r.raise_for_status()
            data = r.json()
        except Exception as e:
            with lock:
                stats["errors"] += 1
            return {"error": str(e)[:300]}
        data["_ms"] = round((time.time() - t0) * 1000)
        hit.write_text(json.dumps(data))
        with lock:
            u = data.get("usage", {})
            stats["calls"] += 1
            stats["cost"] += u.get("cost", 0) or 0
            stats["in_tok"] += u.get("input_tokens", 0) or 0
        return data
