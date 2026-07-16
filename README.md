# Second Brain Starter Kit

**What this is**: everything you need to build your own AI-maintained second brain — a persistent, compounding knowledge base in plain markdown that Claude Code maintains for you.

**Why it exists**: every new AI conversation starts blank. You re-explain who you are, what you're working on, and what you already tried — every single time — because the model has nothing to reason from but the current chat. This kit gives Claude Code a compiled wiki to read from and write to instead, so it reasons from everything you've ever fed it rather than starting from zero.

The architecture is the LLM-wiki pattern ([Karpathy, April 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)): immutable raw sources in, a cross-linked wiki out, an instruction schema in between — plus the layers most DIY builds skip. An **epistemic-quality layer** keeps the brain trustworthy, not just large: load-bearing claims get verified, evidence gets labeled, contradictions get named instead of silently resolved. An **assistant constitution** fixes how Claude behaves toward you so it doesn't have to be re-negotiated every session. A **task system** and **maintenance loops** (lint, retro, memory compaction) keep the whole thing from rotting the way most personal wikis do.

**You own the artifact.** Plain markdown files, versioned with git, readable without any tool. No platform can reprice, lock, or delete your brain.

## Quickstart

The setup is deliberately **flipped from how most tools onboard you**: instead of filling in a form about yourself, you first give the system your original data — then it reads that data, tells you what it sees, and asks you only what the data can't answer.

1. **Get [Claude Code](https://claude.com/claude-code) installed and signed in.** That's the only thing you need before starting — everything else here can wait until it's actually relevant.
2. **Download this kit** (Code → Download ZIP) into the folder that will BE your second brain — e.g. `~/brain/`. Comfortable with git? `git clone` works the same way — useful later for tracking changes and pushing to your own remote, not something you need to know today.
3. **Copy whatever data you already have into `raw/inbox/` — before you open Claude Code at all.** Old exports, notes, a folder of files — drop them in as they are. **Zip files are fine to drop in directly, no need to unzip first.** Don't have anything on hand yet? That's fine too, go get what you can — the per-service how-to is reference material, not something to read now: [`context/export-handout.md`](context/export-handout.md) (quick list) and [`context/data-census.md`](context/data-census.md) (the complete territory, every service). Come back and copy in whatever you get.
4. **Open Claude Code in the folder and send this as your first message:**

   ```
   Hello — my name is [YOUR NAME]. I just cloned the Second Brain Starter Kit
   and I'm ready to set up my second brain. Please run /setup-brain.
   ```

   It reads what's already in the inbox, drafts a picture of who you are and what this brain should focus on, and asks you to **confirm-and-correct** that — plus the one thing it can't infer for you: what's private-forever. From there it writes your `NORTHSTAR.md` and starts ingesting what's in the inbox.
5. **From here it runs largely on its own.** It shouldn't need to stop and ask you things that are already answered in its own documentation — only genuine judgment calls (an ambiguous private-forever question, a real contradiction) surface to you. As more exports arrive over the following days, drop them into `raw/inbox/` and say "ingest this" (or run `/ingest-source`) whenever you're ready.
6. Ongoing habits: ask questions (good answers get filed back as pages), `/wiki-maintenance` at session end, `/wiki-lint` every 5–10 sessions, `/retro` to make the system improve itself.

Whenever you want a visual way to browse it — not required, just nice to have — point [Obsidian](https://obsidian.md) at the `wiki/` folder and read it as a graph.

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

**The wiki starts pre-populated with 26 seed pages** in `wiki/Topics/` — the extra knowledge your brain ships with, so the graph isn't empty on day one and every concept these docs use has a worked page behind it. Each is tagged `origin: kit-seed`; they are yours now — edit, extend, or delete them freely; nothing depends on them staying as shipped. What's in there:

- **The machinery your brain runs on**: Second Brain · Personal Context Layer · Loop Engineering · Claude Code Agentic Primitives · AI Agents · Sub-agents and Agent Teams · Agent Skills · Agent Orchestration · Multi-Agent Systems · Memory Compaction · Engine-Writes-Substrate · The Harness Is the Product · Model Context Protocol (MCP) · Context Engineering · Agent Failure Modes
- **The thinking layer behind the constitution**: Feedback Loops (Universal Pattern) · Culture of Learning · Single-loop vs Double-loop Learning · OODA Loop · Commander's Intent (the lineage of your NORTHSTAR.md) · **Intent-Driven Development** (the intent cascade from your Northstar down to tests) · **Test-Driven Development** (the cascade's executable bottom rung — write the failing test first and an AI executor can't rationalize its way around your intent) · Plan-Writing for AI Coding Agents · Verification Discipline and Assertion Types · Writing as External Memory · Compound Growth

When your own ingested content mentions agents, loops, or feedback — and it will — those wikilinks resolve into this spine from day one.

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
| Find EVERY source you have — the complete census (LinkedIn, Meta, TikTok, every LLM provider, the full Google catalog, fitness, commerce…) + the legal lever when no export exists | `context/data-census.md` |
| Automate the maintenance loops | `context/loops.md`, `context/model-routing.md` |
| Use external tools, CLIs, and model APIs safely | `context/external-tools-and-apis.md` |
| Build and deploy software projects from your brain | `context/building-software-projects.md`, `context/deploying-to-cloudflare.md` |
| Keep the brain healthy over time | `/wiki-maintenance`, `/wiki-lint`, `/retro`, `/memory-compact`, `context/memory-compaction.md` |
| Understand how these docs themselves are organized | `context/about-these-docs.md` |

## The whole project runs a culture of learning

This isn't a feature of one skill — it's the design principle of the entire kit, at every layer:

- **The brain learns**: every ingested source compounds the wiki; every good answer gets filed back as a page instead of evaporating in chat history.
- **The assistant learns**: `/retro` runs at the end of substantive sessions and codifies corrections, near-misses, and insights into `memory/` — so nothing has to be taught twice. `/memory-compact` keeps those lessons loadable as they accumulate.
- **The system's own rules learn**: the constitution and `CLAUDE.md` are living documents — editing them deliberately *is* how you tune your system's character (constitution rule 6: the system that runs month two should be better than the one that ran month one).
- **The docs learn**: hit a question these docs didn't answer? Open an issue. A repeated question is a documentation bug, and maintainers fold it back in ([`context/about-these-docs.md`](context/about-these-docs.md)).
- **Even drift-prevention is a learning structure**: intent pinned at every altitude — your `NORTHSTAR.md` at the top, the constitution in the middle, and *failing-tests-written-first* at the bottom ([`wiki/Topics/Intent-Driven Development.md`](wiki/Topics/Intent-Driven%20Development.md)) — so the system can detect when it's drifting instead of discovering it later.

The background for all of this is the [Culture of Learning](wiki/Topics/Culture%20of%20Learning.md) seed page: the Senge/Argyris/Dweck/Edmondson research lineage, and why cultures where lessons get *captured* compound while cultures where lessons live in conversation decay.

## The honest expectations

- **Progress is milestone-based, not calendar-based** — see `NORTHSTAR.md`'s Milestones section once it's written. One documented build of this pattern found time-invested ≈ time-saved around a month of real use, with the payoff compounding after — a useful data point for expectations, not a schedule to hold yourself to.
- **Capture is not the hard part — distillation is.** Second brains die of the collector's fallacy (hoarding) and taxonomy rot (elaborate tags nobody maintains). This kit's answer: the LLM does the bookkeeping, the schema enforces structure, and the lint loop catches drift. Your job is judgment, not filing.
- **Privacy is architectural here**: `raw/` never leaves your machine (gitignored), the wiki is compiled locally, and anything you mark private-forever during setup stays out of the wiki entirely. If you push your personal brain to a remote, make it a **private** repo.

## Fork it, improve it

This kit is a living template. Issues and PRs welcome — especially new export parsers and schema improvements. See [CHANGELOG.md](CHANGELOG.md) for what's shipped and when.

**Found a gap?** If you hit a question these docs didn't answer, open an issue rather than routing around it silently. The docs are meant to learn the same way the wiki does: a repeated question is a signal, and maintainers fold it back in so the next person doesn't hit the same wall. See `context/about-these-docs.md` for the full discipline this runs on.
