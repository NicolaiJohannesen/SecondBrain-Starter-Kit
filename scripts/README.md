# Export parsers

Convert raw service exports into uniform staging JSON (`{title, content_chars, content}`) that `/ingest-source` processes.

| Script | Input | Notes |
|---|---|---|
| `parse_claude.py` | Claude account export (`conversations.json`, `projects/`) | |
| `parse_grok.py` | Grok/xAI account export JSON | |
| `parse_keep.py` | Google Takeout → Keep | |
| `parse_notebooklm.py` | NotebookLM exports | |

Output goes to `raw/staging/<source>/` (created automatically); ingest from there by topic cluster.

**Caveat**: export formats drift and vary by account. These parsers are known-good against real exports as of mid-2026; expect small adaptations for your data's shape. PRs with fixes or new parsers (calendar ICS, Gmail MBOX, Apple Health XML, bank CSV, WhatsApp TXT) are the most valuable contribution to this kit.
