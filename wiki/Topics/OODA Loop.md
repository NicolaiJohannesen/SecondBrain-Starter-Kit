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
  - OODA
  - Observe-Orient-Decide-Act
  - Boyd's loop
  - Getting inside the loop
---

# OODA Loop

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

A four-phase decision cycle developed by US Air Force pilot and strategist John Boyd: **Observe** (gather raw data), **Orient** (interpret it through experience, training, and mental models), **Decide** (select an action), **Act** (execute). The competitive insight: the side that cycles through this loop faster — while maintaining a more accurate model of reality — gains an advantage that compounds with every iteration.

## The core insight

Boyd developed OODA from studying aerial combat, specifically why a technically inferior fighter jet defeated a superior opponent at a 10-to-1 kill ratio in the Korean War. His answer: the winning pilot could observe the situation more completely (better cockpit visibility) and act on decisions faster (better controls). The machine was worse; the loop was faster and better-informed.

The generalization: advantage goes not to the strongest or fastest actor in isolation, but to whichever side's internal model of reality stays closest to actual reality *and* acts on that model first. An opponent who is always reacting to the previous move rather than the current situation falls further behind with each cycle — until their model is so disconnected from reality that they make a decisive error.

## The Orient phase is the bottleneck

The simplified four-step circle undersells Boyd's real insight. His full diagram shows multiple feedback loops running *within* the Orient phase specifically. Orient isn't a passive step between observing and deciding — it's where the actual cognitive work happens: filtering raw observation through experience, training, and mental models to produce an interpretation of the situation in the first place. Two observers can see the same event and orient to it completely differently depending on what models they bring.

This makes Orient the real competitive variable, not raw speed. Cycling through Observe-Decide-Act quickly on top of a *bad* Orient just produces fast mistakes. Experienced operators, Boyd noted, often bypass conscious Decide and Act altogether — observation triggers response directly, because Orient has internalized the relevant patterns so deeply that it runs below conscious awareness. That's what expertise is: OODA cycles compressed until they're reflexive.

## Double-loop learning at speed

Boyd was explicit that the purpose of OODA isn't just to act faster — it's to continuously "destroy and create" mental models. This is [[Single-loop vs Double-loop Learning]] running at operational tempo: not merely correcting errors within a mental model, but restructuring the model itself when feedback shows it's wrong. Each OODA cycle either confirms the current model or supplies evidence that it needs revision. Getting inside an opponent's loop isn't just about winning the speed race — it's about forcing them to react before they can properly orient, which prevents the double-loop update from happening at all.

## Convergence with other loop frameworks

OODA, the Plan-Do-Check-Act cycle, the scientific method, and the single/double-loop learning distinction are all instances of the same underlying feedback structure, arrived at independently from different domains. What differs is scale and tempo: PDCA is built for systematic improvement over weeks and months; OODA was built for decisions measured in seconds. The underlying logic — observe reality, interpret it, act, observe the result, repeat — is identical. See [[Feedback Loops (Universal Pattern)]] for the general mechanism underneath all of these.

## Applications beyond combat

OODA entered business and strategy vocabulary as shorthand for competitive responsiveness, though "getting inside the competitor's OODA loop" is often used without Boyd's deeper point about Orient quality — speed without an accurate model is just faster mistakes. The more productive applications keep both halves together: rapid observe-orient cycles in a fast-changing crisis, quick hypothesis-test cycles in product development to keep a market model current, and any personal decision process under real uncertainty where the cost of a stale model compounds the longer it goes unchecked.

## Why this matters for AI-assisted work

An agent working on a long task is running an OODA loop whether or not anyone names it that way: observe the current state of the work, orient using its instructions and context, decide the next action, act, then observe the result of that action. The same lesson applies directly — the leverage is almost never in making an agent act faster; it's in making sure its Orient step (the context, instructions, and prior state it's reasoning from) is actually accurate. A fast agent with a stale or incomplete model of the task produces fast mistakes, exactly as Boyd's insight predicts.

## Related

- [[Feedback Loops (Universal Pattern)]] — the general mechanism this page specializes for fast, competitive decision cycles
- [[Single-loop vs Double-loop Learning]] — the model-revision half of OODA, named and generalized beyond combat
- [[Loop Engineering]] — designing an agent's observe/act cycle deliberately rather than letting it emerge by accident
- [[Agent Orchestration]] — a coordinator running its own OODA loop over a team of sub-agents
- [[Compound Growth]] — why a faster, more-accurate loop compounds its advantage over many cycles rather than just winning once
