---
name: wiki-maintenance
description: Quick session-end hygiene check — scoped to pages touched this session. Verifies frontmatter compliance, version-bump audit, alias-aware unresolved-link detection, new-page orphan check, TODO/FIXME scan, log-entry verification, and an uncommitted-work summary. Faster and narrower than /wiki-lint. Use at session end before committing, or whenever you want a quick "is everything clean?" check.
---

# Wiki Maintenance

End-of-session hygiene pass scoped to pages touched in this session only. Faster and narrower than `/wiki-lint`, which is the periodic deep health check across the whole wiki. Run from the repo root.

## Instructions

### Step 1 — Session scope

```bash
echo "=== Modified pages (tracked) ==="
git diff --name-only HEAD -- 'wiki/' 2>/dev/null | grep '\.md$' | grep -v "^wiki/_log.md$"
echo ""
echo "=== Newly created pages (untracked) ==="
git ls-files --others --exclude-standard wiki/ | grep '\.md$'
```

If both are empty, the tree is clean — skip to Step 6 and report.

### Step 2 — Frontmatter compliance

For each touched page, verify required fields are present (`type`, `created`, `updated`, `tags` — see `wiki/_schema.md` for the full spec):

```bash
python3 << 'PYEOF'
import subprocess, re, os

touched = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD', '--', 'wiki/'], text=True).strip().split('\n')
untracked = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard', 'wiki/'], text=True).strip().split('\n')
all_touched = [p for p in touched + untracked if p and p.endswith('.md') and p != 'wiki/_log.md']

issues = []
for p in all_touched:
    if not os.path.exists(p):
        continue
    content = open(p).read()
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m:
        issues.append(f"NO FRONTMATTER: {p}")
        continue
    fm = m.group(1)
    missing = [f for f in ['type', 'created', 'updated', 'tags'] if not re.search(rf'^{f}:', fm, re.MULTILINE)]
    if missing:
        issues.append(f"MISSING {missing}: {p}")

print("\n".join(issues) if issues else "Frontmatter compliance: PASS")
PYEOF
```

### Step 3 — Version-bump audit

Convention: every edit to a page bumps its `version:` integer and its `updated:` date. New pages start at `version: 1`.

```bash
python3 << 'PYEOF'
import subprocess, re, os
from datetime import date

today = date.today().isoformat()
touched = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD', '--', 'wiki/'], text=True).strip().split('\n')
modified = [p for p in touched if p and p.endswith('.md') and p != 'wiki/_log.md']

issues = []
for p in modified:
    if not os.path.exists(p):
        continue
    content = open(p).read()
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m:
        continue
    fm = m.group(1)
    updated_m = re.search(r'^updated:\s*(\S+)', fm, re.MULTILINE)
    if (updated_m.group(1) if updated_m else None) != today:
        issues.append(f"updated NOT today: {p}")

    head_result = subprocess.run(['git', 'show', f'HEAD:{p}'], capture_output=True, text=True)
    if head_result.returncode != 0:
        continue
    head_m = re.match(r'^---\n(.*?)\n---', head_result.stdout, re.DOTALL)
    if not head_m:
        continue
    head_v = re.search(r'^version:\s*(\d+)', head_m.group(1), re.MULTILINE)
    cur_v = re.search(r'^version:\s*(\d+)', fm, re.MULTILINE)
    head_v = int(head_v.group(1)) if head_v else None
    cur_v = int(cur_v.group(1)) if cur_v else None
    if head_v is not None and cur_v is not None and cur_v <= head_v:
        issues.append(f"version NOT bumped (still v{cur_v}): {p}")

print("\n".join(issues) if issues else "Version-bump audit: PASS")
PYEOF
```

### Step 4 — Alias-aware unresolved-link check

```bash
python3 << 'PYEOF'
import os, re, glob

pages = [p for p in glob.glob('wiki/**/*.md', recursive=True)]
alias_to_file = {}
filenames = set()
for p in pages:
    name = os.path.splitext(os.path.basename(p))[0]
    filenames.add(name)
    content = open(p).read()
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m:
        continue
    block = re.search(r'^aliases:\s*\n((?:\s+-\s+.+\n?)+)', m.group(1), re.MULTILINE)
    if block:
        for line in block.group(1).split('\n'):
            a = re.match(r'\s+-\s+(.+)$', line)
            if a:
                alias = a.group(1).strip().strip('"').strip("'")
                alias_to_file[alias] = name
                alias_to_file[alias.lower()] = name

unresolved = {}
for p in pages:
    content = open(p).read()
    for link in re.findall(r'\[\[([^\]|#]+?)(?:\||\])', content):
        link = link.strip()
        if '/' in link:
            link = link.split('/')[-1]
        if link in filenames or link in alias_to_file or link.lower() in alias_to_file:
            continue
        unresolved[link] = unresolved.get(link, 0) + 1

if unresolved:
    print("Unresolved wikilinks (count >= 2, after alias check):")
    for name, count in sorted(unresolved.items(), key=lambda x: -x[1])[:20]:
        if count >= 2:
            print(f"  {count:3d}  [[{name}]]")
else:
    print("Unresolved wikilinks: PASS")
PYEOF
```

### Step 5 — New-page orphan check

Each new page should have at least one inbound reference somewhere in the wiki:

```bash
python3 << 'PYEOF'
import subprocess, os, re, glob

new = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard', 'wiki/'], text=True).strip().split('\n')
new = [p for p in new if p and p.endswith('.md')]
if not new:
    print("No new pages this session.")
else:
    other = [p for p in glob.glob('wiki/**/*.md', recursive=True) if p not in new]
    combined = "\n".join(open(p).read() for p in other if os.path.exists(p))
    issues = []
    for p in new:
        name = os.path.splitext(os.path.basename(p))[0]
        if not any(pat in combined for pat in (f'[[{name}]]', f'[[{name}|', f'/{name}]]', f'/{name}|')):
            issues.append(f"NEW ORPHAN: {p}")
    print("\n".join(issues) if issues else f"New-page orphan check: PASS ({len(new)} new pages, all linked)")
PYEOF
```

### Step 6 — TODO/FIXME scan

```bash
grep -rn -E "TODO|FIXME|XXX:" wiki/ --include="*.md" 2>/dev/null | grep -v "^wiki/_log.md:" || echo "TODO/FIXME scan: PASS (no markers)"
```

### Step 7 — Log-entry check

If substantial work happened this session, verify `wiki/_log.md` has an entry dated today:

```bash
python3 << 'PYEOF'
import subprocess, re
from datetime import date

today = date.today().isoformat()
diff_stat = subprocess.check_output(['git', 'diff', '--stat', 'HEAD', '--', 'wiki/'], text=True)
ins = re.search(r'(\d+) insertion', diff_stat)
new_files = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard', 'wiki/'], text=True).strip().split('\n')
new_files = [f for f in new_files if f.endswith('.md')]
insertions = int(ins.group(1)) if ins else 0

if insertions <= 100 and len(new_files) < 2:
    print("Log entry check: not substantial enough to require a log entry")
else:
    log = open('wiki/_log.md').read()
    dates = re.findall(r'^\| (\d{4}-\d{2}-\d{2}) \|', log, re.MULTILINE) + re.findall(r'^##\s+(\d{4}-\d{2}-\d{2})', log, re.MULTILINE)
    if today in dates:
        print(f"Log entry check: PASS (entry dated {today} present)")
    else:
        latest = max(dates) if dates else "(no dated entries found)"
        print(f"WARNING: substantial session ({insertions} insertions, {len(new_files)} new files) but no log entry dated {today}. Latest: {latest}")
PYEOF
```

### Step 8 — Uncommitted-work summary

```bash
echo "=== Uncommitted work ==="
git status --short | wc -l | tr -d ' '
git diff --stat HEAD 2>/dev/null | tail -1
echo "Untracked files:"
git ls-files --others --exclude-standard wiki/ | head -10
```

### Step 9 — Report

```
## Wiki Maintenance Report — [DATE]

**Session scope**: [N] modified pages + [M] new pages
**Frontmatter compliance**: PASS / [N issues]
**Version-bump audit**: PASS / [N issues]
**Unresolved wikilinks**: [N candidates / PASS]
**New-page orphan check**: PASS / [N orphans]
**TODO/FIXME markers**: [N found / PASS]
**Log entry**: present / missing
**Uncommitted work**: [summary]

**Recommended actions**: [most urgent fixes, or "none — WIKI CLEAN, ready to commit"]
```

## Relation to /wiki-lint

`/wiki-maintenance` is the fast, session-scoped pass — cheap mechanical checks on what changed today. `/wiki-lint` is the periodic (every 5–10 sessions) deep pass across the *entire* wiki — orphan detection wiki-wide, currency drift via sub-agents, contradiction scans, synthesis-ratio audit. Run maintenance every session; run lint periodically.
