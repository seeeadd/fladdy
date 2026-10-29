"""Build the After Harvest YouTube slide kit as a folder and one zip, from the repo (0 tokens, a few seconds).

    python3 scripts/make_brand_kit.py

Writes brand-kit/ (the folders listed in brand-kit-src/README.md) and brand-kit/AfterHarvest-YouTube-Slide-Kit.zip,
for the Drive folder "AFTERHARVEST BRAND KIT". brand-kit/ is rebuilt every run and kept out of git; its sources live
in templates/youtube/ (fonts, art/photo, art/figma, art/stitch-kit, art/real, renders/youtube-light), brand-kit-src/
and guide/ (run guide/build_guide.py first so the PDF is current).
"""
import os, re, shutil, zipfile
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Y = os.path.join(ROOT, "templates", "youtube")
OUT = os.path.join(ROOT, "brand-kit")
ZIP = "AfterHarvest-YouTube-Slide-Kit.zip"

FONTS = ["Olivera-Demo.ttf", "Olivera-Oblique-Demo.ttf", "Literata.ttf", "Literata-Italic.ttf",
         "HankenGrotesk-Variable.ttf", "HankenGrotesk-Italic-Variable.ttf", "IBMPlexMono-Medium.ttf",
         "OFL-HankenGrotesk.txt"]
PROPS = ["wheat", "hat", "folder", "receipt", "graph", "tape1", "tape2", "tickets", "envelope", "planner"]
FIGMA_STITCH = ["stitch-check-olive-cut", "stitch-flower-pink", "stitch-flower-set-12", "stitch-icons-watch-video-ad-money",
                "stitch-number-1-rust", "stitch-sprig-olive-lilac", "scarecrow-dark-coat"]
MARKS = ["hand-arrow-loop-olive-cut", "hand-circle-olive-cut"]


def cp(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(src, "rb") as a, open(dst, "wb") as b:
        b.write(a.read())


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    cp(os.path.join(ROOT, "brand-kit-src", "README.md"), os.path.join(OUT, "README.md"))
    pdf = os.path.join(ROOT, "guide", "Fladdy-Slide-Guide.pdf")
    if os.path.exists(pdf):
        cp(pdf, os.path.join(OUT, "0 guide", "Fladdy-Slide-Guide.pdf"))
    for f in FONTS:
        cp(os.path.join(Y, "fonts", f), os.path.join(OUT, "1 fonts", f))
    for f in ["tokens.json", "colors.css"]:
        cp(os.path.join(ROOT, "brand-kit-src", f), os.path.join(OUT, "2 colours and type", f))
    props = os.path.join(OUT, "3 props (Canva photo cut-outs)")
    for f in PROPS:
        cp(os.path.join(Y, "art", "photo", f + ".png"), os.path.join(props, f + ".png"))
    cp(os.path.join(Y, "art", "photo", "SOURCES.md"), os.path.join(props, "SOURCES.md"))
    stitch = os.path.join(OUT, "4 stitch art")
    for f in sorted(os.listdir(os.path.join(Y, "art", "stitch-kit"))):
        cp(os.path.join(Y, "art", "stitch-kit", f), os.path.join(stitch, f))
    for f in FIGMA_STITCH:
        cp(os.path.join(Y, "art", "figma", f + ".png"), os.path.join(stitch, f + ".png"))
    for f in ["scarecrow-ink-coat.svg", "scarecrow-lilac.svg", "ah-mark.svg"]:
        cp(os.path.join(Y, "art", f), os.path.join(stitch, f))
    for f in MARKS:
        cp(os.path.join(Y, "art", "figma", f + ".png"), os.path.join(OUT, "5 hand marks", f + ".png"))
    for f in sorted(os.listdir(os.path.join(Y, "art", "real"))):
        cp(os.path.join(Y, "art", "real", f), os.path.join(OUT, "6 real pictures", f))
    cp(os.path.join(Y, "art", "sean-cam.jpg"), os.path.join(OUT, "7 face cam", "sean-cam-placeholder.jpg"))
    refs = os.path.join(OUT, "8 slide references (light set)")
    os.makedirs(refs, exist_ok=True)
    src = os.path.join(Y, "renders", "youtube-light")
    for f in sorted(os.listdir(src)):
        if f.endswith(".png"):
            Image.open(os.path.join(src, f)).convert("RGB").save(os.path.join(refs, f[:-4] + ".jpg"), quality=88)

    # 9: the light set as a working template: open youtube-light.html in Chrome, or render it with
    # scripts/render_slides.py. Only the files it loads are copied, at the same relative paths.
    tpl = os.path.join(OUT, "9 slide templates (HTML)")
    html = open(os.path.join(Y, "youtube-light.html")).read()
    for f in ["youtube-light.html", "theme.css", "ink.js", "stitch.js", "lib/rough.js", "lib/rough-LICENSE.txt"]:
        cp(os.path.join(Y, f), os.path.join(tpl, f))
    for f in sorted(os.listdir(os.path.join(Y, "fonts"))):
        cp(os.path.join(Y, "fonts", f), os.path.join(tpl, "fonts", f))
    for ref in sorted(set(re.findall(r'src="(art/[^"]+)"', html))):
        cp(os.path.join(Y, ref), os.path.join(tpl, ref))
    cp(os.path.join(ROOT, "brand-kit-src", "TEMPLATES.md"), os.path.join(tpl, "README.md"))

    files = sorted(os.path.join(d, f) for d, _, fs in os.walk(OUT) for f in fs)
    with zipfile.ZipFile(os.path.join(OUT, ZIP), "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(f, os.path.join("AfterHarvest YouTube Slide Kit", os.path.relpath(f, OUT)))
    size = os.path.getsize(os.path.join(OUT, ZIP)) / 1e6
    print(f"OK brand-kit/: {len(files)} files; {ZIP} {size:.1f} MB")


if __name__ == "__main__":
    main()
