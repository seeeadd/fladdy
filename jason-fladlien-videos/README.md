# Jason Fladlien videos

The four Jason Fladlien videos Sean sent on 2026-10-28, as study files. The video files themselves are not here:
YouTube blocks downloading them from a cloud session, so each folder holds the transcript and the frames instead.

| # | video | length | folder |
|---|---|---|---|
| 1 | [How to Design Webinar Slides (Nobody Does This Right)](https://www.youtube.com/watch?v=rAwgv2hThVw) | 43:00 | [01 How to Design Webinar Slides Nobody Does This Right (rAwgv2hThVw)](<01 How to Design Webinar Slides Nobody Does This Right (rAwgv2hThVw)/>) |
| 2 | [The New Webinar](https://www.youtube.com/watch?v=VtXp0UwwK3Y) | 17:18 | [02 The New Webinar (VtXp0UwwK3Y)](<02 The New Webinar (VtXp0UwwK3Y)/>) |
| 3 | [This is the New Way to Sell](https://www.youtube.com/watch?v=VStitVKO1AI) | 13:51 | [03 This is the New Way to Sell (VStitVKO1AI)](<03 This is the New Way to Sell (VStitVKO1AI)/>) |
| 4 | [AI is (mostly) Bullshit](https://www.youtube.com/watch?v=v2yNV7rkyzI) | 31:35 | [04 AI is mostly Bullshit (v2yNV7rkyzI)](<04 AI is mostly Bullshit (v2yNV7rkyzI)/>) |

## What is in each folder

- `transcript.md`: the full transcript with timestamps (YouTube captions). Paste this into another chat to work from the video.
- `study.md`: each frame time next to the words said over it, to read beside the frames.
- `sheets/S00.jpg ...`: YouTube storyboard frames, 3x3 per sheet, about 10 seconds apart (one sheet is about 90 seconds).
- `transcript.json`, `meta.json`: the same data for scripts (title, length, link).

## Related

- Jason's notes (copy of the Google Doc "Full Jason Fladlien Methodology"): [`sources/fladlien/notes/full-methodology.md`](../sources/fladlien/notes/full-methodology.md)
- The slide rules taken from video 1, with timestamps: [`rules/slide-method.md`](../rules/slide-method.md)

Add another Jason video here with `python3 scripts/ingest_youtube.py <url> --out jason-fladlien-videos`
(then rename its folder to `NN Title (id)`).
