# Second Brain Starter Kit

**What this is**: everything you need to build your own AI-maintained second brain — a persistent, compounding knowledge base in plain markdown that Claude Code maintains for you.

**Why it exists**: every new AI conversation starts blank. You re-explain who you are, what you're working on, and what you already tried — every single time — because the model has nothing to reason from but the current chat. This kit gives Claude Code a compiled wiki to read from and write to instead, so it reasons from everything you've ever fed it rather than starting from zero.

The architecture is the LLM-wiki pattern ([Karpathy, April 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)): immutable raw sources in, a cross-linked wiki out, an instruction schema in between — plus the layers most DIY builds skip. An **epistemic-quality layer** keeps the brain trustworthy, not just large: load-bearing claims get verified, evidence gets labeled, contradictions get named instead of silently resolved. An **assistant constitution** fixes how Claude behaves toward you so it doesn't have to be re-negotiated every session. A **task system** and **maintenance loops** (lint, retro, memory compaction) keep the whole thing from rotting the way most personal wikis do.

**You own the artifact.** Plain markdown files, versioned with git, readable without any tool. No platform can reprice, lock, or delete your brain.

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

## The structure — what every folder is

Once `/setup-brain` has run, this is the map. Everything under `wiki/` is content Claude writes and rewrites over time; everything outside it (the schema, the constitution, the skills) is closer to fixed infrastructure you rarely touch directly.

```
wiki/                   The brain itself — everything Claude reads and writes
  Topics/                 Subject-matter deep dives — a concept you've researched or care about
  Entities/                People, organizations, products, places referenced meaningfully
  Projects/                Things you're building or have built
  Sources/                 One record page per ingested source
  Synthesis/               Cross-source analysis connecting 3+ topics
  Personal/                Health, finance, life knowledge
  Journal/                 Append-only daily log — trajectory, not just state
  Tasks/                   The task system: all-tasks.md (the blob), most-important-now.md, tasks-os.md
  _schema.md               The page-type and frontmatter spec — read before writing any page
  _log.md                  Append-only ingestion log

raw/                    Your originals — immutable, gitignored by default
  inbox/                   The only door in — drop any source here
  ingested/                Everything processed, kept as provenance, filed by topic

CLAUDE.md               The keystone — the schema that turns Claude Code into a disciplined
                         wiki maintainer (page formats, conventions, the three operations)
NORTHSTAR.md             Your purpose statement — what this brain is for, written by /setup-brain
constitution/           What a constitution is + this kit's own six rules (README.md), how the
                         assistant behaves (assistant-constitution.md), how it thinks
                         (epistemic-layer.md), how it verifies (verification.md)
context/                The explanations and how-to guides — see "Find what you need" below
.claude/skills/         The workflows as callable commands (nine, one line each below)
scripts/                Parsers that convert export formats into ingestable staging JSON
memory/                 The assistant's learned lessons about working with you
```

**The wiki starts pre-populated with 24 seed pages** in `wiki/Topics/` — on concepts this kit itself is built from (Second Brain, Culture of Learning, Feedback Loops, AI Agents, Memory Compaction, and others). Each is tagged `origin: kit-seed` in its frontmatter. They exist so the graph isn't empty on day one and so concepts referenced throughout these docs (Northstar, constitution, culture of learning) have a worked page behind them. They are yours now — edit, extend, or delete them freely; nothing about the kit depends on them staying as shipped.

**The nine skills** in `.claude/skills/` — each a callable slash command:

- `/setup-brain` — first-run bootstrap: reads your data, drafts your `NORTHSTAR.md`, personalizes the schema
- `/ingest-source` — process one new source from `raw/inbox/` into the wiki
- `/session-start` — orient at the start of a session: what changed, what's next
- `/wiki-maintenance` — quick end-of-session hygiene check, scoped to pages touched that session
- `/wiki-lint` — periodic whole-wiki health check: orphan pages, stale claims, contradictions
- `/survey-sources` — refresh `raw/MANIFEST.md`, the processing-status tracker
- `/retro` — self-improvement retrospective: codify corrections and near-misses automatically
- `/memory-compact` — keep the `memory/` index within its size limit as it accumulates
- `/assistant` — the default operating mode: how Claude behaves in this project by default

## Find what you need

Organized by what you're trying to do, not by folder — each row links to the doc written for that specific need (a tutorial, a how-to, a reference, or an explanation; see `context/about-these-docs.md` for why the docs are split this way).

| You want to… | Go to |
|---|---|
| Understand *why* this works | `context/why-a-second-brain.md`, `context/the-6-levels.md`, the `wiki/Topics/` seed pages |
| Set up your brain | `/setup-brain`, `context/export-handout.md` |
| Get data in from outside sources (Google Docs/Drive/Gmail/Calendar, Claude/ChatGPT/Grok exports, live connectors) | `context/connecting-outside-sources.md`, `context/how-to-build.md` |
| Automate the maintenance loops | `context/loops.md`, `context/model-routing.md` |
| Use external tools, CLIs, and model APIs safely | `context/external-tools-and-apis.md` |
| Build and deploy software projects from your brain | `context/building-software-projects.md`, `context/deploying-to-cloudflare.md` |
| Keep the brain healthy over time | `/wiki-maintenance`, `/wiki-lint`, `/retro`, `/memory-compact`, `context/memory-compaction.md` |
| Understand how these docs themselves are organized | `context/about-these-docs.md` |

## The honest expectations

- **Breakeven takes about a month.** The one documented field report of this pattern found time-invested ≈ time-saved at the one-month mark. The payoff compounds after that, and is largest for deep, specialized work where re-explaining your context is genuinely expensive.
- **Capture is not the hard part — distillation is.** Second brains die of the collector's fallacy (hoarding) and taxonomy rot (elaborate tags nobody maintains). This kit's answer: the LLM does the bookkeeping, the schema enforces structure, and the lint loop catches drift. Your job is judgment, not filing.
- **Privacy is architectural here**: `raw/` never leaves your machine (gitignored), the wiki is compiled locally, and anything you mark private-forever during setup stays out of the wiki entirely. If you push your personal brain to a remote, make it a **private** repo.

## Fork it, improve it

This kit is a living template. Issues and PRs welcome — especially new export parsers and schema improvements.

**Found a gap?** If you hit a question these docs didn't answer, open an issue rather than routing around it silently. The docs are meant to learn the same way the wiki does: a repeated question is a signal, and maintainers fold it back in so the next person doesn't hit the same wall. See `context/about-these-docs.md` for the full discipline this runs on.
