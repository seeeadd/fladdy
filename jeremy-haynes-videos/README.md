# Jeremy Haynes videos

Jeremy Haynes videos Sean sent, as study files. The video files themselves are not here: YouTube blocks downloading
them from a cloud session, so each folder holds the transcript and the frames instead.

| # | video | length | folder |
|---|---|---|---|
| 1 | [The Most Valuable Webinar Training You'll Ever Watch](https://www.youtube.com/watch?v=P1v-AN3So3A) | 1:40:45 | [01 The Most Valuable Webinar Training Youll Ever Watch (P1v-AN3So3A)](<01 The Most Valuable Webinar Training Youll Ever Watch (P1v-AN3So3A)/>) · [teardown](<01 The Most Valuable Webinar Training Youll Ever Watch (P1v-AN3So3A)/teardown.md>) |

## What is in each folder

- `transcript.md`: the full transcript with timestamps (YouTube captions). Paste this into another chat to work from the video.
- `study.md`: each frame time next to the words said over it, to read beside the frames.
- `sheets/S00.jpg ...`: YouTube storyboard frames, 3x3 per sheet, about 10 seconds apart (one sheet is about 90 seconds).
- `transcript.json`, `meta.json`: the same data for scripts (title, length, link).
- `teardown.md`, when written: the analysis (frameworks, every number, the process, what is on screen, questions for Sean).

Add a video with `python3 scripts/add_video.py <url>`, then tear it down with `sops/video-teardown.md`.
