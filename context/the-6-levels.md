# The 6 Levels of AI Memory Systems

A practical hierarchy for deciding how much memory infrastructure you actually need. Most people using an AI coding assistant for personal knowledge work climb this ladder one rung at a time, and most never need to go past rung 5. Credit: Simon Scrapes, "Every Claude Code Memory System Compared" (April 2026).

| Level | System | When to choose it |
|---|---|---|
| 1 | Native — a `CLAUDE.md` file plus the tool's built-in auto memory | Simple projects, just getting started |
| 2 | Reliable recall — structured folders plus hooks that inject context automatically | When memory needs to load consistently every session, not just sometimes |
| 3 | Semantic search — vector embeddings over your notes | Larger knowledge bases where keyword/file search stops being enough |
| 4 | Verbatim conversations — full conversation storage and retrieval | Long-running projects that need exact historical record, not just summary |
| **5** | **Self-organizing knowledge base — an LLM-maintained wiki (this kit's default)** | Deep research, complex domains, anything where synthesis compounds |
| 6 | Universal brain — a database-backed memory layer (e.g. Postgres + a protocol like MCP) reachable from any tool | Power users switching between multiple AI tools who need one memory layer underneath all of them |

## Why Level 5 is this kit's default

The hierarchy maps directly onto the write-time-vs-query-time distinction in [context/why-a-second-brain.md](why-a-second-brain.md). Level 5 — the LLM wiki — is where compiled, cross-referenced conceptual depth lives: the AI writes and rewrites pages as understanding deepens, and a session starts from that pre-built synthesis instead of re-deriving it. Level 6 optimizes a different thing entirely: universal access and retrieval precision across tools, at the cost of infrastructure and portability.

Most individuals building a personal second brain want Level 5 and should stay there. Level 6 is the right answer for someone actively juggling several different AI assistants day to day and needing one memory layer underneath all of them — a materially different problem from "help me think."

Many serious builders combine levels rather than picking one — for example, Level 2 hooks (auto-inject relevant context at session start) layered on top of a Level 5 wiki (the compiled knowledge those hooks inject). Layering is normal; treat the table as a menu, not a ladder you must fully climb.

## The markdown-vs-database question, answered honestly

A recurring claim is that the real gold standard for personal AI memory is a heavyweight engineered stack — a temporal knowledge graph plus a vector store plus a key-value store, with an automated extraction pipeline. Markdown, on this telling, is the lightweight beginner option you graduate out of.

Independent benchmarking does not support that framing for a single individual's use case. A few specifics worth knowing before you decide:

- The widely circulated claim that graph-based retrieval beats plain vector search by a wide margin traces back to a single vendor tutorial with a handful of hand-crafted test queries — not an independent benchmark.
- The most rigorous independent head-to-head found graph-based and plain-retrieval approaches "exhibit complementary behaviors rather than a consistent winner." Graphs win narrowly on multi-hop and temporal queries, at a substantial cost in indexing and retrieval speed (tens of times slower to build the index).
- On a well-regarded long-term memory benchmark, plain full-context retrieval outperformed two well-known graph/vector memory products on accuracy; the graph products won on token efficiency and latency, not on getting the right answer. A separate benchmark found the best-performing architecture for long-memory question answering was a plain key-value store, not a graph at all.
- The strongest pro-graph numbers in circulation come from vendor-published whitepapers rather than independent evaluation, and at least one headline claim was independently re-run and came in more than 25 points lower than the vendor's reported figure.

The honest, use-case-dependent answer:

| | Markdown wiki wins | Engineered graph/vector stack wins |
|---|---|---|
| User | a single individual | multi-user or multi-tenant production system |
| Scale | up to roughly 50,000–100,000 tokens of dense wiki (fits directly in an AI's context window — no retrieval step needed) | millions of tokens of conversation history across many users |
| Primary value | compounding synthesis, human-auditable, you own the files, zero infrastructure | automatic extraction at scale, time-aware fact tracking, retrieval across huge corpora |
| Provenance / history | git versioning — full history for free | graph validity windows, engineered separately |

For one person building their own second brain, the markdown wiki is the stronger choice. It puts the AI's genuine advantage — synthesis and bookkeeping — to work on the actual bottleneck, rather than using it to justify a data structure the use case doesn't need. The knowledge stays plain-text, readable, owned, and has no infrastructure that can fail out from under you. The engineered stack is the right architecture for a different problem: production memory serving many users at once, which is the market those vendor products are actually built for.

**The load-bearing conclusion, in the independent literature's own words: a well-structured file beats a poorly populated graph.** The bottleneck is the quality of what goes in — curation, verification, editorial judgment — not the sophistication of the storage engine. If you outgrow a plain markdown wiki, the natural next move is to keep the markdown as the canonical, human-owned layer and add a disposable, rebuildable search index on top of it — not to replace the markdown with a database.

## Related
- [context/why-a-second-brain.md](why-a-second-brain.md) — the case for write-time synthesis and the editorial trap
- [context/how-to-build.md](how-to-build.md) — the build manual, which defaults to Level 5
