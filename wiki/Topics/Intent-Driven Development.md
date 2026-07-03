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
  - IDD
  - Intent Driven Development
  - Test-Driven Development
  - TDD
  - Tests as intent anchors
  - Spec-first development
  - Intent cascade
---

# Intent-Driven Development

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

**Intent-Driven Development (IDD)** — the 2026-named methodology (Richard Stockley, [intentdrivendevelopment.org](https://intentdrivendevelopment.org/), April 2026) for working with AI executors: when execution is fast and cheap, the bottleneck moves from *can we build it* to *do we know what to build* — so **intent, specified before and during execution, becomes the primary artifact**, and the human's role shifts from coder to intent author and fidelity reviewer. The underlying primitive is much older: [[Commander's Intent]] (Prussian *Auftragstaktik*, 1857 onward), strategic intent in management literature, the Northstar in product strategy. Your brain's [NORTHSTAR.md](../../NORTHSTAR.md) is this pattern at personal altitude.

## The core claim: intent must survive the delegation gap

When work is delegated — to an AI agent, to a collaborator, to your future self in a different session — implicit intent dies in transit. The delegate substitutes its own defaults (an AI's training priors, generic best practice, what-it-thinks-you-meant). Explicit intent, written where the delegate must read it, is what keeps delegated work nested inside your actual direction. That is why drift is the default and intent artifacts are the countermeasure.

## The cascade — intent at every altitude, checked at every altitude

| Altitude | Intent artifact | Fidelity checked by |
|---|---|---|
| Life / system | NORTHSTAR.md | human judgment (does this serve what the brain is for?) |
| Standing behavior | the constitution | session discipline + review |
| Project | a project page: purpose, decisions, constraints | reviewing the diff against the plan |
| Task / feature | a written spec or plan | fidelity review |
| **Component / behavior** | **a failing test, written first** | **the test runner — fully mechanical** |

Two consequences:

1. **Push intent down the cascade as far as it will go.** Verification gets cheaper at lower altitude — a Northstar needs human judgment to check against; a test needs an exit code. Everything expressible as an automated test converts expensive judgment into free mechanical checking. What remains above the test line is the intent that genuinely needs you.
2. **Every level must derive from the level above.** A test not derived from the spec verifies the wrong thing precisely. A Northstar with no checkable artifacts beneath it drifts invisibly. Intent flows down; learning flows up.

## Why tests are the strongest anti-drift device (TDD in the AI era)

Test-Driven Development (Kent Beck, ~1999): write the **failing test first**, then the minimum code to pass, then refactor. Red → green → refactor. The AI-era reading: the failing test is **intent pre-committed in machine-checkable form** —

- **The agent can't grade its own homework.** An executor that decides *after* building how to verify its work will find it satisfactory. A test fixed *before* implementation sets the success condition while it's still honest — the pre-commitment falsifier from the epistemic layer, applied to code.
- **Externalized intent survives context loss.** Instructions in a conversation decay and die at context compaction; a test suite lives outside the context window and re-asserts the intent at zero cost on every run. The agent can forget; the suite doesn't.
- **Drift becomes an exit code instead of an opinion.** "Did the change preserve behavior?" stops being something the agent believes about itself.

Practice rules: every substantive code change adds or updates tests · for bug fixes, write the failing reproduction FIRST · green baseline before changing anything, green after · test at the deployed configuration, not convenient localhost · the agent that wrote the code doesn't certify it (maker–checker). A test suite is also what makes a coding loop safely automatable at all — gate-able output is a precondition for autonomy (see [[Loop Engineering]]).

## Boundary conditions

Intent artifacts are overhead when work is small, throwaway, or the intent is genuinely *discovered by building* (locking intent before you know it freezes the wrong direction). Visual/UI work needs rendered-state checks rather than unit tests — the principle transfers, the instrument changes. And a green suite can lie (wrong behaviors covered, tests weakened to pass) — which is why the judgment rungs above the test line never fully disappear.

## Related
- [[Commander's Intent]] — the doctrinal parent; [NORTHSTAR.md](../../NORTHSTAR.md) is your instance
- [[Plan-Writing for AI Coding Agents]] — the spec rung directly above tests
- [[Loop Engineering]] — gate-able output as the precondition for autonomous loops
- [[Agent Failure Modes]] — the drift this discipline exists to catch
- [[Verification Discipline and Assertion Types]] — the maker–checker separation
- [[Memory Compaction]] — the parallel evidence: externalized, pinned rules survive what context loses
- [context/building-software-projects.md](../../context/building-software-projects.md) — the build loop these rules execute in
