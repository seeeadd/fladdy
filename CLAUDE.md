# Fladdy (Slides That Sell): instructions for Claude

Fladdy is After Harvest's slide machine: webinar slides and YouTube slides, built on Jason Fladlien's method
(and later Jeremy Haynes, Maciek and other coaches) and the After Harvest brand. It is the sister of the
outreach thumbnail factory (`seeeadd/outreach-thumbnail-factory`) and works the same way: every fix goes
into a rule, a template or a script, so every deck gets it.

Why it exists (Sean, 2026-10-28), in order:
1. content (YouTube videos) with perfect positioning, on our own slides
2. the VSL updated to match
3. outreach again, pitching January launches

## Where things are

| path | what |
|---|---|
| `sources/` | what we learn from, never edited. One folder per coach. A source is cited by file + timestamp |
| `sources/fladlien/notes/full-methodology.md` | copy of the Google Doc "Full Jason Fladlien Methodology" (hooks, pain, curiosity, excite, positioning, paradigm, commitment, close, offer, price, bonuses, risk, scarcity). The doc is the master |
| `jason-fladlien-videos/` | the four Jason videos as study files, one folder each (`NN Title (id)/`: transcript, frame study, frames); README lists them |
| `sources/videos/<id>/` | one YouTube video as a study file (below) |
| `rulings.md` | Sean's answers to "what does Jason mean here?" and every standard he sets. **A ruling beats a source** |
| `scripts/` | the machine |

**Designing any slide: follow `rules/slide-method.md` first** (start from the real line, Jason's "how do we show this?", the human-touch rules, the template tells to avoid). Layouts live in `templates/youtube/` (`theme.css`, `ink.js` for hand marks), rendered with `python3 scripts/render_slides.py <file.html> [--out DIR]`.

Still to come (do not invent them early): `teardowns/` (one per video), `rules/` (slide rules: Jason, brand,
YouTube), `brand/` (the After Harvest kit for slides), `templates/` (the slide layouts), `playbooks/` (one per
webinar section, for the webinar machine).

## Studying a video

`python3 scripts/ingest_youtube.py <url or id> [...]` writes `sources/videos/<id>/`:
`meta.json`, `transcript.json` + `transcript.md` (YouTube's captions with times), `sheets/S00.jpg...`
(YouTube's storyboard: 3x3 frames per sheet, 320x180 each, about 10 s apart) and `study.md` (each frame's
time and the words said over it). It works in a cloud session, where YouTube blocks the video itself; the
script's first lines say how. Read `study.md` next to the sheets: one sheet is about 90 seconds.

Small text on a slide can be unreadable at 320x180. When a teardown needs a slide sharp, run
`python3 scripts/ingest_video.py <url>` on a Mac (full 1080p frames at every slide change; needs
`brew install yt-dlp ffmpeg`).

Cloud setup: `pip install yt-dlp` (node and Chromium are already there).

## Rules for every piece of work here

- Every rule cites where it came from (file + timestamp, or a ruling with its date). Unknown stays out.
- When unsure what a coach means, ask Sean with the timestamp and the frame, then write his answer in
  `rulings.md` with his words and the date. Never guess and build on the guess.
- When Sean sets a new standard, write it into the rules and `rulings.md` in the same turn.
- Keep messages to Sean plain and short: what is done, what is next, what only he can give.
