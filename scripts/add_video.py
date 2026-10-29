"""Add a YouTube video to its coach's folder in one step (SOP: sops/video-teardown.md, step 1).

    python3 scripts/add_video.py <youtube url or id> [--frames-only]

Runs scripts/ingest_youtube.py, reads the channel from meta.json, and files the result as
<channel>-videos/NN Title (id)/ (jason-fladlien-videos/, jeremy-haynes-videos/, a new folder for a new coach),
numbered after the videos already there. Adds the video's row to that folder's README.md (and writes the README
for a new coach), runs scripts/distinct_sheets.py (the frames worth reading, in distinct/), and prints the folder,
the checks, and the distinct-sheet chunks for the teardown agents.
0 tokens; a 1-hour video takes about 2 minutes. Re-running for a video already filed changes nothing.
"""
import json, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = os.path.join(ROOT, ".ingest-tmp")
CHUNK = 12  # distinct sheets per teardown agent (distinct_sheets.py keeps about half the frames)


def video_id(arg):
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/live/|/embed/)([A-Za-z0-9_-]{11})", arg)
    return m.group(1) if m else arg


def clock(sec):
    sec = int(sec)
    h, m, s = sec // 3600, sec % 3600 // 60, sec % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def safe(title):
    t = re.sub(r"[^\w\s&-]", "", title)
    return re.sub(r"\s+", " ", t).strip()


README_HEAD = """# {channel} videos

{channel} videos Sean sent, as study files. The video files themselves are not here: YouTube blocks downloading
them from a cloud session, so each folder holds the transcript and the frames instead. A `teardown.md` in a folder
is the analysis (sops/video-teardown.md).

| # | video | length | folder |
|---|---|---|---|
"""

README_TAIL = """
## What is in each folder

- `transcript.md`: the full transcript with timestamps (YouTube captions). Paste this into another chat to work from the video.
- `study.md`: each frame time next to the words said over it, to read beside the frames.
- `sheets/S00.jpg ...`: YouTube storyboard frames, 3x3 per sheet, about 10 seconds apart (one sheet is about 90 seconds).
- `transcript.json`, `meta.json`: the same data for scripts (title, length, link).
- `teardown.md`, when written: the analysis.

Add a video with `python3 scripts/add_video.py <url>` (sops/video-teardown.md).
"""


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    vid = video_id(args[0])
    for d in os.listdir(ROOT):
        if d.endswith("-videos") and os.path.isdir(os.path.join(ROOT, d)):
            for f in os.listdir(os.path.join(ROOT, d)):
                if f.endswith(f"({vid})"):
                    print(f"ALREADY {d}/{f}")
                    return
    os.makedirs(TMP, exist_ok=True)
    cmd = [sys.executable, os.path.join(ROOT, "scripts", "ingest_youtube.py"), vid, "--out", TMP]
    if "--frames-only" in sys.argv:
        cmd.append("--frames-only")
    if subprocess.run(cmd, cwd=ROOT).returncode:
        sys.exit("FAIL ingest_youtube.py (see above)")
    src = os.path.join(TMP, vid)
    meta = json.load(open(os.path.join(src, "meta.json")))
    channel = meta.get("channel") or "Unknown"
    folder = re.sub(r"[^a-z0-9]+", "-", channel.lower()).strip("-") + "-videos"
    home = os.path.join(ROOT, folder)
    os.makedirs(home, exist_ok=True)
    n = 1 + sum(1 for f in os.listdir(home) if re.match(r"\d\d ", f))
    name = f"{n:02d} {safe(meta['title'])} ({vid})"
    shutil.move(src, os.path.join(home, name))
    shutil.rmtree(TMP, ignore_errors=True)

    readme = os.path.join(home, "README.md")
    row = (f"| {n} | [{meta['title']}](https://www.youtube.com/watch?v={vid}) | {clock(meta.get('duration') or 0)} "
           f"| [{name}](<{name}/>) |")
    if not os.path.exists(readme):
        open(readme, "w").write(README_HEAD.format(channel=channel) + row + "\n" + README_TAIL)
    else:
        lines = open(readme).read().split("\n")
        last = max(i for i, l in enumerate(lines) if l.startswith("| "))
        lines.insert(last + 1, row)
        open(readme, "w").write("\n".join(lines))

    sheets = sorted(f for f in os.listdir(os.path.join(home, name, "sheets")) if f.endswith(".jpg"))
    tr = os.path.join(home, name, "transcript.md")
    words = len(open(tr).read().split()) if os.path.exists(tr) else 0
    print(f"OK {folder}/{name}")
    print(f"   {channel} | {clock(meta.get('duration') or 0)} | {len(sheets)} sheets | transcript {words} words")
    if not words and "--frames-only" not in sys.argv:
        print("   WARN no transcript: re-run later (YouTube 429s), or ask Sean to paste the transcript")
    if words:
        subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "distinct_sheets.py"), os.path.join(home, name)], cwd=ROOT)
    dist = sorted(f for f in os.listdir(os.path.join(home, name, "distinct")) if f.endswith(".jpg")) \
        if os.path.isdir(os.path.join(home, name, "distinct")) else []
    use = dist or sheets
    print(f"   frame chunks for the teardown agents ({'distinct/' if dist else 'sheets/'}):")
    for i in range(0, len(use), CHUNK):
        part = use[i:i + CHUNK]
        print(f"     {part[0][:-4]}-{part[-1][:-4]}")
    if not os.path.exists(os.path.join(ROOT, "CLAUDE.md")) or folder not in open(os.path.join(ROOT, "CLAUDE.md")).read():
        print(f"   NEW coach folder: add `{folder}/` to the table in CLAUDE.md")


if __name__ == "__main__":
    main()
