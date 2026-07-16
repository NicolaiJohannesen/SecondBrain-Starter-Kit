---
name: ingest-source
description: Process a new source (conversation exports, notes, PDFs, images/screenshots, raw markdown) into the wiki — read it (vision for images), write or enrich the affected wiki pages by topic cluster, create a Source page, cross-link, log, and route the file out of the inbox. Use when the user drops a file into raw/inbox/, asks to ingest a source, runs /ingest-source, or points at any unprocessed file. Works for any source type; process by topic cluster, not file-by-file.
---

# Ingest Source

Turns one raw file into compiled, cross-referenced wiki knowledge. Works for any source type — conversation exports, notes apps, PDFs, images, plain markdown. The core discipline: process by **topic cluster**, not file-by-file — read everything a file touches, then write or enrich every affected page in one pass. This produces richer pages and better cross-linking than handling pages one at a time.

## Instructions

### Step 0 — Check the inbox, extract archives, process the whole thing

```bash
ls raw/inbox/ | grep -v ".DS_Store" | grep -v "^._"
```

- **A `.zip`, `.tar`, or `.tar.gz` file** → extract it in place first (`unzip file.zip -d file/`, `tar -xf file.tar.gz`), then treat its contents as newly-arrived inbox files. Don't ask the user to unzip it themselves — that's friction the system should absorb, not pass along.
- **Files found** → group filenames that share significant words into clusters; read and process each cluster together. An image often belongs to the same cluster as a text file (a chart plus its analysis, a screenshot plus the conversation that discusses it) — group them.
- **Multiple clusters found** → process all of them in this same session, one after another, without stopping to ask whether to continue between clusters. Report a brief line per cluster as you finish it, not a check-in before starting the next one. This is what "runs largely on its own" means in practice — see "Defaults" below for what to do instead of asking when something's ambiguous.
- **Inbox empty** → ask which source to process.
- **OS resource-fork stubs** (`._*` files) are not sources — ignore and clean them, never process them.

After a file is fully processed (log updated, cross-links done), move it to `raw/ingested/topic-sources/{topic}/{filename}`, where `{topic}` is a kebab-case folder name. Match an existing topic folder where one already fits; create a new one otherwise. **Announce the destination path explicitly** so the routing is auditable.

**Images route differently — see "Handling images" below.** An image a wiki page needs to *display* must live inside `wiki/assets/{topic}/`, not in `raw/ingested/` — the latter is meant to stay outside the compiled knowledge layer, so an embed pointing there would be broken.

If a filename resembles one already in `raw/ingested/`, `diff` against the likely match first. Empty diff → duplicate, just move it. Non-empty diff → process the new content and rename the moved file with a version suffix (`_v2`, `_pre-v3`) so the evolution is preserved rather than overwritten.

### Step 1 — Read the source

For JSON exports (conversation dumps, structured notes):

```python
import json
with open('raw/inbox/example.json') as f:
    d = json.load(f)
print(d.get('title'), d.get('content_chars'))
print(d['content'][:3000])
```

Files over ~50K characters: read in windows focused on the most relevant sections rather than the whole thing at once — identify 3–5 high-value insight clusters instead of trying to ingest everything in one pass. Exception: if a single source is the primary basis for a page you're about to write (and will be cited in its `sources:` frontmatter), read it in full — under-extracting a foundational source ships the page incomplete.

If the file carries frontmatter identifying its origin (`source: ...`), apply provenance-aware treatment based on that field.

### Handling images

Text sources move to `raw/ingested/` once processed — that's fine, because their *content* has been written into wiki pages and the raw file only needs to survive as provenance. An image a page **displays** is different: the page holds a reference (`![[...]]`) to the actual file, so that file has to live inside the wiki itself.

1. **Read the image with vision first.** Extract text, data, and structure into prose, same as a text source. Apply the same epistemic discipline: OCR'd numbers, dates, and quotes are flagged for verification, never asserted as fact outright — vision misreads digits, and a wrong number that reads confidently is worse than an acknowledged gap.
2. **Classify and route:**

| Image type | Example | Destination | In the page |
|---|---|---|---|
| Display / reference | chart, diagram, screenshot worth showing | `wiki/assets/{topic}/{descriptive-dated-name}.ext` (tracked, in-wiki) | embed **and** extract its data into prose |
| Content-only | screenshot of a paragraph; a slide whose text is the whole point | extract via vision → prose; image → `raw/ingested/topic-sources/{topic}/` as provenance | no embed |
| Personal / non-wiki | a bill, a receipt, a personal photo | leave for manual triage, do not ingest | not ingested |

3. **Loss-prevention: copy, verify, then move.** Never move an image to a freshly-created path in one error-suppressed step — a failed move during a disk-full moment silently loses the file. Instead: `cp` into `wiki/assets/{topic}/` (creating the topic dir first) → confirm the file landed with non-zero size → *then* move the inbox original to `raw/ingested/` as provenance. A display image ends up with two safe copies.
4. **Name descriptively and with a date**, never raw camera/screenshot names (`quarterly-budget-2026-03.png`, not `IMG_4821.png`) — an asset nobody can find by name is half-lost.
5. **Flag anything over ~10 MB.** Downscale or convert rather than bloating the tracked wiki with huge originals.

An embedded asset should earn its place — show something prose can't (a distribution, a structure, a comparison) — and carry a caption. The Source page (Step 7) records its provenance and path.

### Step 2 — Check existing wiki

```bash
grep -rl "TOPIC_KEYWORD" wiki/Topics/ wiki/Entities/ wiki/Projects/
```

Read any overlapping pages before writing anything new. The goal is to enrich, not duplicate.

### Step 3 — Decide create vs. enrich

For each significant topic the source touches:
- **Page already exists** → enrich it (new sections, updated claims, add this source to its `sources:` frontmatter)
- **No page yet, and there's 3–4 sentences of real substance** → create a new page
- **Passing mention only** → add it as an unresolved `[[wikilink]]` from an existing page, rather than forcing a stub into existence

### Step 4 — Research external substrate where it's warranted

If the source mentions an entity, book, public figure, concept, or event only as *background* — not as the substance itself — and Step 2 confirmed there's no existing page on it, the source alone usually isn't enough to write a useful page. Dispatch a research pass before writing.

**Warranted**: a book or article mentioned in passing (author, central claims, context) · a public figure named (biography, positions, current status) · a concept named without explanation (origin, contested aspects) · a historical or current event referenced for substance.

**Not warranted**: the source *is* the substrate (a primary document, a paper, a notebook export) · the mention is genuinely passing and only needs an unresolved wikilink · the wiki already has rich coverage · the material is personal/biographical, where external research rarely adds anything and can raise privacy concerns.

Verify load-bearing claims from research before writing them in: check that cited facts are real and correctly stated (right name, right number, right date), and — for anything genuinely contested — that the source actually supports the framing being given to it, not just that the citation exists. See `constitution/verification.md` for the full verification discipline. Save any unusually good external source found this way into `raw/` rather than discarding it after one use.

### Step 5 — Process by topic cluster

Identify the full set of pages this source touches (typically 3–8). Write or enrich all of them in one pass before moving to the next source — this is what produces cross-linking that actually holds together, instead of pages that each reference a topic they don't actually connect to.

### Step 6 — Write or enrich pages

New page template (see `wiki/_schema.md` for the authoritative field list):

```markdown
---
type: topic
created: YYYY-MM-DD
updated: YYYY-MM-DD
version: 1
sources:
  - "[[SRC - Origin - Title]]"
tags:
  - topic
aliases:
  - Alternate name
---

# Page Title

One-sentence summary.

## Section
Be substantive — preserve the argument chain rather than compressing it to a conclusion. Surface assumptions. Flag contradictions rather than silently resolving them.

## Related
- [[Linked Page]]
```

For an existing page: read it in full first, add only what's genuinely new, append to `sources:`, bump `version:` and `updated:`, and note any contradiction with what's already there explicitly rather than flattening it. Populate `aliases:` richly — alternate terms, informal shorthand, adjacent-domain phrasings — so a wikilink written naturally in a future session resolves instead of creating a dead link.

### Step 7 — Create a Source page

Always create `wiki/Sources/SRC - {Origin} - {Title}.md`:

```markdown
---
type: source
created: YYYY-MM-DD
version: 1
tags:
  - source
---

# SRC — Origin — Title

**Type:** [conversation / note / paper / image]
**Date:** YYYY-MM-DD

## Summary
[2–3 sentences]

## Key Insights
- [Insight 1]

## Pages Touched
- [[Page A]] — what was added
```

### Step 8 — Cross-link

Every new concept gets `[[wikilinks]]` from 2–3 existing pages that should reference it. Confirm the new page's Related section links back to its hubs.

### Step 9 — Update the log

Append to `wiki/_log.md`:

```
| YYYY-MM-DD | source-id | Source description | Pages created (new) | Pages updated |
```

### Step 10 — Update the manifest

If this ingestion completes or advances a cluster tracked in `raw/MANIFEST.md`, update that cluster's status and "Wiki Output" column, and bump the manifest's "Updated:" date.

## Defaults — don't stop to ask, don't guess either

The point of a documented default is that it's neither: not a guess (which can be wrong silently) and not a question (which stops an autonomous run for something already decided). When one of these comes up, apply the default, log what you did, and keep going — only surface something to the user when it's a genuine judgment call none of these cover.

- **Unrecognized or unparseable format** → read whatever text can be extracted, note "format not recognized by any parser" on the Source page, and continue. Don't ask what to do; a partial read logged as partial beats stopping.
- **Archive with mixed content** → extract everything, process each recognized piece by its own type (Step 1 onward), skip and log anything genuinely unreadable. Don't ask which parts matter.
- **Ambiguous topic-cluster placement** (a file could reasonably belong under 2+ existing topics, or under a topic vs. a new one) → make the best-guess placement, note the ambiguity in a one-line comment on the page or in `_log.md`, and let a future `/wiki-lint` pass reconcile it. Don't block ingestion asking which folder is "right."
- **Possible private-forever content, not certain** → default conservative: treat it as raw-only (don't synthesize into a wiki page), flag it explicitly in `_log.md` for the user to review later if genuinely unsure. Don't ask mid-ingest for every borderline file — that's exactly the repeated-interruption pattern autonomous operation exists to avoid.
- **File resembles one already ingested** → the diff-against-previous check (Step 0's routing note) already covers this — apply it, don't ask.
- **A file with no clear topic, or too thin to be worth a page** → per Step 3's own rule, add it as an unresolved wikilink from wherever it's mentioned rather than forcing a stub page, and move on.

## Epistemic standards

- **Empirical claims, statistics, attributed quotes**: verify against external sources before committing them to a page. Soften or flag anything that fails verification. Full protocol at `constitution/verification.md`.
- **Speculation**: label it explicitly ("X argues...", "one possibility is...") — don't let it read as settled fact.
- **Contradictions**: preserve both perspectives with attribution. Don't flatten disagreement into false consensus.
- **Sensitive data**: never write API keys, passwords, account numbers, or other credentials into wiki pages, even as examples.
- **Private-forever material**: check the categories named during setup (`NORTHSTAR.md` / `CLAUDE.md`) before writing anything from health, financial, or other-people's-words sources — those stay in `raw/` only, never synthesized into a wiki page even in general terms.
