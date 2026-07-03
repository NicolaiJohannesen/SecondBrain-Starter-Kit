---
type: topic
created: 2026-07-03
updated: 2026-07-03
version: 1
origin: kit-seed
tags:
  - topic
  - seed
  - domain/psychology
aliases:
  - Double-loop learning
  - Single-loop learning
  - First-order learning
  - Second-order learning
  - Generative learning vs adaptive learning
  - Moderator vs governor
---

# Single-loop vs Double-loop Learning

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

A distinction introduced by organizational psychologists Chris Argyris and Donald Schön — and independently arrived at by James Clerk Maxwell in engineering a century earlier. **Single-loop learning**: correct errors *within* existing assumptions. **Double-loop learning**: detect that the assumptions themselves may need to change.

## The distinction

**Single-loop learning** is the moderator: detect a deviation from target and correct it without questioning the target. The thermostat keeps the room at 72°F — it doesn't ask whether 72°F is the right temperature. A quality inspector rejects defective parts without asking whether the specification is right. A student studies harder for the next test without asking whether the test measures something worth measuring.

**Double-loop learning** is the governor: detect a deviation *and* ask whether the governing variables — goals, assumptions, methods — need to change. Maybe 72°F is wrong for this room. Maybe the defects reveal a flawed manufacturing process, not sloppy workers. Maybe the test is measuring the wrong thing entirely.

The names come from control theory: a single feedback loop runs from sensor to corrector to effector and back. A double loop adds a second loop that monitors the first — capable of modifying the first loop's parameters, or its rules, or its target.

## The Maxwell parallel

Maxwell drew the identical distinction in his 1868 analysis of steam governors, a century before Argyris. A **moderator** adjusts the engine's throttle to hold speed within a fixed range. A **governor** can adjust the target range itself. Maxwell was writing about steam engines; Argyris was writing about organizations — the fact that two people working a century apart in unrelated fields converged on the same two-tier architecture is evidence that the structure is real, not a metaphor borrowed between disciplines. See [[Feedback Loops (Universal Pattern)]] for the fuller mechanism this rests on.

## Why double-loop learning is rare

Argyris spent decades studying why individuals and organizations avoid double-loop learning even when it would obviously help. His finding: **defensive routines**. Questioning the governing variables is threatening, because it implies past decisions were made under a flawed framework — which implicates whoever made them. Organizations respond by making such questions socially costly to raise. The result: single-loop fixes accumulate, the underlying assumption grows more entrenched, and the gap widens between what an organization *says* it values ("we're always learning") and what its behavior actually reveals it values (protecting the existing framework). Argyris called this gap **espoused theory vs. theory-in-use**.

## Building double-loop learning in on purpose

A handful of practices reliably force inquiry past the surface error toward the underlying assumption:

- **Five Whys** — asking "why?" five times in succession after any problem, specifically to push past the first plausible explanation
- **The Act phase of PDCA** (Plan-Do-Check-Act) — asking not just "did this work?" but "was our plan right, our measures right, our goals right?"
- **A pre-mortem** — before starting, ask "assume this failed catastrophically — what went wrong?" This forces assumption-examination before defensive routines have a chance to solidify around a plan already underway
- **Falsifiability as a structural discipline** — the scientific method requires observations capable of disproving the theory to be admitted at all; the framework stays revisable by design, which is double-loop learning as a formal rule rather than an occasional virtue

## Why this matters for an AI-maintained system

An agent or workflow that only ever does single-loop correction will get very good at optimizing whatever it's currently being measured on, and never notice when the measurement itself has gone stale. A [[Culture of Learning]] is, structurally, an environment where double-loop questions get asked routinely rather than only after a visible failure — the retrospective habit that asks not just "did this session go well?" but "is the *process* that produced this session still the right one?" This is the double-loop layer applied to the system maintaining itself, not just to the tasks it performs.

## Failure modes

Single-loop learning fails when the governing variables were wrong to begin with — a system perfects its operation within a flawed frame, optimizing a proxy while the actual goal quietly erodes. Double-loop learning fails in the opposite direction when "questioning our assumptions" becomes cover for avoiding accountability rather than a response to real evidence of systematic failure. The check against that misuse: double-loop questioning should be triggered by evidence, not by discomfort with the current answer.

## Related

- [[Feedback Loops (Universal Pattern)]] — the general mechanism this distinction specializes
- [[OODA Loop]] — Boyd's "destroy and create" Orient phase is double-loop learning run at operational speed
- [[Culture of Learning]] — an environment where double-loop questioning is the default, not the exception
- [[Agent Failure Modes]] — an agent stuck in single-loop correction is a specific, recognizable failure pattern
- [[Compound Growth]] — why double-loop-capable systems keep compounding after single-loop-only systems plateau
