---
name: setup-brain
description: First-run bootstrap for a new second brain. Use when the kit is freshly cloned and NORTHSTAR.md doesn't exist yet, when the user asks to "set up my second brain" / "get started" / runs /setup-brain, or when a session opens against an empty wiki/ directory. Data-first flow — help the user get the system access to their original data (exports, connectors, local folders), interrogate that data to learn who they are, then confirm-and-correct with them and ask only what the data can't answer. Writes NORTHSTAR.md and CLAUDE.md, seeds a first profile page. Must complete before any full ingestion — it shapes the schema everything else compiles against.
---

# Setup Brain

The one-time bootstrap that turns a freshly cloned kit into a system shaped around one specific person. Nothing else in the kit works well until this runs — `/ingest-source` needs a schema to write into, `/session-start` needs a NORTHSTAR.md to read.

**The flow is data-first, on purpose.** The old way — interview the user with a form, then go find data — is backwards. This system's whole premise is that the data already knows most of the answers. So: **(1) get access to the original data, (2) interrogate it, (3) ask the user only what the data can't answer, and confirm what it can.** The user corrects a concrete picture instead of filling in blanks.

**Narrate your intent at every step.** Before each step, tell the user in one or two plain sentences *what you're trying to do and why* — "I'm asking for your Claude export because your conversation history is the densest record of how you think; once I can read it, I'll stop asking you questions it already answers." A user who knows what you're aiming at can help you get there — volunteer a folder you didn't know existed, warn you off a dead end, correct a wrong guess early. A silent setup wastes the person sitting right there.

## Instructions

### Step 0 — Verify the skeleton

```bash
ls -la
git status 2>/dev/null || echo "no git repo yet"
```

Confirm `raw/inbox/`, `raw/ingested/topic-sources/`, `wiki/{Topics,Entities,Projects,Sources,Synthesis,Personal,Journal,Tasks}/`, `memory/`, `constitution/`, `context/` all exist. If any are missing, create them. **If `git status` fails, OR the repo exists but has zero commits, run `git init` (if needed) and commit the bare skeleton** — git is the reversibility layer for everything that follows, and a repo with no history is functionally the same as no repo.

### Step 1 — Get the system access to the original data (the first real step)

Tell the user what you're doing: *"Before I ask you anything about yourself, I want access to your original data — your AI conversation history, notes, calendar, email. I'll learn most of who you are from that, and then I only need you to correct me and fill the gaps. Here's how to get me each source."*

**Say the trade-off out loud, before asking for a single export**: *"You can leave out anything you don't want in here — nothing is mandatory, and you can always add more later. But the more you bring together, the more useful this actually gets — a brain that only sees a slice of you gives you a slice of the value. One honest caveat: consolidating everything means feeding it through an AI session to get processed, so be deliberate about what you include, especially anything genuinely sensitive — that's what Step 3's private-forever question is for."* Say this once, plainly, before the lanes below — not as a legal disclaimer, but so the user makes an informed choice about how much to bring rather than discovering the trade-off midway through.

Work through access in three lanes, most-immediate first:

1. **Already on this machine** — existing notes folders (Obsidian vaults, Notion exports, a `Documents/notes/` directory), browser-history SQLite files, anything the user can point at right now. Ask: *"Is there anything already on this machine I should read — notes, an old vault, exports you've downloaded before?"* Copy (never move) anything offered into `raw/inbox/`.
2. **Live connectors** — if this Claude has Google Drive / Calendar / Gmail connectors available (claude.ai → Settings → Connectors), walk the user through connecting them. These are the only sources that stay *live* rather than batch — calendar and email then feed the brain continuously without re-exports.
3. **Batch exports** — walk `context/export-handout.md` with the user source by source, and ask the open-ended question explicitly rather than relying on memory of a short list: *"What else do you have — Notion or another note-taking app, LinkedIn, Google Drive, anything in Microsoft/OneDrive, industry-specific tools?"* The complete territory (every social network, every LLM provider, the full Google catalog, fitness, commerce, and the legal DSAR lever for services with no export button) is `context/data-census.md` — walk it with the user rather than defaulting to just the big four AI providers. Have them **submit the requests in this session, today**. The reason is structural: exports take hours-to-days to arrive and most download links die in 24–48 hours (some services are as short as 72 hours). The requests are the long pole of the whole setup — start them first, and everything else happens while they're in flight. Tell the user which sources you'd prioritize for *them* and why, as it becomes clear what kind of brain this is.

Nothing here blocks: whatever data is reachable *now* feeds Step 2 immediately; the rest arrives over the coming days into `raw/inbox/`.

### Step 2 — Interrogate the data

Tell the user: *"Now I'm going to read what I can reach — titles and metadata first — and build a draft picture of who you are, what you work on, and what you care about. Then you correct it."*

Do a *light, local* pass over everything reachable — inbox contents, connected sources, pointed-at folders: conversation titles from AI exports (run the matching `scripts/parse_*.py` if the format fits), note titles, filenames, calendar-event patterns, the entities and topics that recur. From that, DRAFT the picture: who this person appears to be, what they seem to work on and care about, which data sources they demonstrably have, which tools they actually live in.

Two hard boundaries: (1) **the scan stays shallow and local until the private-forever answer (Step 3) is on the record** — inferring a privacy boundary from the data is backwards. (2) **This drafts the Northstar; it does not ingest.** No wiki pages get written until setup is complete and `/ingest-source` runs under the finished schema.

If no data is reachable yet (requests in flight, nothing local), say so plainly and fall back to the interview below — noting setup can be re-run richer when the exports land.

### Step 3 — Confirm-and-correct, then ask only the gaps

Present the drafted picture and invite correction: *"Your data suggests you're X, working on Y and Z, living mostly in tools A and B — what's wrong or missing in that picture?"* People are far better at correcting a concrete draft than at answering abstract questions cold.

Then ask only what the data can't answer, one question at a time, each with its why:

1. **What should this brain *do*?** Research depth (a thinking partner for hard problems) · personal/life memory (dates, people, decisions, health, money) · business/project context · all three. Decides the page taxonomy. The data shows what they *have*; only the user knows what they *want from it*.
2. **How do you work across tools?** — confirm against the evidence; read `context/the-6-levels.md` first. Default recommendation: **Level 5** (this kit). Level 6 only for people actively juggling several AI assistants who need one memory layer under all of them.
3. **What is private-forever?** ALWAYS asked explicitly, never inferred — health details, financial specifics, other people's words in messages, anything that must never leave `raw/` or be synthesized into a wiki page even in general terms. This becomes the redaction policy in `CLAUDE.md`, on the record before the first file is processed.

### Step 4 — Explain Northstar + constitution, then write NORTHSTAR.md

Most new users have never met either concept. Explain both using the shipped worked examples — the "what a Northstar even is" section and the system's own Northstar in `NORTHSTAR.md`, and `constitution/README.md` for what a constitution is plus the second brain's own six rules. Their answers then *specialize* the system Northstar rather than starting from a blank page.

Write `NORTHSTAR.md` from the confirmed picture + the three answers. One page: who this is for, what the brain should do, the chosen level and why, and the private-forever boundary stated as a hard rule.

### Step 5 — Fill every remaining placeholder, not just CLAUDE.md's

`CLAUDE.md` is the schema every session reads first. Fill `{{USER_NAME}}`, `{{PURPOSE_SUMMARY}}`, and `{{PRIVACY_BOUNDARIES}}` (its own `## Private-Forever` section — the same categories as NORTHSTAR.md's, restated there on purpose, because CLAUDE.md is read every session and NORTHSTAR.md only "once in a while." Getting this section wrong or skipping it is the single failure mode this step exists to prevent — check it, don't just assume the placeholder is decorative).

Then grep the rest of the repo for any other unfilled `{{...}}` token before moving on — `wiki/_schema.md` and other files may carry their own. An unfilled placeholder anywhere is the single biggest cause of a second brain drifting into an inconsistent mess — every session re-derives its own conventions instead of reading one shared, fully-completed source.

### Step 6 — Seed the first profile page

Write `wiki/Personal/{Name}.md` per `wiki/_schema.md` (`type: personal`, `version: 1`, rich aliases) from what the data + confirmation surfaced. Deliberately thin; it thickens with ingestion. Its job today is to exist as the anchor page others link back to.

### Step 7 — Explain the loop

Close by explaining what happens next, plainly:

1. Exports keep landing in `raw/inbox/` over the coming days — that's normal and expected.
2. `/ingest-source` (or dropping a file and saying "ingest this") processes each into `wiki/` — pages written or enriched, a source record, cross-links, a log line, the original filed as provenance.
3. `/session-start` re-orients each future session from what's already built.
4. `/wiki-maintenance` at the end of substantive sessions; `/wiki-lint` every 5–10 sessions; `/retro` to keep the system's own discipline improving.

### The 30-day test

Be honest about the curve: the first month is mostly investment — field experience says time-invested roughly equals time-saved at one month, compounding after (see `context/why-a-second-brain.md`). The test at 30 days: does a new session start *from* what's compiled, instead of you re-explaining the same background? If sessions still start from zero, ingest more before expecting compounding value.

## Reference

`context/export-handout.md` — the per-service access instructions Step 1 walks through.
`context/data-census.md` — the complete data-source territory (every social network, every LLM provider, the full Google catalog, fitness, commerce, the DSAR lever) — walk this, not just the short list, when asking "what else do you have."
`context/why-a-second-brain.md` — the architecture and failure modes this setup guards against.
`context/the-6-levels.md` — the memory-level menu in Step 3.
`wiki/_schema.md` — frontmatter and page-type conventions for Step 6.
