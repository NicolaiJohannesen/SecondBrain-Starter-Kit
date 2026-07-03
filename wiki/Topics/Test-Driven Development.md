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
  - TDD
  - Test Driven Development
  - Automated testing
  - Automated tests
  - Tests as intent anchors
  - Red-green-refactor
---

# Test-Driven Development

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

**Test-Driven Development (TDD)** — Kent Beck's discipline (named ~1999; *Test-Driven Development: By Example*, 2002): write a **failing test first**, then the minimum code that passes it, then refactor with the test as the safety net. Red → green → refactor. The test is not primarily a bug-catcher; it is **intent, written in executable form, pre-committed before the implementation exists**.

## Why TDD matters more with AI, not less

The pre-AI case for TDD was correctness and design pressure. The AI-era case is stronger and different: **a failing test written first is the one intent artifact an AI executor cannot rationalize away.**

- **Pre-commitment beats self-grading.** An agent that writes code and *then* decides how to verify it grades its own homework — it will find its output satisfactory. A test written *before* the implementation fixes the success condition while it's still honest — the pre-commitment falsifier from the [epistemic layer](../../constitution/epistemic-layer.md), applied to code.
- **Externalized intent survives context loss.** Instructions in a conversation decay across turns and die at context compaction; a test suite lives *outside* the context window and re-asserts the intent at zero cost on every run. The agent can forget; the suite doesn't. (The same evidence pattern as [[Memory Compaction]]'s constraint-pinning finding: rules that survive in checkable form get followed; rules summarized away get violated.)
- **Drift becomes an exit code instead of an opinion.** Without tests, "did the change preserve behavior?" is something the agent believes about itself. With tests, it's mechanical.

## Where tests sit in the intent cascade

TDD and your [NORTHSTAR.md](../../NORTHSTAR.md) are **the same structure at different altitudes** — a fixed, checkable statement of intent, committed before execution, that the work is verified against. [[Intent-Driven Development]] maps the full cascade; tests are its bottom, executable rung:

| Altitude | Intent artifact | Checked by |
|---|---|---|
| Life / system | NORTHSTAR.md | human judgment |
| Standing behavior | the constitution | session discipline + review |
| Task / feature | a written spec or plan | reviewing the diff against the plan |
| **Component / behavior** | **the failing test** | **the test runner — an exit code** |

The operating rule that follows: **push intent down the cascade as far as it will go.** Verification gets cheaper at lower altitudes — a Northstar needs human judgment; a test needs an exit code — so everything expressible as a test should be one. What remains above the test line is the intent that genuinely needs you. The symmetry cuts both ways: tests not derived from the spec verify the wrong thing precisely; a Northstar with no tests beneath it drifts invisibly.

## Practice rules

- Every substantive code change adds or updates tests.
- For bug fixes: **write the failing test that reproduces the bug FIRST**, then fix — the reproduction is the pre-commitment.
- Green baseline before changing anything; green again after — so a failure is attributable.
- **Test at the deployed configuration**, not the convenient localhost setup — a preview-deployment URL is the deployed configuration (see [context/deploying-to-cloudflare.md](../../context/deploying-to-cloudflare.md)).
- The agent that wrote the code doesn't certify it — maker–checker separation ([[Verification Discipline and Assertion Types]]).
- Tests are what make a coding loop safely automatable at all — gate-able output is a precondition for autonomy ([[Loop Engineering]]'s 4-condition test).

## Boundary conditions

Exploratory or throwaway code where the intent is *discovered by building* inverts the economics — writing tests for intent you don't yet have locks in the wrong direction. UI/visual work often needs rendered-state verification (headless screenshots) rather than unit tests — the principle (pre-committed, externalized checks) transfers; the instrument changes. And a green suite can lie: wrong behaviors covered, tests weakened to pass — which is why the judgment rungs above the test line never fully disappear.

## Related
- [[Intent-Driven Development]] — the full cascade this page is the bottom rung of
- [[Commander's Intent]] — the top of the same structure; your NORTHSTAR.md's lineage
- [[Plan-Writing for AI Coding Agents]] — the spec rung directly above tests
- [[Loop Engineering]] — gate-able output as the precondition for autonomous loops
- [[Verification Discipline and Assertion Types]] — the maker–checker separation
- [[Memory Compaction]] — the parallel evidence that externalized, pinned intent survives what context loses
- [context/building-software-projects.md](../../context/building-software-projects.md) — the build loop these rules execute in (step 3: failing test first)
