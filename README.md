# Second Brain Starter Kit

Everything you need to build your own **AI-maintained second brain**: a persistent, compounding knowledge base in plain markdown that Claude Code maintains for you — so your AI reasons from everything you've ever fed it instead of starting from zero every conversation.

The architecture is the LLM-wiki pattern ([Karpathy, April 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)): immutable raw sources in, compiled cross-linked wiki out, an instruction schema in between — plus the layers most DIY builds skip: an epistemic quality layer (so the brain is *trustworthy*, not just large), an assistant constitution, a task system, and the maintenance loops that keep it alive.

**You own the artifact.** Markdown files in folders you control, versioned with git, readable without any tool. No platform can reprice or delete your brain.

## Quickstart (data first — 30 minutes of setup, exports arrive over days)

The setup is deliberately **flipped from how most tools onboard you**: instead of filling in a form about yourself, you first get the system access to your original data — then it reads that data, tells you what it sees, and asks you only what the data can't answer. Throughout, it tells you what it's trying to do and why, so you can help it.

1. **Prerequisites**: [Claude Code](https://claude.com/claude-code) installed and signed in; git; optionally [Obsidian](https://obsidian.md) pointed at `wiki/` as your reading/graph surface.
2. **Clone this kit** (or Code → Download ZIP) into a folder that will BE your second brain — e.g. `~/brain/`.
3. **Get your data flowing — before anything else.** This is the long pole: exports take hours-to-days to arrive and most download links expire in 24–48 hours, so the requests go in first and everything else happens while they're in flight. Three lanes (full per-service instructions: `context/export-handout.md`):
   - **Already on your machine** — old notes folders, an Obsidian vault, previously downloaded exports → drop copies into `raw/inbox/`.
   - **Live connectors** — connect Google Drive / Calendar / Gmail (claude.ai → Settings → Connectors) so calendar and email feed the brain continuously.
   - **Batch exports** — request them today: Claude, ChatGPT, Grok, Google Takeout (Keep / Calendar / Mail), Apple Health, X, Reddit, Kindle…
4. **Open Claude Code in the folder and run `/setup-brain`.** It reads whatever data is already reachable, drafts a picture of who you are and what you work on, and asks you to **confirm-and-correct** — plus the few questions data can't answer (what you want the brain to *do*, and what is private-forever, which is always yours to state explicitly). From your answers it writes your `NORTHSTAR.md` and personalizes the schema. Full ingestion only starts after this — the schema shapes what compilation produces.
5. **As exports arrive, drop them into `raw/inbox/` and run `/ingest-source`.** Claude reads each source, writes/updates wiki pages, cross-links, logs, and files the original away.
6. From then on: ask questions (good answers get filed back as pages), run `/wiki-maintenance` at session end, `/wiki-lint` every 5–10 sessions, `/retro` to make the system improve itself.

## What's in the kit

| Path | What it is |
|---|---|
| `CLAUDE.md` | **The keystone** — the schema that turns Claude Code into a disciplined wiki maintainer (page formats, conventions, the three operations: ingest / query / lint) |
| `NORTHSTAR.md` | Your purpose statement — written by `/setup-brain` from your answers. Never met a "Northstar"? The file explains the concept and ships the second brain's own as the worked example |
| `context/` | The understanding: why this works (`why-a-second-brain.md`), the full build manual (`how-to-build.md`), which memory architecture fits you (`the-6-levels.md`), which Claude model for which job (`model-routing.md`), the automation layer (`loops.md`), and the per-service data-export handout |
| `constitution/` | What a constitution is + the second brain's own six rules (`README.md`), how the assistant behaves (`assistant-constitution.md`), how it thinks (`epistemic-layer.md` — 11 reasoning moves), how it verifies (`verification.md`) |
| `.claude/skills/` | The workflows as callable commands: `/setup-brain`, `/ingest-source`, `/session-start`, `/wiki-maintenance`, `/wiki-lint`, `/survey-sources`, `/retro`, `/memory-compact`, `/assistant` |
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
