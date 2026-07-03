# Export Handout — Gathering Your Data

A standalone, printable checklist for pulling your own data out of the services you already use, so it can be fed into a second brain. Follow it step by step; no other file is needed. Work through the waves in order — they're ranked by how much of "who you are and what you think" each source captures, so the earliest waves pay off first.

Menu paths were verified against vendor documentation in mid-2026. They drift — if a path doesn't match what you see, look for the nearest equivalent under Settings → Privacy or Settings → Data.

## The one rule that matters more than any other

**Download every export link the moment the email arrives, and move the file somewhere permanent immediately.** Claude and ChatGPT export links expire in **24 hours**. X's archive link lasts 7 days. An expired link means requesting the export again and waiting again — sometimes days. Don't let an export email sit unread.

## Wave 1 — AI conversation history

If you use an AI assistant regularly, this is the single highest-value export on this sheet — the closest thing that exists to a transcript of your own reasoning over time.

- **Claude**: go to claude.ai → click your initials (bottom-left) → Settings → Privacy → **Export data**. A download link arrives by email. The ZIP contains `conversations.json`, `projects/`, `memories.json`, and `users.json`. Works on web/desktop only, not the phone apps. **Link expires in 24 hours.**
- **Claude memory**: Settings → Capabilities → "View and edit your memory" — or simply ask Claude to *"write out your memories of me verbatim"* and save the text. There is no structured export button; this is a manual copy.
- **Grok**: go to **accounts.x.ai/data** → Download account data (or grok.com → Settings → Data → Export Data). You get an email when the ZIP is ready. The asset folders inside can be gigabytes.
- **ChatGPT** (if you use it): Settings → Data Controls → **Export data**. Email link, ZIP with `conversations.json` and `chat.html`. **Link expires in 24 hours.**
- **Gemini** (if you use it): [takeout.google.com](https://takeout.google.com) → deselect all → select "Gemini Apps". Verify the export actually contains your conversations before assuming coverage — empty exports have been reported.

## Wave 2 — Notes

- **Google Keep**: [takeout.google.com](https://takeout.google.com) → deselect all → select **Keep** only. You get one JSON/HTML file per note. Selecting only Keep avoids a multi-gigabyte everything-export.
- **Apple Notes**: there is no built-in bulk export. Individual notes: File → Export as PDF. For bulk, use a third-party tool such as `apple-notes-exporter` (on GitHub) — that's also the only way to preserve your folder structure.
- **NotebookLM**: export per notebook.
- **Notion**: Settings → Export all workspace content → choose **Markdown**.
- **Obsidian or any existing markdown folder**: nothing to export — the files are already markdown and can be ingested in place.

## Wave 3 — Calendar, email, contacts

This is what turns a knowledge base into a life record: dates, commitments, correspondence, relationships.

- **Google Calendar**: [takeout.google.com](https://takeout.google.com) → Calendar (you can select individual calendars). Format: ICS. Alternatively, the claude.ai Google Calendar connector gives your assistant live, ongoing read access — calendar is one of the few sources that can stay current without repeated exports.
- **Gmail**: Takeout → Mail. **Restrict the export to specific labels** to keep the file size sane — a full mailbox can be enormous. Format: MBOX. The right long-term split: one Takeout export for the archive, plus the claude.ai Gmail connector (read and draft, cannot send) for the ongoing feed.
- **Google Contacts**: Takeout → Contacts. Format: vCard/CSV. This becomes the seed list of the people who recur in your life.

## Wave 4 — What you actually read, watched, and did

Revealed preference — often more honest than what you deliberately wrote down. Also privacy-sensitive: decide up front what should stay in your private archive only.

- **Chrome history**: this lives on your own computer, not in the cloud — on a Mac, the file is `~/Library/Application Support/Google/Chrome/Default/History` (a SQLite database). Chrome locks it while running, so close Chrome or copy the file first.
- **Safari history**: `~/Library/Safari/History.db`. Reading it requires granting Full Disk Access in macOS privacy settings.
- **YouTube watch history**: Takeout → YouTube → deselect all → select history → and **choose JSON explicitly** — the default is a much less useful HTML file. You'll get `watch-history.json`.
- **Spotify**: account page on the web → Privacy → Download your data → **uncheck "Account data" and check "Extended streaming history"**. The default option silently gives you only the last year; the extended option is your full history. It can take up to 30 days to arrive (usually 1–5).
- **Google Timeline / location history**: this is the big stale-guide trap — Timeline moved **on-device** in 2024–25, so Takeout no longer holds it for most users and older tutorials are wrong. On Android: Settings → Location → Location Services → Timeline → **Export Timeline** (saves a JSON file on the phone). On iPhone: Google Maps app → your picture → Your Timeline → export.

## Wave 5 — Health and money

- **Apple Health**: iPhone Health app → tap your profile icon (top right) → **Export All Health Data** → share the ZIP to yourself. The `export.xml` inside is huge for a multi-year history (500MB+); plan to convert it to CSV before doing anything with it — spreadsheet apps choke on the raw XML.
- **Bank / brokerage**: every institution has its own export, usually on the transaction-history or statements page. Prefer a structured format (OFX/QFX) over plain CSV where you're given the choice. Treat this data as private-archive-only by default.
- **Bills and receipts**: a photo or saved PDF is enough — an AI assistant that reads images can extract the details directly; no scanning step needed.

## Wave 6 — Messages and social platforms

The most sensitive wave, because it contains other people's words, not just yours. Decide your boundary before exporting — a reasonable default is to summarize only your own side's patterns and decisions, and keep what other people said in your private archive only. Whatever you decide, write it down.

- **WhatsApp**: per chat — open the chat → More → **Export Chat**, and choose "without media" for a lighter text file. Exports cap at roughly 40,000 messages per chat (10,000 with media), one chat at a time; very long threads truncate at the cap.
- **iMessage**: on a Mac, your messages live in `~/Library/Messages/chat.db` (SQLite). Reading it requires Full Disk Access, and modern message bodies are stored hex-encoded in a column called `attributedBody` rather than as plain text — they need a decoding step. This one is for the technically comfortable.
- **X / Twitter**: Settings → Your Account → **Download an archive of your data**. Takes 24–48 hours to generate; the link lasts 7 days and can be re-requested every 24 hours. The ZIP includes an HTML viewer.
- **Reddit**: [reddit.com/settings/data-request](https://www.reddit.com/settings/data-request). Arrives as CSV and can take up to 30 days — request this one early.

## Wave 7 — Reading

- **Kindle highlights**: go to [read.amazon.com/notebook](https://read.amazon.com/notebook) on a desktop browser (mobile copying was restricted in late 2025 — use desktop). The Bookcision bookmarklet turns the page into clean JSON or text. If you have a physical Kindle, `My Clippings.txt` is retrievable over USB. Note: publishers cap exports at roughly 10% of any book's text — a licensing restriction, not something you can work around.
- **Papers and PDFs**: before assuming a paper is paywalled, check for a legally open copy — the Unpaywall API looks one up by DOI, and institutional repositories often host author versions.

## After you've gathered a wave

Move every downloaded file into your second brain's inbox folder as soon as it's saved, and never edit the raw file — it stays untouched as the permanent record of what the export contained. The processing step (turning raw exports into wiki pages) is described in [context/how-to-build.md](how-to-build.md).

## Keeping this current

One-time exports go stale. A reasonable refresh schedule:

- **Every three months**: Claude, Grok, and ChatGPT exports. Diff each new export against the previous one so you only process what's new.
- **Yearly, or when something changes**: Apple Health, Spotify, X, Reddit, Google Timeline.
- **Never again, once connected**: Google Calendar and Gmail, if you set up the live connectors — those two stay current on their own.

## Related
- [context/how-to-build.md](how-to-build.md) — the full build manual these tables are drawn from, including what happens to the data once gathered
