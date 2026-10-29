# SOP: ingest a video and tear it down

Sean, 2026-10-29: "Can you also make an SOP for ingesting the video? ... notes for it ... like analysis, because I
really want it in an SOP. Before we do anything, I want Claude to be able to go through it right away."

**Trigger:** Sean pastes a YouTube link, or says "tear down / ingest / study / break down this video". Do it start to
finish without asking. The skill `.claude/skills/video-teardown/` runs this SOP.

**Output, per video:** one folder `<coach>-videos/NN Title (id)/` holding `transcript.md`, `study.md`, `sheets/`,
`meta.json`, and `teardown.md` (the analysis), on GitHub `main`, plus the links sent to Sean.

**Time:** about 2 minutes to ingest, then 10-20 minutes to tear down a 1-hour video (the frames are read by 4
agents at once). Say the estimate when the video is over 1 hour.

---

## 1. Ingest (one command, 0 tokens)

```
python3 scripts/add_video.py <youtube url or id>
```

It downloads the captions and the storyboard frames (`scripts/ingest_youtube.py`), reads the channel, and files
the video as `<channel>-videos/NN Title (id)/`, numbered after the ones already there, with its row added to that
folder's `README.md`. It prints the frame-sheet chunks for step 3.

Check what it prints:
- `OK ...` with a sheet count of about (length / 90 s) and a transcript word count. `ALREADY ...` means the video
  is filed: go to step 2 with that folder.
- `WARN no transcript`: YouTube 429'd the captions. Re-run once; if it still fails, ask Sean to paste the transcript
  (from YouTube's "Show transcript") and save it as `transcript.md` in the folder.
- `NEW coach folder`: add the folder to the table in `CLAUDE.md`.

Frames are YouTube's storyboard (320x180, about one every 10 s) because YouTube blocks the video file in a cloud
session. Small on-screen text is often unreadable at that size: on a Mac, `python3 scripts/ingest_video.py <url>`
gets full 1080p frames at every scene change (needs `brew install yt-dlp ffmpeg`).

If Sean pastes a transcript himself, it is the same video: use the ingested `transcript.md` (it has timestamps)
and use his paste only to check for missing parts.

## 2. Read the transcript (main chat)

Read `transcript.md` from start to end. While reading, collect:
- the **chapter map**: where each part starts (the `[m:ss]` stamps in transcript.md; `transcript.json` has every
  caption line with its start time when you need the exact second);
- every **named idea or framework** (his own names: "the dart system", "majority hook", "Thunderdome");
- every **number** he gives (benchmarks, ranges, budgets, rates, timings, counts) with the exact range he says;
- every **process** in order (the steps, the sequence, the cadence);
- the **stories and examples** and what each one is used to prove;
- **lines worth keeping** word for word;
- **how he sells** inside the video (calls to action, offers, the moment and the wording).

Every item gets its timestamp. Nothing is paraphrased into a claim he did not make.

## 3. Read the frames (4 agents in parallel)

For a video over 30 minutes, start one background agent per chunk printed in step 1 (about 17 sheets each), all
in the same message. Under 30 minutes, read the sheets yourself with the same brief. The brief, with the folder,
the title and the range filled in:

> You are logging what is ON SCREEN in a YouTube video, from storyboard frame sheets, for a slide-design teardown.
> Video: <coach>, "<title>" (<length>).
> Folder: `<absolute path to the video folder>/`
> - `sheets/SNN.jpg`: 960x540 images, each a 3x3 grid of 320x180 frames, read left to right, top to bottom, about
>   10 s apart.
> - `study.md`: for each sheet (heading `## sheets/SNN.jpg [m:ss - m:ss]`), each frame's timestamp (row/col) and the
>   words said while it was on screen.
>
> Your range: sheets <SAA> to <SBB> (inclusive). For each sheet, Read the sheet image with the Read tool and read
> that sheet's section of study.md. Report what is visually on screen. The frames are small: write only text you
> can actually read; never guess; write "(unreadable)" otherwise.
>
> Return markdown only, in exactly this shape:
>
> ## SAA [m:ss-m:ss]
> - shots: one entry per distinct visual state with the frame time where it starts. Types: talking head / screen
>   share (name the app or page) / iPad or whiteboard drawing / slide / B-roll / text overlay / split screen /
>   picture-in-picture.
> - on-screen text: exact words you can read, each with its time.
> - technique: how the visual supports what is said, only when notable.
>
> After the last sheet, add `## Patterns in SAA-SBB` with 3-6 bullets: how often the visual changes, rough share of
> talking head vs screen/drawing, recurring layouts (face position and size, colours, captions, branding),
> anything a slide designer could copy.
>
> Be factual and terse. Do not retell the spoken content beyond naming what the visual shows. No preamble.

Keep the agents' logs: they go into `teardown.md` as the appendix "Frame log", so a later chat can check any claim
about the visuals without re-reading 600 frames.

## 4. Write `teardown.md` in the video folder

Use this template. Facts come from the video with a `[m:ss]` stamp; anything that is our reading is in the two
sections marked as ours. Unknown stays out. No em dashes in the file.

```
# Teardown: <title>

<coach> · <upload date> · <length> · <youtube link>
Files here: transcript.md (timestamps), study.md (frames + words), sheets/ (frames). Torn down <date> (sops/video-teardown.md).

## In one paragraph
What the video teaches, for whom, and its spine, in 4-6 sentences.

## Chapter map
| # | starts | part | what it covers |

## The frameworks
One block per named idea: his name for it, [m:ss], what it is in his words, how he uses it.

## Every number
| what | his number | range he gives | [m:ss] |

## The process, in order
The step-by-step he lays out (cadences, sequences, schedules), as numbered lists.

## Stories and examples
| story | [m:ss] | what it proves |

## Lines worth keeping
> "verbatim line" [m:ss]

## What is on screen (from the frames)
- How the video is shot: share of talking head / screen / drawing / slides; how often the picture changes.
- The devices he uses, each with [m:ss] (live drawing, real pages, real emails, spreadsheets, text overlays).
- What Fladdy can copy for slides (each with the [m:ss] that shows it).

## How he sells inside the video
Every call to action: [m:ss], what is offered, the wording, where in the video it sits.

## For After Harvest (our reading, not his)
How this applies to 3-day events, the VSL, outreach, the YouTube videos. Mark each point as ours.

## Where he differs from Jason Fladlien (when the topic overlaps)

## Questions for Sean
What is unclear and changes what we build. One line each, with the [m:ss].

## Candidate rules (not adopted until Sean says yes)
Rules this video would add to rules/ or a playbook, each with its [m:ss]. When Sean agrees, move them into the
rules and add a row to rulings.md with his words.

## Appendix: frame log
The agents' logs from step 3, unedited.
```

## 5. Ship it

1. `git add` the video folder (and `CLAUDE.md` if a coach folder was new); commit; push the working branch.
2. Merge to `main` and push it (Sean, 2026-10-29: "merge to main, make a folder for it"). `main` is what GitHub
   shows by default.
3. Send Sean three links: the folder, `transcript.md`, `teardown.md` (GitHub `main` URLs; spaces in folder names
   become `%20`). Say in two lines what the teardown found and list the "Questions for Sean".

## Notes

- One coach per folder: `jason-fladlien-videos/`, `jeremy-haynes-videos/`, and a new one when a new coach comes
  (the channel name decides; `add_video.py` makes it).
- Inspiration videos (layouts only, like Deya's) are not teardowns: `python3 scripts/ingest_youtube.py <url>
  --frames-only --out sources/inspiration/<name>`.
- When a teardown says something that contradicts a ruling in `rulings.md`, the ruling wins; list the clash under
  "Questions for Sean".
