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
  - Loop Engineering
  - Agent Loops
  - Loop-Engineered Operating System
  - Engineering the Loop
---

# Loop Engineering

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

The discipline of building the **autonomous loops that let work run itself**, so the human stays at the *judgment* layer instead of doing the work each time. The shift: you stop prompting the model turn-by-turn and start writing the loops that run the system. The harness — not any single prompt — becomes the product (see [[The Harness Is the Product]]).

## What a loop is made of

A loop is a repeatable unit of work the system runs without a human in the inner cycle. The building blocks (their concrete mechanics are catalogued in [[Claude Code Agentic Primitives]]):

- **Scheduled agents** — work that fires on a timer rather than on a human prompt.
- **Verifier / maker-checker sub-agents** — a second agent checks the first's output against an objective gate, so quality doesn't depend on the maker being right (see [[Multi-Agent Systems]]).
- **Skills** — versioned, callable workflows (the operational layer described in [[Personal Context Layer]]) so a procedure isn't re-derived each session.
- **Persistent-state substrate** — the [[Personal Context Layer]] a loop reads from and writes back to, so knowledge compounds across runs.
- **Hooks and objective gates** — automated checks (tests, linters, predicates) that pass or fail a step deterministically, replacing human review on the routine cases.

The human's remaining job is the irreducible part: set the direction, make the calls the gate can't, and curate what the loop feeds on.

## The autonomy spectrum — loops are not one thing

Loops span a spectrum of autonomy and complexity, not a single shape. Placing a task on the spectrum tells you which mechanism to build:

1. **Research-frontier** — experiment-driven systems that try, measure, and keep what works. Highest autonomy, least predictable.
2. **Bounded multi-day goals** — a single verifiable objective the system grinds toward for hours or days. Reliable *because* the end state is checkable.
3. **Interval exploration / polling** — re-running a task on a schedule, either polling a known state or running a broad open-ended question to explore directions you wouldn't have picked.
4. **Daily minutia automations** — the low end: inbox triage, doc generation, routine scans, weekly regeneration of reference files. Scheduled, repetitive, high-volume.

**Autonomy is a dial, not a switch.** A loop doesn't have to run end-to-end — the human can sit at any depth. Drafting an action (an email, a change) without taking the final irreversible step (sending it, merging it) is the same discipline everywhere: automate to the last reversible step, keep a person on the irreversible one.

Loops that maintain the substrate other loops read are a distinct, high-leverage class: a scheduled job that regenerates reference files or skill definitions from the week's work, turning recent activity into a form the system can reload next time. This is a self-review routine generalized — the system improving its own context layer, an on-ramp to continual learning (see [[Single-loop vs Double-loop Learning]]).

## The 4-condition test — when a loop pays off

Building a loop has a fixed cost; it only pays back when the task is loop-shaped. A loop is worth engineering when **all** of these hold:

1. **Repeats** — the task recurs (ideally weekly or more), so the build amortizes.
2. **Gate-able** — the output can be checked by an objective predicate, not just human taste.
3. **Stable inputs** — the shape of the input doesn't change every run, or the loop breaks more than it saves.
4. **Tolerable failure** — a bad run is caught by the gate or is cheap to revert, not catastrophic.

If any of these fails, do the task manually. Building the loop first burns the attention it was meant to save.

## Manual first → processize → loop

The correct sequence — and the standard error is skipping straight to step three:

1. **Manual** — do the task by hand a few times; learn its real shape.
2. **Processize** — write it down as a repeatable procedure once it's stable.
3. **Loop** — automate it behind a schedule and a gate, only after the 4-condition test passes.

This is why, for instance, a new process should be run by hand before it's automated — it isn't proven or gate-able yet, and an autonomous loop built on an unstable process amplifies mistakes instead of removing work.

## Related
- [[The Harness Is the Product]] — the loop and the harness are what compound and stay yours as the underlying model changes
- [[Personal Context Layer]] — the substrate a loop reads from and writes back to
- [[Feedback Loops (Universal Pattern)]] — the general pattern this discipline instantiates in agent systems
- [[Claude Code Agentic Primitives]] — the concrete mechanics this discipline is built on
- [[Multi-Agent Systems]] — verifier/maker-checker patterns that make loops trustworthy
- [[Single-loop vs Double-loop Learning]] — the distinction between loops that execute and loops that improve themselves
