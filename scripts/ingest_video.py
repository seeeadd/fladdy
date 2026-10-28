"""One YouTube video -> a study file: a frame at every slide change, each with the words said over it.

    python3 scripts/ingest_video.py <youtube url or id> [...] [--out sources/videos]

Writes sources/videos/<id>/: meta.json, captions.vtt, frames/NNNN_<seconds>.jpg, study.md.
The MP4 is kept in sources/videos/<id>/video.mp4 but stays out of git (too big; keep it in Drive).
Run it on a Mac: YouTube blocks cloud machines (403 on video, 429 on captions, 2026-10-28).
Needs yt-dlp and ffmpeg (`brew install yt-dlp ffmpeg`). Safe to re-run: finished steps are skipped.
"""
import json, os, re, subprocess, sys


def ytdlp(*args):
    return subprocess.run(["yt-dlp", *args], capture_output=True, text=True)


def seconds(stamp):
    parts = stamp.replace(",", ".").split(":")
    while len(parts) < 3:
        parts.insert(0, "0")
    return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])


def read_vtt(path):
    """Auto captions repeat the previous line in every cue; keep only the new words."""
    cues, prev = [], ""
    for block in re.split(r"\n\n+", open(path, encoding="utf-8").read()):
        m = re.search(r"([\d:.]+) --> ([\d:.]+)", block)
        if not m:
            continue
        text = " ".join(l for l in block.split("\n") if "-->" not in l and not l.startswith(("WEBVTT", "Kind:", "Language:")))
        text = re.sub(r"<[^>]+>", "", text).strip()
        new = text[len(prev):].strip() if prev and text.startswith(prev) else text
        if new and new != prev:
            cues.append((seconds(m.group(1)), new))
        prev = text
    return cues


def ingest(url, root):
    vid = re.search(r"(?:v=|youtu\.be/|^)([\w-]{11})", url).group(1)
    url = f"https://www.youtube.com/watch?v={vid}"
    out = os.path.join(root, vid)
    frames_dir = os.path.join(out, "frames")
    os.makedirs(frames_dir, exist_ok=True)

    meta_path = os.path.join(out, "meta.json")
    if not os.path.exists(meta_path):
        p = ytdlp("--skip-download", "--dump-json", url)
        if p.returncode:
            sys.exit(f"FAIL {vid}: {p.stderr.strip().splitlines()[-1]}")
        d = json.loads(p.stdout)
        json.dump({k: d.get(k) for k in ("id", "title", "uploader", "upload_date", "duration", "description")},
                  open(meta_path, "w"), indent=1)
    meta = json.load(open(meta_path))

    mp4 = os.path.join(out, "video.mp4")
    if not os.path.exists(mp4):
        # 1080p so the slide text in the frames is readable
        p = ytdlp("-f", "bv*[height<=1080][ext=mp4]/bv*[height<=1080]", "--remux-video", "mp4", "-o", mp4, url)
        if p.returncode:
            sys.exit(f"FAIL {vid} video: {p.stderr.strip().splitlines()[-1]}")

    vtt = os.path.join(out, "captions.vtt")
    if not os.path.exists(vtt):
        ytdlp("--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", "en.*,en",
              "--sub-format", "vtt", "-o", os.path.join(out, "cap"), url)
        got = sorted(f for f in os.listdir(out) if f.startswith("cap") and f.endswith(".vtt"))
        if got:
            os.rename(os.path.join(out, got[0]), vtt)

    if not os.listdir(frames_dir):
        # a frame at every scene change, and at least one every 30 s
        p = subprocess.run(["ffmpeg", "-loglevel", "info", "-i", mp4, "-vf",
                            "select='isnan(prev_selected_t)+gt(scene,0.25)+gte(t-prev_selected_t,30)',showinfo",
                            "-vsync", "vfr", "-q:v", "3", os.path.join(frames_dir, "f%04d.jpg")],
                           capture_output=True, text=True)
        times = [float(t) for t in re.findall(r"pts_time:([\d.]+)", p.stderr)]
        for name, t in zip(sorted(os.listdir(frames_dir)), times):
            os.rename(os.path.join(frames_dir, name), os.path.join(frames_dir, f"{name[1:5]}_{int(t):05d}.jpg"))

    frames = sorted(os.listdir(frames_dir))
    starts = [int(f.split("_")[1][:5]) for f in frames]
    cues = read_vtt(vtt) if os.path.exists(vtt) else []
    with open(os.path.join(out, "study.md"), "w", encoding="utf-8") as f:
        f.write(f"# {meta['title']}\n\n{meta['uploader']} | {meta.get('upload_date')} | {url}\n\n"
                "Each frame is followed by the words said while it is on screen.\n\n")
        for i, (name, t0) in enumerate(zip(frames, starts)):
            t1 = starts[i + 1] if i + 1 < len(starts) else float("inf")
            said = " ".join(w for t, w in cues if t0 <= t < t1)
            f.write(f"## [{t0 // 60}:{t0 % 60:02d}] frames/{name}\n\n{said}\n\n")
    print(f"OK {vid} {meta['title']!r}: {len(frames)} frames, {len(cues)} caption lines"
          + ("" if cues else " (NO CAPTIONS)"))


if __name__ == "__main__":
    args = sys.argv[1:]
    root = "sources/videos"
    if "--out" in args:
        i = args.index("--out")
        root = args[i + 1]
        del args[i:i + 2]
    if not args:
        sys.exit(__doc__)
    for a in args:
        ingest(a, root)
