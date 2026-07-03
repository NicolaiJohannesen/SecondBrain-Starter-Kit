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
  - Claude Agent Skills
  - Claude Skills
  - SKILL.md
  - Skills architecture
  - Progressive disclosure (Skills)
  - Three-tier loading
  - Custom Skills
  - Pre-built Skills
---

# Agent Skills

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

**Folder-based packaged capabilities that an agent discovers and loads progressively, turning a general-purpose agent into a specialist for a specific task — without paying token costs for content the task doesn't need.**

## What they are

A Skill is a directory containing one required file (`SKILL.md`) and optional supplementary materials — other markdown docs, scripts, reference data. The agent reads the directory the way a new team member reads an onboarding folder: skim the title page first, dive deeper only when relevant.

Anthropic ships pre-built Skills (spreadsheet, document, and presentation handling; an API reference), and anyone can author custom ones — this kit ships several under `.claude/skills/`.

## The load-bearing design — three-tier progressive disclosure

This is the architectural insight that makes the format work. Skills load in three stages, each with a different token cost:

| Level | When loaded | Cost | What it contains |
|-------|-------------|------|------------------|
| **1. Metadata** | Always (system prompt at startup) | ~100 tokens per skill | YAML frontmatter — `name` and `description` only |
| **2. SKILL.md body** | When the Skill is triggered | <5K tokens | Full instructions, workflows, best practices |
| **3. Bundled files** | As referenced during the task | Effectively unlimited | Other markdown, scripts (run via bash — code never enters context), reference data |

The consequence: **you can install many Skills without a context penalty**, because the agent only knows each Skill exists and roughly when to use it. Bundled files — scripts, large reference docs, schemas — are read only when the task actually needs them. This is the same design pattern behind [[Context Engineering]]: reduce the cost of *not* loading information a given turn doesn't need.

## SKILL.md format

```yaml
---
name: my-skill-name
description: What this skill does AND when it should be used
---

# Skill Name

## Instructions
Step-by-step guidance.

## Examples
Concrete examples.
```

**Constraints:** `name` is lowercase letters, numbers, and hyphens only (max 64 characters, no reserved vendor words); `description` is non-empty, max 1024 characters, and should specify *both* what the Skill does *and* when it should be invoked — it's what the agent reads at decision time to decide whether to load it.

## Where Skills live

The location depends on the surface. In a CLI coding agent, a personal Skill lives in a per-user directory shared across every project; a project Skill lives inside the repo (`.claude/skills/<name>/SKILL.md`, in this kit's case) and travels with it via version control — anyone who clones the project gets the Skill. Hosted chat and API surfaces have their own upload paths and do not automatically share Skills with the CLI. A workflow worth writing once should usually live in the filesystem-based form so it can be versioned and shared via git.

## How they compare to other agent capabilities

| Capability | Where it lives | What it's for |
|---|---|---|
| **Skills** | Filesystem folders + SKILL.md | Reusable workflows the agent auto-discovers and loads progressively |
| **Slash commands** | `.claude/commands/<name>.md` | User-invoked actions — manually triggered, not auto-discovered |
| **MCP servers** | External processes ([[Model Context Protocol (MCP)]]) | Connect the agent to external tools over a wire protocol |
| **Sub-agents** | Markdown files describing role + tool access | Spawned mid-conversation to handle specific subtasks — see [[Sub-agents and Agent Teams]] |

Skills and slash commands are the closest pair — both filesystem-based. The difference: a Skill loads automatically when the agent judges it relevant; a slash command runs only when explicitly typed. Slash commands are deliberate; Skills are reactive.

## Authoring best practices

- **The description is the trigger.** It must specify both what the Skill does and when to use it. A vague description means the agent either over-invokes (wasting context) or under-invokes (dead weight).
- **Default to a short SKILL.md.** Push detail into bundled reference files, read on demand.
- **Use scripts for deterministic operations.** A script that always returns the same output for the same input beats asking the model to compute the equivalent in its head, and the script's code never enters context.
- **Test with representative tasks.** Iterate on the description until the agent triggers in the right cases and skips the wrong ones.
- **Audit before installing untrusted Skills.** A Skill is code that runs in your session — treat installation like installing software, not reading a document.

## Boundary conditions

- **Skills are not portable across surfaces** without separate installation on each, and network access varies — full in a CLI environment, restricted or absent inside sandboxed API execution.
- **Pre-installed packages on a hosted execution surface can't be extended at runtime** — check the platform's docs for what's available.

## Related

- [[Context Engineering]] — the general discipline Skills' progressive disclosure instantiates at the workflow layer
- [[Loop Engineering]] — a Skill is often the packaged, reusable form of a loop worth running repeatedly
- [[Claude Code Agentic Primitives]] — Skills as one of the primitives alongside sub-agents, hooks, and slash commands
- [[Sub-agents and Agent Teams]] — the adjacent primitive for delegated execution rather than instruction-loading
- [[The Harness Is the Product]] — Skills are part of the persistent harness layer where improvements accumulate across sessions
