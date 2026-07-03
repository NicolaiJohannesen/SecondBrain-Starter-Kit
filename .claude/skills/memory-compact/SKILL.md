---
name: memory-compact
description: Run a memory-compaction cycle when the memory layer outgrows its limits. Use when memory/MEMORY.md nears ~200 lines, a section or cluster index outgrows ~15-25 entries, the same lesson exists in 3+ memory files, or retrieval keeps surfacing the wrong memory. Executes the method in context/memory-compaction.md: structure first, view second, content last — pinned invariants exempt, byte-verbatim moves verified, archive-never-delete, every compaction a git commit.
---

# Memory Compact

Executes the method in [context/memory-compaction.md](../../../context/memory-compaction.md) — read it first; this skill is the checklist and the verification machinery.

## Triggers (check proactively, e.g. during /retro)

```bash
wc -l memory/MEMORY.md                                    # near/over 200 → compact
for f in memory/index_*.md; do [ -f "$f" ] && echo "$(grep -c '^- \[' "$f") $f"; done | sort -rn | head -3   # >25 → split or consolidate
```

## The cycle

1. **Commit the current state first** — git is the version layer; every compaction must be diffable and reversible. `git add memory/ && git commit -m "pre-compaction snapshot"`.
2. **Structure first (tiering)**: if the index is over limit, move unpinned entries into `memory/index_<theme>.md` cluster files, one line each left in MEMORY.md: `- [Theme](index_theme.md) — what lesson-classes live there (N entries)`. **Pinned entries — high-stakes rules (⭐) and core user/project context — keep direct lines, verbatim, always.** When cutting is unavoidable, descriptive/reference entries go before rule entries.
3. **View second (merging)**: within an oversized cluster, merge same-class entries into one generalized rule whose memory file states the class, the rule, and **quotes 2–3 worked specimens verbatim** (dates, exact wording). Never merge entries that merely share a domain but encode different lessons. **The correction always survives the merge** — the anti-pattern and its fix both carry into the merged file.
4. **Content last and least (consolidating files)**: only in a dedicated maintenance session. Superseded files move to `memory/archive/` with a `superseded-by:` header — **never deleted**. Knowing what you used to believe, and when it changed, is itself information.

## Verification (mandatory — the doer isn't the checker)

Every original entry line must appear byte-identical in exactly one place after a restructure:

```bash
python3 - << 'PYEOF'
import glob, collections, subprocess
orig_text = subprocess.run(["git", "show", "HEAD:memory/MEMORY.md"], capture_output=True, text=True).stdout
orig = [l for l in orig_text.splitlines() if l.startswith("- [")]
pool = collections.Counter()
for f in ["memory/MEMORY.md"] + glob.glob("memory/index_*.md"):
    for l in open(f).read().splitlines():
        if l.startswith("- ["):
            pool[l] += 1
missing = [l for l in orig if pool[l] == 0]
print(f"original entries: {len(orig)} | missing (reworded/dropped): {len(missing)}")
for l in missing[:10]: print("  ", l[:120])
print(f"MEMORY.md now: {sum(1 for _ in open('memory/MEMORY.md'))} lines (limit ~200)")
PYEOF
```

Zero missing + under the limit = pass. Deliberately merged lines (step 3) are listed explicitly in the report so every "missing" line is accounted for, never assumed. Any unaccounted line: restore verbatim before committing.

5. **Commit the compaction** with a message naming what was tiered/merged/archived. **Audit one cycle later**: at the next `/retro`, check whether any consolidated rule failed to fire where its specimen would have — if so, restore the detail from the archive.
