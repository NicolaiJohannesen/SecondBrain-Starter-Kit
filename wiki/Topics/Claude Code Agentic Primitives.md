---
type: topic
created: 2026-07-02
updated: 2026-07-02
version: 1
origin: kit-seed
tags:
  - topic
  - seed
  - domain/ai
aliases:
  - /goal
  - /loop
  - Claude Code Routines
  - Routines
  - Claude Code scheduling
  - Scheduled tasks
  - Keep Claude working
  - Autonomous session primitives
  - Stop hook
---

# Claude Code Agentic Primitives

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

The native mechanisms Claude Code gives you to make work run **without prompting each step**, and the decision rules for which one to reach for. This is the *mechanics* layer that [[Loop Engineering]] (the discipline) is built on: Loop Engineering says build the loop so the human stays at the judgment layer; this page documents the actual loops the CLI ships with.

## The one question that picks the primitive

Every one of these mechanisms keeps work going without you typing the next prompt. They differ on three axes, and the answers pick the tool:

1. **What starts the next unit of work?** — a *condition being unmet* (`/goal`), a *time interval* (`/loop`, Routines, Desktop tasks), or an *external event* (Routines via GitHub/API).
2. **Does it need to survive the session — or the machine — closing?** — in-session (`/goal`, `/loop`) vs. durable (Routines = cloud, Desktop tasks = local daemon).
3. **Does it need your local files?** — local execution (`/loop`, Desktop tasks) vs. a fresh cloud clone (Routines).

## `/goal` — work until a condition holds

`/goal <condition>` sets a completion condition and Claude keeps taking turns until the condition is met, without you prompting each step. After every turn a small fast evaluator model reads the condition and the conversation and returns yes/no plus a short reason. "No" → Claude takes another turn. "Yes" → the goal clears itself.

**The load-bearing insight — the evaluator cannot call tools.** It judges only what Claude has already surfaced in the conversation. This dictates how you write the condition: write it as something Claude's own output can *demonstrate in the transcript*. "All tests in the auth suite pass" works, because the test run lands in the transcript. "The code is bug-free" doesn't, because nothing in the transcript can prove it. A condition that survives many turns has one measurable end state, a stated check for how Claude proves it, and any constraints that must hold. To bound runaway sessions, put a turn or time clause in the condition itself — "...or stop after 20 turns."

`/goal` is a wrapper around a session-scoped prompt-based Stop hook. If you need custom evaluation logic (a deterministic script rather than a model judgment), a hand-written Stop hook is the underlying machinery `/goal` is a shortcut over.

## `/loop` — re-run on an interval

`/loop` re-runs a prompt on repeat while the session stays open, in three modes:

| What you provide | Behavior |
|---|---|
| Interval **and** prompt | Runs your prompt on a fixed cadence |
| Prompt only | Claude picks the interval dynamically each iteration based on what it saw |
| Nothing | Runs a built-in maintenance prompt (or a project-defined default) at a dynamic interval |

**Key distinction from `/goal`**: `/loop` fires on a clock; `/goal` fires on the previous turn finishing, gated by a condition. `/loop` stops when you press escape, when a time limit elapses, or — in dynamic mode — when Claude judges the work provably complete. One-time reminders don't need `/loop` at all — plain language like "remind me in an hour to check the deploy" schedules a single self-deleting task.

**The session constraint**: `/loop` tasks only fire while the session is running and idle. Closing the terminal stops them, unless the session is backgrounded to keep it alive without a visible terminal.

## The three-tier scheduling comparison

When work must run unattended — beyond an open session — there are three durable options:

| | Cloud (Routines) | Desktop scheduled task | `/loop` |
|---|---|---|---|
| Runs on | Managed cloud | Your machine | Your machine |
| Machine must be on | No | Yes | Yes |
| Open session required | No | No | Yes |
| Local file access | No (fresh clone) | Yes | Yes |
| Minimum interval | 1 hour | 1 minute | 1 minute |

Rule of thumb: cloud for work that must run reliably without your machine; a local scheduled task when it needs local files and tools; `/loop` for quick polling inside a session.

## Routines — cloud autopilot

A routine is a saved configuration — a prompt, one or more repos, an environment, and connectors — that runs on managed cloud infrastructure, so it keeps working when your machine is closed. Each routine takes one or more triggers: **scheduled** (hourly/daily/weekly presets or custom cron, one-hour minimum interval), **API** (a per-routine endpoint you can call from other tools), or **event-driven** (reacting to events on a connected repository). Each run is a full autonomous cloud session with no permission prompts; repos are cloned fresh each run.

A green run status means the session started and exited cleanly — **not** that the task succeeded. Failures surface inside the transcript, not the status dot; open the run to confirm. This is the same discipline that applies everywhere in agent work: the status is the claim, the transcript is the evidence.

## Practitioner patterns from the field

- **The goal-style primitive tends to be the more reliable of the two**, and can run for multiple days on a bounded, verifiable task — for example, building parsers for a large set of documents across many sites. The insight that makes a long goal work is always the same: the task must be bounded and objectively checkable.
- **The goal pattern is a harness convention, not one vendor's trick.** It's the harness-native version of an older manual technique — repeatedly re-running the same prompt to keep an agent grinding on a problem — now built into the tool instead of a hand-rolled script.
- **Interval loops are also useful for open-ended exploration, not just polling.** A distinct field use: run a broad open-ended question on an interval and let the model explore directions you wouldn't have picked yourself — treating it like handing a problem to an ambitious junior collaborator and seeing what comes back.
- **Autonomy is a dial, not a switch.** A loop doesn't need to go end-to-end; have it draft an email or a change without taking the final irreversible action. That's the same draft-not-send discipline described in [[Loop Engineering]].

## Choosing a primitive for your own loops

Match the mechanism to the shape of the task: a bounded, multi-turn job with a checkable end state ("every inbox file is processed and filed") fits a goal-style condition — write the condition against something the transcript can prove, and add an "or stop after N turns" clause. Recurring interval work (a daily scan, a weekly regeneration pass) fits a scheduled loop. Anything that must not depend on a terminal staying open belongs on a durable, cloud-style schedule instead of an in-session one — the trade is no local-file access and typically a one-hour floor on frequency.

## Related
- [[Loop Engineering]] — the discipline these mechanics are built to serve
- [[Sub-agents and Agent Teams]] — the parallel-dispatch surface these primitives can trigger
- [[The Harness Is the Product]] — where scheduling primitives sit in the larger picture of what makes an agent setup durable
- [[Agent Orchestration]] — coordinating multiple agents once a loop is running
- [[Feedback Loops (Universal Pattern)]] — the general pattern these mechanics instantiate
