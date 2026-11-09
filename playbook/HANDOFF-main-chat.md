# Handoff: the main Fladdy chat (2026-10-28 to 2026-10-29)

For a fresh chat. It covers everything the first Fladdy chat built, decided and left open, so you can carry on without
reading that chat. Source: the claude.ai cloud session `session_011DXSQiHkohnvERXvgbS9yh`, "☎️ Webinarjam slides mastery
agent system". It ran from 2026-10-28 08:40 to 2026-10-29 06:56 UTC: 58 messages from Sean and 205 text replies. The
cleaned transcript is `playbook/transcripts/main-chat-digest-2026-10-28_to_10-29.md`. Written 2026-11-09.

**Where it stopped.** Sean asked where to get the guide PDF and the slide images. The last reply pointed him to the files
attached in chat and on GitHub, and said they can't go into Drive automatically. Nothing was mid-build. `main` was at
`9be3c17` ("Brand kit: add the light set as a working HTML template folder"), and the working branch
`claude/charming-maxwell-3aqibu` was the same commit.

**The next job, as the chat left it:** rebuild the four weak light-set slides (part two, proof, which one sells, why
events sell more) in the light set's own style. That means no tape, real screenshots, one funny cut-out per slide, and
the audit's fixes (builds, the mechanism slide, bigger type, two colours). Sean has not said "go" on this. Ask first, and
get answers to the open clashes below if you can.

## 1. What Fladdy is

After Harvest's slide machine: webinar slides and YouTube slides, built on Jason Fladlien's method. Later it adds Jeremy
Haynes, Maciek and other coaches, all in the After Harvest brand. Sean named it "Fladdy (Slides That Sell)" (README).
It works like its sister repo, the outreach thumbnail factory (`seeeadd/outreach-thumbnail-factory`): every fix becomes a
rule, a template or a script, so every deck after it gets the fix.

Why it exists, in Sean's order (2026-10-28 14:08): "1. Make content with perfect positioning 2. Update vsl accordingly 3.
Then do outreach again > pitching january launches". Content means YouTube videos on our own slides.

The first idea (2026-10-28 08:40) was bigger: a "webinar machine" with about 50 agents, one per section of Jason's
webinar, each a deep specialist. Sean wants the same depth of SOP as the thumbnail factory, and wants to be asked what
Jason means rather than have Claude guess. The chat recommended building in Claude Code on a GitHub repo, with sources,
playbooks per section, one agent per section, rulings that beat sources, two approval gates (brief, then deck) and
testing against Jason's real webinars. That machine is **not built yet**. On 2026-10-28 14:08 Sean switched to a slide
brand kit for YouTube first.

The people:
- **Sean**: the user. Runs After Harvest. The face on the YouTube slides (the face circle).
- **Stephanie**: After Harvest's designer, who made the Figma work.
- **Deya**: a YouTuber whose slide layouts are the visual inspiration ("Deya's peg, but in our brand, not girly, not the
  same aesthetic, more neutral and connected to After Harvest", from Sean's brief to his designer).
- **Jay Clouse**: a client. His "$100,000+ launch" post and chat are the real proof on the slides.
- **Coaches**: Jason Fladlien (slide method, webinar method), Jeremy Haynes (webinar funnel), Maciek (no material yet).

## 2. Where things live

### The repo

`seeeadd/fladdy`, private. Sean created it himself (2026-10-28 14:47), because GitHub would not let Claude create repos.

| path | what |
|---|---|
| `CLAUDE.md` | instructions for every chat; starts by pointing here |
| `rulings.md` | Sean's answers and standards, his words with dates. **A ruling beats a source** |
| `playbooks/` | the method cut to one short cited file per topic. `core.md` first, then what `README.md` lists for the job |
| `playbook/` | this handoff and `transcripts/` (Sean asked for the singular folder; it is not `playbooks/`) |
| `rules/slide-method.md` | how a slide is designed: start from the real line, "how do we show this?", what was tried and rejected |
| `audits/2026-10-29-light-set-vs-jason.md` | the light set checked slide by slide against Jason's slide teardown |
| `guide/Fladdy-Slide-Guide.pdf` | the 27-page slide guide (Jason's 34 rules, our look, layouts, process, checklists, 8 decisions); built by `guide/build_guide.py` from `guide/slide-guide.html` |
| `brand-kit-src/` | sources for the brand kit zip: `README.md` (colours, type, the rules in one place), `TEMPLATES.md`, `tokens.json`, `colors.css` |
| `templates/youtube/` | the slides in HTML. `youtube-light.html` is **the base**. Also `theme.css`, `ink.js` (rough.js hand marks), `stitch.js` (cross-stitched numbers), `thread.js` + `sewn.css` (the rejected sewn set), `stage.css` (dark), `art/`, `fonts/`, `lib/`, `renders/` |
| `templates/youtube/art/real/SOURCES.md` | where every real picture and stock placeholder came from. `art/photo/SOURCES.md` lists the Canva-generated props |
| `jason-fladlien-videos/`, `jeremy-haynes-videos/` | one folder per video, `NN Title (id)/`: transcript.md, study.md, sheets/, distinct/, teardown.md |
| `TEARDOWNS.md` | one page linking every video, its transcript and its teardown |
| `sops/video-teardown.md` + `.claude/skills/video-teardown/SKILL.md` | the video SOP and its skill: paste a YouTube link and it runs start to finish |
| `sources/fladlien/notes/full-methodology.md` | copy of Sean's Google Doc "Full Jason Fladlien Methodology" (about 65,000 words). The Doc is the master |
| `sources/inspiration/deya/` | 22 Deya videos as frame sheets, `best/` (the 24 best title layouts on one board), `AUDIT.md` (her look, detail by detail) |
| `assets/models/` | the face detector `distinct_sheets.py` uses |
| `scripts/` | the machine (section 7) |

The template sets in `templates/youtube/`, oldest first: `title-pages.html` (rounds 1-2), `vsl-opening.html` (VSL rounds
3-4), `youtube-launches-vs-events.html` ("boring af"), `directions.html` (A/B/C), `youtube-dark.html` (B+C dark stage),
`layouts.html` (14 layouts on the dark stage), `youtube-light.html` (**the base**), `youtube-sewn.html` (rejected).

### Outside the repo

Private links are not written here. Ask Sean for them, or find them by name.

| place | what is there |
|---|---|
| Google Drive, folder "AFTERHARVEST BRAND KIT" | Sean's brand kit: logo packages, colours, the scarecrow kit, guarantee badges, a design system. Subfolder `youtube-slides-kit` (made by the chat) holds a read-me Doc, the audit as a Doc, `tokens.json`, `colors.css`, and `templates (HTML)` (the light-set code plus a how-to Doc). **Not there yet:** the kit zip (36 MB) and the guide PDF. Sean has to drag those in himself |
| Google Doc "Full Jason Fladlien Methodology" | Jason's notes, the master of `sources/fladlien/notes/full-methodology.md` |
| Figma file "VSL (Copy)" | the VSL working canvas, Loom thumbnails, a brand note (colours, three fonts, "thread vs glass"), Sean's VSL lessons, and the source of the stitch art and the real screenshots |
| Canva: the VSL assets deck | Sean's raw VSL slides; pages 15-28 are his designer brief and notes. Read-only, never changed |
| Canva leftovers from the chat | "Fladdy assets (scratch)" (the generated props), "Presentation - Launch Lab: Why Live Events Sell More" (a generated candidate) and about 15 uploaded images. The connector can't delete them; Sean can |
| Canva brand kits | one called "Jay Clouse" and one with no name. Whether the unnamed one is After Harvest's was asked twice and never answered |
| theafterharvest.com | the site: Olivera, Literata, Plex Mono, Hanken Grotesk; offer "Get my free event plan" |

### Publishing rules (how the chat shipped work)

- Work on a `claude/...` branch, then commit and push after each finished piece. Sean asked "merge to main, make a folder
  for it" (2026-10-29 00:02), and from then on finished work went to `main`, followed by GitHub links to Sean. The video
  SOP merges to `main` on its own.
- Half-written files (agents still writing) go to the working branch marked "in progress". Never to `main` until checked.
- Each coach's videos get their own folder (`<coach>-videos/`), with a README listing them.
- Send slides one by one, full size, with no contact sheet and no grey border around them (ruling 2026-10-28).
- Always send the GitHub link. Sean asks "where is it / give me the link" often.
- No pull request unless Sean asks.
- **Drive:** the Drive connector can only create files by typing out their contents. Text and code work; images, fonts,
  PDFs and zips do not, and embedding an image in a Doc drops it too. Say so up front, and have Sean drag binaries in.
- **Canva:** the connector can't search Canva's Elements library, can't change fonts (so no Olivera), and can't delete
  designs or uploads. It is good for filling a slide that is already well designed, not for designing one.
- Large renders make pushes slow (the 14 layouts were about 19 MB). Report a push only once it has finished.

### Environment variables

None. No script reads an environment variable, and the chat set none (names or values). Cloud setup is
`pip install yt-dlp`. Node and Chromium are already there; Playwright's Chromium is at `/opt/pw-browsers/chromium`.

## 3. Timeline (UTC; commits are on `main`)

**2026-10-28**
- 08:40-08:47: the webinar-machine idea and its design (sources, playbooks, agents, rulings, two gates, answer key).
- 14:08: the switch to a YouTube slide brand kit; the three goals. 14:28: the name, Jason's notes Doc, the Figma file and
  Jason's four video links. 14:36: the Drive brand kit.
- 14:38: the chat said YouTube blocks the cloud machine and "that path is closed". 14:46: Sean pushed back. By 15:00 all
  four Jason videos were study files (storyboard frames plus captions via an embedded player). Commit `945f849`.
- 15:07-15:14: Sean's designer brief; Deya's 22 videos pulled and her 24 best layouts put on one board (`43ba78f`).
  The Olivera demo turns out to have no punctuation.
- 15:17: Sean: don't buy Olivera; drafts take "15 minutes tops"; YouTube slides simpler, "just the foundations".
- 15:20 round 1 (`422920f`), 15:28 round 2 (`4c37e3e`): rejected as "too much like Claude... templateized".
- 15:39 round 3 on the real VSL lines (`d3557d9`, `rules/slide-method.md` started): rejected as "messy".
- 15:47-16:15 round 4, clean, one photo object per slide (Canva-generated envelope and planner): Sean said "1. give
  me the templates" (`b9f4b17`, `ba4706c`). 16:16: "put them in canva" plus a hypothetical YouTube video.
- 16:38: the YouTube set was "boring af". 16:40: three directions (`0f291d9`) were "placeholders"; Sean liked B and C.
- 16:45: dark stage set (`810acfd`). 16:46: "When are you going to make the real nice templates with interesting
  layouts?" 16:55: 14-layout library (`4b7035a`).
- 17:29: "Can you make a light one?... It still looks very Claude." 23:48: the light set, 11 slides, Canva-generated
  props, the brand's cross-stitch (`1ffd718`).
- 23:51: Sean: more real, "real pictures, real screenshots"; flagged four slides.

**2026-10-29**
- 00:00-00:04: Sean asked for the videos and links several times; the videos were merged to `main` in their own folder
  (`317b4f1`). 00:04: Jeremy Haynes' video added (`fa6c5e7`).
- 00:07: Sean asked for an SOP so any chat can tear down a video "right away". 00:14: SOP, skill, `add_video.py` and
  the Jeremy teardown from all 612 frames (`6794a1c`).
- 00:16-00:39: the four Jason teardowns in parallel, `TEARDOWNS.md`, `check_teardown.py` (`60a129a` to `5076c46`).
  The chat raised four clashes between Jason's slide video and Sean's standards.
- 01:19: Sean asked for faster teardowns and for key summary notes. 01:26: "yes build both now". 01:32: the frame filter
  `distinct_sheets.py` plus a quick mode (`1544205`). 01:39: 16 playbooks plus `core.md` and the index merged
  (`4f84763` to `906e7c7`). Findings: part of Jason's Doc was "Compiled By: Claude (Anthropic)"; the paradigm section
  is pasted twice; the Doc's After Harvest sections sell older offers.
- 01:44: "go back to the slides with real photos now". 01:53: four slides redone with real screenshots from the Figma VSL
  file and picjumbo stock placeholders, still taped (`0dd6ce6`).
- 01:58: "too simple... not a fan of putting tapes on the pictures... go through Deya's audit". 02:15: "Can you not use
  Canva elements?", misread as "don't". 02:35: the sewn set plus `sources/inspiration/deya/AUDIT.md` (`4d15945`).
- 02:47: "they look like a very bad recreation of Deya's". 02:51-03:48: a Canva build from a generated design; Sean:
  "jeez that aint cute"; stopped and thrown away.
- 06:07: "Fuck that. Let's just use HTML because you design better using HTML." The light set became the base and the
  rules were corrected (`f86e399`).
- 06:15-06:37: the brand kit, the audit and the guide PDF (`ccab5aa`). The Drive subfolder got the text parts.
- 06:37-06:56: Sean expected the assets and templates in Drive too. The template code went into Drive (`9be3c17`). The
  PDF, the images and the zip could not, and Sean must drag them in.

## 4. Sean's preferences and standards, in one place

Checked against `rulings.md` (13 rows, 2026-10-28 and 2026-10-29). "R" means the ruling is in `rulings.md`; "chat only"
means Sean said it in the chat but `rulings.md` does not have it.

**The work**
- Order of the work: content with perfect positioning, then the VSL, then outreach for January launches. (R)
- The name: Fladdy (Slides That Sell). (R)
- Never guess what a coach means: ask with the timestamp and the frame, then write his answer in `rulings.md`. (CLAUDE.md)
- When he sets a standard, write it into the rules in the same turn. (CLAUDE.md)
- A pasted YouTube link means: tear it down right away with the SOP, no briefing (00:07: "Before we do anything, I want
  Claude to be able to go through it right away"). (CLAUDE.md, chat only in rulings)
- Every chat gets summary notes by topic, not the full sources (01:19). The playbooks do this. (CLAUDE.md)
- Speed matters. He calls out slow estimates ("I don't believe that would take 40 minutes. That's 15 minutes tops,
  literally"). (chat only)
- Messages short and plain: what is done, what is next, what only he can give. (CLAUDE.md)
- Tell him what you're doing before going deep into tools ("what are you doing", 15:59, after a long Canva run). (chat only)
- Merge finished work to `main` and send the link; each coach's videos in their own folder (00:02). (chat only)
- Push back when you're told something is impossible. He was right about YouTube (14:46). (chat only)

**The look**
- Type: Olivera headlines, Literata subheadings, Hanken Grotesk body ("we're using a grotesque on our website"). (R)
- Use the free Olivera demo; never buy it ("We're not even going to sell it"). Work around its missing punctuation. (R)
- YouTube slides: "a little bit simpler and not overly after-harvest... adaptable to different stuff... just the
  foundations". (R)
- Not "too much like Claude": no templated label/headline/italic stack, no placeholder copy. Derive from the
  transcripts, Jason's lessons and Deya's layouts. "More brain in the layouts." (R)
- Not messy either: "nicely made", with no grey border or contact-sheet frame around delivered slides. (R)
- Not boring, not placeholders: real detail on real things. (R)
- Interesting layouts, never the same layout twice in a row; the face is part of the composition. (R)
- Real pictures and real screenshots on every story or proof slide. Free stock is fine as a marked placeholder ("you can
  get real pics from online even if they are placeholders"). (R)
- More human touch, "our own" identity, leaning toward Deya but **not a copy of her** ("a very bad recreation"). (R)
- No tape stuck on photos ("very generic"). (R)
- Slides are made in HTML ("you design better using HTML"). The light set is the base. (R)
- Canva elements: he wanted them used, but not slides designed through Canva's generator ("jeez that aint cute"). (R)
- In Drive he wants the slides as PNG or JPG images, not HTML (06:49: "Instead of the HTML, can you put the PNG or
  JPG version of the image?"). (chat only)
- He wants the brand kit, the templates and the assets in the Drive brand-kit folder, not only on GitHub. (chat only)

**Where the chat, the repo and `rulings.md` disagree**
1. **"Full and a little playful" is not Sean's ruling.** The audit (D13 and clash 1) cites "ruling 2026-10-28, full and
   a little playful", but no row in `rulings.md` has those words, and Sean never said them in the chat. The idea came
   from the assistant (17:30: "Deya's slides are full..."). Sean's actual words were "it still doesn't feel complete"
   and, later, "more texture or a bit more content, more text maybe". So clash 1 below is weaker than the audit says.
2. **Canva props: allowed or retired?** The 2026-10-29 ruling says "Canva-made props are allowed again", but
   `rules/slide-method.md` §3f still says "The Canva props of the light set (wheat, hat, graph paper, tape, folders,
   tickets) are retired". The base set still uses them. Note also that "allowed again" was the assistant's reading of
   "I thought you were going to use Canva elements"; Sean never said those words.
3. **The dark stage.** The 2026-10-28 round-4 ruling still reads "the YouTube look is the dark stage". The 2026-10-29
   rows make the light set the base, so the older row is stale.
4. **The paper colour.** `theme.css` uses `#FBFAF6` (the Figma note), but the brand kit and the light set use
   `#FBF8F1`. Sean never answered which brand source is current: the July design system (`#F1ECE1`, Literata headlines,
   pixel-stitch wheat only) or the Figma note (`#FBFAF6`, Olivera, flowers plus crystal).
5. **AI-made objects vs Jason's "no AI pictures".** `rules/slide-method.md` §3 says to generate the focal object in
   Canva. Jason avoids AI pictures [slides 7:22, 20:05], and the audit says to replace stock with real things. Sean
   has not ruled on this (open item 4 below).
6. **Tape in the base set.** The ruling says no tape on photos, but `youtube-light.html` s3, s7 and s10 are still taped.
   This is the work still to do, not a rule clash.

## 5. Open items

**Clashes for Sean, from `audits/2026-10-29-light-set-vs-jason.md`** (the rulings stand until he answers):
1. Props and fullness vs Jason's minimalism [5:34]: keep at most two props per slide, at the edges? (See disagreement 1:
   the "full and playful" ruling it cites doesn't exist.)
2. Three type voices with italics (ruling 2026-10-28) vs one font, no italics [13:35, 33:10]: keep, with at most two
   voices a slide?
3. The face circle on every slide (Sean's brief) vs Jason's webcam beside the slide [11:58]: keep for YouTube; for
   webinar decks too?
4. Pace: a build every 5-10 s on YouTube slides, or still pictures between talking-head shots?
5. Emojis as count icons [37:54], or our own stitch icons for counts?

**Raised in the chat, still unanswered**
1. Plain like Jason ("better to look ugly with design than it is to look pretty" [16:06]) or "nicely made"? (00:39,
   `core.md`, the guide's 8 decisions)
2. Real photos and screenshots only, or AI-generated props too? (00:39)
3. Which close does the webinar machine build first: Jeremy's book-a-call close or a checkout close like our Day 3?
   Price on screen or not [Jeremy 1:19:03]? (00:14, `core.md`)
4. Do Jeremy's benchmarks go into our decks and calculators (30%+ show, 80% still there at the pitch, 30%+ book, 70%
   show to the call, 35% close)? (00:14)
5. Add a "why now" or "who I am" video, plus short FAQ videos, to the page after people register for our events? (00:14)
6. Try Jeremy's free AI slide tool as a benchmark? (00:14)
7. Should our videos feed one unlisted core video [Jason new webinar 13:11]? Is the VSL that core video? (`core.md`)
8. Should each video get its own "world" inside our style (a county fair for "launches vs 3-day events")? (02:35; asked
   for the sewn set, which was then rejected)
9. The After Harvest sections of Jason's Doc sell older offers (a $15K retention rebuild, a Black Friday 15% revenue
   share). Still current, or rewrite them around the free event plan? (01:39)
10. Which brand source is current (disagreement 4), and is the unnamed Canva brand kit After Harvest's? (14:38, 15:01, 02:51)
11. Each playbook and each teardown ends with its own "questions for Sean".

**Work not done**
1. The four weak light-set slides (s3 part two, s7 proof, s8 which one sells, s10 why events sell more): take the tape off,
   add real screenshots and one cut-out joke per slide, and match the craft of the six good ones (06:14). Not started;
   waiting on Sean's go.
2. The audit's "what to make next": the mechanism slide with its four states and the agenda's progress states; s4, s5,
   s7 and s10 rebuilt one idea per slide; a build order for every slide (`data-step`, a render per step); the intro tease
   and the recap; s11 as Jason's CTA without a price; type size and colour checked on every render.
3. Real screenshots for the stock spots: a launch inbox, a live session or whiteboard from our events, a sales or
   checkout screen. Only Sean can give these. Stock files start with `stock-`.
4. Drive: Sean has to drag in the 36 MB kit zip (`AfterHarvest-YouTube-Slide-Kit.zip`, rebuilt by
   `python3 scripts/make_brand_kit.py`; `brand-kit/` is not in git), the guide PDF and the 11 slide JPGs
   (`templates/youtube/renders/youtube-light/`). The first, older zip has no templates; don't use it.
5. "Put them in canva" (2026-10-28 16:16) was never done. Since then Sean has said HTML. Ask whether he still wants
   Canva copies, and if so, have him or his designer make one slide by hand to fill.
6. Sharp 1080p frames for slides whose small text was unreadable at 320x180: run `scripts/ingest_video.py` on a Mac.
7. The webinar machine itself (about 50 section agents, gates, answer key): not started. The playbooks are its base.
8. Maciek: no material yet.
9. `rules/`, `brand/`: CLAUDE.md says "still to come, do not invent them early" (only `rules/slide-method.md` exists).
10. Fix disagreement 2 in `rules/slide-method.md` once Sean confirms the Canva-props reading.

## 6. Test recipes

```bash
python3 scripts/render_slides.py templates/youtube/youtube-light.html --out templates/youtube/renders/youtube-light
```
This renders each `section.slide` to a PNG plus `sheet.jpg`. Look at every render before sending: text collisions,
marks crossing letters, the face covering key words.

```bash
python3 scripts/check_playbooks.py
```
```bash
python3 scripts/check_teardown.py
```
```bash
python3 scripts/teardown_index.py
```
```bash
python3 scripts/playbook_index.py
```
These are the gates (exit code = number of FAILs) and the index rebuilds. Run the indexes before committing.

```bash
python3 scripts/add_video.py https://www.youtube.com/watch?v=VIDEO_ID
```
This files a video under `<coach>-videos/` and runs the frame filter; then follow `sops/video-teardown.md`. Add `quick`
to the request for a transcript-only teardown (about 5 min).

```bash
python3 scripts/make_brand_kit.py
```
This rebuilds `brand-kit/` and the zip from `brand-kit-src/` and the templates.

What worked for YouTube in a cloud session: the frames come from YouTube's storyboard strips (320x180, about every 10 s,
via yt-dlp with the `mweb` player client), and the captions come from opening the embed player in Chromium with a referer
and saving its `timedtext` request. The video files themselves are blocked (403, captcha). The first lines of
`scripts/ingest_youtube.py` explain it.

Other things learned: rembg's `birefnet-general-lite` cuts light objects off light backgrounds; `isnet-general-use`
drops them. Most stock sites block the cloud machine; picjumbo (with curl), pxhere and ISO Republic (both CC0) worked.
X posts need a login, so take screenshots from the Figma file. Olivera needs a 0.022em text stroke to match the site,
and its missing punctuation falls back to Literata (`ink.js`).

## 7. Mistakes made in that chat (don't repeat them)

1. **Gave up on YouTube too early.** It told Sean "that path is closed" and asked him to use his Mac. He pushed back,
   and storyboard frames plus captions worked within 15 minutes.
2. **Padded time estimates.** "About 40 minutes" for drafts that Sean said take "15 minutes tops"; they were done in
   about 3 minutes. Several later estimates were also long.
3. **Templates before thinking.** Rounds 1-2 were empty boxes with placeholder copy and none of the real assets,
   transcripts or Deya ("underwhelming", "too much like Claude"). It repeated the same label/headline/italic stack it
   had already listed as a template tell.
4. **Overcorrected to messy.** Round 3 copied "messy" from the brief too literally, and shipped on a grey contact sheet.
5. **Went quiet in long tool runs.** A deep Canva run with no explanation got "what are you doing" and an interrupt.
6. **Ignored direct questions while busy.** Between 23:52 and 00:02 Sean asked four times where the teardowns and videos
   were and for a link, while the replies kept talking about stock photos. Answer the person first.
7. **Said yes and didn't do it.** "Put them in canva" was accepted and never done.
8. **Same layout on every slide.** The five dark slides shared one composition ("boring", "placeholders").
9. **Misread "Can you not use Canva elements?"** as "don't". It retired the props, built the sewn set (a copy of Deya
   with needlework swapped in) and wrote the misreading into the rules. Sean: "a very bad recreation of Deya's". When a
   message can be read two ways, ask.
10. **Copied the inspiration instead of learning from it.** The sewn set took Deya's compositions. Take her tricks (real
    things, a face that things touch, one joke per point), not her layouts.
11. **Designed through Canva's generator.** The candidates were generic, and the connector can't use Olivera or search
    Elements. Sean: "jeez that aint cute".
12. **Over-promised Drive.** It said the kit would go into Drive, but the connector can't upload images, fonts, PDFs or
    zips. Sean expected the assets and templates there. Say what a connector can't do before starting.
13. **An interrupt killed background agents.** Sean's interrupt stopped the four Deya audit agents and their notes were
    lost (a fifth failed on a content filter). Save agents' progress to files as they go.
14. **Wrote an idea into the audit as a ruling.** "Full and a little playful" was cited as Sean's ruling when it was the
    assistant's own reading (section 4, disagreement 1). Cite only words Sean said.
