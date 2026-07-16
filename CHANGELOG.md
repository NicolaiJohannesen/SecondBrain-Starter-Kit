# Changelog

All notable changes to this kit are recorded here. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## Unreleased

### Added
- **`context/ancillary-options.md`** — optional tooling to extend the brain once it's running: Obsidian-format skills for anyone browsing the wiki in Obsidian, a cross-vendor agentic-CLI reference (orchestrator + specialist-subprocess pattern), the MCP-server safety question (can it search-only, or can it also transact) with a worked travel example, and a hardware-aware speech-to-text decision guide (Apple Silicon → local Whisper is fine; older Intel Macs → cloud dictation apps are strictly better on both accuracy and CPU cost, not just more convenient). Nothing here is required; the kit works fully without any of it.

### Changed — a second round of real feedback, same day
- **Prerequisites now progressive, not a wall.** Only Claude Code is a real blocking requirement; git is mentioned in passing where it's actually relevant (cloning) instead of listed as a prerequisite, and Obsidian moved to the end as an optional nice-to-have. Complexity should reveal itself as it becomes relevant, not front-load before the reader has seen any value.
- **Corrected a mischaracterization: this was never about asking fewer questions.** It's about not asking ANY question until the data has genuinely been exhausted — effort before asking, not a target count. `setup-brain`'s Step 2 rewritten from "a light, local pass" to an explicitly thorough read (open files, read content, not just titles); the "ask as little as possible" framing replaced with "spend real time first, the few surviving questions are a consequence of that effort, not the goal."
- **Documented the under-inclusion failure mode.** Added as a fourth failure mode in `context/why-a-second-brain.md` (parallel to the collector's fallacy, taxonomy death, silent staleness): most people who build one of these want full context, and holding back too much — out of caution about effort or mild sensitivity rather than genuine privacy — makes the brain "nearly useless" (thin, patchy answers; nothing to cross-reference). Reinforced at the actual decision point in `setup-brain`'s Step 1 trade-off framing.

### Changed — real field feedback (first non-author test of the kit)
- **Removed the 30-day test mechanism entirely, replaced with Milestones.** A fixed calendar checkpoint doesn't fit everyone's pace; `NORTHSTAR.md`, `setup-brain`, and `how-to-build.md` now track achievement-based checkpoints instead (setup complete → first real ingest → first re-use → first self-made connection → first maintenance catch). `CLAUDE.md`'s "done at 30 days" framing removed too.
- **Restructured the Quickstart sequence** — copying data into `raw/inbox/` now happens *before* `/setup-brain` runs, not after. The old order (request exports → run setup → drop exports in later) meant setup ran against an empty inbox in practice; now the user brings what they have first, so setup has real material from the start. Zip files can be dropped in directly — no manual unzip required.
- **Cut the number of explicit questions `/setup-brain` asks.** What the brain should focus on and which delegation level fits are now drafted from the data (like who-you-are already was) and confirmed in one combined pass; only the private-forever question — which structurally can't be inferred — is still asked as a standalone question.
- **`/ingest-source` now extracts archives automatically** (`.zip`/`.tar`/`.tar.gz`) instead of assuming pre-extracted files, and processes every cluster found in one session rather than stopping between them.
- **Added a "Defaults — don't stop to ask" section to `/ingest-source`**: documented defaults for unrecognized formats, mixed-content archives, ambiguous topic placement, and borderline-private content, so autonomous runs act on a decided default instead of guessing or interrupting for things the docs already answer.
- **`/setup-brain` now offers to chain straight into ingesting the inbox** in the same session once setup finishes, instead of ending the session and requiring a separate invocation.

### Changed
- Quickstart step 3 ("get your data flowing") rewrote as one clear action (request your AI-conversation export right now, with the exact click path) instead of a three-lane taxonomy dumped in the reader's face — the full source list stays one hop away in `context/export-handout.md` / `context/data-census.md`, where it belongs. Step 4 similarly trimmed — the instruction leads, the explanation follows in one sentence instead of a parenthetical before it.

## 0.2.0 — 2026-07-14

**Cold-start validated.** A blind dry-run (a fresh agent with zero memory of the authoring session, playing a brand-new user against a scratch clone) proved the `/setup-brain` data-first flow works end-to-end — and found one real bug the authoring session's own re-reads had missed.

### Fixed
- **`CLAUDE.md` had no section for private-forever categories at all.** Only `NORTHSTAR.md` (read "once in a while," per the kit's own docs) carried that boundary — `CLAUDE.md` (read every session) didn't. A session following the setup instructions literally could miss the privacy rule entirely. `CLAUDE.md` now carries its own Private-Forever section mirroring `NORTHSTAR.md`'s field; `NORTHSTAR.md` stays canonical if the two ever disagree.
- `wiki/_schema.md` carried a dangling `{{USER_NAME}}` placeholder that `/setup-brain`'s Step 5 never mentioned filling — now points at `CLAUDE.md` instead of forking the same fact into a second token.
- `wiki/_schema.md`'s Quality Standards table had no row for `personal`-type pages.
- `/setup-brain` Step 0's git-init trigger was binary ("if `git status` fails") and missed the case where a repo exists with zero commits.
- The Karpathy citation in `context/why-a-second-brain.md` linked a bare profile page instead of the actual gist.

### Added
- **A literal copy-paste start prompt** in the README's Quickstart (`Hello — my name is [YOUR NAME]...`) — an explicit trigger for `/setup-brain` instead of relying on Claude noticing an empty wiki on its own.
- `context/data-census.md` — the complete per-service data-export territory (every social network, every LLM provider, the full Google catalog, fitness, commerce, plus the GDPR/CCPA legal lever for services with no export button).
- `/setup-brain` Step 1 now states the data-consolidation trade-off explicitly before asking for any export, and points at the full data census instead of a short hardcoded source list.
- `wiki/Topics/Intent-Driven Development.md` and `wiki/Topics/Test-Driven Development.md` — the intent cascade from a Northstar down to a failing test, and why tests are the strongest anti-drift device an AI-assisted build has.
- `context/deploying-to-cloudflare.md`, `context/connecting-outside-sources.md`, `context/external-tools-and-apis.md`, `context/building-software-projects.md`, `context/memory-compaction.md`, `context/about-these-docs.md`.
- The `/memory-compact` skill.
- 26 kit-seed Topic pages in `wiki/Topics/` — the machinery and thinking layer the brain ships already knowing.

## 0.1.0-dev — 2026-07-03

Initial public release. MIT-licensed. Authored fresh into a standalone repo (PII-scanned before every push, nothing bulk-copied from any private source). Core: `CLAUDE.md` schema template, `NORTHSTAR.md` template, the constitution (assistant behavior, epistemic layer, verification discipline), the data-first `/setup-brain` bootstrap, `/ingest-source`, `/session-start`, `/wiki-maintenance`, `/wiki-lint`, `/survey-sources`, `/retro`, `/assistant`, four export parsers.
