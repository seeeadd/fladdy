"""Render every <section class="slide"> of an HTML file to its own 1920x1080 PNG, plus one contact sheet.

    python3 scripts/render_slides.py templates/youtube/title-pages.html [--out DIR]

Writes <out>/<section id>.png and <out>/sheet.jpg (default out: <html folder>/renders/). 0 tokens.
"""
import os, sys
from PIL import Image
from playwright.sync_api import sync_playwright

CHROMIUM = "/opt/pw-browsers/chromium" if os.path.exists("/opt/pw-browsers/chromium") else None


def render(html, out):
    os.makedirs(out, exist_ok=True)
    paths = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROMIUM)
        pg = b.new_page(viewport={"width": 1920, "height": 1080})
        pg.goto("file://" + os.path.abspath(html))
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(600)
        for i, el in enumerate(pg.query_selector_all("section.slide")):
            sid = el.get_attribute("id") or f"s{i + 1}"
            path = os.path.join(out, f"{sid}.png")
            el.screenshot(path=path)
            paths.append(path)
        b.close()
    cols, w, h, gap = 2, 960, 540, 16
    rows = (len(paths) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w + (cols + 1) * gap, rows * h + (rows + 1) * gap), "#d9d4c9")
    for i, path in enumerate(paths):
        sheet.paste(Image.open(path).convert("RGB").resize((w, h), Image.LANCZOS),
                    (gap + (i % cols) * (w + gap), gap + (i // cols) * (h + gap)))
    sheet.save(os.path.join(out, "sheet.jpg"), quality=88)
    print(f"{len(paths)} slides -> {out}")


if __name__ == "__main__":
    args = sys.argv[1:]
    out = None
    if "--out" in args:
        i = args.index("--out")
        out = args[i + 1]
        del args[i:i + 2]
    for html in args:
        render(html, out or os.path.join(os.path.dirname(html), "renders"))
