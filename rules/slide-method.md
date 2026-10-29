# How a Fladdy slide is designed (round 4, 2026-10-28)

Rounds 1 and 2 were rejected: "too much like Claude", "templateized", "not derived from Jason or Deya",
"doesn't feel human-touched". This is the method that replaced them. Every slide goes through it.

## 1. Start from the real line, never from a layout

Take the exact line from the script (the VSL deck, the video outline). Write down:
- **The belief**: what the viewer must believe after this slide ("they chose me", "my quarter is full").
- **How do we show this?** Jason asks it of every slide (slide video 37:00). The answer is a real thing:
  their inbox, their planner, the screenshot, the receipt. Not a metaphor, not stock, not an AI picture
  (19:05, 20:17: "screenshots are your best friend").
- **The build**: the order things appear in as it is said (Jason: motion every ~6 s; the brief: "each one pops up").

Only then pick the layout.

## 2. Jason's rules that decide the layout

- The most important words are the biggest; titles like "here's what you'll discover" go small (1:47).
- One idea per slide; slides are free, split rather than crowd (6:05).
- Lists read top to bottom (1:29).
- Two colours: ink plus the one accent on the words that matter (6:45).
- The reveal: duplicate the slide, lay ~80% paper over it, put the new line on top (31:24).
- The framework slide comes back each section with progress (23:20).
- Tease later slides in the intro, cut off at the edge (3:01).

## 3. Nicely made first (round 4 ruling: "it looks messy... doesn't look nicely made")

- **One focal object per slide, shot like a product photo**: a real-looking envelope, planner, phone. Generate
  it (Canva generate-image; the brief: "combine it with Google Gemini AI for more realistic images"), export
  it full size, cut it out (`rembg`: `isnet-general-use`; for a light object on a light ground use `birefnet-general-lite`, isnet dropped the lower tickets), give it a soft two-layer drop shadow. These live
  in `templates/youtube/art/photo/`.
- **Wide margins (112px), nothing collides, the headline has its own space.** Headlines hand-broken.
- **One precise hand mark at most**: the website's underline path (`.u`), never a scribble.
- **No handwriting font, no messy collage.** Order with a slight tilt reads human; disorder reads unfinished.
- **The facecard shows Sean's photo in previews** (`art/sean-face-preview.png`) so a slide reads as finished.
- **Deliver each slide on its own**, full size, no contact-sheet frame.

## 3b. The YouTube look: dark stage + the object (ruling 2026-10-28, "i like the idea of b and c")

The light set was "boring af" and the three directions "placeholders". What fixed it, in `youtube-dark.html`:
- **The stage**: warm near-black `#1D1914`, a soft gold spotlight behind the focal object (`--gx/--gy`), a 6% dot grid.
  Type is eggshell; the subhead is Literata italic `#CFC6B4`.
- **One gold moment per slide** (`#E8A100`): the lit B, the word FREE, the highlighted line in the post. Never two.
- **The object carries real detail**: the tickets have "Admit one · live online" and "No. 0001" printed on them,
  rotated with the paper (-8.6deg); the post is the real post with its real numbers. A blank box reads as a placeholder.
- **The object repeats**: the quiz tickets come back as the Day 1-3 agenda (Jason 23:20, the framework returns).
- **Faded wrong answer, lit right one**: the outlined A beside the gold B.
- White cards (posts, the website) sit under the light with a deep shadow, so they glow off the stage.

## 3c. The layout library (ruling 2026-10-28, "real nice templates with interesting layouts")

Pick each slide's layout from `templates/youtube/layouts.html` by the job the line does, never one layout for a
whole video (five slides of "headline left, object right" was the miss):

| layout | job | camera |
|---|---|---|
| L01 cold open | the hook question | huge circle, right half |
| L02 the map | where we are (returns each part, Jason 23:20) | circle, top right |
| L03 chapter | the pattern interrupt between parts | box inside a colour panel |
| L04 the turn | "But..." | small, bottom right |
| L05 the number | one number is the point | overlaps the number |
| L06 step + screen | a step shown on the real screen, loupe on the detail | box, bottom left |
| L07 side label | proof, taped on | circle, top right |
| L08 split | two choices, two grounds | on the seam |
| L09 list | top to bottom, the current point lit | huge, off the right edge |
| L10 quote | their real words | small, bottom right |
| L11 story break | a story starts | centred under the title |
| L12 reveal | the answer over the washed slide (31:24) | stays sharp |
| L13 calendar | time made visible | bottom left |
| L14 end screen | YouTube's last 5-20 s, two video tiles | bottom left |

The camera preview is `art/sean-cam.jpg` (from the factory's `template/youtube/sean_profile.webp`); in the edit the
live camera goes there.

## 3d. Why it still read as Claude, and the light set that answers it (ruling 2026-10-28)

The dark library still "looked very Claude". The tells, now banned:
- **The caps label / serif headline / italic line stack** on slide after slide (a spaced-out mono caps label over
  every title). Deya never does it. Her titles mix three voices at three sizes: a small lead-in, a huge word, a
  script line, sometimes a tiny aside in brackets.
- **Tasteful and empty**: one object, lots of air, nothing funny. Deya's slides are full and a little playful: the
  cat in the crown, the graduation cap on her own head, leaves and pears at the edges, grid paper, tape, a sticker.
- **Website parts rebuilt as boxes.** Real things (a taped screenshot, a stitched number on graph paper) instead.

The light set (`youtube-light.html`, 11 slides) is the recipe:
- Type: Literata italic lead-in (sentence case), Hanken Grotesk 900 for the shout (caps or lowercase), Olivera or
  Olivera Oblique for the script line, IBM Plex Mono in sentence case for typewriter body, underlined.
- After Harvest's own hand: the cross-stitch. `stitch.js` stitches any number or short word
  (`<div data-stitch="$100K" data-cell="15" data-color="#C98A1E">`); the stitch icons (flower, sprig, check) are
  the little marks; the stitched scarecrow is the character.
- Harvest props at the edges (wheat, kraft folders, tickets) and on the face (the straw hat on story slides);
  `art/photo/SOURCES.md` lists each with its Canva media id.
- Grounds: warm paper, sage and rust panels or bands; the face big, unframed, soft shadow.

## 3e. Real pictures, real screenshots (ruling 2026-10-29)

Sean on the light set: "in my slides, there to be real pictures, real screenshots... more texture or a bit more
content, more text maybe", then "you can get real pics from online even if they are placeholders".
- Every story or proof slide carries at least one real picture. Best first: our own (a lead's page, our event's
  ticket, a client's post, our chat with them; the VSL file in Figma holds many), then a free stock photo as a
  placeholder (`stock-*` in the name, so it is easy to find and swap).
- Show them as objects: a print (`.prt`, white border, layered shadow), tilted 2-6 degrees, overlapping a little,
  pinned or sewn on (3f; the tape and the highlighter swipe of the first try are retired).
- Under each one, a one-line source in Plex Mono (`.src`): where it is from and its date ("x.com/jayclouse, 9:45
  PM, 7/9/26"). Proof without a source reads as made up.
- More text means a caption per picture (a bold line + one typewriter line), not a paragraph.
- Never retype a screenshot as boxes, never a fake UI. A small source image is upscaled once (2x Lanczos +
  unsharp) and shown no bigger than it reads.
- Every file and its source: `templates/youtube/art/real/SOURCES.md`. Closed from a cloud session: Unsplash,
  Pexels, Pixabay, Freepik; picjumbo works with curl.

## 3f. Our own hand: needlework, not stationery (rulings 2026-10-29)

Sean on the real-picture slides: "a little bit too simple... they look very AI-edited... I was expecting something
leaning towards Deya... make it our own... not a fan of putting tapes on the pictures. They're very generic... we
really need a bit more human touch", then "can you not use Canva elements?". The audit of Deya is
`sources/inspiration/deya/AUDIT.md`; this is what we take and what we make our own.

Deya's look is stationery: paper, tape labels, binder clips, a pen, her cat. After Harvest's is needlework, because
the brand already is (the cross-stitch icons; the stitched "AD" struck through with a real red thread). So:
- **The hand is thread** (`thread.js`): a running-stitch loop round the line that matters, a stitched arrow, one
  laid red thread joining a claim to its proof, a long straight stitch through what is wrong (the brand's "AD").
  Never a pen doodle, never a highlighter.
- **Things are pinned or sewn on**: a pearl-head pin through a print's corner, a running stitch round a print
  (`data-sew`), one cross-stitch tacking a ticket down. Never tape, never a clip.
- **Labels are woven**, the kind sewn into a collar (`.wl` + `data-tack`), in mono caps.
- **The face sits in an embroidery hoop** (`data-hoop`), and things touch it: the seam ends at it, the hem runs
  behind it, a thread is tied to it.
- **Numbers are cross-stitched** (`stitch.js`).
- **Grounds are cloth where it helps**: a sage linen band with a frayed edge and a sewn hem, aida cloth, two
  pieces of the page sewn together down a seam. Partial, never every slide.
- **Harvest things carry the content**: a list as seed packets ("sow: day 1, harvest: day 3"), hung from one
  thread.
- **One joke per video**: the crow (the brand's character is a scarecrow), standing on the thing it mocks.
- **No Canva-made elements.** The marks, cloth, pins, labels, packets and hoop are drawn in code (`thread.js`,
  `sewn.css`); objects are real photos with a licence (pxhere and ISO Republic are CC0; `art/real/SOURCES.md`).
  The Canva props of the light set (wheat, hat, graph paper, tape, folders, tickets) are retired.
- The set: `templates/youtube/youtube-sewn.html`.

## 4. What makes it look human (Deya, the brief, Mino)

- **The real artefact is the picture**: Deya shows her actual task list, her actual bookshelf.
- ~~Messy on purpose~~ (tried in round 3 from the brief's "messy looking" note; Sean rejected it). A slight
  tilt on each sticky or card is enough.
- **Hand marks are drawn, not shapes**: circles, underlines, arrows and boxes come from `ink.js` (rough.js),
  or are the real hand-drawn marks from Figma. A circle never crosses the letters it marks.
- Hand notes in Virgil are for the Figma whiteboards (Mino look) only, not for the Canva title pages.
- **The face is part of it**: the facecard overlaps the inbox, sits in front of the planner. Same spot on
  every slide (the brief: space for Sean's facecard), but things touch it.

## 5. The tells of a template (never)

- the label / headline / italic line stack on every slide
- a row of identical cards, evenly spaced
- the same soft shadow on everything, confetti sprinkled to fill space
- invented copy; a fake fact
- every headline with one italic accent word by reflex

## Type

Olivera headlines (thickened like the website), Literata subheadings, Hanken Grotesk body, IBM Plex Mono
labels, Virgil for hand notes. The Olivera demo has no punctuation: `ink.js` sets the Literata stand-in tight.
