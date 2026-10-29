"""Check the playbooks in playbooks/ against their format (playbooks/_how-to-write.md).

    python3 scripts/check_playbooks.py [file ...]      (no argument: every playbook)

FAIL: a required section is missing, or there are no citations. WARN: em dashes, or a length far outside
800-1,800 words. Exit code = number of FAILs. 0 tokens.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTIONS = ["Read this when:", "## In 5 lines", "## The rules", "## How to do it", "## Examples",
            "## Mistakes he calls out", "## Lines worth keeping", "## After Harvest", "## Open questions for Sean"]


def check(path):
    name = os.path.basename(path)
    text = open(path).read()
    fails = 0
    for s in SECTIONS:
        if s not in text:
            print(f"FAIL {name}: missing '{s}'")
            fails += 1
    cites = len(re.findall(r"\[(?:doc L|Jason |Jeremy |ruling )", text))
    if not cites:
        print(f"FAIL {name}: no citations")
        fails += 1
    words = len(text.split())
    if text.count("—"):
        print(f"WARN {name}: {text.count(chr(8212))} em dashes")
    if not 600 <= words <= 3000:
        print(f"WARN {name}: {words} words")
    if not fails:
        print(f"PASS {name}: {words} words, {cites} citations")
    return fails


def main():
    files = sys.argv[1:] or sorted(f for f in glob.glob(os.path.join(ROOT, "playbooks", "*.md"))
                                   if not os.path.basename(f).startswith(("_", "README", "core")))
    sys.exit(sum(check(f) for f in files))


if __name__ == "__main__":
    main()
