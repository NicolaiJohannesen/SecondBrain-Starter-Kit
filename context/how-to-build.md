# How to Build a Second Brain

The step-by-step manual for building a second brain from zero to a compounding, loop-maintained system, using Claude Code and plain markdown files.

**The load-bearing shape of the problem**, learned from auditing every data-export channel a person's digital life actually offers: almost every personal data source is a manual, request-and-wait, one-shot batch export. Only a handful of sources (calendar, email, some file storage) offer live API access. This means a second brain is necessarily built in batch waves and kept current by periodic re-export loops — not event-driven sync. Design for that from day one: gathering the data is a batch problem, keeping it current is a loop problem, and an AI assistant is what finally makes the loop problem tractable. That's the thing that killed every pre-AI attempt at this.

## Principles before steps

The failure modes here are known. Design against them before writing the first file, not after noticing the wiki has gone stale.

- **Compile once, keep current.** Write-time synthesis — ingest a source, update the relevant pages, cross-link — beats query-time retrieval for a single individual, because knowledge compounds instead of being re-derived on every question. Full argument in [context/why-a-second-brain.md](why-a-second-brain.md).
- **Own the artifact, not the tool.** Markdown files in folders you control, git-versioned, local-first. Every platform in the data-gathering table below can reprice, break, or shut down; your compiled brain must not depend on any of them.
- **Raw sources are immutable; the wiki is derivative.** Exports land in a `raw/` directory and are never edited — that's the provenance layer that keeps the compiled synthesis auditable, and the countermeasure to the editorial trap described in [context/why-a-second-brain.md](why-a-second-brain.md).
- **The collector's fallacy is the number-one killer, and an AI assistant doesn't cure it — it moves it upstream.** The failure pattern: dumping ever more material into `raw/` on the assumption that "the AI will handle it." Possessing information isn't knowing it. The cure is an enforced distillation cadence (the ingest and lint loops below), not more capture.
- **Classification schemes die; schema-enforced structure survives.** Elaborate tag taxonomies and folder hierarchies are the most commonly abandoned layer of every personal knowledge system. What survives: daily notes, wikilinks, and a machine-enforced schema (your instructions file) doing the classification so you never have to tag anything correctly by hand.
- **Honest cost expectation.** The best available field data point — a builder about one month in, roughly 760 pages — reports time invested roughly equal to time saved at that point. The payoff is conditional on deep, narrow, recurring work where re-deriving context is genuinely expensive, and it compounds over months, not days. Expect the first month to feel like pure investment.
- **Automation must be reversible.** Every scheduled agent should write a log entry for what it changed, and changes should stay revertible — git makes this nearly free. "Be careful" is not a fix; reversibility is the actual fix.
- **The markdown-vs-database question is settled for this use case.** For a single individual with up to roughly 50,000–100,000 tokens of dense wiki, markdown wins on auditability, ownership, and zero infrastructure. Add a search index only if the corpus outgrows the context window — markdown stays canonical either way. Full verification in [context/the-6-levels.md](the-6-levels.md).

## Step 0 — Start the data flowing, then define purpose and schema

**The ordering that actually works: request your data access first, define the schema second, ingest third.** The export requests are the long pole — they take hours-to-days to arrive and the download links expire fast (Step 2 has the details) — so they go in *before* anything else, and the thinking happens while they're in flight. And if you're setting up with an AI assistant, get it access to the data *before* it interviews you: the data answers most of the questions, and the assistant should interrogate what it can reach, present you a draft picture, and ask only what the data can't answer (with the privacy boundary — question 5 below — always answered by you explicitly, never inferred). An assistant doing this should say what it's trying to do at each step, so you can help it.

What must still happen **before any full ingestion** is the schema: the intake below. The answers become your instructions file (the equivalent of a `CLAUDE.md`), which is the single highest-leverage document in the whole system — a well-designed schema turns the AI into a disciplined maintainer; a vague one turns it into a generic chatbot that happens to write files.

1. **Who are you and what do you do?** This seeds the personal-biography and people/entity pages.
2. **What should the brain actually do?** Research depth, personal/life memory, work context, or some mix of the three. This decides your page taxonomy.
3. **What data sources exist?** Run the table in Step 2 as a checklist.
4. **How do you work across tools?** Pick a level from [context/the-6-levels.md](the-6-levels.md). Default for deep, compounding knowledge: Level 5, the self-organizing wiki. Just getting started: Level 1–2. Juggling several AI tools at once: consider Level 6.
5. **What is private-forever?** Name it now — health information, finances, private messages, other people's words. This becomes your redaction and visibility policy in Step 3, not an afterthought bolted on later.

## Step 1 — Stand up the skeleton (one session)

1. **Folders**: an inbox drop zone for new material, a processed/provenance archive for everything once it's been ingested, a `wiki/` directory with subfolders for topics, people/entities, projects, source records, and personal pages, plus an append-only session log and a page-schema reference file.
2. **`git init`** the whole tree. Use a private remote or none at all. Commit after every session — git is your reversibility layer and gives you history for free.
3. Point a markdown editor with a graph view (Obsidian is the common choice) at the `wiki/` folder as your human read/browse surface. Run Claude Code at the repository root as the maintainer.
4. **Write your instructions file** (the schema): frontmatter format, wikilink conventions, an alias discipline, the ingest workflow, the log convention, any voice rules. This document is worth iterating on more than any single wiki page — it's what turns generic AI assistance into a disciplined maintainer of *your* system specifically.
5. **Give every page frontmatter**: type, created date, updated date, a version number, tags, aliases. Rich aliases are what keep the page graph connected as your own language varies from session to session — the same idea referred to three different ways should still resolve to one page.

A tooling note worth knowing before you invest in the wrong setup: terminal-based AI coding assistants with direct filesystem access have proven more reliable for this than editor plugins that try to do the same thing inside a notes app — plugin-based approaches have a documented history of vault bloat and fragility. Plain files plus a CLI beats an integration layer.

## Step 2 — Gather the data (the waves)

The core of the build. Ordered by density of self — how much "who you are and what you think" per exported megabyte — so the brain becomes useful starting with the very first wave. Export menus drift; re-verify the exact click-path against the vendor's current settings page before relying on this table.

**The iron rule of export links: download the moment the email arrives, and move the file into your `raw/` folder immediately.** Claude and ChatGPT export links expire in 24 hours; X's lasts 7 days. An expired link means re-requesting and waiting again.

### Wave 1 — AI conversations

Years of your own questions, reasoning, decisions, and drafts. For anyone who thinks out loud with an AI assistant, this is the closest thing that exists to a transcript of your own mind, and it should be the first thing you export.

| Source | How | Format | Gotchas |
|---|---|---|---|
| **Claude** | claude.ai → your initials (bottom-left) → Settings → Privacy → **Export data** → email link | ZIP: `conversations.json`, `projects/`, `memories.json`, `users.json` | Link dies in 24 hours. Web/desktop only (not the iOS/Android apps). Project conversations arrive flattened — reconstruct project boundaries at parse time. |
| **Claude memory** | Settings → Capabilities → "View and edit your memory", or ask Claude *"write out your memories of me verbatim"* | text → paste into a `.md` file | No structured export button; manual copy. |
| **Grok** | **accounts.x.ai/data** → Download account data (or grok.com → Settings → Data → Export Data) | ZIP of JSON (a backend JSON dump plus asset folders) | Email arrives when ready; asset folders can run to gigabytes. Share links are a separate per-conversation surface, not covered by the bulk export. |
| **ChatGPT** (if used) | Settings → Data Controls → **Export data** → email link | ZIP: `conversations.json` + `chat.html` | 24-hour link expiry; the raw JSON is messy — expect some parser work. |
| **Gemini** (if used) | Google Takeout → "Gemini Apps" | HTML/JSON | Exports have been known to come back as empty stubs — verify contents before assuming coverage. |

### Wave 2 — Notes

Deliberate capture — material you already distilled once, by hand.

| Source | How | Format | Gotchas |
|---|---|---|---|
| **Google Keep** | [takeout.google.com](https://takeout.google.com) → deselect all → select Keep only | per-note JSON/HTML | Fine-grained selection avoids a multi-gigabyte everything-export. |
| **Apple Notes** | No bulk export. Per-note: File → Export as PDF/Markdown; bulk: a third-party tool like `apple-notes-exporter` (GitHub) | md/pdf | Folder structure is preserved only via third-party tools, not native export. |
| **NotebookLM** | per-notebook export | mixed | |
| **Notion / Obsidian / existing vaults** | native export (Notion: Settings → Export all workspace content → Markdown) | md/csv | Existing markdown note folders can often be ingested in place, no export needed. |

### Wave 3 — Life logistics: calendar, email, contacts

This is what turns a knowledge wiki into a life brain: dates, commitments, correspondence, relationships.

| Source | How | Format | Gotchas |
|---|---|---|---|
| **Google Calendar** | Google Takeout → Calendar (per-calendar selectable) — or live via the **claude.ai Google Calendar connector** | **ICS** | The connector gives ongoing read access — calendar is one of the only sources that can stay *live* rather than batch. |
| **Gmail** | Takeout → Mail (restrict to specific labels to keep the size sane) — or live via the **Gmail API / claude.ai Gmail connector** (read + draft; cannot send) | **MBOX** | Takeout for the archive plus the connector for the ongoing feed is the right split. If you build your own API access: an OAuth "Internal" consent screen skips Google's app review (Workspace accounts only — consumer Gmail accounts must use "External" in testing mode instead). |
| **Google Contacts** | Takeout → Contacts | vCard/CSV | Seeds your people/entities pages — every recurring person in your life gets a page. |

### Wave 4 — Behavioral trails

What you actually read, watched, and where you went — revealed preference, often more honest than what you wrote down deliberately. Also the most privacy-sensitive wave after messages; decide per your Step 0 privacy answer what stays raw-only and never gets summarized into the compiled wiki.

| Source | How | Format | Gotchas |
|---|---|---|---|
| **Chrome history** | copy `~/Library/Application Support/Google/Chrome/Default/History` on macOS (a SQLite database; tables `urls`, `visits`) — equivalent paths on Windows/Linux | SQLite | Chrome locks the live file — copy it first or close Chrome. |
| **Safari history** | `~/Library/Safari/History.db` | SQLite | The reading process needs Full Disk Access in macOS privacy settings. |
| **YouTube watch history** | Takeout → YouTube → deselect all → history → choose **JSON** | `watch-history.json` | Choose JSON explicitly; the default format is HTML. |
| **Spotify** | account page → Privacy → Download your data → **uncheck "Account data", check "Extended streaming history"** | JSON | The default option silently gives only 1 year of history. The extended export can take up to 30 days to arrive (usually 1–5). |
| **Google Timeline / Location History** | **On-device now**: Android → Settings → Location → Location Services → Timeline → Export Timeline → JSON saved on the phone. iPhone: Google Maps app → your picture → Your Timeline → export | JSON | The big stale-guide trap: Takeout no longer holds Timeline data for most users (it moved on-device in 2024–25). Older tutorials pointing at Takeout are wrong. |

### Wave 5 — Body and money

| Source | How | Format | Gotchas |
|---|---|---|---|
| **Apple Health** | iPhone Health app → profile icon (top right) → **Export All Health Data** → share the ZIP | `export.xml` | Huge for multi-year history (500MB+); convert XML→CSV before ingestion — spreadsheet tools choke on the raw XML. |
| **Bank / brokerage** | per-institution CSV/OFX export from the transaction-history or statements page | CSV/QFX/OFX | No standard across banks; prefer OFX/QFX over CSV where offered. Almost certainly raw-only and local-only under your Step 0 privacy policy. |
| **Utility bills / receipts** | photograph or save as PDF → drop in the inbox | pdf/jpg | An AI assistant with image reading handles these directly at ingest — no separate OCR step. |

### Wave 6 — Messages and social

Other people's words — the highest privacy bar of any wave, and worth pausing on deliberately rather than exporting reflexively.

| Source | How | Format | Gotchas |
|---|---|---|---|
| **WhatsApp** | per-chat: open the chat → More → **Export Chat** (choose "without media" for a lighter text export) | `.txt` | Caps around 40,000 messages per chat (10,000 with media); one chat at a time; very long threads truncate at the cap. |
| **iMessage** | `~/Library/Messages/chat.db` (SQLite) on a Mac | SQLite | Requires Full Disk Access; modern message bodies live hex-encoded in the `attributedBody` column, not the `text` column — a decoding step is needed before they're readable. |
| **X / Twitter** | Settings → Your Account → **Download an archive of your data** | ZIP + HTML viewer | 24–48 hours to generate; the link lasts 7 days; re-requestable every 24 hours. |
| **Reddit** | [reddit.com/settings/data-request](https://www.reddit.com/settings/data-request) | CSV | Can take up to 30 days to arrive — request early. |

**Consent boundary.** Messages contain other people's words, not just your own. A reasonable default: ingest and summarize *your own* side's patterns and decisions into the compiled wiki; keep the counterparty's content raw-only unless you have a specific, considered reason and it does no harm to anyone. This is a judgment call — write down whatever you decide, explicitly, in your Step 0 privacy policy, so it's a decision rather than a default you never actually made.

### Wave 7 — Reading

| Source | How | Format | Gotchas |
|---|---|---|---|
| **Kindle highlights** | [read.amazon.com/notebook](https://read.amazon.com/notebook) (desktop web) + the Bookcision bookmarklet → JSON/TXT; physical Kindle: `My Clippings.txt` via USB | txt/json | Publishers cap exports at roughly 10% of a book — a licensing restriction, not a bug. Mobile-notebook copying was restricted in late 2025 — use the desktop web page. |
| **Papers / PDFs** | the Unpaywall API (lookup by DOI) or institutional repositories — many paywalled papers have a legally open PDF | PDF | |

### The re-export cadence

One-shot exports go stale. Put the refresh on a schedule — a calendar reminder is enough; the request step itself needs a human, since almost nothing in this list is a one-click re-download.

- **Quarterly**: Claude, Grok, ChatGPT exports. Diff each new export against the previous one and ingest only what's new.
- **Live, no export needed**: Google Calendar and Gmail, once a connector is authorized.
- **Yearly or on-event**: Apple Health, Spotify, X, Reddit, Google Timeline.
- **Continuous by design**: a daily journal, inbox drops, and conversation summaries you save as you go — this marginal-capture path is what makes the big periodic re-exports progressively less important over time.

## Step 3 — Ingest: parse, cluster, compile

1. **Parse each export format into a uniform staging structure** — a simple `{title, content, metadata}` shape works for almost everything. You'll write one small parser per format family the first time you encounter it (JSON exports, MBOX for email, ICS for calendar, XML for health data, SQLite for message databases, CSV for financial data, plain text for chat exports) — each parser is written once and reused every time that source re-exports.
2. **Run a privacy gate before any cloud processing.** A structured pass for obvious personal-identifying detail (account numbers, addresses, phone numbers) plus a judgment pass for whatever you named private-forever in Step 0. There is no consumer tool that does this well out of the box as of writing — the discipline of keeping raw exports local-only and only the curated wiki cloud-processed is itself the mitigation.
3. **Ingest by topic cluster, not file by file.** Read related sources together and write or enrich all the affected pages in one pass — this produces meaningfully richer pages and a better-connected graph than processing one file at a time. A single source can touch ten or fifteen pages once you account for every entity, topic, and cross-reference it mentions.
4. **Every source that gets ingested should produce**: a source record page (provenance — where this came from, when), updates to every topic/entity page it touches, new wikilinks connecting it to related material, one line in the append-only log, and the raw file moved from the inbox into the processed archive.
5. **Track the backlog in a manifest file** once you have more than a handful of sources queued. At real scale — thousands of conversations, hundreds of notes — an honest tracker is what makes a months-long backlog tractable rather than something you quietly stop trusting.
6. **Prioritize by compounding value, not by chronology.** Conceptual material (what you think) first, then people (who matters), then projects, then logistics trails last. A brain that knows your ideas but not your calendar is more useful than the reverse.

## Step 4 — Install the quality controls

A compiled wiki reads confidently whether or not it's actually right — this is the editorial trap from [context/why-a-second-brain.md](why-a-second-brain.md). Build these controls in from day one, not after the first embarrassing error:

- **Verify load-bearing claims at ingest time**, using cheap parallel lookups for the first pass and escalating to a more capable model only for genuinely ambiguous or contested cases (see [context/model-routing.md](model-routing.md)).
- **Flag contradictions rather than silently resolving them.** A named tension, with both sources cited, is the honest move — picking a winner without saying so is not.
- **Label evidence by type**: empirical, expert opinion, or speculation, so opinion can't quietly harden into fact simply because it's been sitting in the wiki for a year.

## Step 5 — Wire the loops

This is where scheduled and autonomous work earns its place — but only after manual practice, and only for tasks that pass a real bar. See [context/loops.md](loops.md) for the full framework; the summary:

| Loop | Cadence |
|---|---|
| Inbox sweep and ingest | daily, or every session start |
| Daily journal | continuous, every session |
| Health check (orphaned pages, stale claims, contradictions, gaps) | every 5–10 sessions |
| Re-export reminders | quarterly |
| Self-improvement review | end of every substantive session |

Every autonomous run should log what it changed, and every change should stay revertible through git. Anything outward-facing (an email, a message to someone else) should be drafted, not sent automatically — keep a human on the one step that can't be undone.

## Step 6 — Compound

- **Query, then file back.** A good answer, comparison, or analysis produced during a session is worth saving as its own wiki page — asking questions grows the brain just as much as adding new sources does.
- **Keep a daily journal alongside the append-only log** — a time-ordered memory layer that sits next to the topic-ordered wiki and is often faster to search when you're trying to recall *when* something happened rather than *what* you concluded.
- **Distill opportunistically.** Every time you open a page to answer a question, that's a chance to sharpen it slightly — this is the only maintenance cadence most people actually sustain, so lean into it rather than scheduling a separate "polish" pass nobody gets to.
- **Review the page graph roughly monthly.** Orphaned pages and unresolved links are your to-write list, generated automatically by the structure of the wiki itself.
- **The 30-day test of whether it's working**: do your sessions start from compiled context instead of you re-explaining yourself from scratch? That specific, acute pain — re-briefing a forgetful assistant every single time — should be measurably gone by then. If it isn't, something upstream (schema, ingest discipline, or source selection) needs revisiting before you add more data.

## Related
- [context/why-a-second-brain.md](why-a-second-brain.md) — the underlying case and the failure modes this manual designs against
- [context/the-6-levels.md](the-6-levels.md) — the architecture menu Step 0.4 picks from
- [context/model-routing.md](model-routing.md) — which model tier for ingest vs. verification vs. synthesis
- [context/loops.md](loops.md) — the maintenance-loop framework Step 5 wires in
- [context/export-handout.md](export-handout.md) — a standalone, printable version of the Step 2 export tables
