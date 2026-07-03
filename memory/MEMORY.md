# Memory Index

Cross-session memory: durable corrections, preferences, and reference facts that should persist without re-deriving them each session. This index is a table of contents — one line per memory, pointing at a detail file in this same folder when the memory needs more than a line to explain.

## Convention

- One line per entry: `- [Short name](filename.md) — one-sentence summary of what it says`
- Keep entries genuinely short here; put the reasoning, worked examples, and triggering context in the linked file, not in this index.
- Two rough categories, by filename prefix:
  - `feedback_*.md` — a correction that changed behavior going forward (something was done wrong, here's the fix and why)
  - `reference_*.md` — a standing fact worth not re-deriving (a workflow, a path, a piece of external context)
- When this file grows past a comfortable read length, that's a signal to tighten entries to one line each and move any accumulated detail fully into the linked files — not a signal to start dropping entries.

## Entries

*(empty — entries accumulate here as corrections and reference facts get captured)*

## Size discipline (from birth)

- This index has a working limit of ~200 lines. It is a **router, not a store** — one line per memory: `- [Title](file.md) — hook (≤200 chars)`.
- High-stakes rules get a ⭐ and keep direct lines forever (pinned — exempt from compaction).
- When the index nears its limit or a section outgrows ~15 entries, run `/memory-compact` (method: [context/memory-compaction.md](../context/memory-compaction.md)): tier the structure first, merge same-class entries second (specimens cited, corrections preserved), consolidate files last — always into git, never by deletion. Stale files move to `memory/archive/`, never get deleted.
