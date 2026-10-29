"""Check a teardown.md against the SOP (sops/video-teardown.md, step 4) before it ships.

    python3 scripts/check_teardown.py [--quick] [<video folder or teardown.md> ...]   (no folder: every teardown)

FAIL: a template section is missing, or a frame sheet is not in the appendix log (the distinct/ sheets when the log
uses them, else sheets/; --quick, the quick mode of the SOP, only needs the appendix to exist).
WARN: few [m:ss] stamps, or an em dash in our own writing (above the appendix). Exit code = number of FAILs. 0 tokens.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTIONS = ["# Teardown:", "## In one paragraph", "## Chapter map", "## The frameworks", "## Every number",
            "## The process, in order", "## Stories and examples", "## Lines worth keeping", "## What is on screen",
            "## How he sells inside the video", "## For After Harvest", "## Where he differs from",
            "## Questions for Sean", "## Candidate rules", "## Appendix: frame log"]


def check(path, quick=False):
    folder = path if os.path.isdir(path) else os.path.dirname(path)
    td = os.path.join(folder, "teardown.md")
    name = os.path.relpath(folder, ROOT)
    if not os.path.exists(td):
        print(f"FAIL {name}: no teardown.md")
        return 1
    text = open(td).read()
    fails = 0
    for s in SECTIONS:
        if not re.search(r"^" + re.escape(s), text, re.M):
            print(f"FAIL {name}: missing section '{s}'")
            fails += 1
    body, _, appendix = text.partition("## Appendix: frame log")
    logged = set(re.findall(r"^#+ *([SD]\d\d)\b", appendix, re.M))
    kind = "distinct" if any(x.startswith("D") for x in logged) else "sheets"
    sheets = sorted(os.path.basename(f)[:-4] for f in glob.glob(os.path.join(folder, kind, "[SD]*.jpg")))
    missing = [] if quick else [x for x in sheets if x not in logged]
    if missing:
        print(f"FAIL {name}: {len(missing)} of {len(sheets)} {'storyboard' if kind == 'sheets' else kind} sheets not in the frame log ({', '.join(missing[:8])}"
              f"{'...' if len(missing) > 8 else ''})")
        fails += 1
    stamps = len(re.findall(r"\[~?\d{1,2}:\d\d(?::\d\d)?", body))
    if stamps < 40:
        print(f"WARN {name}: only {stamps} timestamps above the appendix")
    dashes = body.count("—")
    if dashes:
        print(f"WARN {name}: {dashes} em dashes above the appendix")
    if not fails:
        what = "quick mode" if quick else f"{len(sheets)}/{len(sheets)} {'storyboard' if kind == 'sheets' else kind} sheets logged"
        print(f"PASS {name}: {len(SECTIONS)} sections, {what}, {stamps} stamps, "
              f"{text.count(chr(10))} lines")
    return fails


def main():
    quick = "--quick" in sys.argv
    paths = [a for a in sys.argv[1:] if a != "--quick"] or \
        sorted(os.path.dirname(p) for p in glob.glob(os.path.join(ROOT, "*-videos", "*", "teardown.md")))
    sys.exit(sum(check(p, quick) for p in paths))


if __name__ == "__main__":
    main()
