# Personal Data Census — every input, and how to get it

**The complete map of where your life's data lives and how to extract every piece of it** — the exhaustive per-service reference behind the seven data-gathering waves in [how-to-build.md](how-to-build.md). The build guide tells you the *order* (density-of-self first); this census is the *whole territory*: every social network, every LLM provider, the full Google catalog, professional platforms, commerce, media, body data, files — plus the legal lever that works when no export button exists. Researched and primary-source-verified 2026-07-03; export paths drift, so re-verify menu trails at execution time.

## How to read this census (the philosophy)

- **A census is a menu, not a mandate.** The collector's fallacy applies at the export layer too: pulling forty archives you never distill is hoarding with extra steps. Use the signal-density ranking (below) to decide what gets *compiled* into the wiki, what stays *raw-only*, and what isn't worth requesting at all.
- **The new primitive is the scheduled export, not the one-big-pull.** Google Takeout now schedules recurring exports (every 2 months × 1 year); Google Photos does incremental new-items-only exports; Slack Business+ schedules weekly. Perpetually-growing sources (photos, fitness, mail) should run on standing schedules; one-shot pulls are for the static long tail.
- **Calendar the download, not just the request.** Expiry windows are short and unforgiving: LinkedIn 72h · Meta/TikTok 4 days · Garmin **3 days** · Whoop/MyFitnessPal 7 days · GitHub 7 days · Apple 14 days · Discord 30 days. An expired link means re-requesting and re-waiting.
- **Always take the slow/full path.** Nearly every service offers a fast export and a full one (LinkedIn's 10-minute pick-list vs 24-hour archive; Meta's standard export vs 15-day "data logs"; Netflix's 2-field CSV vs the full privacy request). For a context layer, the fast path is a teaser — request the full artifact.
- **The privacy gate from the setup interview (`/setup-brain` question 5) governs everything here**: what's tagged private-forever lands in `raw/` and never gets compiled; other people's words (messages) follow the consent boundary.

## The universal lever — when there is no export button

**A DSAR (Data Subject Access Request) under GDPR Art. 15 (access) + Art. 20 (portability) compels any company serving people in the EU/EEA to hand over your data within one month** (extendable +2 months for complex requests, but they must say so within the first month). The self-serve button is what the company *chose* to show; the DSAR returns what they *hold* — routinely more (inferred ad profiles, support transcripts, appended third-party data). California's CCPA/CPRA is the parallel lever (45 days +45; applies to businesses over $26.625M revenue — the inflation-adjusted 2026 figure, not the commonly cited $25M).

Practice: find `privacy@` / `dpo@` in the privacy-policy footer or the OneTrust-style rights portal; cite **Art. 15 as the primary request and Art. 20 for the machine-readable format**; provide reasonable identity proof; mention DPA escalation if stalled — it unsticks requests.

Use the button when a real one exists; DSAR when (a) there is none, (b) the button is scoped narrower than what they hold, or (c) you want the enforceable deadline.

The ready-to-send template:

```
Subject: Data Subject Access Request — Art. 15/20 GDPR (Data Access + Portability)

Hello,

I am writing to exercise my right of access under Article 15 GDPR, and my
right to data portability under Article 20 GDPR where applicable to data you
process on the basis of my consent or a contract with me.

Please provide: (1) confirmation of whether you are processing my personal
data; (2) a complete copy of that data; and (3) the supplementary information
required under Article 15(1) — purposes, categories, recipients, retention
period, and source if not collected directly from me.

Where technically feasible, please provide the data in a structured, commonly
used, machine-readable format (e.g. CSV or JSON) per Article 20. I am happy
to provide reasonable proof of identity.

Please respond within one month of receipt per Article 12(3) GDPR. If you
believe this request qualifies for the two-month extension for complex
requests, please notify me within the initial month with your reasoning.

[Full name] · [Account email] · [Account ID/username]
```

(California variant: cite the right to know and data portability under CCPA as amended by CPRA; deadline 45 days, +45 with notice.)

## LLM providers

The big four (Claude, ChatGPT, Grok, Gemini) are covered in [how-to-build.md](how-to-build.md) Wave 1. The rest bifurcate cleanly — real button vs email-a-human:

| Provider | Export? | Path | Notes |
|---|---|---|---|
| **Mistral (Vibe** — Le Chat rebranded May 2026**)** | ✅ | admin.mistral.ai/account/export (admin surface, not chat settings) | near-immediate |
| **Microsoft Copilot** | ✅ | account.microsoft.com/privacy → Copilot → Export all activity history → CSV | **three separate export buttons** (Copilot app / M365 apps / Copilot Chat) — take all three |
| **Meta AI** | ✅ | meta.ai → Settings → Data & privacy → Download; in-app chats have separate dialogs | HTML/JSON; 4-day window; deleted chats excluded |
| **character.ai** | ✅ | Settings → Legal & Privacy → Export my data | ZIP of JSON (user/character/message) |
| **Perplexity** | ⚠️ weak | no bulk button; Data Privacy Form (de-facto DSAR, ~30 days) | per-thread share/PDF; community exporters exist |
| **DeepSeek** | ❌ | privacy@deepseek.com only | browser-extension exporters or copy-paste; data on mainland-China servers |
| **Poe (Quora)** | ❌ bulk | per-chat export, paid tiers only; privacy@poe.com | in-product export bots (@savechats) as workaround |

## Social networks

| Service | Path | Format | Wait / expiry | Load-bearing gotchas |
|---|---|---|---|---|
| **LinkedIn** | Settings & Privacy → Data privacy → **Get a copy of your data** | ZIP of CSVs | fast tier ~10 min; **full archive ≤24h**; link 72h | take the FULL archive (adds connections, messages, searches, AI conversations); excludes "Who's Viewed"; desktop only; connections' emails withheld where they opted out |
| **Facebook / Instagram / Threads** (one tool) | **Accounts Center → Your information and permissions → Export your information** — request once per profile | **JSON** (choose over HTML) + media (quality selectable) | hours–24h typical; "data logs" up to 15 days; **link 4 days** | the slower "data logs" request is a separate, richer artifact; ads data only from the main profile; Threads export is **mobile-only**; recurring-export option exists when exporting to an external service |
| **TikTok** | Settings and privacy → Account → **Download your data** | TXT or **JSON** | up to a few days; link 4 days | includes watch + search history — dense taste signal |
| **Snapchat** | accounts.snapchat.com/v2/download-my-data | ZIP (JSON + media) | ~7 days | Memories included; already-vanished ephemeral content is gone regardless |

## Messaging

WhatsApp and iMessage are covered in [how-to-build.md](how-to-build.md) Wave 6 (with the consent boundary). The rest:

| Service | Reality |
|---|---|
| **Telegram** | Best-in-class: **Desktop app → Settings → Advanced → Export Telegram data** — JSON or browsable HTML, media included, per-type toggles, local file (no expiry). Fresh desktop logins wait 24h before export unlocks. |
| **Discord** | Settings → Data & Privacy → **Request your data** → ZIP of **JSON** (not CSV), up to 30 days, link 30 days. Left-server coverage is inconsistent. |
| **Slack** | **The inverted case: members have NO self-serve message export on any plan.** Public-channel exports need an admin; private channels + DMs need Business+/Enterprise owner tooling. If you live in someone else's free workspace, your own DM history may be unreachable — capture as you go. |
| **Signal** | **Structurally export-hostile by design** — no server copy exists, so even a DSAR returns ~nothing. The only strategy: maintain your own encrypted local backups continuously (Android Secure Backups; desktop DB is keyed to the OS keychain). |

## Professional & writing

| Service | Path | Get | Gotcha |
|---|---|---|---|
| **GitHub** | Settings → Account → Export account data (tar.gz, link 7 days) | profile/activity metadata | **the archive is NOT the code** — `git clone` for repos; `gh api` for issues/PRs/stars |
| **Stack Exchange** | policies.stackoverflow.co/data-request (DSAR-style) | personal data | your *public* Q&A is easier via SEDE (data.stackexchange.com) or the API |
| **Medium** | Settings → Security and apps → Download your information | ZIP of HTML (incl. drafts) | HTML-only → `medium-2-md` for Markdown |
| **Substack (writer)** | Publication Settings → Exports | posts HTML + CSV index + full subscriber CSV | subscriber-side: no reading-data export exists |
| **Goodreads** | My Books → Import/Export → **Export Library** | one CSV incl. ratings + review text | the API is dead (2020) — the CSV is the only sanctioned path |
| **WordPress** | Tools → Export (or `wp export`) | **WXR** XML: posts, pages, comments | **media files are NOT in the WXR** — copy `wp-content/uploads/` separately |

## Google — the complete Takeout catalog

Takeout mechanics: choose split size (up to 50GB), deliver to email link or straight into Drive/Dropbox/OneDrive; **scheduled exports = every 2 months × 1 year, each a FULL re-export** (not incremental — except Google Photos' separate new-items-only schedule). Beyond the famous four (Gmail MBOX · Calendar ICS · Keep · Drive with **Docs→docx-or-PDF chosen at export time**), the catalog worth knowing:

| Service | Get | Format | Gotcha |
|---|---|---|---|
| **Photos** | media + per-file JSON sidecars | original + JSON | **true dates/GPS live ONLY in the sidecars** (EXIF stripped on upload); sidecar naming changed late-2024 (`.supplemental-metadata.json`) breaking old merge scripts; per-album partial export possible |
| **My Activity** (Search, YouTube, Assistant) | full activity log | **choose JSON** — the HTML default mis-parses dates and OOMs parsers | the densest behavioral record Google holds; mine for quarterly summaries, don't ingest raw |
| **Maps (your places)** + **Saved** | reviews, starred, saved lists | GeoJSON | TWO separate exports (your-places vs Saved) — easy to grab one and miss the other; reviews are authored opinion — high signal |
| **Contacts** | all contacts | vCard default; CSV needs manual selection | seeds Entities/ |
| **Chrome** | bookmarks, history, Reading List | HTML; Reading List is a non-standard blob | curation artifacts — small and dense |
| **YouTube (own)** | uploads, playlists, subscriptions (CSV), comments, likes | mixed | large channels: hours–days to generate |
| **Fit** | daily aggregates + sessions | CSV + TCX | weight/body-composition historically drops out — verify before trusting |
| **Pay/Wallet** | transactions | CSV under a nested "Transactions made on Google" folder | raw-only signal |
| **Play** | purchase/install history | JSON | book purchases = taste signal; app history = noise |
| **Blogger** | posts/comments | `feed.atom` (the sole remaining path) | WordPress importer expects XML — needs a converter |

## Apple / iCloud

- **privacy.apple.com → "Get a copy of your data"**: sign-in records, iCloud content (contacts/calendars/notes/bookmarks/mail), purchase histories, support records. Ready ≤7 days; **download window 14 days**.
- **iCloud Photos**: the web UI caps selection at 1,000 items — the real bulk path is **Mac Photos app → Download Originals → Export Originals** (overnight-to-days for big libraries).
- Health, Notes, iMessage: [how-to-build.md](how-to-build.md) Waves 2/5/6.

## Commerce (mostly raw-only signal)

**Amazon**: Account → "Request your personal information" — multiple CSVs, usually 6–36h. **PayPal**: Activity → Reports — CSV but **only 12 months per request** (7 years total = multiple pulls). **eBay**: official request ~1 week; no clean first-party CSV. **Uber**: Privacy Center → Download — trips + prices. Banking/brokerage: [how-to-build.md](how-to-build.md) Wave 5.

## Media & curation

**Netflix**: the quick `NetflixViewingHistory.csv` is 2 fields; the full privacy request is far richer; **per profile**. **Letterboxd**: Settings → Export — clean CSVs (diary ≠ watched — take both). **Instapaper**: CSV/HTML, instant. **Feedly**: feedly.com/i/opml — subscriptions only (Boards/Read-Later NOT included). **Podcasts**: Pocket Casts in-app OPML; Overcast web-only since 2024. **Steam**: help portal / GDPR flow, no one-click button. **⚠️ Pocket is DEAD** — shut down July 2025, data deleted Nov 2025; any guide still saying "export your Pocket" is a dead instruction.

## Body & places

| Service | Path | Wait | Gotcha |
|---|---|---|---|
| **⚠️ Fitbit — TIME-BOMBED** | must migrate to a Google account; export then flows via Takeout (full history JSON/CSV incl. per-minute HR) | — | **legacy logins die 2026-05-19; unmigrated accounts + ALL historical data DELETED after 2026-07-15** — the one census item with a hard expiry on inaction |
| **Strava** | Settings → My Account → Request your archive | hours–10 days | ZIP: activities.csv + per-activity GPX/FIT/TCX |
| **Garmin** | garmin.com data-management → Request Data Export | up to 30 days | **file self-deletes after 3 days** — download immediately; nested-zip structure |
| **Oura** | Membership Hub → Download Data (CSV) | up to 10 days | durations in raw seconds |
| **Whoop** | app → Data Export | ≤24h; link 7 days | rate-limited to one request/24h |
| **MyFitnessPal** | Settings → Download Your Data | 1–24h; link 7 days | **Premium-gated** — free tier cannot self-export |

Body data is the one category a context layer has *no other source for* — compile weekly/monthly aggregates, keep raw sensor CSVs raw.

## Files & docs

**Dropbox**: hard caps — 20GB per zip, 10k files per download; big accounts export via the desktop sync folder, not the web. **Microsoft**: OneDrive files directly; the Privacy Dashboard export (≤30 days) is activity data, not files. **Evernote**: desktop-app-only ENEX export, 100-note/one-notebook batches — `evernote-backup` (open source) automates full dumps. Notion/Obsidian: [how-to-build.md](how-to-build.md) Wave 2.

## Signal-density ranking — what's worth compiling

**Compile into the wiki** (dense self-expression per byte): LLM conversations (the densest source that exists) · Maps reviews + starred places (authored opinion + a map of intention) · Letterboxd/Goodreads ratings-with-reviews · OPML subscription lists + Chrome Reading List (curation = what you chose to attend to) · YouTube subscriptions/likes · your own writing everywhere (Medium/Substack/WordPress/GitHub) · LinkedIn profile+messages · body-data *aggregates* · My Activity mined into quarterly "what was I researching" summaries.

**Raw-only** (transactional exhaust; keep for the ledger, don't narrate): Amazon/eBay/PayPal/Google Pay orders · Uber trips · Play app history · raw browsing history · raw sensor streams.

**Skip unless a specific need exists**: airline/hotel loyalty DSARs (30–45 days for thin booking records) · game-activity dumps.

## The no-export-at-all list (plan around these)

Signal (structurally nothing — self-capture only) · Slack-as-member (admin-gated) · Poe (paywalled per-chat) · DeepSeek (email-only) · Perplexity (form = de-facto DSAR) · Substack-as-reader · Snapchat's already-vanished content. For everything else on this list that a DSAR *can* reach: the template above.

## Related
- [how-to-build.md](how-to-build.md) — the operational seven-wave ordering this census feeds
- [[Personal Context Layer]] · [[Second Brain]] — what the inputs feed
- [[Memory Compaction]] — what happens when it all gets big
