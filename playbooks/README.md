# Playbooks

The distilled version of everything Fladdy has learned: Sean's Jason Fladlien methodology doc (65,000 words) and the
video teardowns (55,000 words), cut to one short file per topic, every point cited back to its source. A new chat
reads `core.md` (one page), then only the files its task needs, about 5,000 words instead of 120,000. The sources
stay the master: go there only to check a quote.

## Which files for which job

| job | read |
|---|---|
| a YouTube video | core, youtube, hooks, curiosity, slides; plus the part you are writing |
| the VSL | core, webinar-map, hooks, pain, positioning, paradigm, close, offer |
| a webinar or Day 1-3 deck | core, webinar-map, slides; then the playbook for each part as you reach it |
| an offer or pitch slide | core, offer, price, bonuses, risk, scarcity, close |
| any slide design | core, slides (and `rules/slide-method.md`) |
| funnel numbers, a calculator, a diagnosis | core, funnel-numbers |

## Every playbook

| file | read it when | words |
|---|---|---|
| [core.md](core.md) | always, first | 719 |
| **Plan a whole webinar, VSL or long video** | | |
| [webinar-map.md](webinar-map.md) | planning a whole webinar, VSL or long video; deciding which playbook a task needs; checking that a deck has every step in the right place. | 2,199 |
| **The parts of a webinar, VSL or video, in order** | | |
| [hooks.md](hooks.md) | writing a webinar or video hook, a YouTube title, the first line of an ad, a VSL opening. | 1,800 |
| [pain.md](pain.md) | writing the pain or problem part of a webinar, a VSL or a video. | 1,800 |
| [curiosity.md](curiosity.md) | building curiosity, teasing what is coming, open loops, the agenda or "on this webinar" part (of a webinar, a video intro or the VSL), writing blind bullets, moving from one section to the next. | 1,929 |
| [excite.md](excite.md) | making an offer, a result or a promise feel exciting; turning features into outcomes; using facts, stats and testimonials; the person vs process close; the intro's promise. | 2,020 |
| [positioning.md](positioning.md) | positioning the presenter, the product or the vehicle; the "why listen to me" part of a webinar, VSL or video; picking proof for slides; putting a client or partner forward as the star. | 2,004 |
| [paradigm.md](paradigm.md) | writing the paradigm shift, the "old way vs new way", the big idea of a webinar or video; picking the paradigm strategy for an offer; choosing stated or implied; planning a beta launch or a big promise. | 2,417 |
| [commitment.md](commitment.md) | getting small commitments and yeses from the audience, chat engagement, building to the pitch. | 1,807 |
| [close.md](close.md) | writing the transition into the pitch and the close of a webinar, a VSL or a video CTA. | 2,197 |
| **The offer** | | |
| [offer.md](offer.md) | building or presenting an offer, the stack, what is included. | 1,897 |
| [price.md](price.md) | revealing or justifying a price, price anchors, payment plans, value vs price. | 1,937 |
| [bonuses.md](bonuses.md) | designing or presenting bonuses (choosing, naming, the bonus slides, the value stack, the webinar-only special). | 2,018 |
| [risk.md](risk.md) | writing guarantees, risk reversal, handling objections (the guarantee slide, the objection section after the offer, the closes, a sales call). | 1,573 |
| [scarcity.md](scarcity.md) | adding scarcity or urgency, deadlines, limited spots (the close, a fast-action bonus, a webinar-only special, a launch window, an offer sold from YouTube). | 1,940 |
| **Format** | | |
| [slides.md](slides.md) | designing any slide, deck, YouTube visual or VSL visual (webinar decks, Day 1-3 event decks, the YouTube slides, the VSL). | 2,797 |
| [youtube.md](youtube.md) | planning, scripting or structuring a YouTube video, a video series, or the "core video". | 2,843 |
| **The funnel around it** | | |
| [funnel-numbers.md](funnel-numbers.md) | planning the funnel around an event or webinar; setting or checking numbers (budget, opt-in, show, retention, booking, close); diagnosing a funnel that underperforms; scaling one that works. | 2,190 |

## How they are made and kept

- Format, citations and style: [`_how-to-write.md`](_how-to-write.md). Citations: `[doc L1234]` is a line of
  `sources/fladlien/notes/full-methodology.md`; `[Jason slides 16:06]` is a timestamp in that video's teardown (see
  `TEARDOWNS.md`); `[ruling 2026-10-28]` is a row of `rulings.md`.
- `python3 scripts/check_playbooks.py` checks every file has its sections and citations;
  `python3 scripts/playbook_index.py` rebuilds this page.
- When Sean answers an open question: write it in `rulings.md`, update the playbook it changes (and `core.md` if it
  is a big one), so every chat after that gets it.
- When a new video is torn down: fold anything new into the playbooks it touches, cited to its teardown.
