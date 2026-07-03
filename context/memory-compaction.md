# Memory Compaction — how to shrink memory without losing lessons

At some point every memory system gets too big: the index passes its load limit, the folder holds hundreds of one-fact files, retrieval gets noisy. Resizing it the wrong way is worse than not resizing it — the field's documented failures are all about compression that silently destroyed the most important content. This is the method, distilled from what agent-memory systems and knowledge-management practice converged on by 2026.

## The architecture the field converged on

**A small, always-loaded index of pointers · a lossless store underneath · compression by abstraction-with-citations · rules and corrections are the LAST thing allowed to be lost, not the first.**

Every serious system implements some version of this: MemGPT/Letta page evicted content to recall storage rather than deleting it ([arXiv:2310.08560](https://arxiv.org/abs/2310.08560)); Zep's temporal graph marks superseded facts invalid but never removes them ([arXiv:2501.13956](https://arxiv.org/abs/2501.13956)); Stanford's generative agents compress many observations into few insights *with citations back to the evidence* ("insight X, because of memories 1, 5, 3" — [arXiv:2304.03442](https://arxiv.org/abs/2304.03442)); Letta's "memory defragmentation" reorganizes memory as git-committed markdown files so every compaction is diffable and reversible.

## Why the naive approach fails (the evidence)

- **Summarization loses corrections first.** A correction looks like a small detail; summarizers keep gist. Practitioner reports agree: after context compaction, agents "make mistakes you specifically corrected earlier." A rule stripped of its failure story reverts to "be careful" — a hope, not a fix.
- **Safety rules are the tail, and compression eats the tail.** The Governance Decay study ([arXiv:2606.22528](https://arxiv.org/abs/2606.22528)): agents violated 0% of standing constraints while the constraint text survived in context — and up to 30–59% after compaction summarized it away. The fix that restored 0% was **constraint pinning**: rules live in a region compaction is not allowed to touch.
- **Repeated self-rewriting degrades the tail** (by analogy to model collapse, [Shumailov et al., Nature 2024](https://www.nature.com/articles/s41586-024-07566-y)): each summarize-the-summary pass loses rare-but-critical information first. Never compact the output of a compaction without the originals still available.

## Rules for compacting the INDEX (e.g. `memory/MEMORY.md` with a line limit)

1. **The index is a router, not a store.** Each line's only job is to make the right file findable — a ≤200-character hook plus a link. Any line trying to *teach* gets its teaching moved into the file. (Luhmann's index held ~3,200 keywords for ~67,000 notes; an index can be radically smaller than its store.)
2. **Pin the invariants — they are exempt.** Hard behavioral rules (never delete without asking; the privacy boundary; anything marked high-stakes) keep direct index lines through every compaction, verbatim. When the limit forces cuts, descriptive and reference entries go before rule entries, always.
3. **Merge by class, not by topic proximity.** When several entries are instances of one underlying rule, write ONE generalized entry and keep the instances as **worked specimens cited by the rule**. Never merge entries that merely share a domain but encode different lessons — that's gist-compression, the exact move that loses corrections.
4. **Tier the structure before shrinking the content.** Group entries under section headers; when a section outgrows the rest, promote it to its own second-level index file (`index_<theme>.md`) and leave one line behind. (The map-of-content pattern: ~10–15 entries per section is where navigation works.)
5. **Demote by usage × importance, never either alone.** Hasn't-fired-in-months AND low-stakes → demote to a cluster file. Rarely-fires but high-stakes → never demotes on staleness; rare-but-critical is precisely the tail that compression destroys first.
6. **Compact opportunistically, not in batch rewrites.** Distill an entry when real use touches it. A batch "summarize the whole index" pass adds no new information — it's the self-rewriting collapse case.

## Rules for compacting the STORE (hundreds of one-fact memory files)

1. **Never delete — supersede.** Stale or contradicted files move to `memory/archive/` (or gain a `superseded-by:` header) with provenance intact. Knowing what you used to believe, and when it changed, is itself information.
2. **Consolidate on a "sleep cycle," not mid-task.** In a dedicated maintenance session, cluster same-class files and distill each cluster into one generalized rule file that names the class, states the rule, and **quotes 2–3 worked specimens verbatim** (dates, exact wording). The specimen files then archive with pointers to the consolidated rule.
3. **The correction must survive the merge.** When merging files, both the anti-pattern that was corrected and the correction itself carry into the merged file. This is the single most-documented loss mode; guard it explicitly.
4. **Two-tier: hot vs cold.** A small set of files earns always-loaded status (high-fire-rate or high-stakes). Everything else is cold — findable via the index, grep, and search, loaded only on demand. Compaction pressure applies to the hot tier only; the cold tier may grow indefinitely because it costs nothing until retrieved.
5. **Fix retrieval before shrinking the store.** If the folder "searches badly," the first fix is access paths — consistent naming, front-matter keywords, class indexes — not burning content to save an index.
6. **Version every compaction and audit one cycle later.** Compact on a git commit so the merge is diffable and reversible. If a generalized rule later fails to prevent a recurrence its specimen would have caught, the compression lost the load-bearing detail — restore it from the archive.

## The trigger

Run a compaction cycle when any of these fires: the index passes its load limit · a section of the index outgrows ~15 entries · the same lesson exists in 3+ files · retrieval keeps surfacing the wrong memory. Then compact the *structure* first (tiering), the *view* second (merging index lines), and the *content* last and least (consolidating files, always into git, never deleting).

## Related

- [why-a-second-brain.md](why-a-second-brain.md) — the editorial trap; raw-stays-immutable is this same principle at the wiki layer
- [loops.md](loops.md) — the maintenance-loop cadence a compaction cycle belongs to
- `memory/MEMORY.md` — the index these rules govern
