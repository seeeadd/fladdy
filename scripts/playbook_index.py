"""playbooks/README.md: which playbooks to read for which job, and every playbook with its word count.

    python3 scripts/playbook_index.py

Rebuild it after a playbook is added or changed. 0 tokens.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "playbooks")

GROUPS = [("Plan a whole webinar, VSL or long video", ["webinar-map"]),
          ("The parts of a webinar, VSL or video, in order",
           ["hooks", "pain", "curiosity", "excite", "positioning", "paradigm", "commitment", "close"]),
          ("The offer", ["offer", "price", "bonuses", "risk", "scarcity"]),
          ("Format", ["slides", "youtube"]),
          ("The funnel around it", ["funnel-numbers"])]

JOBS = [("a YouTube video", "core, youtube, hooks, curiosity, slides; plus the part you are writing"),
        ("the VSL", "core, webinar-map, hooks, pain, positioning, paradigm, close, offer"),
        ("a webinar or Day 1-3 deck", "core, webinar-map, slides; then the playbook for each part as you reach it"),
        ("an offer or pitch slide", "core, offer, price, bonuses, risk, scarcity, close"),
        ("any slide design", "core, slides (and `rules/slide-method.md`)"),
        ("funnel numbers, a calculator, a diagnosis", "core, funnel-numbers")]

HEAD = """# Playbooks

The distilled version of everything Fladdy has learned: Sean's Jason Fladlien methodology doc (65,000 words) and the
video teardowns (55,000 words), cut to one short file per topic, every point cited back to its source. A new chat
reads `core.md` (one page), then only the files its task needs, about 5,000 words instead of 120,000. The sources
stay the master: go there only to check a quote.

## Which files for which job

| job | read |
|---|---|
"""

TAIL = """
## How they are made and kept

- Format, citations and style: [`_how-to-write.md`](_how-to-write.md). Citations: `[doc L1234]` is a line of
  `sources/fladlien/notes/full-methodology.md`; `[Jason slides 16:06]` is a timestamp in that video's teardown (see
  `TEARDOWNS.md`); `[ruling 2026-10-28]` is a row of `rulings.md`.
- `python3 scripts/check_playbooks.py` checks every file has its sections and citations;
  `python3 scripts/playbook_index.py` rebuilds this page.
- When Sean answers an open question: write it in `rulings.md`, update the playbook it changes (and `core.md` if it
  is a big one), so every chat after that gets it.
- When a new video is torn down: fold anything new into the playbooks it touches, cited to its teardown.
"""


def when(text):
    m = re.search(r"Read this when:(.*?)(?=\nSources:|\n\n)", text, re.S)
    return " ".join(m.group(1).split()) if m else ""


def main():
    out = [HEAD + "\n".join(f"| {a} | {b} |" for a, b in JOBS), "", "## Every playbook", "",
           "| file | read it when | words |", "|---|---|---|"]
    core = os.path.join(DIR, "core.md")
    if os.path.exists(core):
        out.append(f"| [core.md](core.md) | always, first | {len(open(core).read().split()):,} |")
    for group, files in GROUPS:
        out.append(f"| **{group}** | | |")
        for f in files:
            p = os.path.join(DIR, f + ".md")
            if os.path.exists(p):
                t = open(p).read()
                out.append(f"| [{f}.md]({f}.md) | {when(t)} | {len(t.split()):,} |")
            else:
                out.append(f"| {f}.md | not written yet | |")
    open(os.path.join(DIR, "README.md"), "w").write("\n".join(out) + "\n" + TAIL)
    print("playbooks/README.md rebuilt")


if __name__ == "__main__":
    main()
