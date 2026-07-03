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
  - Spec for AI coding agent
  - AI agent specifications
  - Plan shape for AI engineer
  - Premise check before deep spec
  - Specs for AI vs specs for humans
---

# Plan-Writing for AI Coding Agents

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

A spec written for an AI coding agent has a different shape than a spec written for a human engineer. A human engineer needs a precise contract because handoffs lose fidelity and re-work is expensive. An AI coding agent needs **enough context to make judgment calls, then specs to constrain those calls at the edges**. Overspecifying an agent's plan produces friction — the agent waits on details that don't actually matter. Underspecifying produces wandering — the agent doesn't know what shape to commit to. Getting the shape right is a distinct skill from writing a good spec for a person, not a lighter version of the same skill.

## Why the shape differs

Classical specs were written for human engineers in organizations where handoffs were lossy and durable: heavy, precise contracts defended against fidelity loss across a handoff; acceptance-criteria checklists worked because the engineer would build exactly what was checked; edge cases had to be enumerated because anything unspecified would be implemented inconsistently by different people; and the spec had a long shelf life because a different engineer might pick it up weeks later.

Working with an AI coding agent in the same session removes most of those constraints. There's no handoff loss to defend against — the same conversation that plans the work also executes it. Given a clear intent and a short list of design principles, the agent can make sound judgment calls on edge cases without asking, which a heavy spec actively suppresses. Iteration happens inside the same session or the same day, so a heavy contract makes correcting course *more* expensive, not less. And the agent typically has the surrounding codebase in context already, so the spec doesn't need to re-state conventions the agent can just read.

A spec calibrated for a human engineer, handed to an agent instead, produces three costs: wasted context budget (the agent reads more spec than it needs — see [[Context Engineering]]), suppressed judgment (edge cases the agent could have reasoned through are pre-decided, badly, by a spec author guessing at cases in advance), and expensive iteration (rewriting the spec costs more than rewriting the implementation would have).

## Six elements of a right-shaped plan

**1. Premise check, at the top.** State the premise the plan rests on and invite pushback before any deep implementation work happens. If the premise is wrong, no amount of downstream detail-quality rescues the result — so surface it first, cheaply, rather than burying it inside a wall of acceptance criteria where it's expensive to notice and correct.

**2. Intent before specs.** Name *what the feature is for* and *what success looks like* before naming what to build. This is what the agent uses to resolve an edge case the spec didn't anticipate — it reads the intent and decides, rather than asking or guessing.

**3. Design principles for judgment calls.** A short list of principles the agent applies when the spec doesn't cover a case — not acceptance criteria, but reasoning substrate. "Mirror the existing convention in module X" or "default to the safer of two options when ambiguous" each let the agent resolve a class of decisions on its own rather than escalating every one.

**4. Lightweight specs.** Acceptance criteria stated as outcomes, not behaviors; a file plan as paths plus a one-line description each, not full code skeletons. The agent fills implementation in from intent, principles, the acceptance criteria, and the existing codebase — a full code skeleton in the plan usually oversteps into decisions the agent was better positioned to make itself.

**5. Explicit out-of-scope.** A short list of what's deliberately deferred, with any forward-compatible slots (a naming convention, a config namespace) reserved. Without this, agents tend to quietly add adjacent features they assume are obviously in scope — sometimes correctly, but at the cost of the plan's coherence.

**6. A ground-truth validation step.** Not a unit test — a specific, concrete check for *did this actually do what it was supposed to do*, run after shipping. Naming this step in the plan is what keeps it from being skipped under time pressure.

## A worked pattern: less spec, better outcome

A recurring pattern across planning sessions: a first draft of a plan, written before any pushback, tends to be long — heavy on full code skeletons and exhaustive edge-case enumeration — and produces a *correctly built version of the wrong feature*, because the premise underneath it was never surfaced for challenge. A second draft, written after a premise check surfaces a better framing, is typically shorter — half the length or less — but produces a substantially better feature, because the plan now spends its words on intent and principles instead of pre-deciding details the agent could reason through itself. **The plan gets shorter and the outcome gets better in the same revision.** That combination is the signature of a right-shaped AI-agent plan; if a revision only gets longer or only gets shorter without the outcome improving, the shape hasn't actually changed yet.

## Plan template skeleton

```markdown
## Premise check (push back before going deep)
What I'm assuming: [premise]
What this shape leads to: [outcome]
Alternatives considered and rejected: [list]
Where you might want to push: [the one most worth challenging]

## Intent
[Why this exists] [What success looks like] [What this is NOT]

## Design principles (use these for judgment calls, don't ask)
- [Principle + reason]

## Acceptance criteria
1. [Outcome, not behavior]

## File plan
### New — [path]: [brief description]
### Modified — [path]: [what changes]

## Out of scope (defer)
- [Adjacent feature], deferred because [reason]

## Ground-truth validation (post-ship)
After shipping: [specific check]
If it fails: [investigation path]
```

## When a heavier spec is still the right call

Lightweight plans assume same-session continuity between the person planning and the agent implementing. Reach for a heavier spec instead when: the implementing agent is a genuinely different session with no shared context to lean on; the work is high-irreversibility (migrations, security-critical changes) where over-specifying is cheap insurance against an expensive mistake; multiple agents are implementing adjacent pieces in parallel and need an explicit coordination contract; or the eventual implementer is a human who may pick the work up much later. The default for same-session work with an AI coding agent is lightweight — reach for heavier specs deliberately, not by default.

## Related

- [[Commander's Intent]]
- [[Context Engineering]]
- [[Verification Discipline and Assertion Types]]
- [[Engine-Writes-Substrate]]
- [[Loop Engineering]]
