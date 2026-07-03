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
  - agent orchestration
  - agentic orchestration
  - Orchestrator and specialists
---

# Agent Orchestration

Agent orchestration is the discipline of coordinating one or more [[AI Agents]] — and their underlying model calls, tool invocations, and state — so they collectively accomplish a complex task. As agent capabilities mature, orchestration skill becomes the scarce, high-leverage competency: not the ability to do the task, but the ability to design the loop that gets it done reliably.

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

## The load-bearing move

Every orchestration topology answers the same architectural question: **where does the human have to be, and where can the system operate without them?** Single-agent designs put the human at the prompt level — every turn requires input. Manager patterns put the human at the manager level, conversing with one centralized agent. Decentralized handoff patterns put the human at the topology-design level: they chose the routing, but execution flows between specialists without them. Reading across these, the progression is *increasing human autonomy from the operational loop*. Each topology relocates the human's attention to a less granular level of the system. Identify where you can afford to be the bottleneck, and pick the topology that puts you there — treating the agents as the design variable when your own attention is the constraint produces architectures that look elegant on paper and run at the speed of your availability in practice.

This is the orchestration-layer specialization of [[The Harness Is the Product]]'s broader claim: the harness is what allocates a human's attention across the system, and orchestration is the row that decides at what altitude that allocation happens.

## The agent loop as foundation

All orchestration patterns rest on the same primitive: a *run loop*. An agent receives input (a message, prior tool results, memory), produces a response or tool call, executes the tool, receives the result, and iterates until an exit condition is met. Orchestration sophistication lies in how these loops are composed, nested, and coordinated. See [[OODA Loop]] for the general observe-orient-decide-act shape this specializes.

## Single-agent orchestration

The default starting point: one model with a well-chosen tool set and clear instructions handles a workflow end-to-end. Easier to evaluate, debug, and maintain than any multi-agent alternative. Key mechanisms: parameterized prompt templates instead of dozens of near-duplicate prompts, incremental tool addition (expand capability by adding tools before splitting into agents), and explicit exit conditions (a final-output signal, a response with no further tool call, an error state, a max-turn limit) — unbounded loops are a common failure mode without one.

## Multi-agent orchestration patterns

**Manager pattern (hierarchical)** — a central agent coordinates specialized sub-agents by calling them as tools, retains context, and synthesizes their results into one coherent response. Best for a single user-facing experience backed by specialized capabilities on demand.

**Decentralized pattern (peer handoffs)** — agents operate as peers; when one determines another is better suited, it performs a one-way handoff of execution and state, and steps out. A common shape is a triage agent at the entry point routing to specialists without central coordination. Best when task separation is clean and no central synthesis is needed.

**Declarative vs. code-first graphs** — some frameworks require the whole agent graph to be pre-defined declaratively (visual clarity, cumbersome as workflows grow dynamic); code-first frameworks express orchestration logic directly in code, enabling more adaptive workflows.

## The General-Soldier pattern

A pattern that emerged for personal AI systems spanning multiple projects, addressing *context bleed* — one project's constraints and vocabulary leaking into another, compounding as the system accumulates more context. A root instruction file (the General) defines identity, values, and system-wide conventions; per-project instruction files (the Soldiers) define project-specific goals, constraints, and past decisions. Each Soldier operates with isolated context: the General's character, without cross-contamination from other active projects. Multiple independent builders converged on nearly identical implementations without coordinating — convergent independent discovery in a fast-moving field is strong evidence the pattern is robust, and it isn't tied to any one framework; it works wherever instruction files can be scoped hierarchically. [[Agent Skills]] sit within the Soldier layer as callable, versioned procedures rather than re-derived instructions.

## Workflow vs. agent distinction

A **workflow** is an LLM and tools orchestrated through predefined code paths — predictable, lower risk. An **agent** dynamically directs its own process and tool use — more flexible, higher latency and cost, needing more guardrails. This is a spectrum, not a binary; most production systems are hybrid. A newer move collapses the binary from the other direction: rather than a human pre-writing the workflow code, the model writes the deterministic orchestration script at runtime — fan-out, conditionals, verification loops — then executes it outside the conversation. You get predefined-code-path predictability *and* agentic adaptivity, because the agent authored the code path. See [[Sub-agents and Agent Teams]] for the concrete feature.

## Choosing a pattern

| If… | Use… |
|---|---|
| Single coherent task, low coordination overhead is the priority | Single-agent orchestration |
| Specialized capabilities behind one user-facing experience, synthesis needed | Manager pattern |
| Clean task separation, no synthesis needed | Decentralized handoffs |
| Long-running personal work across projects, protecting against context bleed | General-Soldier split |
| Task decomposes into independent, bounded sub-tasks whose outputs merge cleanly | [[Multi-Agent Systems\|multi-agent dispatch]] |
| Coherence across output matters more than parallelism speed | Single-threaded with strong [[Context Engineering]] |

The diagnostic shortcut: **your attention is the constraint; pick the topology that puts it at the altitude you can sustain.** Someone who can spend two hours a day on agent work picks differently than someone who can spend thirty minutes — not because the work differs, but because the bottleneck does.

## Failure modes per pattern

Each pattern has a characteristic failure mode, catalogued in depth at [[Agent Failure Modes]]: single-agent tool-set growth past ~15–20 capabilities fragments decisions; manager-pattern context budgets overflow and synthesis degrades; decentralized handoffs lose state between agents unless payloads are explicit; General-Soldier instructions leak between layers without periodic audit; multi-agent dispatch hits the *Flappy Bird problem* when sub-tasks weren't actually independent (full diagnostic in [[Multi-Agent Systems]]).

## Related

- [[The Harness Is the Product]] — the synthesis spine this page's patterns are components of
- [[Sub-agents and Agent Teams]] — the concrete implementation these abstract topologies instantiate
- [[Multi-Agent Systems]] — the architectural pattern developed in full depth: token economics, failure modes, boundary conditions
- [[Agent Failure Modes]] — the per-pattern failure modes mapped above, at full depth
- [[AI Agents]] — the conceptual foundations these topologies coordinate
- [[OODA Loop]] — the general loop shape single-agent orchestration specializes
