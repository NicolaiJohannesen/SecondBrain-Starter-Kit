# Changelog

All notable changes to this kit are recorded here. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

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
