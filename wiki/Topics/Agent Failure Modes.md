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
  - Agent failures
  - Failure mode taxonomy
  - Prompt injection
  - Sub-agent runaway
  - Token budget runaway
  - MCP security
  - YOLO mode failure
---

# Agent Failure Modes

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

A capable model in a weak harness fails in specific, repeatable, named ways. Most of those failure modes do not look like errors. They look like the agent working — tokens flowing, tools firing, outputs accumulating — while the actual work degrades silently. By the time something visibly breaks, the cause is several steps back in a chain nobody traced. The central operational fact about agents in production: **the failure modes that matter are the ones that don't trigger alarms.**

## The hierarchy of failure

Ordered by invisibility-to-monitoring rather than frequency. The first five are silent; the rest trigger something detectable, often after the damage is done.

| # | Failure mode | Visibility | Structural fix lives in |
|---|---|---|---|
| 1 | Prompt injection from untrusted content | Silent until exploitation | Permission scoping, sandboxing |
| 2 | Silent tool-call failures, error compounding | Silent (looks like hallucination) | Verification gates |
| 3 | Context rot at session length | Silent (looks like degraded quality) | [[Context Engineering]] |
| 4 | Multi-agent decision incoherence | Silent until integration | Coordination discipline |
| 5 | Tool bypass (agent fabricates instead of calling) | Silent (looks plausible) | Tool description design |
| 6 | Sub-agent runaway spawning | Visible in token usage | Effort-scaling heuristics |
| 7 | Memory loss at context-window limits | Visible after the loss | State persistence |
| 8 | Token-budget runaway in autonomous loops | Visible in spend | Cost attribution, circuit breakers |
| 9 | Infinite tool-call loops | Visible after timeout | Iteration caps |
| 10 | Directory-relative path failures | Visible (error messages) | Tool interface constraints |
| 11 | MCP supply-chain attacks | Visible after compromise | Server vetting, least privilege |
| 12 | Hallucination in production | Visible when users notice | Confidence stratification |

## Five load-bearing specifics

**Prompt injection compounds with capability.** Independent research testing coding assistants in maximum-privilege configurations found attack success rates as high as 80%+ against agents with shell and filesystem access, versus far lower rates against safeguarded systems. The attack surface is not the model; it is the harness's permission scoping. Teams that harden CI/CD while leaving development agents wide open have inverted their risk posture.

**Silent errors compound multiplicatively.** At 95% per-step reliability, three sequential tool calls yield ~86% end-to-end success. At twenty steps: ~36%. A documented production case: an agent created hundreds of duplicate records before anyone noticed a retry loop — each individual write succeeded; the failure was at a level the success signal never reached.

**Context rot degrades continuously, not at a cliff.** As token count grows, recall accuracy drops smoothly rather than suddenly — the model doesn't crash, it gives plausible-looking wrong answers. Task-duration research shows agent success rates decay exponentially with elapsed time, each agent having a rough "half-life" past which reliability falls below 50%. See [[Context Engineering]] for the mechanism and the mitigations (compaction, structured notes, sub-agent isolation).

**Token-budget runaway looks identical to productive work from the outside.** A session sending full history on every step creates accumulation costs proportional to step-count squared, not step-count. Multiple documented incidents describe unattended agent loops burning thousands of dollars overnight — invisible until the invoice arrives, because tool calls and outputs kept flowing the whole time.

**MCP servers are an underregulated attack surface.** Independent scans of the open-source Model Context Protocol server ecosystem found the large majority requiring credentials, most relying on static long-lived keys with no rotation, and only a small fraction implementing modern auth. See [[Model Context Protocol (MCP)]] for the protocol-level detail.

## Structural fixes, not vigilance

None of these are solved by "being more careful." Each has a fix that lives at the harness or tool-interface layer: sandboxed execution, absolute-path enforcement, iteration ceilings, per-session token budgets with circuit breakers, and verification gates between pipeline steps. [[The Harness Is the Product]] is the frame for why the fix belongs there rather than in the prompt. [[Verification Discipline and Assertion Types]] covers the gate discipline that catches silent tool-call failures before they compound.

## Boundary conditions

This taxonomy is not exhaustive — new failure modes surface as agents take on new task classes. Some interact: context rot, silent tool failures, and sub-agent runaway can combine in one long session into a confident, expensive, wrong answer. The specific numbers cited here are period snapshots; the mechanisms persist longer than the statistics.

## Related

- [[The Harness Is the Product]]
- [[Context Engineering]]
- [[Multi-Agent Systems]]
- [[Model Context Protocol (MCP)]]
- [[Verification Discipline and Assertion Types]]
- [[Feedback Loops (Universal Pattern)]]
