# Ancillary Options

None of this is required. The kit works fully without any of it. This is a reference for optional tooling that plugs in around the brain once it's running — organized by the question each one answers.

## Obsidian skills — if you're viewing the wiki in Obsidian

If you're using [Obsidian](https://obsidian.md) to browse `wiki/` as a graph (the Quickstart's optional last step), three small skills from [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) (MIT) are worth vendoring into `.claude/skills/` so Claude authors Obsidian-flavored content correctly instead of guessing at the syntax:

- **`obsidian-markdown`** — Obsidian Flavored Markdown: callouts, embeds, block references (`^id`), inline comments (`%%...%%`).
- **`obsidian-bases`** — `.base` files, Obsidian's database-style views over frontmatter. Useful once the wiki has enough pages that a filtered/sorted view (recently updated, orphans, by tag) beats a hand-maintained index page.
- **`json-canvas`** — `.canvas` files for visual mind-maps/flowcharts, if you use those in Obsidian.

Skipped from the same repo, and why: `defuddle` (weaker than a dedicated fetch script for pulling readable text from web pages) and `obsidian-cli` (only useful if you're developing an Obsidian plugin, not for normal wiki use). Two more from the same repo exist and didn't change as of this writing — check the repo directly if it's been a while.

## CLI options — other agentic CLIs, if Claude Code alone isn't enough

Claude Code is the default and sufficient on its own. If a specific gap shows up — image generation, live web-search grounding, a second model's opinion for adversarial verification — the pattern that's emerged across 2025–2026 is **one CLI as orchestrator, others dispatched as specialist subprocesses**, not picking a single tool to commit to:

| CLI | Vendor | Invoke | Notes |
|---|---|---|---|
| **Claude Code** | Anthropic | `claude --print "..."` | The orchestrator this kit assumes |
| **Gemini CLI** | Google | `gemini -p "..."` | Google Search grounding built in; check current support status before relying on it — Google's CLI landscape has shifted more than once |
| **Grok Build** | xAI | `grok -p "..."` | A coding-specialist agent, not a general reasoning model — useful for a second opinion on code, not prose |
| **Codex CLI** | OpenAI | `codex exec --json "..."` | JSONL output designed for piping (`npm test \| codex exec`) |
| **Aider** | Open source | `aider --message "..." --model <any>` | The one genuinely multi-backend option — Claude, GPT, Gemini, Grok, or local models from a single tool, API-key-only |

Whichever you add, the practical value is **cross-vendor paired dispatch**: running the same question through two differently-trained models produces real disagreement to learn from, not just two phrasings of the same answer. This CLI landscape moves fast — verify current install commands and auth requirements before relying on anything above; treat this table as a starting map, not a frozen reference.

## MCP options — extending what the brain can reach live

[Model Context Protocol](https://modelcontextprotocol.io) servers give Claude live access to an external service instead of a one-shot export. The kit's connectors section already covers Google Drive/Calendar/Gmail; beyond those, MCP servers exist for nearly any domain. **Travel is a worked example** of the pattern — the same evaluation applies to any domain (finance, project-management tools, calendars beyond Google):

**The one question that matters for any MCP server: can it only search, or can it also transact?** A server that can only search and return results is low-risk to add. A server that can also place an order, make a booking, or spend money needs its OAuth scopes read personally before any credential goes near it — don't assume "read the docs" is the same as "it's read-only."

Worked example (travel): a flight-search server backed by an API like Duffel can be built to call *only* the search endpoint and never the booking endpoint — structurally safe by construction, not by promise. The same provider often has a parallel "stays" (hotel) API using the same account; extending an existing read-only integration to a sibling product from the same vetted provider is usually a better move than onboarding an entirely new company's API key for one more domain. Community MCP registries (mcp.so, glama.ai, smithery.ai) are worth searching before building anything from scratch — but always check the safety question above before wiring in a key, regardless of how polished the README looks.

## Speech-to-text — if you dictate instead of type

If you dictate into Claude Code rather than typing, your operating system's built-in dictation is the default — but it isn't always the best choice, and the right answer depends on your hardware, not just preference:

- **Apple Silicon Macs** have a Neural Engine, so on-device transcription (native dictation, or a local Whisper model via a tool like whisper.cpp with Core ML acceleration, or MLX Whisper) can be fast, accurate, and free of any network dependency. Local is a genuinely good option here.
- **Older Intel Macs have no such accelerator.** Native dictation on Intel Macs is actually cloud-processed already (Apple removed the offline path from Intel Macs years ago), and a documented daemon bug (`corespeechd`) is a common cause of dictation spiking CPU usage on these machines — not model-inference cost, a bug. Running a *local* Whisper model here would be strictly worse: no Metal/Core-ML/Neural-Engine acceleration exists to fall back on, so only the least-accurate small models run fast enough to feel responsive, while a competent cloud option gets better accuracy at near-zero local CPU cost.

If native dictation feels slow, inaccurate, or CPU-heavy, cloud-based dictation apps built specifically for AI coding workflows (several exist as of 2026, often with a free tier worth trying first) typically add an LLM cleanup pass that fixes homophone and grammar errors raw transcription misses, and several explicitly support chunking long dictation so it lands cleanly in a terminal input. Try the free tier of whichever is current before paying for anything — the free allotments are usually enough to tell if it solves your actual problem.

## A note on all of this

Every section above will drift — CLIs get renamed, MCP servers get built or abandoned, dictation apps ship new tiers. Verify current names, prices, and setup commands before acting on anything here; treat this page as a map of *where to look*, not a frozen source of truth.
