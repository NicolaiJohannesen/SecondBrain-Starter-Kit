---
name: setup-brain
description: First-run bootstrap for a new second brain. Use when the kit is freshly cloned and NORTHSTAR.md doesn't exist yet, when the user asks to "set up my second brain" / "get started" / runs /setup-brain, or when a session opens against an empty wiki/ directory. Data-first flow — the user has already copied whatever data they have into raw/inbox/ before running this (the README tells them to); read what's there, interrogate it, confirm-and-correct with the user, and ask only the one thing that can't be inferred (what's private-forever). Writes NORTHSTAR.md and CLAUDE.md, seeds a first profile page, then offers to chain straight into ingesting the inbox. Must complete before any full ingestion — it shapes the schema everything else compiles against.
---

# Setup Brain

The one-time bootstrap that turns a freshly cloned kit into a system shaped around one specific person. Nothing else in the kit works well until this runs — `/ingest-source` needs a schema to write into, `/session-start` needs a NORTHSTAR.md to read.

**The flow is data-first, on purpose, and the data comes first in time too.** The README tells the user to copy whatever they already have into `raw/inbox/` *before* they ever open Claude Code — so by the time this skill runs, there is usually real material sitting there already, not a blank folder. Read it, draft from it, and confirm — don't ask questions the inbox can already answer.

**This is not about asking fewer questions — it's about not asking ANY question until the data has genuinely been exhausted.** The discipline is effort, not a count: spend real time actually reading what's in the inbox before you formulate anything to ask, so what's left to ask is only what truly can't be figured out from what's there. A shallow skim that quickly reaches for a question is the failure mode this whole flow exists to prevent — asking early because working it out would take longer is exactly backwards. Do the work first; the questions that survive after a genuinely thorough read tend to be few, but that's a consequence of the effort, not the goal itself. In practice only one thing is structurally impossible to infer no matter how thoroughly you read: what's private-forever, because a privacy boundary can't be guessed from someone's own data. Everything else — what the brain should focus on, which delegation level fits — gets worked out from a real read and folded into one combined confirmation, not asked cold.

**Narrate your intent, briefly.** Before checking the inbox or writing anything, say in one sentence what you're about to do and why — not a lecture, just enough that the user can redirect you before you go the wrong way.

## Instructions

### Step 0 — Verify the skeleton

```bash
ls -la
git status 2>/dev/null || echo "no git repo yet"
```

Confirm `raw/inbox/`, `raw/ingested/topic-sources/`, `wiki/{Topics,Entities,Projects,Sources,Synthesis,Personal,Journal,Tasks}/`, `memory/`, `constitution/`, `context/` all exist. If any are missing, create them. **If `git status` fails, OR the repo exists but has zero commits, run `git init` (if needed) and commit the bare skeleton** — git is the reversibility layer for everything that follows, and a repo with no history is functionally the same as no repo.

### Step 1 — Read what's already in the inbox

```bash
ls -la raw/inbox/
```

The user was told to copy their data in before running this — check what's actually there first, rather than opening with questions. If the inbox has real content: say so plainly ("I can see you've already dropped in X — reading that now") and move straight to Step 2.

**If a file is an archive** (`.zip`, `.tar`, `.tar.gz`) — extract it in place before reading (`unzip`, `tar -xf`) rather than asking the user to unzip it themselves; that friction belongs to the system, not the person.

**If the inbox is empty or thin**, say so and offer the two ways to add more, briefly — this is now a secondary, ongoing action, not a blocking gate:
- **Live connectors** (Google Drive / Calendar / Gmail via claude.ai → Settings → Connectors) — the only sources that stay continuously live.
- **Batch exports** — point at `context/export-handout.md` (quick list) and `context/data-census.md` (the complete territory) as reference to go get more, whenever convenient. Mention the consolidation trade-off once, briefly, if it comes up: *"bring in as much as you reasonably can — most people who do this find it becomes far more useful with full context, and a thin slice of your life gives thin answers back. Leave out what's genuinely sensitive using the private-forever question below as the actual boundary, not effort or mild discomfort — see `context/why-a-second-brain.md`'s under-inclusion section if you want the full reasoning."*

Either way, proceed to Step 2 with whatever is reachable right now — don't block on requests still in flight.

### Step 2 — Interrogate the data thoroughly — this is where the real effort goes, before any question gets asked

Tell the user: *"Before I ask you anything, I'm going to actually read what's here — not just skim titles — so the questions that are left are the ones the data genuinely can't answer."*

**Take real time on this. Read content, not just filenames.** A quick skim of titles and metadata produces a shallow, generic draft that asks questions the data could have answered if you'd actually looked. Open the files, read what's in them (run the matching `scripts/parse_*.py` first if the format fits), follow threads across multiple files if the inbox has several — the goal is a draft specific enough that confirming it takes one line, not a conversation. The order that matters here: **exhaust what the data can tell you BEFORE formulating anything to ask** — the depth of this step is what determines how few questions Step 3 needs, not a rule about question count.

From a genuinely thorough read, draft the **whole picture in one pass**, not just who-they-are:

- who this person appears to be, what they work on, what they care about — specific enough to be checkable, not a vague summary
- **what this brain should likely focus on** — research depth, personal/life memory, business/project context, or a mix — inferred from what the data actually shows, not asked cold
- **which level fits** (read `context/the-6-levels.md`) — default to Level 5 unless the data suggests otherwise (e.g. evidence of juggling several AI assistants → Level 6)

One hard boundary: **this drafts the Northstar; it does not ingest.** Reading deeply to inform the draft is not the same as writing wiki pages — no pages get written until setup is complete and `/ingest-source` runs under the finished schema. Depth of reading here costs nothing; depth of writing is still gated.

If nothing is reachable yet, say so plainly — there's nothing to read thoroughly, so Step 3 becomes direct questions in that case, which is expected and fine. That's the one situation where asking early is correct, because there's no data to exhaust first.

### Step 3 — Confirm the whole draft in one pass, then ask the one thing that can't be inferred

Present the **full draft** — who they are, what the brain should focus on, the level — as one combined picture: *"Your data suggests you're X, working on Y and Z, and this reads like a [research / business / life] brain at Level 5 — what's wrong or missing in that?"* One correction pass, not a sequence of separate questions.

Then ask exactly one explicit question, always, never inferred:

**What is private-forever?** Health details, financial specifics, other people's words in messages, anything that must never leave `raw/` or be synthesized into a wiki page even in general terms. This becomes the redaction policy in `CLAUDE.md`, on the record before the first file is processed.

### Step 4 — Explain Northstar + constitution, then write NORTHSTAR.md

Most new users have never met either concept. Explain both using the shipped worked examples — the "what a Northstar even is" section and the system's own Northstar in `NORTHSTAR.md`, and `constitution/README.md` for what a constitution is plus the second brain's own six rules. Their answers then *specialize* the system Northstar rather than starting from a blank page.

Write `NORTHSTAR.md` from the confirmed picture: who this is for, what the brain should do, the chosen level and why, and the private-forever boundary stated as a hard rule. Fill the Milestones section as-is from the template — it's not personalized, it's the same checklist for everyone.

### Step 5 — Fill every remaining placeholder, not just CLAUDE.md's

`CLAUDE.md` is the schema every session reads first. Fill `{{USER_NAME}}`, `{{PURPOSE_SUMMARY}}`, and `{{PRIVACY_BOUNDARIES}}` (its own `## Private-Forever` section — the same categories as NORTHSTAR.md's, restated there on purpose, because CLAUDE.md is read every session and NORTHSTAR.md only "once in a while." Getting this section wrong or skipping it is the single failure mode this step exists to prevent — check it, don't just assume the placeholder is decorative).

Then grep the rest of the repo for any other unfilled `{{...}}` token before moving on. An unfilled placeholder anywhere is the single biggest cause of a second brain drifting into an inconsistent mess.

### Step 6 — Seed the first profile page

Write `wiki/Personal/{Name}.md` per `wiki/_schema.md` (`type: personal`, `version: 1`, rich aliases) from what the data + confirmation surfaced. Deliberately thin; it thickens with ingestion. Its job today is to exist as the anchor page others link back to.

### Step 7 — Offer to keep going, right now, in the same session

If there's real, unprocessed content already sitting in `raw/inbox/` (there usually is, per Step 1), **offer to continue straight into ingesting it now** rather than ending the session and making the user come back and ask separately: *"There's still N files in the inbox — want me to start ingesting them now?"* If yes, run `/ingest-source` in a loop across the inbox in the same session, applying the "don't stop to ask" discipline in that skill's own instructions — this is the system doing what Step 2 of this skill promised: reading what the user brought and getting on with it, not requiring a second invocation to actually start.

If the inbox is empty or the user wants to stop here, close by explaining what happens next, plainly:

1. As exports keep landing over the coming days, drop them into `raw/inbox/` and say "ingest this" (or run `/ingest-source`).
2. `/session-start` re-orients each future session from what's already built.
3. `/wiki-maintenance` at the end of substantive sessions; `/wiki-lint` every 5–10 sessions; `/retro` to keep the system's own discipline improving.

### Milestones, not a calendar

Point the user at `NORTHSTAR.md`'s Milestones section rather than restating it here — progress is checked by what's actually happened (first real ingest, first re-use, first self-made connection, first maintenance catch), not by a day count. There is no "30-day test"; some builds hit these in a week, others take longer depending on how much comes in and how deep the domain is.

## Reference

`context/export-handout.md` — the per-service access instructions, for when the inbox needs more.
`context/data-census.md` — the complete data-source territory — the reference to reach for on "what else do you have," not a script to read aloud.
`context/why-a-second-brain.md` — the architecture and failure modes this setup guards against.
`context/the-6-levels.md` — the memory-level menu for Step 2's draft.
`wiki/_schema.md` — frontmatter and page-type conventions for Step 6.
