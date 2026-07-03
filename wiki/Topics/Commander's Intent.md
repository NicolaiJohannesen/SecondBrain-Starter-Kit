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
  - domain/military
aliases:
  - Mission Command
  - Auftragstaktik
  - Mission-type tactics
  - Intent-Based Leadership
  - Leader-Leader Model
  - Empowered Execution
  - Disciplined Initiative
  - Specify outcomes not processes
  - Northstar
  - North Star
---

# Commander's Intent

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

A 150-year-old military doctrine that solves a permanent coordination problem, and — it turns out — the same primitive that keeps an AI agent from drifting off task. **Centralized, detailed instruction fails under complexity because information degrades and speed matters more than precision.** The fix: state clearly *what success looks like* and *why*, instead of specifying *how* to get there — then trust whoever (or whatever) is closest to the situation to find the method.

## The military origin

The doctrine's German name is *Auftragstaktik* ("mission-type tactics"); the modern US Army term is **Mission Command**. It emerged from humiliation: in 1806 Napoleon destroyed the Prussian army at Jena because Prussian officers required detailed orders from superiors before acting, and froze when communications broke down. The Prussian Reform Movement that followed — led by Gerhard von Scharnhorst and later codified by Helmuth von Moltke the Elder — rebuilt officer culture around the *denkender Soldat*, "the thinking soldier": every officer should understand intent well enough to act without further orders.

Current US Army doctrine (ADP 6-0) defines **Commander's Intent** with three parts:

1. **Purpose** — why the operation matters
2. **Key Tasks** — the few activities critical enough to constrain execution (not an exhaustive task list)
3. **End State** — what success looks like when it's over

The explicit design goal: subordinates should be able to act competently in the *absence* of new orders, because they understand intent well enough to improvise toward it. Moltke's own summary of why this must be so is the most famous line in the doctrine, usually compressed to "no plan survives contact with the enemy" — the fuller, verified original: *"No plan of operations extends with any certainty beyond the first encounter with the main enemy forces."* The plan's value is the preparation it enables, not the instructions themselves.

## Two civilian rediscoveries

The pattern keeps getting rediscovered outside the military because the underlying trade-off — coordination vs. adaptation under incomplete information — reappears anywhere a principal cannot be present for every decision.

**Stanley McChrystal**, commanding a counter-terrorism task force that was structurally too slow against a faster, distributed adversary, built *Shared Consciousness* (extreme information transparency) and *Empowered Execution* (decision authority pushed to whoever had the best local information) — documented in *Team of Teams* (2015).

**David Marquet**, given command of the US Navy's worst-performing submarine, replaced the traditional leader-follower model with a **Leader-Leader** model: sailors were trained to say "I intend to..." instead of "Request permission to..." — forcing active ownership of decisions instead of passive deference. The submarine went from worst to first in the fleet.

Both are the same primitive as the military doctrine: specify the end state and the why; delegate the how; make the delegation safe by building real trust and real competence underneath it, not just issuing the words.

## The AI-agent application

The same primitive is the fix for the most common failure mode in agent work: **drift**. An agent given a vague or purely procedural instruction will optimize the nearest measurable local proxy — "make the code compile" instead of "build something reliable" — because the proxy is easier to verify than the actual goal. A persistent, explicit statement of intent interrupts this by giving the agent something to check its own actions against at every step: *does this action still serve the stated end state?*

This is exactly what a **Northstar** is for an agent system: a short, explicit statement of what the system is *for*, checked against at decision points, that survives when the specific plan doesn't. See [NORTHSTAR.md](../../NORTHSTAR.md) for this kit's own worked Northstar — it is this page's military concept applied to a second brain. The mapping is direct: Purpose and End State are the Northstar's job; Key Tasks are the constraints an agent should treat as non-negotiable even while improvising everything else.

## The adversarial check — doer and checker as separate agents

Commander's Intent solves *drift*; it does not by itself solve *hallucination* or *blind spots* — a single agent executing toward an intent can still be confidently wrong, because its errors live inside its own reasoning chain and its own re-reading of its own work rarely catches them. The structural fix, familiar from generative adversarial networks: run a second, independent agent whose only job is to find what's wrong with the first agent's output, with no stake in how it was produced. The checker's value comes specifically from sitting *outside* the executor's reasoning chain — the same reason a second pair of eyes catches an editing mistake the author reread past five times. Doer and checker must be genuinely separate; an agent "reviewing its own work" just re-runs the same chain and re-confirms the same blind spot.

## Related

- [[Feedback Loops (Universal Pattern)]] — the executor/checker cycle is a reinforcing loop; intent is the attractor that keeps it from drifting
- [[Agent Orchestration]] — the practical architecture for splitting work across an intent-holding coordinator and executing sub-agents
- [[Sub-agents and Agent Teams]] — doer/checker as a concrete sub-agent pairing
- [[Multi-Agent Systems]] — Commander's Intent as the coordination primitive that lets many agents act coherently without a bottleneck at the center
- [[Verification Discipline and Assertion Types]] — the disciplined version of "checking the output," for claims rather than actions
- [[Agent Failure Modes]] — drift and unchecked hallucination as the two failure modes this page's two halves each address
