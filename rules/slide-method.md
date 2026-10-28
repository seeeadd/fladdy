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
  it full size, cut it out (`rembg`, `isnet-general-use`), give it a soft two-layer drop shadow. These live
  in `templates/youtube/art/photo/`.
- **Wide margins (112px), nothing collides, the headline has its own space.** Headlines hand-broken.
- **One precise hand mark at most**: the website's underline path (`.u`), never a scribble.
- **No handwriting font, no messy collage.** Order with a slight tilt reads human; disorder reads unfinished.
- **The facecard shows Sean's photo in previews** (`art/sean-face-preview.png`) so a slide reads as finished.
- **Deliver each slide on its own**, full size, no contact-sheet frame.

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
