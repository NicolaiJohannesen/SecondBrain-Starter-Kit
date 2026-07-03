# Second Brain Starter Kit

Everything you need to build your own **AI-maintained second brain**: a persistent, compounding knowledge base in plain markdown that Claude Code maintains for you — so your AI reasons from everything you've ever fed it instead of starting from zero every conversation.

The architecture is the LLM-wiki pattern ([Karpathy, April 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)): immutable raw sources in, compiled cross-linked wiki out, an instruction schema in between — plus the layers most DIY builds skip: an epistemic quality layer (so the brain is *trustworthy*, not just large), an assistant constitution, a task system, and the maintenance loops that keep it alive.

**You own the artifact.** Markdown files in folders you control, versioned with git, readable without any tool. No platform can reprice or delete your brain.

## Quickstart (30 minutes to a working system)

1. **Prerequisites**: [Claude Code](https://claude.com/claude-code) installed and signed in; git; optionally [Obsidian](https://obsidian.md) pointed at `wiki/` as your reading/graph surface.
2. **Clone this kit** (or Code → Download ZIP) into a folder that will BE your second brain — e.g. `~/brain/`.
3. **Open Claude Code in that folder and run `/setup-brain`.** It interviews you (who you are, what the brain is for, what data you have, what stays private-forever), writes your `NORTHSTAR.md`, and personalizes the schema. **Do this before ingesting anything** — the schema shapes what compilation produces. Pro move: if you already have data exports, drop them into `raw/inbox/` *first* — setup then drafts most of its questions' answers from your own data and just asks you to confirm-and-correct.
4. **Request your data exports today** — see `context/export-handout.md`. Most services take hours-to-days to deliver, and some download links expire in 24 hours, so request now.
5. **Drop exports into `raw/inbox/` and run `/ingest-source`.** Claude reads each source, writes/updates wiki pages, cross-links, logs, and files the original away. Repeat as data arrives.
6. From then on: ask questions (good answers get filed back as pages), run `/wiki-maintenance` at session end, `/wiki-lint` every 5–10 sessions, `/retro` to make the system improve itself.

## What's in the kit

| Path | What it is |
|---|---|
| `CLAUDE.md` | **The keystone** — the schema that turns Claude Code into a disciplined wiki maintainer (page formats, conventions, the three operations: ingest / query / lint) |
| `NORTHSTAR.md` | Your purpose statement — written by `/setup-brain` from your answers. Never met a "Northstar"? The file explains the concept and ships the second brain's own as the worked example |
| `context/` | The understanding: why this works (`why-a-second-brain.md`), the full build manual (`how-to-build.md`), which memory architecture fits you (`the-6-levels.md`), which Claude model for which job (`model-routing.md`), the automation layer (`loops.md`), and the per-service data-export handout |
| `constitution/` | What a constitution is + the second brain's own six rules (`README.md`), how the assistant behaves (`assistant-constitution.md`), how it thinks (`epistemic-layer.md` — 11 reasoning moves), how it verifies (`verification.md`) |
| `.claude/skills/` | The workflows as callable commands: `/setup-brain`, `/ingest-source`, `/session-start`, `/wiki-maintenance`, `/wiki-lint`, `/survey-sources`, `/retro`, `/assistant` |
| `wiki/` | Your brain-to-be: Topics, Entities, Projects, Sources, Synthesis, Personal, Journal, Tasks (+ `_schema.md`, `_log.md`) |
| `raw/` | Your originals — immutable, **gitignored by default** so personal data never gets pushed anywhere |
| `scripts/` | Parsers for common export formats (Claude, Grok, Google Keep, NotebookLM) |
| `memory/` | The assistant's behavioral memory — lessons it learns about working with you |

## The honest expectations

- **Breakeven takes about a month.** The one documented field report of this pattern found time-invested ≈ time-saved at the one-month mark. The payoff compounds after that, and is largest for deep, specialized work where re-explaining your context is genuinely expensive.
- **Capture is not the hard part — distillation is.** Second brains die of the collector's fallacy (hoarding) and taxonomy rot (elaborate tags nobody maintains). This kit's answer: the LLM does the bookkeeping, the schema enforces structure, and the lint loop catches drift. Your job is judgment, not filing.
- **Privacy is architectural here**: `raw/` never leaves your machine (gitignored), the wiki is compiled locally, and anything you mark private-forever during setup stays out of the wiki entirely. If you push your personal brain to a remote, make it a **private** repo.

## Fork it, improve it

This kit is a living template. Issues and PRs welcome — especially new export parsers and schema improvements.
