#!/usr/bin/env python3
"""Rebuild the gallery wall for the /generate skill.

Scans the flat generations folder and writes gallery.html beside the media —
a single self-contained masonry page (newest first, hover-play videos,
click-to-lightbox). Relative src paths mean it works from file:// with no
server and no manifest fetch. Re-run after each generation batch.
"""

import html
import json
import os
import subprocess
import sys
from pathlib import Path

# Portable: current project's knowledge/generations, overridable via GENERATIONS_DIR.
GEN_DIR = Path(os.environ.get("GENERATIONS_DIR") or Path.cwd() / "knowledge" / "generations")
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}
VIDEO_EXT = {".mp4", ".webm", ".mov"}

CSS = """
:root{--bg:#111014;--card:#1b1a20;--ink:#e8e5de;--dim:#8b8794;--accent:#e05d2a}
*{margin:0;box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:15px/1.5 Georgia,'Times New Roman',serif;padding:2rem}
header{max-width:1400px;margin:0 auto 2rem}
h1{font-size:1.6rem;font-weight:400;letter-spacing:.02em}
h1 b{color:var(--accent);font-weight:700}
header p{color:var(--dim);font-size:.85rem;margin-top:.25rem}
.wall{max-width:1400px;margin:0 auto;columns:4 300px;column-gap:14px}
.tile{break-inside:avoid;margin:0 0 14px;background:var(--card);border-radius:14px;overflow:hidden;cursor:pointer;position:relative;transition:transform .18s ease,box-shadow .18s ease}
.tile:hover{transform:translateY(-3px);box-shadow:0 10px 30px rgba(0,0,0,.5)}
.tile img,.tile video{display:block;width:100%;height:auto}
.tile .cap{position:absolute;inset:auto 0 0;padding:1.4rem .7rem .5rem;font-size:.72rem;color:#cfccc5;background:linear-gradient(transparent,rgba(0,0,0,.75));opacity:0;transition:opacity .18s}
.tile:hover .cap{opacity:1}
.lb{position:fixed;inset:0;background:rgba(10,9,12,.92);display:none;align-items:center;justify-content:center;padding:3vmin;z-index:9}
.lb.open{display:flex}
.lb img,.lb video{max-width:94vw;max-height:92vh;border-radius:10px}
.empty{color:var(--dim);text-align:center;padding:5rem 0;font-style:italic}
"""

JS = """
const lb=document.getElementById('lb');
document.querySelectorAll('.tile').forEach(t=>{
  const v=t.querySelector('video');
  if(v){t.addEventListener('mouseenter',()=>{v.muted=true;v.play().catch(()=>{})});
       t.addEventListener('mouseleave',()=>{v.pause();v.currentTime=0})}
  t.addEventListener('click',()=>{
    const s=t.querySelector('img,video');
    lb.innerHTML=s.tagName==='VIDEO'
      ?`<video src="${s.getAttribute('src')}" controls autoplay loop></video>`
      :`<img src="${s.getAttribute('src')}">`;
    lb.classList.add('open')})});
lb.addEventListener('click',e=>{if(e.target===lb){lb.innerHTML='';lb.classList.remove('open')}});
addEventListener('keydown',e=>{if(e.key==='Escape'){lb.innerHTML='';lb.classList.remove('open')}});
"""


def caption(f):
    sidecar = f.with_suffix(f.suffix + ".json")
    if sidecar.is_file():
        try:
            meta = json.loads(sidecar.read_text())
            return f"{meta.get('model', '')} · {meta.get('prompt', '')[:110]}"
        except (json.JSONDecodeError, OSError):
            pass
    return f.name


def main():
    GEN_DIR.mkdir(parents=True, exist_ok=True)
    (GEN_DIR / "refs").mkdir(exist_ok=True)
    files = sorted(
        (f for f in GEN_DIR.iterdir()
         if f.is_file() and f.suffix.lower() in IMAGE_EXT | VIDEO_EXT),
        key=lambda f: f.stat().st_mtime, reverse=True)
    tiles = []
    for f in files:
        cap = html.escape(caption(f))
        src = html.escape(f.name)
        media = (f'<video src="{src}" preload="metadata" loop playsinline></video>'
                 if f.suffix.lower() in VIDEO_EXT else
                 f'<img src="{src}" loading="lazy" alt="{cap}">')
        tiles.append(f'<figure class="tile">{media}<figcaption class="cap">{cap}</figcaption></figure>')
    wall = "\n".join(tiles) if tiles else '<p class="empty">Nothing generated yet — type /generate and ask for something.</p>'
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Generations</title><style>{CSS}</style></head><body>
<header><h1><b>/generate</b> — the wall</h1><p>{len(files)} pieces · newest first · hover a video to preview, click anything to enlarge</p></header>
<main class="wall">{wall}</main>
<div class="lb" id="lb"></div>
<script>{JS}</script></body></html>"""
    out = GEN_DIR / "gallery.html"
    out.write_text(page)
    print(f"gallery rebuilt: {out} ({len(files)} items)")
    if "--open" in sys.argv:
        subprocess.run(["open", str(out)], check=False)


if __name__ == "__main__":
    main()
