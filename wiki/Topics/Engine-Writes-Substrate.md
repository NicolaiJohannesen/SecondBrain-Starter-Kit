---
type: topic
created: 2026-07-03
updated: 2026-07-03
version: 1
origin: kit-seed
tags:
  - topic
  - seed
  - domain/ai
aliases:
  - Founder-as-Reviewer Pattern
  - Asynchronous Human Review Pattern
  - Engine Writes Human Reads
  - Operator at the Edges
---

# Engine-Writes-Substrate

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

The pattern of an **engine producing durable output autonomously + a human reviewing asynchronously**, rather than the human being in the loop during the work itself. The engine writes to a durable substrate — a page, file, or dashboard; the human opens it later, reads, marks a status, ships or skips; the engine reads those markings on its next cycle.

**The architectural principle**: humans stay strategic by NOT being in operational loops. The substrate is the contract between the two layers.

## When this pattern applies

| Signal | Why it fits |
|---|---|
| Work happens at times the human isn't available | The engine runs on schedule; the human reviews whenever convenient |
| Output benefits from batched review | Several entries reviewed together calibrate better than one-at-a-time |
| Review is strategic (approval, judgment, ship/skip) but the work itself is routine (drafting, triage, formatting) | Cleanly separates the strategic edge from the routine middle |
| Mobile-friendly review matters | A plain file or page is readable anywhere, no dedicated app needed |
| An audit trail matters | The substrate preserves what was produced and what was decided |

## When it does NOT apply

- **The decision loop is too short** — real-time approval is needed and synchronous oversight is required.
- **The engine can't produce useful drafts** — the domain requires too much in-the-moment context the engine doesn't have.
- **The substrate would outgrow review capacity**, or an audit trail isn't valued enough to justify the overhead.

## The pattern shape

```
Engine (autonomous, scheduled or triggered)
   ↓ runs without a human in the loop
   ↓ produces output applying codified discipline
                ↓
        DURABLE SUBSTRATE
   (a page, file, or dashboard)
   - structured format (frontmatter + entries)
   - status field per entry (pending / approved / skipped / hold)
   - timestamp + provenance
                ↓
Human (asynchronous, when convenient)
   ↓ opens the substrate on whatever device
   ↓ scans top-to-bottom, fast per-entry review
   ↓ marks status, adds notes if needed
                ↓
Engine (next cycle reads the markings)
   ↓ archives processed entries
   ↓ triggers any downstream step tied to an approved entry
   ↓ honors the human's decisions, doesn't redo what's marked done
```

## A worked specimen

An autonomous drafting engine scans an inbox, clusters items by topic, and drafts a response for each into a "Pending Review" file: item summary, drafted response in a code block, a short rationale, and a status field defaulting to `🟡 PENDING`. The human opens the file once a day, reads top to bottom at roughly 30 seconds an entry, and marks each `✅ APPROVED — sent [date]`, `❌ SKIPPED — reason`, or `⏸ HOLD — reason`. The engine's next run archives resolved entries to a history file and only ever appends new ones — it never rewrites an entry the human has already marked. The shape generalizes: the same structure works for reviewing research summaries, incoming feedback clusters, or draft outreach messages — engine writes structured entries, human reads and marks status, engine respects the marking on the next cycle.

## Substrate properties that make this work

1. **Frontmatter for metadata** — type, dates, version, tags.
2. **Entries in one section, newest first**, so the human sees what's pending without scrolling past the archive.
3. **A per-entry status field** — the status is the contract both sides read and write against — plus a format comment documenting the entry schema, so it doesn't drift.
4. **An archive section or separate history file** — processed entries move out; the pending section stays small.
5. **Read-only respect of human markings** — the engine must never overwrite an entry the human has marked, or the contract breaks and trust dies.

## Why this beats the alternatives

- **vs. synchronous human-in-the-loop** — the human doesn't need to be available when the work happens; review batches better than one-at-a-time interruptions.
- **vs. full automation with no review** — strategic decisions stay human; catastrophic errors get caught before they propagate; an audit trail is preserved.
- **vs. notification-driven workflows** — no ping-noise, no context evaporation (messages get scrolled past; a durable file persists).

## The architectural principle, restated

> **Engine writes. Human reads. Substrate is the contract.**

The human stays strategic by not being in the operational loop. The engine produces consistent, disciplined output on its own schedule. The substrate carries state forward across asynchronous cycles, and each layer trusts the other's zone.

## Related

- [[Loop Engineering]] — this pattern is one shape a maintenance/production loop can take when the review step needs a human
- [[Feedback Loops (Universal Pattern)]] — the human-marking step is the correction signal the loop feeds back on its next cycle
- [[Agent Orchestration]] — where this pattern sits relative to other human-in/out-of-the-loop topologies
- [[Writing as External Memory]] — the substrate file is durable memory the engine and human share, functioning the same way externalized notes function for a single mind
- [[Second Brain]] — the substrate typically lives inside your own second brain, where you already look daily
