#!/usr/bin/env python3
"""Fetch a YouTube video's metadata and transcript as one Markdown file.

Usage: python3 -I transcript.py <url-or-id> [--lang ru,en] [--out DIR] [--print auto|all|head]

Needs yt-dlp on PATH (brew install yt-dlp / pipx install yt-dlp). Standard library only.
Prints the Markdown to stdout when it is short (--print auto, the default), otherwise the
header and the path of the full file. Exit codes: 0 ok, 2 no yt-dlp, 3 video unavailable,
4 no captions in any language.
"""

import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

PRINT_LIMIT = 40000  # characters; above this only the header goes to stdout
PARAGRAPH_SECONDS = 30


def find_ytdlp():
    path = shutil.which("yt-dlp")
    if path:
        return path
    for candidate in ("/opt/homebrew/bin/yt-dlp", "/usr/local/bin/yt-dlp", os.path.expanduser("~/.local/bin/yt-dlp")):
        if os.access(candidate, os.X_OK):
            return candidate
    return None


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def pick_track(meta, wanted):
    """Return (lang, is_auto). Manual captions beat automatic ones; the original track beats translations."""
    manual = meta.get("subtitles") or {}
    auto = meta.get("automatic_captions") or {}
    original = meta.get("language")
    orig_auto = [k for k in auto if k.endswith("-orig")]

    order = []
    for lang in wanted + ([original] if original else []):
        if lang and lang not in order:
            order.append(lang)

    for lang in order:
        for key in manual:
            if key == lang or key.split("-")[0] == lang:
                return key, False
    if orig_auto and (not wanted or orig_auto[0].split("-")[0] in wanted):
        return orig_auto[0], True
    for lang in order:
        if lang in auto:
            return lang, True
    if manual:
        return next(iter(manual)), False
    if orig_auto:
        return orig_auto[0], True
    if auto:
        return ("en" if "en" in auto else next(iter(auto))), True
    return None, None


TS = re.compile(r"(\d+):(\d{2}):(\d{2})[.,](\d{3})\s+-->")


def parse_vtt(text):
    """Return [(seconds, line)] with tags stripped and the rolling repeats of auto captions removed."""
    out = []
    last = ""
    start = None
    for raw in text.splitlines():
        m = TS.match(raw)
        if m:
            h, mi, s, _ = map(int, m.groups())
            start = h * 3600 + mi * 60 + s
            continue
        if start is None or not raw.strip() or raw.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        line = html.unescape(re.sub(r"<[^>]+>", "", raw)).strip()
        if not line or line == last:
            continue
        if out and last and line.startswith(last):
            line = line[len(last):].strip()
            if not line:
                continue
        out.append((start, line))
        last = line
    return out


def stamp(seconds):
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def paragraphs(lines):
    paras = []
    cur_start, cur = None, []
    for t, line in lines:
        if cur_start is None:
            cur_start = t
        if t - cur_start >= PARAGRAPH_SECONDS and cur:
            paras.append((cur_start, " ".join(cur)))
            cur_start, cur = t, []
        cur.append(line)
    if cur:
        paras.append((cur_start, " ".join(cur)))
    return paras


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--lang", default="", help="preferred caption languages, comma-separated")
    ap.add_argument("--out", default=os.path.join(tempfile.gettempdir(), "needt-youtube"))
    ap.add_argument("--print", dest="mode", default="auto", choices=["auto", "all", "head"])
    args = ap.parse_args()

    ytdlp = find_ytdlp()
    if not ytdlp:
        print("ERROR no-ytdlp: install with `brew install yt-dlp` or `pipx install yt-dlp`", file=sys.stderr)
        return 2

    url = args.video if "/" in args.video else f"https://www.youtube.com/watch?v={args.video}"
    res = run([ytdlp, "-J", "--skip-download", "--no-warnings", "--no-playlist", url])
    if res.returncode != 0:
        print("ERROR unavailable: " + (res.stderr.strip().splitlines() or ["unknown"])[-1], file=sys.stderr)
        return 3
    meta = json.loads(res.stdout)
    vid = meta["id"]
    wanted = [x.strip() for x in args.lang.split(",") if x.strip()]
    lang, is_auto = pick_track(meta, wanted)

    os.makedirs(args.out, exist_ok=True)
    lines = []
    if lang:
        with tempfile.TemporaryDirectory() as tmp:
            flag = "--write-auto-subs" if is_auto else "--write-subs"
            run([ytdlp, "--skip-download", "--no-warnings", "--no-playlist", flag, "--sub-langs", lang,
                 "--sub-format", "vtt", "-o", os.path.join(tmp, "%(id)s.%(ext)s"), url])
            files = [f for f in os.listdir(tmp) if f.endswith(".vtt")]
            if files:
                with open(os.path.join(tmp, files[0]), encoding="utf-8") as fh:
                    lines = parse_vtt(fh.read())

    date = meta.get("upload_date") or ""
    if len(date) == 8:
        date = f"{date[:4]}-{date[4:6]}-{date[6:]}"
    head = [
        f"# {meta.get('title', vid)}",
        "",
        f"- url: https://www.youtube.com/watch?v={vid}",
        f"- channel: {meta.get('channel') or meta.get('uploader') or '?'}"
        + (f" ({meta['channel_follower_count']:,} subscribers)" if meta.get("channel_follower_count") else ""),
        f"- published: {date or '?'} · duration: {stamp(meta.get('duration') or 0)}"
        + (f" · views: {meta['view_count']:,}" if meta.get("view_count") is not None else ""),
        f"- captions: {lang} ({'auto' if is_auto else 'manual'})" if lines else "- captions: none",
    ]
    chapters = meta.get("chapters") or []
    if chapters:
        head += ["", "## Chapters", ""] + [f"- {stamp(c['start_time'])} {c.get('title', '')}" for c in chapters]
    desc = (meta.get("description") or "").strip()
    if desc:
        head += ["", "## Description", "", desc[:3000] + (" …" if len(desc) > 3000 else "")]

    body = ["", "## Transcript", ""]
    body += [f"[{stamp(t)}] {p}" for t, p in paragraphs(lines)] if lines else ["(no captions available)"]

    doc = "\n".join(head + body) + "\n"
    path = os.path.join(args.out, f"{vid}.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(doc)

    words = sum(len(p.split()) for _, p in lines)
    status = f"FILE {path} · {len(doc):,} chars · ~{words:,} words"
    if args.mode == "all" or (args.mode == "auto" and len(doc) <= PRINT_LIMIT):
        print(doc)
    else:
        print("\n".join(head))
        print("\n(transcript too long to print; read the file)")
    print(status)
    return 0 if lines else 4


if __name__ == "__main__":
    sys.exit(main())
