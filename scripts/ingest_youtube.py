"""A YouTube video -> a study file: what is on screen every ~10 s, with the words said over it.

    python3 scripts/ingest_youtube.py <youtube url or id> [...] [--out sources/videos]

Writes sources/videos/<id>/:
  meta.json          title, channel, date, length
  transcript.json    every caption line with its start time (YouTube's own captions)
  transcript.md      the same as readable text, one line per ~30 s with a [m:ss] stamp
  sheets/S00.jpg ... YouTube's storyboard sheets (3x3 frames, 320x180 each, ~10 s apart): look at these
  study.md           per sheet, each frame's time and the words said while it was on screen

Works in a cloud session, where YouTube blocks the video itself (403 on every stream, a captcha on the
watch page, 2026-10-28):
  - the frames are the storyboard (the hover previews), served from i.ytimg.com, which is not blocked;
    mweb is the client that offers the 320x180 level (the others stop at 160x90)
  - the transcript is fetched by the embedded player in Chromium (with a referrer, or the embed refuses),
    whose captions URL is not tied to one IP; it is then downloaded with retries (it 429s a few times)
For full-resolution frames run scripts/ingest_video.py on a Mac instead.
Needs: yt-dlp, node (yt-dlp's JS solver), playwright + Chromium, Pillow. 0 tokens. Safe to re-run.
"""
import asyncio, io, json, os, re, subprocess, sys, time, urllib.request

CHROMIUM = "/opt/pw-browsers/chromium" if os.path.exists("/opt/pw-browsers/chromium") else None
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"


def fetch(url, tries=12):
    """GET with retries: YouTube answers 429 from this network now and then."""
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            last = e
            time.sleep(2 + i)
    raise last


def video_info(vid):
    p = subprocess.run([sys.executable, "-m", "yt_dlp", "--no-warnings", "--js-runtimes", "node",
                        "--extractor-args", "youtube:player_client=mweb", "-j",
                        f"https://www.youtube.com/watch?v={vid}"], capture_output=True, text=True)
    if p.returncode:
        sys.exit(f"FAIL {vid}: {p.stderr.strip().splitlines()[-1] if p.stderr.strip() else 'yt-dlp failed'}")
    return json.loads(p.stdout)


def storyboard(info, out):
    """Download the biggest storyboard level; return [(sheet file, [frame start seconds])]."""
    boards = [f for f in info["formats"] if f.get("format_note") == "storyboard" or f["format_id"].startswith("sb")]
    sb = max(boards, key=lambda f: (f.get("width") or 0))
    per = sb["rows"] * sb["columns"]
    os.makedirs(os.path.join(out, "sheets"), exist_ok=True)
    sheets, t = [], 0.0
    for i, frag in enumerate(sb["fragments"]):
        path = os.path.join(out, "sheets", f"S{i:02d}.jpg")
        if not os.path.exists(path):
            open(path, "wb").write(fetch(frag["url"]))
        step = frag["duration"] / per
        sheets.append((path, [t + k * step for k in range(per)]))
        t += frag["duration"]
    return sheets, sb


async def captions_url(vid):
    """The embedded player fetches its own captions; catch that request's URL."""
    from playwright.async_api import async_playwright
    found = []
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True, executable_path=CHROMIUM,
                                    args=["--autoplay-policy=no-user-gesture-required", "--mute-audio"])
        ctx = await b.new_context(viewport={"width": 1280, "height": 720}, ignore_https_errors=True,
                                  locale="en-US", user_agent=UA)
        pg = await ctx.new_page()
        pg.on("request", lambda r: found.append(r.url) if "/api/timedtext" in r.url else None)
        await pg.goto(f"https://www.youtube.com/embed/{vid}?autoplay=1&mute=1&cc_load_policy=1&cc_lang_pref=en&hl=en",
                      wait_until="domcontentloaded", referer="https://example.com/")
        for _ in range(30):
            if found:
                break
            await pg.wait_for_timeout(1000)
        await b.close()
    en = [u for u in found if "lang=en" in u] or found
    return en[0] if en else None


def transcript(vid, out):
    path = os.path.join(out, "transcript.json")
    if os.path.exists(path):
        return json.load(open(path))
    url = asyncio.run(captions_url(vid))
    if not url:
        print(f"WARN {vid}: the player fetched no captions")
        return []
    url = re.sub(r"fmt=[^&]+", "fmt=json3", url) if "fmt=" in url else url + "&fmt=json3"
    data = json.loads(fetch(url, tries=20))
    lines = []
    for ev in data.get("events", []):
        text = "".join(s.get("utf8", "") for s in ev.get("segs", []) or []).replace("\n", " ").strip()
        if text:
            lines.append({"t": round(ev["tStartMs"] / 1000, 2), "text": text})
    json.dump(lines, open(path, "w"), indent=0)
    return lines


def stamp(sec):
    sec = int(sec)
    return f"{sec // 3600}:{sec // 60 % 60:02d}:{sec % 60:02d}" if sec >= 3600 else f"{sec // 60}:{sec % 60:02d}"


def ingest(arg, root):
    vid = re.search(r"(?:v=|youtu\.be/|^)([\w-]{11})", arg).group(1)
    out = os.path.join(root, vid)
    os.makedirs(out, exist_ok=True)
    info = video_info(vid)
    meta = {k: info.get(k) for k in ("id", "title", "channel", "upload_date", "duration", "webpage_url")}
    json.dump(meta, open(os.path.join(out, "meta.json"), "w"), indent=1)
    sheets, sb = storyboard(info, out)
    lines = transcript(vid, out)

    with open(os.path.join(out, "transcript.md"), "w", encoding="utf-8") as f:
        f.write(f"# {meta['title']}\n\n{meta['channel']} | {meta['upload_date']} | {meta['webpage_url']}\n\n")
        block, start = [], None
        for ln in lines:
            if start is None:
                start = ln["t"]
            block.append(ln["text"])
            if ln["t"] - start >= 30:
                f.write(f"[{stamp(start)}] {' '.join(block)}\n\n")
                block, start = [], None
        if block:
            f.write(f"[{stamp(start)}] {' '.join(block)}\n\n")

    cols = sb["columns"]
    with open(os.path.join(out, "study.md"), "w", encoding="utf-8") as f:
        f.write(f"# {meta['title']}\n\n{meta['channel']} | {meta['upload_date']} | {meta['webpage_url']}\n\n"
                f"Frames are YouTube's storyboard: {sb['width']}x{sb['height']}, {sb['rows']}x{cols} per sheet, "
                f"read left to right, top to bottom. Under each frame, the words said until the next one.\n\n")
        starts = [t for _, ts in sheets for t in ts]
        k = 0
        for path, ts in sheets:
            f.write(f"## sheets/{os.path.basename(path)}  [{stamp(ts[0])} - {stamp(ts[-1])}]\n\n")
            for j, t0 in enumerate(ts):
                if t0 > (meta["duration"] or 1e9):
                    break
                t1 = starts[k + 1] if k + 1 < len(starts) else 1e9
                said = " ".join(ln["text"] for ln in lines if t0 <= ln["t"] < t1)
                f.write(f"- row {j // cols + 1} col {j % cols + 1} [{stamp(t0)}] {said}\n")
                k += 1
            f.write("\n")
    print(f"OK {vid} {meta['title']!r}: {len(sheets)} sheets ({len(starts)} frames), {len(lines)} caption lines"
          + ("" if lines else " (NO CAPTIONS)"))


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
