# Wiki Schema — LLM Instruction Set

This file defines how the wiki works. Read it before processing any source.

## Purpose

This is a personal knowledge base built on the Karpathy LLM-wiki pattern. It's an Obsidian vault where each page is a persistent, compounding artifact. Synthesis happens once, at ingest time — not re-derived on every query.

The wiki belongs to {{USER_NAME}}. Content spans whatever domains matter to that person — see NORTHSTAR.md for the current scope.

## Vault Structure

```
wiki/
├── Topics/       # Subject-matter deep dives
├── Entities/     # People, organizations, products, places
├── Projects/     # Your own projects and endeavors
├── Sources/      # One summary per ingested source
├── Synthesis/    # Cross-source analysis pages
└── Personal/     # Personal knowledge (health, finance, life)
```

## Page Types

| Type | Folder | Naming | When to Create |
|------|--------|--------|---------------|
| **Topic** | `Topics/` | Plain title: `Compound Interest.md` | A subject you've researched or care about |
| **Entity** | `Entities/` | Plain title: `Some Company.md` | A specific person, org, product, or place referenced meaningfully |
| **Project** | `Projects/` | Plain title: `My Project.md` | Something you're building or have built |
| **Source** | `Sources/` | `SRC - {Origin} - {Title}.md` | Always — one per ingested source |
| **Synthesis** | `Synthesis/` | Plain title | Cross-source analysis connecting 3+ topics |
| **Personal** | `Personal/` | Plain title | Personal health, finance strategy, life knowledge |

## Page Template

```markdown
---
type: topic
created: YYYY-MM-DD
updated: YYYY-MM-DD
version: 1
sources:
  - "[[SRC - Origin - Title]]"
tags:
  - topic/subtopic
aliases:
  - Alternate Name
---

# Page Title

Brief 1-2 sentence summary of what this page covers.

## Section Heading

Content organized with ## headers. Be substantive — capture key insights,
not just surface-level summaries.

## Related
- [[Other Page]]
- [[Another Page]]
```

### Frontmatter Rules

- `type`: one of `topic`, `entity`, `project`, `source`, `synthesis`, `personal`
- `created` / `updated`: YYYY-MM-DD; bump `updated` (and `version`) on every substantive edit
- `version`: integer, increments on every substantive edit — cheapest signal for "reworked since last read"
- `sources`: wikilinks to the source pages that contributed to this page
- `tags`: hierarchical — every page gets at least a type tag and a domain tag
- `aliases`: populate richly (see CLAUDE.md's aliases discipline) — the goal is that any wikilink written naturally later resolves rather than creating a dead link

## Links

`[[Page Title]]` or `[[Page Title|display text]]`. Link generously; link to pages that don't exist yet (Obsidian shows these unresolved, they go live once created). Every page ends with a `## Related` section.

## Merge Protocol

When a source covers a topic that already has a page: read the existing page fully, identify what's genuinely new, integrate additively into the right sections, add the source to `sources:`, bump `updated` and `version`. **Never overwrite existing content.** If the new source contradicts the existing page, record both perspectives with their sources rather than silently picking one.

## Sensitivity Rules

Never write into the wiki: passwords, PINs, or credentials; API keys or secrets; financial account numbers or balances; government ID numbers; private addresses or phone numbers. If a source mixes sensitive data with useful knowledge, extract only the non-sensitive knowledge — a note about investment *strategy* is fine, the actual portfolio numbers are not.

## Quality Standards — per page type

| Criterion | Topic | Synthesis | Entity | Project | Source |
|-----------|-------|-----------|--------|---------|--------|
| **Clarity** — the reader wrestles with the idea, not the words | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Vivid mapping** — abstract ideas made concrete via examples | ✓ | ✓ | ✓ | — | — |
| **Productive struggle** — one moment the reader must think before the answer arrives | ✓ | ✓ | — | — | — |
| **Boundary conditions** — names where the model breaks or doesn't apply | ✓ | ✓ | ✓ | — | — |
| **Layered depth** — surface takeaway for skimmers, deeper structure for rereaders | ✓ | ✓ | — | ✓ | — |
| **Load-bearing insight** — one central reframe at the structural climax, not buried | ✓ | ✓ | — | ✓ | — |

**Topic and Synthesis pages** need all of it — a page that only defines a term has failed; it should build a mental model the reader didn't have before and can use 30 days later.

**Entity pages** need clarity + vivid mapping + boundary conditions. Describe the person, org, or place concretely; name where a characterization breaks. Avoid hagiography.

**Project pages** need the single most important insight findable at a glance, plus layered depth for someone going deeper.

**Source pages** need clarity only. They're records, not arguments — accurate and scannable is the whole job.
