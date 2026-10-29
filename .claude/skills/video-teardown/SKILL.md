---
name: video-teardown
description: Ingest a YouTube video and tear it down, start to finish, with no briefing. Use the moment Sean pastes a YouTube link, or says "tear down this video", "ingest this", "study this video", "break down this video", "make one for this too", or "do a teardown". Files the video in its coach's folder (transcript, frames), reads the transcript and every frame (4 agents in parallel for long videos), writes teardown.md next to it, merges to main and sends the links.
---

# Video teardown

Follow `sops/video-teardown.md` exactly; it holds the agent brief and the teardown template. In short:

1. `python3 scripts/add_video.py <url>`: files the video as `<coach>-videos/NN Title (id)/` and prints the
   frame-sheet chunks. Handle its WARN / NEW lines as the SOP says.
2. Read `transcript.md` whole: chapter map, named frameworks, every number with its range, processes in order,
   stories, lines worth keeping, calls to action. Everything with its `[m:ss]`.
3. Frames: one background agent per printed chunk, all started in one message, with the SOP's brief (over 30
   minutes of video); under 30 minutes, read the sheets yourself. Wait for every agent.
4. Write `teardown.md` in the video folder from the SOP template; the agents' logs go in its appendix.
5. `python3 scripts/teardown_index.py` (rebuilds TEARDOWNS.md); commit, push the working branch, merge to `main`,
   push `main`; send Sean the folder, transcript, teardown and TEARDOWNS.md links plus the open questions.

Say the time estimate first when the video is over an hour (about 2 minutes to ingest, 10-20 minutes to tear down).
