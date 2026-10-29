"""Print guide/slide-guide.html to guide/Fladdy-Slide-Guide.pdf (A4, page numbers in the footer). 0 tokens.

    python3 guide/build_guide.py
"""
import os
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
CHROMIUM = "/opt/pw-browsers/chromium" if os.path.exists("/opt/pw-browsers/chromium") else None
FOOT = ('<div style="width:100%;font-family:monospace;font-size:7px;color:#6E6554;padding:0 16mm;display:flex;'
        'justify-content:space-between"><span>Slides that sell · the Fladdy slide guide</span>'
        '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROMIUM)
    pg = b.new_page()
    pg.goto("file://" + os.path.join(HERE, "slide-guide.html"))
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(800)
    out = os.path.join(HERE, "Fladdy-Slide-Guide.pdf")
    pg.pdf(path=out, format="A4", print_background=True, display_header_footer=True,
           header_template="<div></div>", footer_template=FOOT,
           margin={"top": "17mm", "bottom": "19mm", "left": "16mm", "right": "16mm"})
    b.close()
print("OK", out, os.path.getsize(out) // 1024, "KB")
