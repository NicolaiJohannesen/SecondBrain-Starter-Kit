---
name: setup-brain
description: First-run bootstrap for a new second brain. Use when the kit is freshly cloned and NORTHSTAR.md doesn't exist yet, when the user asks to "set up my second brain" / "get started" / runs /setup-brain, or when a session opens against an empty wiki/ directory. Interviews the user, writes NORTHSTAR.md and CLAUDE.md from their answers, seeds a first profile page, and points them at requesting their data exports. Must run before any ingestion — it shapes the schema everything else compiles against.
---

# Setup Brain

The one-time bootstrap that turns a freshly cloned kit into a system shaped around one specific person. Nothing else in the kit works well until this runs — `/ingest-source` needs a schema to write into, `/session-start` needs a NORTHSTAR.md to read. Run this first, always.

## Instructions

### Step 0 — Verify the skeleton

```bash
ls -la
git status 2>/dev/null || echo "no git repo yet"
```

Confirm `raw/inbox/`, `raw/ingested/topic-sources/`, `wiki/{Topics,Entities,Projects,Sources,Synthesis,Personal,Journal,Tasks}/`, `memory/`, `constitution/`, `context/` all exist. If any are missing, create them — the folder layout is load-bearing, not decorative.

If `git status` fails, run `git init` and make a first commit of the bare skeleton before touching content. Git is the reversibility layer for everything that follows; nothing should be built on a tree with no history.

### Step 0.5 — Mine the inbox before asking anything

Check `raw/inbox/` before starting the interview. If the user has already dropped exports or notes there, **most of the interview's answers are sitting in that data** — and asking cold questions the substrate can already answer is the exact failure this whole system exists to end.

```bash
ls -la raw/inbox/
```

If the inbox is non-empty, do a *light, local* pass — titles and metadata first, not deep content synthesis: conversation titles from AI exports (run the matching `scripts/parse_*.py` if the format fits), note titles, filenames, the entities and topics that recur. From that, DRAFT provisional answers to interview questions 1–4: who this person appears to be, what they seem to work on and care about, which data sources they demonstrably have, which tools they actually use. Then run the interview as **confirm-and-correct** instead of blank-form: *"Your data suggests you're X working on Y, with sources A/B/C — what's wrong or missing in that picture?"* People are far better at correcting a concrete draft than at answering abstract questions from a standing start.

Two hard boundaries: (1) **Question 5 — private-forever — is ALWAYS asked explicitly and never inferred.** Inferring a privacy boundary from the data is backwards: the scan itself must stay shallow and local until that answer is on the record. (2) The inbox scan drafts the Northstar; it does not ingest. No wiki pages get written from inbox content until setup is complete and `/ingest-source` runs under the finished schema.

If the inbox is empty, proceed with the cold interview below — and mention that dropping exports in first (see `context/export-handout.md`) makes setup smarter if they'd rather do that and come back.

### Step 1 — Interview, one question at a time

Do not batch these into a form. Ask one, wait for the answer, then ask the next — each answer should genuinely shape the next question, and a wall of questions gets skimmed rather than answered. Explain briefly *why* each question matters so the user isn't just filling in blanks.

1. **Who are you and what do you do?** Seeds `wiki/Personal/` and the entity pages this brain will build around. Get enough to write a real profile page, not a one-liner.
2. **What should this brain *do*?** Offer the menu: research depth (a thinking partner for hard problems) · personal/life memory (dates, people, decisions, health, money) · business/project context (a specific piece of work) · all three. This decides the page taxonomy — a research-only brain barely touches `Personal/`; a life-memory brain leans on it heavily.
3. **What data sources do you actually have?** Walk the checklist out loud rather than asking abstractly — most people don't remember what they've got until prompted: Claude conversations, ChatGPT, Grok, Gemini, Google Keep, Apple Notes, Notion, calendar, email, browser history, health data, bank/brokerage statements, messages (WhatsApp/iMessage/X), Kindle highlights. For each "yes," note it — Step 5 turns this into a concrete request list.
4. **How do you work across tools?** One AI assistant used deeply, or several switched between constantly? Read `context/the-6-levels.md` before asking this one so the recommendation is grounded, not generic. Default recommendation: **Level 5** (the LLM-maintained wiki this kit builds) — right for anyone doing deep, recurring, compounding work with one primary tool. Only recommend Level 6 (a database-backed layer reachable from multiple tools) if they're actively juggling several AI assistants day to day and need one memory layer under all of them.
5. **What is private-forever?** Name it explicitly, now — health details, financial specifics, other people's words in messages, anything that should never leave `raw/` and never get synthesized into a wiki page even in general terms. This becomes the redaction policy in `CLAUDE.md`. Don't let this be an afterthought discovered mid-ingestion; get it on the record before the first file is ever processed.

### Step 2 — Write NORTHSTAR.md

Using the five answers (confirmed against the inbox evidence where it existed), write `NORTHSTAR.md` at the repo root. It's the one-page statement of what this brain is *for* — every later prioritization call (what to ingest first, what a lint pass should flag, what `/retro` should optimize toward) reads back to this file. Keep it short — a page, not a manifesto. Cover: who this is for, what the brain should do (from answer 2), the chosen memory level (from answer 4) and why, and the private-forever boundary (from answer 5) stated as a hard rule, not a suggestion.

### Step 3 — Fill CLAUDE.md placeholders

`CLAUDE.md` at the repo root is the schema document every session reads before doing anything — frontmatter conventions, wikilink rules, the ingest workflow, the folder layout. Fill in the placeholders (`{{USER_NAME}}`, `{{PURPOSE_SUMMARY}}`, and any private-forever categories from Step 1.5) with the interview answers. If `CLAUDE.md` doesn't exist yet in this clone, write it from the kit's template rather than skipping the step — an unfilled schema is the single biggest cause of a second brain drifting into an inconsistent mess, because every session re-derives its own conventions instead of reading one shared source.

### Step 4 — Seed the first profile page

Write `wiki/Personal/{Name}.md` using the frontmatter format in `wiki/_schema.md` (`type: personal`, `created`, `updated`, `version: 1`, `tags`, `aliases`). Populate it with what the interview surfaced — who they are, what they do, what matters to them right now. This is deliberately thin at first; it thickens as ingestion proceeds. Its job today is to exist as an anchor page other pages can link back to.

### Step 5 — Point at the export handout, today

Read `context/export-handout.md` and hand the user the concrete request list built from their Step 1 answers (which sources they said "yes" to). This step has to happen in this same session, not later — the reason is structural, not urgency theater: **most export links expire in 24–48 hours**, and the data itself can take days to arrive. Requesting on day one means the exports are ready to ingest by the time the rest of the setup is done; requesting on day five means another week of waiting on top. Tell them plainly: request now, the data will show up in a few days, that's normal and expected.

### Step 6 — Explain the loop

Close the setup by explaining the operating loop in plain terms, so the user knows what happens next without having to ask:

1. Exports and any other material land in `raw/inbox/`.
2. Running `/ingest-source` (or just dropping a file and saying "ingest this") processes it into `wiki/` — writing or enriching pages, creating a source record, cross-linking, logging, and filing the original away as provenance.
3. `/session-start` at the top of each future session re-orients from what's already built.
4. `/wiki-maintenance` runs at the end of substantive sessions; `/wiki-lint` runs every 5–10 sessions to catch drift.
5. `/retro` runs at the end of substantive sessions to keep the system's own operating discipline improving.

### The 30-day test

Tell the user honestly what to expect: the first month is mostly investment, not payoff — this matches the field experience of people who've built these systems (see `context/why-a-second-brain.md`). The test that matters at 30 days: does a new session start *from* what's already compiled instead of re-explaining the same background every time? If yes, the loop is working. If the wiki still feels thin or sessions still start from zero, that's a signal to ingest more before expecting compounding value.

## Reference

`context/why-a-second-brain.md` — the architecture and the failure modes this setup guards against.
`context/the-6-levels.md` — the memory-level menu referenced in Step 1.4.
`wiki/_schema.md` — the frontmatter and page-type conventions referenced in Step 4.
