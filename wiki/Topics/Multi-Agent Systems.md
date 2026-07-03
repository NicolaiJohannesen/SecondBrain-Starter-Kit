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
  - Multi-agent architecture
  - Agent teams
  - Multi-agent orchestration
  - Flappy Bird problem
  - Cognition multi-agent critique
  - Anthropic multi-agent research system
---

# Multi-Agent Systems

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

The default should be one agent. Two of the most credible engineering teams in the field spent a year converging on this point from opposite directions: *most tasks people reach for multi-agent architectures to solve do not actually require multi-agent architectures.* The question this page answers is the narrower, sharper one: **when does multi-agent actually pay off, and what is the cost when it doesn't.**

Multi-agent is an architectural choice with a measurable token cost — Anthropic's published figure is roughly 15× the token consumption of a single-call exchange, against roughly 4× for a single agent looping on its own. The decision isn't "should I be sophisticated and use multiple agents?" It's "does this task clear a 15× cost threshold *and* decompose in a way multi-agent can exploit?" Most tasks fail one of those two filters. The ones that pass produce gains nothing else matches.

## Vocabulary cleanup

Three terms get conflated, and the conflation hides real distinctions:

- **Sub-agent** — a child agent dispatched by a parent within a single platform's harness, returning a distilled result. The parent keeps running; the child runs in isolation with its own context window and cannot recursively spawn further children. See [[Sub-agents and Agent Teams]].
- **Multi-agent system** — the architectural pattern where multiple agent instances coordinate on one task, whether same model or different, same machine or across, sharing state or only return-values. Sub-agents are one shape of this. Handoff-based frameworks, agent-to-agent protocols, and isolated-VM coordinator patterns are others — different shapes, and the differences matter.
- **Agent orchestration** — the coordination topology (manager / decentralized / handoff / parallel-merge) chosen when building a multi-agent system. See [[Agent Orchestration]]. Orchestration is *part of* multi-agent design, not a synonym for it.

Collapsing these three terms is what makes "multi-agent gives a 90% gain" and "don't build multi-agents" read as a contradiction. They aren't contradicting each other — they're describing different task classes with different coordination shapes.

## When multi-agent wins

Anthropic published a detailed account of its multi-agent research system in 2025. The architecture: one lead agent plans the work and dispatches 3–5 sub-agents in parallel, each with a clean context window, a non-overlapping objective, and a defined tool set. Each reports back; the lead synthesizes. On internal research evaluations, this beat a single strong agent by roughly 90%, at roughly 15× the token cost of a single chat interaction.

What made the 15× pay off was harness discipline, not the multi-agent shape alone:

1. **Effort-scaling heuristics** in the lead agent's instructions — without them, lead agents spawned 50+ sub-agents for simple queries. A calibration (simple fact-finding → one sub-agent; complex research → ten-plus with divided responsibilities) kept sub-agent count tracking task complexity.
2. **Parallel tool calling** inside sub-agents plus parallel sub-agent dispatch — up to a 90% reduction in research time.
3. **A dedicated tool-description-rewriting sub-agent** that tested downstream tools on real queries and rewrote their descriptions to prevent observed failures — the single highest-ROI intervention, roughly 40% faster downstream completion, with no model change.
4. **Memory checkpointing** before the context window neared its limit, so new sub-agents could spawn clean when needed.

The task property that made it work: the research decomposed cleanly into independent searches. A sub-agent looking for X doesn't need to know what a parallel sub-agent looking for Y found — the return values merge without renegotiating shared context.

## When multi-agent breaks

A separate widely-read engineering post argued forcefully against the architecture for coding work. Its central claim: **dispersed decision-making produces incompatible implicit decisions that cannot be reconciled after the fact.** The canonical illustration — the *Flappy Bird problem* — has a user ask an agent to build a simple game clone; sub-agents dispatched in parallel to build the background and the sprite each produce internally consistent but mutually mismatched pieces, with no way to reconcile them without redoing the work.

The deeper principle: a system should feel like a single continuous decision-maker, because coding work is full of implicit decisions — naming, layout, error-handling style — that propagate constraints across the whole output. A single thread concentrates those decisions where they stay consistent; dispersed threads make them independently and drift. The prescribed fix was single-threaded agents with sophisticated context compression, not more agents.

## The reconciliation

The same team that argued against multi-agent later shipped a coordinator-plus-isolated-worker architecture of their own — scoping work into bounded pieces, assigning each to a fully isolated environment, then compiling the results. This isn't a reversal. It's the specific pattern their critique was never about: **bounded** sub-tasks (scope fully specified before dispatch, no implicit decisions left to conflict) run in **isolated** environments (conflicts surface at merge time, not as silent drift). The Anthropic position and the Cognition-style position aren't opposed architecturally — they're opposed at the task-class level. Parallelize what genuinely decomposes; centralize what requires coherence.

## The diagnostic

> **Does this task decompose into independent, bounded sub-tasks whose return values can be merged without renegotiating shared context?**

If yes, multi-agent wins — parallel literature searches, parallel verification passes on separate claims, parallel file-by-file refactors where each file is self-contained. If no, single-thread plus strong [[Context Engineering]] wins — a single coherent piece of writing, a bug spanning multiple components, an API where cross-endpoint consistency matters. This is mechanical, not a vibe check: trace the dependency. If a sub-task's output is correct only conditional on another sub-task's output it cannot see, they are coupled, and parallelizing corrupts the result.

A paired-verification setup — one agent argues for a claim, another argues against, a synthesizer reads both — is multi-agent done right: neither sub-agent's output depends on seeing the other's, so the decomposition is genuinely clean. See [[Verification Discipline and Assertion Types]].

## Token economics

The 15× multiplier is real. A single autonomous multi-agent run on a meaningful question can consume hundreds of thousands of tokens; an hour-long unmonitored loop can produce a large, unexpected bill. It pays off when task value clears the threshold by a comfortable margin, the task is high-leverage or high-stakes, single-agent attempts have measurably hit a quality ceiling, and the harness moves above are in place. It doesn't pay off when a single agent with good context engineering would do, when the task admits no clean decomposition, or when cost discipline — budgets, circuit breakers, attribution — is absent.

## Failure modes specific to multi-agent

Implicit decision conflicts (Flappy Bird); sub-agent runaway spawning without effort-scaling heuristics; coordination overhead exceeding the parallelism gain on highly-coupled tasks; silent error compounding (a 3–15% per-call tool-failure rate multiplies across parallel sub-agents); memory-checkpoint loss at the context boundary; token-budget runaway compounding with per-step inefficiency. Each has a structural fix in the harness, not the model — see [[Agent Failure Modes]].

## Related

- [[The Harness Is the Product]] — the spine; multi-agent is one architectural choice within the harness
- [[Agent Orchestration]] — coordination topologies this page's architectures instantiate
- [[Sub-agents and Agent Teams]] — one concrete implementation of multi-agent
- [[Context Engineering]] — the discipline that makes single-thread alternatives viable, and makes multi-agent return values mergeable
- [[Verification Discipline and Assertion Types]] — paired-agent dispatch as multi-agent done right
- [[Agent Failure Modes]] — the full failure taxonomy, mapped to harness-level fixes
