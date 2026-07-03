---
name: wiki-lint
description: Periodic whole-wiki health check — orphan pages, isolated stubs, stale claims (verified via parallel sub-agents), contradictions between pages, and knowledge gaps (most-referenced unresolved wikilinks). Produces a report; does not auto-fix. Use when the user asks to lint, audit, or health-check the wiki, runs /wiki-lint, or every 5–10 sessions to catch drift before it compounds.
---

# Wiki Lint

Deep periodic health check across the whole wiki, run every 5–10 sessions or whenever drift is suspected. Unlike `/wiki-maintenance` (session-scoped, mechanical), this pass looks at the *entire* wiki and includes judgment calls — currency, contradiction, and coverage gaps — not just formatting. Run from the repo root. This skill **reports**; a human decides which findings are worth acting on.

## Instructions

### Step 1 — Structural health

Orphan pages (zero inbound wikilinks):

```bash
python3 << 'EOF'
import os, re, glob
pages = glob.glob('wiki/**/*.md', recursive=True)
inbound = {os.path.splitext(os.path.basename(p))[0]: 0 for p in pages}
for p in pages:
    for link in re.findall(r'\[\[([^\]|#/]+)', open(p).read()):
        link = link.strip()
        if link in inbound:
            inbound[link] += 1
special = {'_log', '_schema'}
orphans = sorted(k for k, v in inbound.items() if v == 0 and k not in special)
for name in orphans:
    print(f"ORPHAN: {name}")
print(f"\nTotal orphans: {len(orphans)}")
EOF
```

Isolated stubs (fewer than 2 outbound wikilinks):

```bash
python3 << 'EOF'
import re, glob
for p in sorted(glob.glob('wiki/**/*.md', recursive=True)):
    if len(re.findall(r'\[\[', open(p).read())) < 2:
        print(f"STUB (< 2 links): {p}")
EOF
```

### Step 2 — Knowledge gaps

Most-referenced unresolved wikilinks — the strongest candidates for new pages, because multiple existing pages already assume this concept deserves one:

```bash
python3 << 'EOF'
import os, re, glob
pages = glob.glob('wiki/**/*.md', recursive=True)
existing = {os.path.splitext(os.path.basename(p))[0].lower() for p in pages}
mentioned = {}
for p in pages:
    for link in re.findall(r'\[\[([^\]|#/]+)', open(p).read()):
        link = link.strip()
        if link.lower() not in existing:
            mentioned[link] = mentioned.get(link, 0) + 1
for name, count in sorted(mentioned.items(), key=lambda x: x[1], reverse=True)[:30]:
    print(f"{count:3d}  [[{name}]]")
EOF
```

### Step 3 — Currency check

For each domain this wiki covers, identify claims likely to have aged out — this is a judgment call that varies by what the wiki actually covers, so define the domain list once for this wiki rather than assuming a generic set. Typical categories worth a check: anything tied to a fast-moving field (technology, prices, markets), anything medical or scientific (guidelines, published findings, trial status), anything organizational (a person's role, a company's status).

Use parallel sub-agents (a cheap, fast model — fetch-and-compare, not deep reasoning) to verify a batch of specific claims against current external sources. Escalate to a stronger model only when a claim comes back contested or ambiguous.

### Step 4 — Contradiction scan

Read pairs of pages covering the same domain and check for inconsistency — a wiki that has grown by incremental ingestion will accumulate pages that drifted apart on a shared claim (a survival estimate, a definition, a figure) without anyone noticing, because each page read fine in isolation. For each contradiction found: **preserve both perspectives with source attribution — do not flatten**. A named tension with both claims and their provenance is more valuable than a silently picked winner.

### Step 5 — Synthesis gaps

Target ratio: roughly 1 synthesis page per 15–20 topic pages. Identify:
- Highly-connected topic clusters (3+ topics that reference each other repeatedly) with no synthesis page tying them together
- Synthesis pages under ~300 words — candidates for enrichment rather than being left thin

### Step 6 — Missing pages worth creating

Rank the top 5 candidate new pages by:
1. Inbound unresolved-wikilink count from Step 2 (most-referenced first)
2. Relevance to what `NORTHSTAR.md` says this brain is actually for
3. Whether source material to write from already exists somewhere in `raw/`

### Step 7 — Report

```
## Wiki Lint Report — [DATE]

**Structural**
- Orphans: [N] pages with 0 inbound links
- Stubs: [N] pages with < 2 outbound links

**Knowledge Gaps**
Top missing pages by reference count:
1. [[X]] — mentioned N times

**Currency**
[Findings per domain, or "no checks run this pass — scope not defined"]

**Contradictions found:** [list, or "none found"]

**Synthesis ratio:** [N synthesis / N topic] — [healthy / needs attention]

**Recommended actions:**
1. [Most urgent fix]
```

For a lint pass spanning many pages or more than ~10 verification claims, state the scope upfront and confirm before running the full sweep — this can be a lot of sub-agent dispatch, and the user should know the shape of it before it runs.

## Reference

`context/why-a-second-brain.md` — the "silent staleness" failure mode this skill exists to catch.
