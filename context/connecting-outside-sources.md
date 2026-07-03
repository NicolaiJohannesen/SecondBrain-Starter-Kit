# Connecting Outside Sources

How to get information *into* the brain from outside services once you've moved past one-shot exports — the live connections that keep a source current without you re-requesting anything.

## The two lanes

- **Batch exports** — a request-and-wait download you process once and re-request on a schedule. Covers almost everything: AI conversation history, notes, messages, health data. Full table and click-paths: [export-handout.md](export-handout.md).
- **Live connections** (this doc) — a small number of sources that stay continuously current once authorized, no re-export needed. Calendar, email, and file storage are the only personal sources that currently offer this.
- Everything not in the second category is a periodic re-export loop, not a live sync — design for that from the start.

## Google connectors (claude.ai)

Settings → Connectors → connect the ones you use. Each grants a specific, scoped capability:

| Connector | What it gives |
|---|---|
| **Gmail** | Search, read, and draft — it cannot send. Drafts wait in your outbox for you to review and send yourself, which is the right place for the one step that can't be undone. |
| **Google Drive** | Read-only access to files, including search and metadata. **Google Docs are readable through this connector** — there's no separate "Docs connector"; Drive covers it. |
| **Google Calendar** | Read plus event management — list, create, update, delete, and respond to events, and suggest meeting times. |

These three are the only continuously-live personal sources available this way. Everything else you connect (or export) stays a batch problem.

## Google Takeout for the same sources, in bulk

The connectors give you the ongoing feed; Takeout gives you the historical bulk dump underneath it — you generally want both, not one instead of the other:

- **Docs**: arrive as `.docx` via a Drive export, not the connector.
- **Gmail**: MBOX, and worth restricting to specific labels to keep the file size sane.
- **Calendar**: ICS, one file per calendar.

Full paths, gotchas, and the rest of the export waves: [export-handout.md](export-handout.md).

## MCP servers — the general mechanism

The Model Context Protocol is the general answer to "how does an AI assistant reach a tool or data source it doesn't have built in." Five things worth knowing before you add one:

- It's an open standard (not vendor-specific), under Linux Foundation governance since December 2025.
- It solves an M×N integration problem by turning it into M+N: any client that speaks MCP can use any server that speaks MCP, without a custom integration per pair.
- A server exposes tools, resources, or prompts; a client (claude.ai, Claude Code, or another MCP-speaking assistant) connects to it and calls what it exposes.
- Adding one: in claude.ai, Settings → Connectors → Add custom connector. In Claude Code, `claude mcp add`.
- Full concept page: [[Model Context Protocol (MCP)]].

**The security reality, stated plainly.** The public MCP server ecosystem is immature. Independent audits have found that most open-source servers use static, long-lived credentials rather than OAuth, and that agents without safeguards are highly vulnerable to prompt injection carried inside a malicious server's responses. The rule that follows from this:

- **Vet every server individually** before connecting it — who publishes it, what it can reach, what it does with what it's given.
- **Prefer official or first-party servers** over community ones for anything touching real credentials.
- **Never hand a server broader access than its job needs.** A server that only needs to read a calendar shouldn't also hold a key that can send email.

## Web content

Fetching a page or article into the inbox is a smaller version of the same in-flow. Two things to know:

- Client-rendered pages (a lot of modern JS-heavy sites) can return an empty page to a simple fetch — you may need a headless browser that waits for content to render before reading it.
- Save what you'll actually cite. If a source is going to inform a wiki page, keep a copy of it in `raw/` — provenance you'd otherwise lose the moment the page changes or disappears.

## Cadence table

| Source | Cadence |
|---|---|
| Gmail, Calendar, Drive (once connected) | Live — no re-export needed |
| Other MCP servers | Live while connected, scoped to what you authorized |
| AI conversation exports, notes, messages | Quarterly re-export (see [export-handout.md](export-handout.md)) |
| A daily journal, inbox drops, saved web sources | Continuous, by habit rather than schedule |

## Related
- [export-handout.md](export-handout.md) — the full batch-export tables these connectors sit alongside
- [how-to-build.md](how-to-build.md) — Step 2 gathers the data this doc keeps current
- [[Model Context Protocol (MCP)]] — the concept page behind the MCP section above
- [[Personal Context Layer]] — why a continuously current personal substrate is worth building at all
