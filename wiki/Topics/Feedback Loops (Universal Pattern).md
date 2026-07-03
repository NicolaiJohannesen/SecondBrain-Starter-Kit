---
type: topic
created: 2026-07-02
updated: 2026-07-02
version: 1
origin: kit-seed
tags:
  - topic
  - seed
  - domain/systems
  - domain/philosophy
aliases:
  - Feedback loops
  - Control loops
  - Cybernetics
  - Negative feedback
  - Positive feedback
  - Iterative correction
  - Error correction loop
  - Self-correcting system
---

# Feedback Loops (Universal Pattern)

In 1868, James Clerk Maxwell published a paper called "On Governors" — a mathematical analysis of the centrifugal regulators used to control steam engines. He did not know he was naming a mechanism that already ran through everything: blood glucose regulation, predator-prey cycles, democracy, the scientific method, compound interest. He thought he was solving a problem in mechanical engineering. He had found the structural spine of adaptive behavior across every domain.

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

**A feedback loop** is a cyclical mechanism in which the output of a system is returned as input, letting the system monitor and adjust its own behavior. It shows up in biology, engineering, politics, psychology, economics — not because each domain happens to share a metaphor, but because feedback is a **structural feature of any system that learns, adapts, or regulates itself**.

## The mechanism: sensor, comparator, actuator

Every feedback loop has three parts. A **sensor** measures the current state. A **comparator** checks that state against a target (explicit or implicit) and computes the gap. An **actuator** acts on the gap to close it. A thermostat senses room temperature, compares it to a setpoint, and drives the heater. A market senses demand through prices, compares it to supply, and drives production. A person senses the reaction to something they said, compares it to the response they wanted, and adjusts what they say next. Once you have this three-part shape in view, you start seeing it everywhere — which is useful, as long as you also check that the return path is real (see Failure modes, below).

## Maxwell's three parameters

Maxwell's paper did more than describe a device — it extracted a diagnostic framework for *any* self-regulating system. Three parameters determine whether a loop stabilizes, oscillates, or flies apart:

- **Gain** — how strongly the system responds to a detected error. Too much and it overcorrects; too little and it drifts.
- **Damping** — how much the system resists rapid change, preventing overshoot into the opposite direction.
- **Inertia** — how slowly the system's state changes in response to a force. High inertia means errors accumulate slowly but also take a long time to correct.

It is the *relationship* between the three — not any one alone — that determines the loop's behavior. When a feedback loop misbehaves, one of these three is miscalibrated.

## Moderator vs. governor — the single-loop / double-loop split

Maxwell drew a distinction that organizational theorists Chris Argyris and Donald Schön independently rediscovered a century later, calling it [[Single-loop vs Double-loop Learning]]. A **moderator** corrects deviations within fixed rules — the thermostat holds 72°F without ever asking whether 72°F is right. A **governor** adjusts the rules themselves — asking whether the target, not just the output, needs to change. Single-loop learning keeps a system stable; only double-loop learning lets it adapt when the world changes the rules underneath it.

## Negative and positive feedback

**Negative feedback** subtracts the output from the input, resisting deviation from a set point — homeostasis, thermostats, predator-prey balance. **Positive feedback** reinforces the input, amplifying small deviations — population growth, viral spread, bank runs, compound interest. Real systems use both, switching between stabilizing and amplifying modes as conditions change.

## The delay problem

The most underappreciated property of a feedback loop is the **delay** between a signal being generated and the correction taking effect. Long delays produce oscillation: by the time the correction lands, the system has already overcorrected in the other direction — this is the mechanism behind business cycles and policy overshoot. A practical implication follows directly: shortening the loop is usually more valuable than enriching the signal. Timely mediocre feedback beats perfect feedback that arrives six months late.

## What makes a loop actually work

Two loops can look identical and produce radically different results. Four properties decide it: **signal specificity** (vague feedback produces vague adjustment), **delay** (short delays let the next cycle actually use the signal), **noise ratio** (a signal contaminated with irrelevant information can't be attributed to the right cause), and **measurement validity** (a loop optimizes whatever it measures — which may not be what actually matters; a well-known failure mode when the metric and the goal quietly diverge).

## The universal algorithm: variation, selection, retention

The deepest formulation — arrived at independently by Karl Popper, Donald Campbell, and Richard Dawkins — is that feedback loops across domains are not merely similar but *structurally identical*, running the same three-step algorithm on different substrates:

| Domain | Variation | Selection | Feedback mechanism |
|---|---|---|---|
| Biological evolution | Mutation + recombination | Environmental fitness | Survival & reproduction |
| Scientific method | Hypotheses | Experimental testing | Falsification |
| Markets | Competing products/prices | Consumer choice | Price signals |
| Agile software | Small increments | User reaction | Retrospective |
| Habit formation | Cue → routine → reward | Neurochemical response | Dopamine loop |

Systems that suppress variation, selection, or retention don't just stop improving — they degrade, because they've cut the return path that lets reality correct them.

## Why this is the root concept here

This page is the mechanism underneath most of what makes a second brain, an agent harness, or any AI-assisted workflow actually improve over time rather than just repeat. [[Loop Engineering]] is the deliberate design of tight feedback loops into a workflow. [[Culture of Learning]] is what a system looks like when double-loop learning is the norm rather than the exception. [[Compound Growth]] is what a well-tuned loop produces when it runs for long enough without breaking. If a system you're building isn't improving, the diagnostic question is always the same: is the loop open or closed, and how long is the delay?

## Related

- [[Single-loop vs Double-loop Learning]] — the moderator/governor distinction, worked in full
- [[OODA Loop]] — a deliberate, fast-tempo feedback loop applied to decision-making under pressure
- [[Loop Engineering]] — designing tight feedback loops into a workflow on purpose
- [[Culture of Learning]] — what an organization or agent system looks like when this pattern runs by default
- [[Compound Growth]] — the long-timescale product of a feedback loop that keeps closing
- [[Agent Failure Modes]] — several agent failure modes are just this page's loop-quality properties failing in an AI context
