# Audit: the light YouTube set against Jason Fladlien's slide method

2026-10-29. Sean: "go through the Jason Fladlien teardown of the transcript that we made and audit this whole thing so
we can really make it work."

What was audited: `templates/youtube/youtube-light.html`, all 11 slides (renders in
`templates/youtube/renders/youtube-light/`). What it was audited against: the teardown of Jason's slide video,
`jason-fladlien-videos/01 How to Design Webinar Slides Nobody Does This Right (rAwgv2hThVw)/teardown.md`, read whole,
and `playbooks/slides.md` (which adds his other three videos). Every rule is cited `[m:ss]` in that video. Where a rule
clashes with one of Sean's rulings, the ruling stands and the clash is listed at the end as a question.

Verdicts: **keeps** (the slide already follows the rule), **breaks** (fix it), **clash** (Jason and a ruling disagree).

## The short version

The light set looks better than anything before it, and it already does several things Jason asks for: real
screenshots with the source under them, a question as a title, the agenda that shows where we are. Where it falls short
of his method is everything that happens *over time*: it is 11 still pictures, when his decks are hundreds of slides
built one line at a time, with a mechanism slide that comes back and a recap. The look is the strong part; the method
is the missing part.

The six fixes that matter most, in order:

1. **Design the builds.** Every slide gets a build order (what appears when, as it is said); one idea per slide, so the
   11 become about 40 [6:09, 21:18, 28:44-28:52].
2. **Make the 3-day event the mechanism slide**, the most designed slide in the set, and bring it back with progress
   states each time a day is covered [23:04-25:00].
3. **Replace every stock photo** with a real thing of ours (s8, s10) [9:07, 20:05].
4. **Never make the number the biggest thing** (s5): make the meaning big and show the number as the real screenshot
   [27:40, 35:13].
5. **Two colours per slide**: ink plus one accent; the harvest props stay at the edges and never compete with the key
   words [7:06, 10:44].
6. **Bigger type**: key line 56px or more, support 40px or more; only source lines stay small [14:02-14:33].

## Deck-level findings

| # | Jason's rule | the light set | verdict | fix |
|---|---|---|---|---|
| D1 | Slides are free; one idea per slide; split rather than crowd [6:05-6:51] | 11 slides, several carrying two or three ideas (s7: post + chat + membership; s10: three reasons at once) | breaks | One idea per slide; s7 becomes 3 slides, s10 becomes 4 (one per reason, then the three together) |
| D2 | Motion every ~6 s; about 500 slides a webinar [28:44-28:52] | No builds designed; every slide appears whole | breaks | Write the build order for every slide (see per-slide table); in teaching stretches something appears every 5-10 s |
| D3 | Functional animation: one item at a time, in reading order, as it is said [9:25, 12:14, 21:18] | none | breaks | Each element gets a step; renders get a `--step N` frame per step (see the guide, part 4) |
| D4 | The mechanism slide is the most important content slide; it comes back with progress: done small and ticked, current biggest, next faded, a coloured arrow [23:04-25:00, 27:28] | The 3 days appear only as a typed note on s3 and chips on s8; no mechanism slide | breaks | Build "The 3-day event" mechanism slide (Day 1 teach, Day 2 teach, Day 3 cart opens) and reuse it in every section with its states |
| D5 | Each key slide seen three times: intro, teaching, recap [3:37-3:58] | no recap; nothing returns except the agenda | breaks | Add a recap slide ("so far today") that brings back the mechanism and the proof |
| D6 | Intro tease: a slide inside a slide; a wall of later slides cut off at the bottom [2:48-4:38] | the agenda (s2) is a list of folder names | breaks (partly) | After s1, tease 3-4 later slides as screenshots under a small title, then the cut-off wall |
| D7 | The least important thing is never the biggest: title, name, numbers, step numbers, price [1:55, 13:18, 23:42, 27:40, 41:22] | s5 makes "$100K" the biggest thing; s10 stitches step numbers 1-3 | breaks | See s5 and s10 below |
| D8 | Titles tell the story in active voice; a label becomes a question [22:52, 26:05] | s8 does it ("Which one sells?"); s3, s4, s10 are labels | breaks (partly) | s3 "Three days, then the cart opens."; s10 "Same list. Why does the event sell more?" |
| D9 | Two colours [7:06, 10:44] | s1 uses rust, olive, pink, gold and ink; s9, s10, s11 add pink and gold props | breaks | Ink plus one accent (rust) on the words that matter; sage only as a ground; props keep their own colour but stay at the edges, small |
| D10 | Bigger fonts; buyers are 30-50+ [14:02-14:33] | body text in Plex Mono 27-32px; polaroid captions 19px | breaks | Key line 56px+, supporting line 40px+, sources 18-20px; YouTube is watched on phones |
| D11 | Show, don't tell; real things; stock only when nothing real exists [2:08, 9:07, 20:05] | s3, s5, s6, s7 show real things; s8 and s10 use stock (an inbox, a calendar icon, a whiteboard, a laptop) | breaks (s8, s10) | Our real inbox of launch emails, our real Zoom, a real calendar invite, a real checkout or payment notice |
| D12 | Screenshot the reality: strip the noise, keep the source line, highlight the key line [19:36-20:50] | sources under s3, s5, s7, s8; highlight on s7 | keeps | Keep; add the highlight wherever a screenshot is the proof (s3, s6) |
| D13 | Cut what does not persuade: logos, swooshes, icons, glows, taglines, the presenter's photo [5:34-5:56, 11:20-11:58] | decorative wheat, flowers, coin, sprig, tape, the straw hat | clash | Ruling 2026-10-28 asks for full and playful slides. House rule: at most two props per slide, at the edges, never touching the key words; each prop should carry meaning (wheat = the harvest = results) |
| D14 | One font, three faces; no italics [13:35, 33:10] | three voices: Literata italic, Hanken 900, Olivera script, Plex Mono | clash | Rulings 2026-10-28 set the three type voices. Keep them, but never more than two voices on one slide besides the source line |
| D15 | Metaphors carried or dropped [16:20-16:52, 24:19, 32:03] | "Today's harvest" over kraft folders (harvest + office) | breaks (mildly) | Either the harvest (rows, a field, seed packets) or the folders ("three folders, in order"); not both |
| D16 | Numbers as countable things [9:39-10:15, 35:42] | none | missing | E.g. "nine years" as nine calendar years crossed off, then the one launch |
| D17 | His CTA slide: what you get, one call to action, one URL bar [40:58-42:14] | s11 has the URL, the time and "free", plus two end-screen tiles | breaks (partly) | Show what is in the plan (topic, structure, numbers, revenue floor) as a stack, one bar with theafterharvest.com; the end-screen tiles only in the last 20 s |
| D18 | The presenter's photo is unnecessary with a webcam [11:58]; the webcam sits beside the slide | the face is a large circle on every slide | clash (by design) | Sean's brief asks for the facecard space on every slide; this is the Deya format for YouTube, not Jason's webinar format. Keep, and never let it cover the key words |
| D19 | YouTube: teaching is the sale; soft sell; no invented scarcity [Jason new webinar 7:18-11:08] | s6 and s11 sell softly, no scarcity | keeps | Keep |

## Slide by slide

| slide | what it is | keeps | breaks | fix | build order |
|---|---|---|---|---|---|
| s1 title | "why creators are SWAPPING LAUNCHES for 3-day events (and why it works)", face circle, wheat, tickets | the face big; a question-like promise | the topic is the biggest thing (fine for a title card); five colours | rust only on "for 3-day events"; drop the pink flower or the sprig; keep wheat and tickets at the edges | lead-in, shout, script line, aside |
| s2 agenda | "Today's harvest", three kraft folders, a check, "we are here" | where we are (tick + arrow) [24:56] | all three folders the same size; harvest + folders metaphor | current folder biggest and lifted, done one small and ticked, next one faded [24:35]; title "Three folders, in order" | folder 1, folder 2, folder 3, then the tick and arrow move each time it returns |
| s3 part two | sage band, stitched 2, "The 3-day event.", the Launch Lab page + ticket taped, typed note | real page and ticket with the source | taped (Sean: no tape); label title; the 3 days only as a typed note | no tape; title "Three days, then the cart opens."; the 3 days become the mechanism slide that follows | band and title, the page, the ticket, the note |
| s4 problem | "The ACTUAL problem...", Plex Mono paragraph, scarecrow by the face | the turn word in the accent | all telling, nothing shown; 2 sentences of 30px mono | show it: the real 7 launch emails in an inbox (built one by one), then the sales page alone ("with nobody in the room") | title, email 1-7 stack in, then the lone sales page |
| s5 number | "Jay Clouse, nine years in:", "$100K" stitched on graph paper, source line | the source line; the stitch is ours | the number is the biggest thing [27:40, 35:13] | make "nine years, then his first $100K launch" the big line; show the real post (screenshot) with the line highlighted; or nine years as nine crossed-off calendars, then the post | nine years (the calendars), then the post, then the highlight |
| s6 step | "step 3: get the plan", the plan card, "takes about 5 minutes" burst | a real artefact; a small step label | the step number is small (good); the burst is a sticker (decoration) | check the plan card is a real client's or label it a sample; keep the sticker only if it carries the fact (5 minutes) | label, line, the plan card, the 5 minutes |
| s7 proof | "proof #1" up the edge, post, chat, The Lab photo, line | real screenshots with sources and the highlight [20:43] | three proofs on one slide; taped | split: (a) the post with the line highlighted, (b) the chat, 3:57 AM then 8:47 AM, (c) The Lab photo; no tape | post, highlight, then next slide the chat lines one by one |
| s8 which | "same list, same offer. WHICH ONE SELLS?", a launch vs a 3-day event, polaroids, chips | the question title; the contrast on one slide [28:57] | the inbox is stock; polaroids + chips + ticket + face is a lot | our real inbox; the real Zoom stays; drop the polaroid frames for plain prints; keep one ticket | question, a launch side, "or", the event side, then the chips |
| s9 story | "STORY TIME", "The morning Jay messaged me", the 8:47 AM quote, hat on the face | a story break; the real quote | the quote is typed, not the real message | show the real chat message as the build (3:57 AM, then 8:47 AM) | pill, title, then the real message |
| s10 list | sage ground, "Why events sell more", three taped polaroids numbered 1-3, closing line | three reasons (rule of three [38:53]) | stock photos; step numbers (no numbering when you can count to three [28:10]); three ideas at once | one reason per slide, each with a real thing; then the three together as the recap; no numbers | reason 1, 2, 3 each alone, then all three |
| s11 end | "want the plan FOR YOURS? (it's free)", the URL, two end-screen tiles, folder, wheat | one call to action, soft, no scarcity | what is in the plan is not shown | the plan's contents as a short stack, one bar with the URL; tiles only in the last 20 s | stack items, then the bar |

## What to make next (in this order)

1. The mechanism slide (D4) with its four states, then the agenda (s2) with its progress states.
2. s4, s5, s7, s10 rebuilt one idea per slide with real things (D1, D11, D16).
3. Builds for every slide (D2, D3): a `data-step` on each element and a render per step.
4. The intro tease and the recap (D5, D6).
5. s11 as Jason's CTA without a price (D17).
6. Type sizes and colour per slide checked against D9 and D10 on every render.

## Clashes for Sean (the rulings stand until he answers)

1. Props and fullness (ruling 2026-10-28, "full and a little playful") vs Jason's minimalism [5:34]: keep at most two
   props per slide at the edges?
2. Three type voices with italics (ruling 2026-10-28) vs one font, no italics [13:35, 33:10]: keep, at most two voices a
   slide?
3. The face circle on every slide (Sean's brief) vs Jason's webcam beside the slide [11:58]: keep for YouTube; for
   webinar decks too?
4. Pace: build every 5-10 s on YouTube slides, or keep them as still pictures between talking-head shots?
5. Emojis as count icons [37:54] or our own stitch icons for counts?
