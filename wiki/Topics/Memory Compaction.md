---
type: topic
created: 2026-07-02
updated: 2026-07-02
version: 1
origin: kit-seed
tags:
  - topic
  - seed
  - domain/ai
aliases:
  - Memory compression
  - Memory resizing
  - Compaction
  - Memory defragmentation
  - Index compaction
---

# Memory Compaction

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

How to shrink an AI system's long-term memory when it outgrows its load limits — **without losing the lessons it exists to keep**. This is 2026 convergent practice across agent-memory systems (MemGPT/Letta, Zep, Stanford's generative-agents work) and knowledge-management tradition (Forte's building-a-second-brain method, Andy Matuschak's spaced-repetition writing, Luhmann's Zettelkasten).

## The problem shape

Memory that grows unboundedly eventually fails one of three ways: the **index** passes its load limit (the tail silently stops loading — the system doesn't know it forgot), **retrieval** degrades (the right memory stops surfacing among hundreds of entries), or **maintenance** collapses (nobody can hold the structure in their head anymore). The naive fix — summarize everything smaller — is documented to destroy the most valuable content first: *corrections* read as small details and get gisted away; *rarely-firing but critical rules* are the statistical tail, and compression eats the tail first. A published "governance decay" study found constraint violations jumped from 0% to 30–59% once standing rules were summarized out of the active context.

## The architecture

**A small always-loaded index of pointers · a lossless store underneath · compression by abstraction-with-citations · rules and corrections are the last thing allowed to be lost.**

This is the same principle a [[Personal Context Layer]] runs on at the memory layer: keep the raw record immutable, keep a compiled view derived from it, and never let the derived view become the only copy.

## The method

**Index rules** (for a line-limited router file, e.g. a memory index):
1. The index is a **router, not a store** — one line, one hook, one link; the teaching lives in the linked file.
2. **Pin the invariants** — high-stakes rules: direct lines forever, exempt from compaction. Cut descriptive entries before rule entries, always.
3. **Merge by class, not topic proximity** — one generalized rule citing its worked specimens; never merge entries that share a domain but encode different lessons.
4. **Tier structure before shrinking content** — promote an outgrown section to a second-level file, leave one line behind pointing to it.
5. **Demote by usage × importance, multiplied** — stale AND low-stakes demotes; rare-but-critical never demotes on staleness alone.
6. **Opportunistic, not batch** — compact what use touches; a full self-rewrite with no new information is the collapse case, not the fix.

**Store rules** (for hundreds of one-fact memory files):
1. **Supersede, never delete** — archive with provenance; knowing what you used to believe is information.
2. **Consolidate on a dedicated pass** — same-class files merge into one generalized rule quoting 2–3 specimens verbatim.
3. **The correction survives every merge** — the anti-pattern and its fix both carry into the merged file; a rule stripped of its failure story is "be careful," a hope, not a fix.
4. **Hot/cold tiers** — a small always-loaded set; the cold tail grows freely because it costs nothing until retrieved.
5. **Fix retrieval before shrinking** — naming, keywords, class indexes first; don't burn content to save an index.
6. **Version every compaction, audit one cycle later** — diffable, reversible; if a generalized rule misses a recurrence its specimen would have caught, restore the detail.

## Triggers (when to run it)

- The index passes its load limit
- A section outgrows roughly 15–25 entries
- The same lesson exists in 3+ files
- Retrieval keeps surfacing the wrong memory

Then: structure first (tiering) → view second (merging index lines) → content last and least (consolidating files; archived, never deleted).

## Operationalization in this kit

This kit ships the method as [context/memory-compaction.md](../../context/memory-compaction.md) plus a `/memory-compact` skill that executes the cycle with a byte-verbatim verification step — run it when your own memory index starts showing the triggers above.

## Related

- [[Personal Context Layer]] — the same lossless-store principle at the whole-brain layer, not just the memory index
- [[Loop Engineering]] — compaction as a maintenance loop with a detectable trigger
- [[Second Brain]] — the system this discipline keeps usable as it grows
- [[Culture of Learning]] — a memory system that forgets its corrections cannot sustain a learning culture
