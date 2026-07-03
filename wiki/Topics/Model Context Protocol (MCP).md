---
type: topic
created: 2026-07-03
updated: 2026-07-03
version: 1
origin: kit-seed
tags:
  - topic
  - seed
  - domain/ai
aliases:
  - MCP
  - Model Context Protocol
---

# Model Context Protocol (MCP)

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

The Model Context Protocol (MCP) is an open standard, released by Anthropic in late 2024, that standardizes how AI systems connect to external data sources and tools. The canonical analogy: MCP is the USB-C port for AI — a universal connector replacing the proliferation of bespoke, one-off integrations with a single protocol any AI application can implement.

## The problem MCP solves

Before MCP, every data source an agent needed to reach required a custom integration. Connecting one agent to a code host, a chat tool, a file store, and a database meant four separate, incompatible implementations. MCP replaces this many-to-many integration problem with a many-plus-many one: each data source implements one MCP server; each AI tool implements one MCP client. The combinatorics collapse.

## Architecture

MCP follows a client-server model with five components:

| Component | Role |
|---|---|
| MCP Host | The AI application that wants to access data (an IDE, a desktop app, a custom agent) |
| MCP Client | The protocol client embedded in the host; holds a 1:1 connection to a single server |
| MCP Server | A lightweight program exposing specific capabilities via the standardized interface |
| Local Data Sources | Files, databases, services on the host machine that servers can securely access |
| Remote Services | External APIs and cloud services servers connect to on the host's behalf |

A single host can connect to many servers at once, each exposing a different system.

## What servers expose

Three capability types: **resources** (data the model can read — files, records, API responses), **tools** (functions the model can invoke to take actions or query systems), and **prompts** (reusable, parameterizable prompt templates and workflows).

MCP is a foundational piece of the [[AI Agents]] infrastructure stack — it is the preferred integration approach for the base "agent that calls tools" pattern. An agent that can reach any MCP server gains access to a growing ecosystem of pre-built integrations without custom code for each one.

## Ecosystem state

The protocol crossed from "promising standard" to genuine infrastructure quickly. Governance transferred to a neutral, multi-vendor foundation, with major model providers and cloud vendors as founding members alongside Anthropic — meaningful because it signals durability beyond any single company's roadmap. SDKs exist in multiple languages; broad client adoption spans coding assistants, IDEs, and general-purpose chat apps. The many-to-many integration problem is, for practical purposes, solved at the protocol layer.

## Where MCP is still rough

The protocol is mature; the *ecosystem* quality is not, and the distinction matters for anyone using MCP in production. Independent security scans of the open-source server ecosystem consistently find: the large majority of servers require credentials, most rely on static long-lived keys with no rotation policy, only a small fraction implement modern OAuth-style auth, and most store API keys directly in environment variables. There is no trusted curation layer between the long tail of low-quality servers and a connecting agent — no equivalent of a vetted-package registry, no default rotation discipline across most of the ecosystem.

The security surface is the load-bearing risk. Every server an agent connects to is a new attack surface. A "confused deputy" pattern — a server acting on a request without verifying which agent or user actually issued it — is common in the current state. Prompt injection against an MCP-enabled agent can lead to arbitrary code execution, credential theft, or supply-chain compromise; attack success rates against unguarded MCP-enabled agents have been measured in the range of 80%+ in adversarial testing. See [[Agent Failure Modes]] for the taxonomy this sits inside.

## When to use MCP vs. alternatives

| If… | Use… | Why |
|---|---|---|
| A personal agent needs filesystem, git, or terminal access | MCP via a local server | The canonical use case |
| Composing multiple agentic tools across vendors | Direct process composition for now; MCP cross-vendor routing is maturing | Cross-vendor MCP composition is still early tooling |
| A single one-off capability call | A direct API call | MCP adds protocol overhead for no benefit on a single call |
| Enterprise multi-agent integration needing auth and audit | MCP with a vetted private registry | Vetting is mandatory — treating the public ecosystem as trusted is where most pilots fail |
| Exposing your own service for AI consumption | Build an MCP server | The standard wins the integration |

The practitioner distinction worth holding onto: "use MCP" is a different recommendation from "use any MCP server you find." For personal use, vet each server individually before connecting it. For anything higher-stakes, build or use a private, audited registry — the public long tail is a security risk wearing a developer-experience costume.

## Boundary conditions

MCP is not a security boundary — a standardized message format says nothing about the trust level of the code on the other end of the connection. MCP is also not a coordination layer *between* agents (that is a separate problem space); conflating the two produces designs that solve neither well. And MCP is not a substitute for a direct API call when there's no agent loop involved — a single capability call routed through an MCP server pays protocol overhead for no gain.

## Related

- [[AI Agents]]
- [[Agent Orchestration]]
- [[Agent Failure Modes]]
- [[Multi-Agent Systems]]
- [[Sub-agents and Agent Teams]]
- [[The Harness Is the Product]]
