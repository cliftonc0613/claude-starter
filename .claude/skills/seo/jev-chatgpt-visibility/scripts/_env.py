"""Shared settings: finds API keys and picks the Jev model.

Keys are read from the environment first, then from these files in order:
  ./jev-chatgpt/<domain>/.env
  ~/.config/jev-seo/.env
  ~/.config/jev-internal-links/.env
"""
import os
from pathlib import Path

KEYS = ("OPENROUTER_API_KEY", "DATAFORSEO_USERNAME", "DATAFORSEO_PASSWORD")


def load_keys(workdir):
    files = [Path(workdir) / ".env",
             Path.home() / ".config/jev-seo/.env",
             Path.home() / ".config/jev-internal-links/.env"]
    for f in files:
        if not f.exists():
            continue
        for line in f.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip("'\""))
    return [k for k in KEYS if not os.environ.get(k)]


# "~typesafe/jev-latest" follows TypeSafe's newest release. Pin a version
# (e.g. "typesafe/jev-1.13") when you need runs to be comparable over time.
def jev_model():
    return os.environ.get("JEV_MODEL", "~typesafe/jev-latest")
