# How to write a Fladdy playbook (shared brief)

Fladdy is After Harvest's slide machine (YouTube slides, then the VSL, then webinar decks), built on Jason Fladlien's
method. After Harvest builds and runs 3-day live events (online challenges) for creators and coaches; its offer is a
free event plan on theafterharvest.com. Repo: /home/user/fladdy.

A playbook is the short, distilled version of one topic, so a new chat can read only what its task needs instead of
the 65,000-word source doc. Every chat will trust it, so it must be complete (no rule or technique dropped), exact
(his words where it matters) and cited.

Read first: `rulings.md` (Sean's standards; a ruling beats a source, apply them and say where they change Jason).

## File format (exactly these sections, in this order)

```
# <Topic> playbook

Read this when: <the tasks that need it, e.g. "writing a webinar hook, a YouTube title, an ad's first line">.
Sources: <files with line ranges or teardown timestamps>. Built 2026-10-29. The source is the master: re-check a quote there.

## In 5 lines
Five short lines a person could act on without reading further.

## The rules
Numbered. Each rule: one or two plain sentences, then its citation. Every distinct rule, technique, type, step or
criterion in the source gets its own number; group related ones under small bold labels if there are many.

## How to do it
The step-by-step he teaches, plus fill-in templates (blanks in [brackets]) where he gives a formula.

## Examples
His real examples, one or two lines each, cited. Keep the ones that teach something different; drop repeats.

## Mistakes he calls out
What not to do, cited.

## Lines worth keeping
5-10 verbatim quotes, cited.

## After Harvest
"From the doc": the After Harvest applications already written in the source (keep their substance, cited).
"Our reading": anything you add, marked as ours, short.

## Open questions for Sean
Where the source is unclear, contradicts itself, or clashes with a ruling or with another coach. One line each, cited.
```

## Citations
- The methodology doc: `[doc L1234]` (line number in `sources/fladlien/notes/full-methodology.md`).
- A teardown: `[Jason slides 16:06]`, `[Jason new webinar 12:31]`, `[Jason new way 1:48]`, `[Jason AI 10:34]`,
  `[Jeremy 1:17:57]` (the video's own [m:ss] as written in its teardown).
- A ruling: `[ruling 2026-10-28]`.

## Style
Plain, short sentences; Sean is not a technical reader. Sentence case. No em dashes (use a colon, a comma or a full
stop). No filler, no "in conclusion". Aim for 800-1,800 words per playbook: about a tenth of the source, but nothing
that changes what someone would do may be lost. Facts only from the sources; unknown stays out.

## Do / don't
- Write only the playbook files named in your task, in /home/user/fladdy/playbooks/. No other edits, no git commands.
- Read the whole source range for your topic (use Read with offset/limit in chunks of about 400 lines).
- When done, reply with only: each file path, its word count, and its open questions (one line each).
