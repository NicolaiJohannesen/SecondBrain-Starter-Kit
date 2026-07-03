---
name: session-start
description: Orient at the start of a session — load NORTHSTAR.md, recent log entries, journal tail, inbox count, and open tasks, then recommend the next highest-value action. Use when the user starts a new session, runs /session-start, asks for context or status, or asks "where did I leave off" / "what should I work on".
---

# Session Start

Load context fast and orient toward the highest-value work. Run from the repo root.

## Instructions

### Step 1 — Load current state (run in parallel)

```bash
# The one-page statement of what this brain is for
cat NORTHSTAR.md 2>/dev/null || echo "NORTHSTAR.md missing — run /setup-brain first"

# Last 5 log entries
tail -5 wiki/_log.md 2>/dev/null

# Most recent journal entry, if the journal is in use
ls -t wiki/Journal/*.md 2>/dev/null | head -1 | xargs tail -30 2>/dev/null

# Page count by folder
find wiki -name "*.md" -not -path "*/skills/*" | grep -v "_log\|_schema" | \
  sed 's|wiki/||' | cut -d/ -f1 | sort | uniq -c | sort -rn

# Inbox contents awaiting ingestion
ls raw/inbox/ 2>/dev/null | grep -v ".DS_Store"

# Open tasks, if a task file exists
cat wiki/Tasks/*.md 2>/dev/null | head -50
```

If `NORTHSTAR.md` doesn't exist, stop here and recommend running `/setup-brain` — nothing else in the kit orients correctly without it.

### Step 2 — Quick health check

```bash
python3 << 'EOF'
import os, re, glob
wiki = 'wiki'
pages = glob.glob(f'{wiki}/**/*.md', recursive=True)
inbound = {os.path.splitext(os.path.basename(p))[0]: 0 for p in pages}
for p in pages:
    try:
        for link in re.findall(r'\[\[([^\]|#/]+)', open(p).read()):
            link = link.strip()
            if link in inbound:
                inbound[link] += 1
    except Exception:
        pass
special = {'_log', '_schema'}
orphans = [k for k, v in inbound.items() if v == 0 and k not in special]
print(f"Orphan pages ({len(orphans)}): {', '.join(sorted(orphans)[:10])}")
EOF
```

### Step 3 — Recommend the next action

Weigh, in order:
1. **Inbox files awaiting ingestion** — usually the highest-value next step, since a second brain compounds through ingestion.
2. **Open tasks** in `wiki/Tasks/` flagged as next-up.
3. **Orphan pages** needing a cross-link pass.
4. **Maintenance due** — if it's been 5–10 sessions since the last `/wiki-lint`, that's due.

### Output format

```
## Session Context — [DATE]

**Northstar:** [one-line summary from NORTHSTAR.md]
**Last processed:** [from log]
**Page count:** Topics: X | Entities: X | Projects: X | Sources: X | Synthesis: X | Personal: X
**Inbox:** [X] files [or "empty"]
**Orphans:** [count] — [top 3 names]

**Recommended next action:**
1. [Primary recommendation with reason]
2. [Secondary]
```
