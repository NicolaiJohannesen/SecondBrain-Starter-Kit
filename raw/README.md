# raw/

Original source material — conversation exports, articles, notes, PDFs — kept immutable and never edited. The compiled wiki in `wiki/` is derivative of this material, not a replacement for it; there should always be a path back to the original source behind any wiki page.

- **`inbox/`** — the only drop zone. Put any new source file here; the ingest workflow reads it, processes it into the wiki, and moves it to `ingested/topic-sources/{topic}/` when done. Don't move files out of the inbox by hand.
- **`ingested/`** — everything that's been processed, kept as provenance, organized by kebab-case topic folder.
- **`MANIFEST.md`** — the processing-status tracker.

## Why this whole directory is gitignored by default

`raw/` holds your actual source material, which is very likely to contain personal information you don't want in a git history — let alone a pushed remote. The kit's `.gitignore` excludes everything under `raw/` except this README and the empty placeholder files that keep the folder structure intact. If you want version history on your raw sources, do that deliberately (a private repo, a separate backup target) rather than by accident through the kit's default git setup.
