# The slide templates (the light set)

`youtube-light.html` holds the 11 approved YouTube slides, each one `<section class="slide">` of 1920 x 1080. Everything
it loads is in this folder at the same relative paths, so it works as is.

## To look at them

Open `youtube-light.html` in Chrome. Each slide is one 1920 x 1080 block, one under the other.

## To make a new slide from one of them

1. Copy the slide's whole `<section ...> ... </section>` (they are marked `<!-- 1 title -->`, `<!-- 2 agenda -->` ...).
2. Change the words (each text element is marked `data-edit`) and the pictures (`src="art/..."`; put a new picture
   in `art/real/` and add its source to `art/real/SOURCES.md`).
3. Positions and sizes are in the `<style>` block at the top, one group per slide (`.s1 ...`, `.s2 ...`).
4. Follow the guide (`0 guide/Fladdy-Slide-Guide.pdf`), part 4 and the part 5 checklist.

## To export them as pictures

In the repo (github.com/seeeadd/fladdy): `python3 scripts/render_slides.py templates/youtube/youtube-light.html`
writes one PNG per slide. In Chrome without the repo: a full-page screenshot, or DevTools > capture node screenshot on
one `<section>`.

## Files

| file | what |
|---|---|
| youtube-light.html | the 11 slides and their layout styles |
| theme.css | fonts, colours, the paper grain |
| ink.js | hand marks drawn with rough.js (`data-ink`), and Olivera's missing punctuation |
| stitch.js | cross-stitches any number or short word (`data-stitch="$100K"`) |
| lib/rough.js | the rough.js library (MIT, see its licence) |
| fonts/ | Olivera demo, Literata, Hanken Grotesk, IBM Plex Mono, Virgil |
| art/ | every picture the slides use |
