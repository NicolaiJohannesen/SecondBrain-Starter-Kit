---
name: survey-sources
description: Build or refresh raw/MANIFEST.md — the authoritative tracker of which raw sources have been processed into the wiki. Reads titles only (no content), clusters by topic, cross-references existing wiki coverage, and writes a fresh manifest with status per cluster and a prioritized processing queue. Use when asked to survey sources, refresh the manifest, audit the backlog, or run /survey-sources. Classification pass only — no wiki pages are created or modified.
---

# Survey Sources

A classification pass, not an ingestion pass: read titles only, no content, no wiki edits. It exists to answer "what's still unprocessed, and what should I ingest next?" before committing to a full `/ingest-source` run. Run from the repo root.

## Instructions

### Step 0 — Account-dump exports are cumulative: compute the delta first

A fresh export of an entire account's history (a full conversation dump, a full notes export) re-contains everything that was ever there — it is **not** all new material if a prior export already exists. Surveying the whole thing as if it's new wastes the pass and misrepresents the backlog size.

Before surveying a fresh full-account export:

1. Find the **date of the last export** of that same source (check `raw/MANIFEST.md` for the last recorded export date, or the export's own directory name if dated).
2. Filter items by creation date **after** that cutoff — that's the actual new material. Also flag older items whose modification date is after the cutoff (continued threads, edited notes).
3. Survey only the delta, then cross-reference it against existing wiki coverage — a meaningful fraction of "new" items are often already represented via other channels.

```python
import json
data = json.load(open("raw/inbox/export/data.json"))
CUTOFF = "2026-01-01"  # date of the last processed export of this source
new = [item for item in data["items"] if (item.get("create_time") or "")[:10] > CUTOFF]
print(len(new), "new of", len(data["items"]))
```

Record the new export and its delta count in the manifest under a dated subsection — don't rewrite the history of what was already assimilated.

### Step 1 — Read all source titles

Extract only the title (and size, if available) from every file awaiting processing. Do not read content fields at this stage.

```python
import json, os, glob

def get_titles(pattern):
    results = []
    for f in sorted(glob.glob(pattern)):
        try:
            with open(f) as fp:
                d = json.load(fp)
            results.append((os.path.basename(f), d.get('title', '[no title]'), d.get('content_chars', 0)))
        except Exception as e:
            results.append((os.path.basename(f), f'[parse error: {e}]', 0))
    return results

for label, pattern in [
    ('raw/inbox',                    'raw/inbox/*.json'),
    ('raw/ingested/topic-sources',   'raw/ingested/topic-sources/**/*.json'),
]:
    items = get_titles(pattern)
    print(f"\n=== {label} ({len(items)} files) ===")
    for fname, title, chars in items:
        print(f"  {title}  [{chars:,} chars]  ({fname})")
```

### Step 2 — Read existing wiki coverage

```bash
ls wiki/Sources/
grep "^|" wiki/_log.md | head -100
```

Grep for keywords relevant to the clusters you expect to find, extending the search as needed.

### Step 3 — Cluster the titles

Assign each file to exactly one cluster based on its title and any obvious keywords — the cluster list is specific to what this brain actually covers, so build it from what's really in `raw/inbox`, don't force items into a generic template. Use "Other / Unsurveyed" for anything that doesn't fit cleanly.

### Step 4 — Cross-reference status

Per cluster:
- **Complete** — wiki `Sources/` pages exist for this cluster and `_log.md` shows multiple sessions on the topic
- **Partial** — some wiki coverage exists but isn't comprehensive, or source pages exist but the content was only partially extracted
- **Not started** — no wiki Source page, or only generic passing mentions in `_log.md`
- **Low value** — clearly low-density (logistics, one-off questions, tool troubleshooting with no conceptual depth) — safe to skip

When genuinely unsure, classify as "Not started" rather than "Complete" — an honest backlog is more useful than an optimistic one.

### Step 5 — Write raw/MANIFEST.md

```markdown
# Source Processing Manifest

**Updated:** YYYY-MM-DD
**Purpose:** Tracks which raw sources have been processed into the wiki. Update after each ingestion session.

## Status Key
[Not started] | [Partial] | [Complete] | [Low value (skip)]

---

## raw/inbox/ (N files)

| Cluster | Files | Status | Wiki Output |
|---|---|---|---|
| Cluster name | N | Complete | [[Page A]], [[Page B]] |

---

## Processing Queue (priority order)

1. `raw/inbox/...` — [Cluster name] (N files) — relates to [[Project or Topic]]
```

### Step 6 — Update after ingestion

After `/ingest-source` processes a cluster: change its status to Complete, add the resulting pages to "Wiki Output," update the "Updated:" date, and drop it from the Processing Queue.
