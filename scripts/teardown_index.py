"""TEARDOWNS.md: one page linking every video, its transcript and its teardown (SOP: sops/video-teardown.md, step 5).

    python3 scripts/teardown_index.py

Scans every <coach>-videos/NN Title (id)/ folder and rewrites TEARDOWNS.md at the repo root. A video without a
teardown.md yet is listed as "not yet". 0 tokens. Run it after every teardown, before the commit.
"""
import json, os, re
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def clock(sec):
    sec = int(sec)
    h, m, s = sec // 3600, sec % 3600 // 60, sec % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def link(path):
    return quote(path)


def summary(teardown):
    """The first sentence of the teardown's 'In one paragraph' section."""
    text = open(teardown).read()
    m = re.search(r"## In one paragraph\s+(.+?)(?:\n\n|\n## )", text, re.S)
    if not m:
        return ""
    para = " ".join(m.group(1).split())
    first = re.split(r"(?<=[.!?])\s", para)[0]
    return re.sub(r"\s*\[[^\]]*\]", "", first)


def main():
    lines = ["# Teardowns", "",
             "Every video we study, its transcript and its teardown, one row each. Rebuilt by "
             "`python3 scripts/teardown_index.py` (sops/video-teardown.md). Add a video by pasting its YouTube link "
             "into a Claude Code chat on this repo.", ""]
    total = done = 0
    for coach in sorted(d for d in os.listdir(ROOT) if d.endswith("-videos") and os.path.isdir(os.path.join(ROOT, d))):
        videos = sorted(f for f in os.listdir(os.path.join(ROOT, coach)) if re.match(r"\d\d ", f))
        if not videos:
            continue
        name = coach[:-len("-videos")].replace("-", " ").title()
        lines += [f"## {name}", "", "| # | video | length | teardown | transcript | what it is |", "|---|---|---|---|---|---|"]
        for v in videos:
            folder = os.path.join(ROOT, coach, v)
            meta = json.load(open(os.path.join(folder, "meta.json")))
            rel = f"{coach}/{v}"
            td = os.path.join(folder, "teardown.md")
            total += 1
            if os.path.exists(td):
                done += 1
                tlink, what = f"[teardown]({link(rel + '/teardown.md')})", summary(td)
            else:
                tlink, what = "not yet", ""
            lines.append(f"| {v[:2]} | [{meta['title']}]({meta.get('webpage_url', '')}) | {clock(meta.get('duration') or 0)} "
                         f"| {tlink} | [transcript]({link(rel + '/transcript.md')}) | {what} |")
        lines.append("")
    lines += [f"{done} of {total} videos torn down.", ""]
    open(os.path.join(ROOT, "TEARDOWNS.md"), "w").write("\n".join(lines))
    print(f"TEARDOWNS.md: {done}/{total} torn down")


if __name__ == "__main__":
    main()
