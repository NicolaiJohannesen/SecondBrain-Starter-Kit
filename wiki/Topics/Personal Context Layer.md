---
type: topic
created: 2026-07-03
updated: 2026-07-03
version: 1
origin: kit-seed
tags:
  - topic
  - seed
  - domain/ai
aliases:
  - Context Layer
  - LLM Wiki Pattern
  - Karpathy LLM Wiki
  - LLM Wiki
  - Personal Knowledge System
  - AI Second Brain
---

# Personal Context Layer

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

A persistent, compounding knowledge structure that an AI maintains on your behalf, so it can reason from pre-built understanding rather than re-deriving knowledge from scratch on every query. The consumer-facing name for the same idea is [[Second Brain]]. This kit exists to install one for you from day one.

## The core problem: query-time synthesis throws the work away

Most AI interactions follow the same pattern: upload documents, ask a question, get an answer. Under the hood this is retrieval-augmented generation (RAG) — the AI retrieves relevant chunks at query time and synthesizes an answer on the fly. The answer can be excellent, but nothing is preserved. The next question starts over. This scales poorly with complexity: as sources multiply, query-time synthesis gets more expensive and more approximate, perpetually rediscovering what was already worked out.

## Compile once, keep current

The alternative is write-time synthesis. When a new source arrives, the AI reads it, extracts what matters, and integrates it into the existing knowledge base — updating relevant pages, flagging contradictions with old claims, building cross-references. The hard cognitive work happens once, at ingestion. The result is a compounding artifact: a wiki where connections are already built and synthesis already reflects everything read so far. Subsequent queries are cheap — the AI reads pre-built understanding instead of reconstructing it. Andrej Karpathy named this fork precisely: knowledge compiled once and kept current, versus re-derived on every query.

A useful contrast: a query-time system is a perfectly organized filing cabinet with a brilliant librarian who reads the relevant files and improvises an answer each time you ask. A personal context layer is a study guide a great tutor keeps rewriting as you learn — continuously updated, cross-referenced, each new chapter integrated into everything before it.

## Three operations

- **Ingest** — a new source arrives; the AI reads it, writes a source-summary page, updates every relevant topic/entity page, flags contradictions, builds wikilinks. A single source can touch a dozen pages. Good conversation outputs — rich answers, comparisons, analyses — get filed back as pages too, not just external sources.
- **Query** — questions are answered from the pre-built synthesis, cheaper and richer than query-time retrieval. Good answers get filed back into the wiki so explorations accumulate rather than vanishing into chat history.
- **Lint** — periodic health-checking of the whole wiki: longitudinal drift, orphan pages with no inbound links, concepts mentioned but never given their own page, claims that newer sources have quietly superseded.

## The editorial trap

Every time raw source becomes a wiki page, editorial decisions get made — what to frame, what to omit, how to connect ideas. Nuance can get dropped; errors get baked in and then read as authoritative because the page reads so cleanly. Raw sources must stay immutable and accessible, or the source of truth quietly shifts from material to summary with no way back. The countermeasures aren't optional polish — they're what makes compilation trustworthy rather than merely large: verification against external sources, logical consistency under scrutiny, surfacing hidden assumptions, cross-referencing claims across multiple sources, preserving genuine contradictions instead of resolving them into false coherence, and distinguishing peer-reviewed evidence from opinion.

## The Memex lineage

Vannevar Bush described the Memex in 1945: a personal, actively curated knowledge store with associative trails between documents. His insight was that connections between documents are as valuable as the documents themselves — meaning lives in relationships, not isolated pages. The web inherited a different character: public and hyperlinked, but not privately curated or actively maintained. This pattern is closer to what Bush envisioned than to what the web became; the problem he couldn't solve — someone has to keep cross-references current — is exactly what an LLM maintainer removes.

## Skills as the operational layer

Compiled knowledge with no encoded workflow still forces re-derivation every session. The missing bridge is a **skills layer**: versioned files encoding recurring workflows as single callable commands (see [[Agent Skills]]). A skill for ingestion encodes: read the source, check for overlap, identify the topic cluster, write pages with correct structure, log the change. This closes the memory-execution loop — the wiki knows what it knows, and the agent knows how it works — and turns those workflows into an editable, improvable asset rather than a procedure re-derived from scratch each session.

## The schema is the highest-leverage document

The instruction document that tells the AI how the knowledge base is structured — conventions, ingestion rules, conflict handling — is the highest-leverage artifact in the whole system. A well-designed schema turns the AI into a disciplined maintainer; a vague one turns it into a generic chatbot that happens to write files. The schema co-evolves with the domain: as edge cases arise, the instructions sharpen. The operating principle: own the artifact, not the tool — files in folders you control, not knowledge locked in a platform that can reprice or disappear.

## The 6-level practical hierarchy

A useful decision framework (Simon Scrapes, "Every Claude Code Memory System Compared," April 2026) mapping directly onto the write-time-vs-query-time fork:

| Level | System | When to choose |
|-------|--------|-----------------|
| 1 | Native memory files — auto-loaded instructions | Simple projects, getting started |
| 2 | Reliable recall — structured folders + hooks | When memory needs to load consistently |
| 3 | Semantic search — vector embeddings | Larger knowledge bases |
| 4 | Verbatim conversations — full history storage | Long-running projects needing exact history |
| **5** | **Self-organizing knowledge base — this pattern** | Deep research, complex domains, team wikis |
| 6 | Universal brain — engineered graph/vector store | Power users switching between multiple AI tools |

Many serious users combine levels — Level 2 hooks with a Level 5 wiki, for instance. The natural default for personal, research-heavy use is to reach Level 5 and stay there.

## Is a heavyweight graph store the "gold standard"? No — it's use-case-dependent

A recurring 2026 claim is that the real gold standard is an engineered temporal-graph-plus-vector stack, and a markdown wiki is merely the lightweight option. The independent evidence doesn't support that as a universal ranking. The most-cited *"graphs beat vector retrieval 80/20"* figure traces to a single hand-crafted tutorial blog, not a peer-reviewed benchmark. The most independent head-to-head (Han et al., 2025) found graph retrieval and standard retrieval have *complementary* strengths rather than a consistent winner — graphs win narrowly on multi-hop/temporal queries at a steep cost in index-build and retrieval speed, and on at least one major benchmark, plain full-context retrieval beat both leading graph-memory products on raw accuracy. Vendor-published "90%+" figures for graph products have been independently re-evaluated far lower.

The honest split: for a **single individual**, a markdown wiki wins — it fits in context (no retrieval step needed up to tens of thousands of tokens), stays human-auditable, and requires no infrastructure. An engineered graph/vector stack wins for **multi-user, production-scale** memory, a different problem entirely. The load-bearing conclusion, straight from the independent literature: a well-structured file beats a poorly populated graph — the bottleneck is ingestion quality, not retrieval architecture. Curation and verification discipline is where quality actually lives (see [[Verification Discipline and Assertion Types]]), not the storage engine.

## Related
- [[Second Brain]] — the consumer-facing name for this same architecture
- [[The Harness Is the Product]] — this layer is the persistent-memory tier of a full agent harness
- [[Agent Skills]] — the operational layer that turns compiled knowledge into repeatable workflows
- [[Verification Discipline and Assertion Types]] — the discipline that keeps compilation trustworthy
- [[Compound Growth]] — why a maintained knowledge base compounds rather than plateaus
- [[Agent Orchestration]] · [[AI Agents]] — the agent layer that reads and writes this substrate
