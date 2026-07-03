# External Tools and APIs

How to reach outward from the brain — calling other CLIs, other model vendors' APIs, and other services — without leaking a credential in the process.

## External CLIs — the general pattern

Your main assistant orchestrates; specialist CLIs fill the gaps it doesn't cover natively — image generation, live-search grounding, a second opinion from a different vendor's model. A genuinely different training corpus makes paired verification stronger than asking the same model twice, per [context/model-routing.md](model-routing.md)'s escalation logic.

The invocation shape is consistent enough across tools to learn once:

- `<cli> --print "prompt"` or `-p "prompt"` — non-interactive, single-shot call, the form you want from a script or a sub-agent.
- A JSON output flag (`--json`, `--output json`, or similar) when you need to parse the result rather than read it.
- Rate limits bite on rapid sequential calls more than on volume — space out a batch rather than firing it all at once, or check the vendor's documented limit first.

## GitHub CLI (`gh`) essentials

Why reach for `gh` instead of git plus the browser: it infers the repo and branch from your current directory, so routine PR and issue work is a single command instead of a context switch.

| Task | Command |
|---|---|
| Authenticate | `gh auth login` |
| Create a repo | `gh repo create <name> --private` (or `--public`) |
| Clone a repo | `gh repo clone owner/repo` |
| Open a PR | `gh pr create --title "..." --body "..."` (or `--web` to finish in the browser) |
| List PRs | `gh pr list` |
| File an issue | `gh issue create` |
| List issues | `gh issue list` |

Plain `git` still does the actual `add` / `commit` / `push` — `gh` is the layer on top for the GitHub-specific parts of the workflow.

## API keys — the hygiene that actually matters

Most of what's written about key hygiene is more elaborate than what's actually load-bearing. The short list that matters:

- **`.env` at the project root, and `.env` in `.gitignore` from the first commit** — before the first key ever gets written to disk, not after.
- **Commit a `.env.example`** with variable names only (`ANTHROPIC_API_KEY=`), so the shape of what's needed is documented without the values ever touching git.
- **If a key leaks, rotate at the provider first.** Deleting the file does nothing — the key still lives in git history, in any fork, and in scanner caches that already indexed the commit. The order is: rotate the key at the provider, check the provider's usage logs for anything that ran on the leaked key, then scrub git history (`git filter-repo` or BFG), then update every deploy target that had the old value. The median enterprise key-rotation time is reported around 94 days — treat that as the number to beat, not the norm; act within the hour, not the quarter.
- **A pre-commit hook that scans for secrets** (`gitleaks` is a common choice) catches a key before it's committed at all, which is a strictly better place to catch it than after.
- **A password-manager alternative for local secrets**: on macOS, `security add-generic-password` — omit the `-w value` flag so it prompts interactively, keeping the secret out of your shell history.
- **2026-specific**: an AI coding agent with filesystem access can read any `.env` sitting in the project directory it's running in. Keep secrets out of an agent's context when you can avoid putting them there — pass them through environment variables the agent doesn't need to read directly, rather than pasting values into a prompt.
- **Client-side JavaScript keys are public by definition** — anything shipped to a browser can be extracted by whoever loads the page. Proxy the call through a server-side function instead of embedding the key client-side.

## Calling external model APIs

The pattern is the same across vendors: a key in the environment, the vendor's official SDK, and `os.getenv` (or your language's equivalent) to read it — never a key typed directly into source.

```
ANTHROPIC_API_KEY   →  the Anthropic SDK
OPENAI_API_KEY       →  the OpenAI SDK
XAI_API_KEY          →  OpenAI-SDK-compatible, base_url="https://api.x.ai/v1"
```

xAI's Grok API is a useful special case: it's wire-compatible with the OpenAI SDK, so you point the same client at a different `base_url` rather than installing a separate library.

**Cost awareness, without quoting numbers that will be stale by the time you read this**: prompt caching and batch APIs are the two biggest cost levers most people leave on the table. Cached input tokens cost a small fraction of a fresh input token; batch processing (submit now, get results within a set window) typically runs at roughly half the synchronous price. Both are worth checking before assuming a workload is too expensive to run. **Always read the provider's own pricing page before quoting a number** — aggregator blogs and older training data go stale fast, and prices move.

## When to call an API directly vs. reach for MCP

- **A single, deterministic call** (generate this image, get a second opinion on this text, classify this input) → call the API directly. It's simpler, faster, and easier to debug than standing up a server for one call shape.
- **An agent choosing among three or more tools at runtime**, where what gets called depends on what the agent decides mid-task → MCP. That's the coordination problem MCP is built for; see [[Model Context Protocol (MCP)]] and [context/connecting-outside-sources.md](connecting-outside-sources.md) for the mechanism and the security discipline around it.

## Related
- [context/model-routing.md](model-routing.md) — the tier/effort framework this doc's CLI and API calls should follow
- [context/connecting-outside-sources.md](connecting-outside-sources.md) — MCP servers and live connectors, the data-in counterpart to this doc's tools-out focus
- [[Model Context Protocol (MCP)]] — the concept page behind the MCP decision rule above
- [[Sub-agents and Agent Teams]] — dispatching work across specialist agents, the orchestration layer these tools plug into
