---
type: project
created: {{DATE}}
updated: {{DATE}}
version: 1
tags:
  - project
  - operational
aliases:
  - Tasks OS
  - To-do system
  - Task OS
---

# Tasks OS

The operating manual for the task system: one capture file, one ranked view, and a discipline that keeps them from drifting apart.

## Start here

1. **Everything lives in one file: [[all-tasks|the blob]].** Open it, find the right section, drop a one-line `- [ ]` task. Tasks don't live in project folders — those hold project *information* (specs, decisions), not the to-do list.
2. **Tag it; don't rank it.** Add the tags below. Don't decide priority at capture time — that happens later, at review.
3. **When unsure, capture anyway.** A roughly-tagged task in the blob beats a well-considered one that never got written down. Tags can be improved later; a task that was never captured can't be.

## The two files

- **The blob** *(the source — edit here)* — [[all-tasks]]: every task, one place, unordered. Capture here, richly tagged. This is the miscellaneous pile — filter on the way out, not on the way in.
- **The Now-list** *(the view — read-only)* — [[most-important-now]]: strictly ordered, never buckets. #1 is always the single most important thing needing your attention right now. Generated from the blob at review time — don't edit it directly.

## When a task balloons into a project

A task can start as a single line and grow until it's really a project. That's expected, not a failure of the system:

1. The substance moves into project information — a page under `wiki/Projects/<Project>/`, not the blob.
2. The blob keeps a one-line pointer: "→ now a project, see [[…]]".
3. Smaller follow-up tasks spawned from the project stay in the blob as normal tasks.

## The capture contract

Drop the task into the right section of the blob with these tags. Don't rank at capture; rank at retrieval. Tags can always be improved later — capture is the only non-negotiable step.

| Tag | Values | Why |
|---|---|---|
| `shape` | single / fanout / pipeline | does it parallelize into sub-tasks? |
| `window` | none / deadline:DATE / irreversible | closing windows dominate ranking |
| `blocked-by` | task ref | the dependency chain |
| `value` | 1-5 | how much this matters |
| `energy` | peak / low | does it need focused attention, or fit a low-energy slot? |
| `est` | rough size | for calibrating actual-vs-estimate over time |

Plus one `state:` line per section: `active` / `maintenance` / `dormant (re-activate when: …)`.

## The loop

1. **Capture** — into the blob, tagged. A few seconds. The only must.
2. **Rank (at review)** — read the blob, weigh value against window against effort, propose an ordering for the Now-list, then adjust by hand.
3. **Work** — pull from the top of the Now-list. Anything genuinely parallelizable (`shape:fanout`) can run alongside other work rather than serially.
4. **Archive** — mark done `- [x]`, move it to "Done this week" in the blob, and write a short journal entry (see below). Don't delete the history.

## Done is a claim; the journal is the evidence

A checked-off box is an assertion, not proof. When a task gets marked done, write a paired entry in the day's journal file (`wiki/Journal/YYYY-MM-DD.md`) capturing what was actually tested or verified, what was explicitly *not* tested, and anything worth flagging for later. If something marked done later turns out to be broken or incomplete, the journal entry is what makes the gap investigable — without it, "done" is just a claim someone made once and nobody can check.

## The guards

- Capture-with-tags is the only non-negotiable step. Everything downstream is improvable later.
- Rank only at review time. Don't spend effort re-ranking within a single work session — pull from the top and go.
- Estimate, then log the actual effort when done. The gap between the two, over time, is what makes future estimates better.

## Files

- [[all-tasks]] — the blob: every open task, add and change tasks here
- [[most-important-now]] — the ranked few that need attention right now (generated from the blob)

## Related

- [../../CLAUDE.md](../../CLAUDE.md) — the overall operating schema this task system sits inside
