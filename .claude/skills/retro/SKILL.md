---
name: retro
description: Proactive self-improvement retrospective. Run at the end of every substantive session by default — not only when asked. Scans the session for corrections the user had to give, knowledge held but not applied, and near-misses; codifies each into memory or skills automatically and surfaces only genuine judgment calls. The point is to move the learning loop's sensor from the user to the system, so they stop having to say what to learn.
---

# Retrospective / Self-Improvement Mode

**The problem this exists to solve**: a system that only improves when the user notices a gap and spells it out has the user as its sensor. That makes them the bottleneck on *learning*, not just on decisions. The fix is to build the sensor into the system — run the detectors the user would run, automatically, and act on what they find. The user keeps the direction and the taste; the system catches its own gaps.

## When this runs

- By default, at the end of every substantive session, before the final summary — not gated on being asked.
- After any substantial multi-step build or ingestion pass.
- On demand (`/retro`).

This is the proactive layer, sitting alongside (not replacing) the ordinary discipline of updating memory right after a correction. This skill looks for learnings even when nothing was explicitly flagged.

## The detectors

Detectors 1–5 are **corrective** — they sense failures and gaps. Detector 6 is **generative** — it senses discovery, new value above baseline. A corrective-only loop only prevents regression; the generative detector is what raises the ceiling.

1. **Correction detector — what did the user have to tell me?** Scan their turns for corrections and restated preferences ("no," "don't," "remember to," "why didn't you," "that's not what I meant," or any re-specification of something already stated once). Every one is a learning. Check it against what's already in memory; if it's genuinely new, codify it as a new rule or a worked example added to an existing one. A correction that only lives in the chat transcript is a correction that will recur.

2. **Gap-audit — what do we know but didn't apply?** For every relevant skill or convention this session touched: was it actually followed in full? Enumerate the skills that exist (`ls .claude/skills/*/SKILL.md`) rather than relying on memory of what they contain — recall bias is exactly the weakness this detector exists to catch. Apply a checklist-shaped skill across *all* its dimensions and *all* applicable surfaces — a partial application (closing one slice, deferring the rest) reads as done when it isn't; re-audit before claiming the gap closed.

3. **Near-miss detector — what did I redo, almost get wrong, or fight the tooling on?** Reworked edits, failed approaches, surprising tool behavior. Each is a process fix: change the default, the script, or the check so it structurally can't recur — don't rely on "be more careful next time."

4. **Anticipation check — what's the next thing they'll have to ask for?** Given the trajectory of this session, what gap is forming that hasn't been named yet? Surface it, or pre-empt it.

5. **Deferred-intent detector — what did we start and not finish?** Scan the session's work for partial work masquerading as done: a placeholder left in, a "for now" comment, a page created but never cross-linked, a checklist applied to some pages but not all. Close it, or log it as a named, owned gap — never let "started" read as "done."

6. **Insight detector — what did we figure out that's new and worth keeping?** The generative counterpart to 1–5. Scan for genuinely novel value: a better method reasoned out mid-session, a pattern spotted, a sharp framing, a good idea surfaced in passing. This is the most perishable thing in the system — an uncaptured insight is gone at session end, with no correction forthcoming to regenerate it later. Capture it only if it would meaningfully help a future session AND isn't already covered — not every passing thought earns a permanent home.

## Then: codify and surface

- **Codify the clear ones silently.** Write or upgrade the memory rule, add the skill step, fix the gap. A detected gap gets closed, not listed as an open question.
- **Route each lesson to the layer that will actually enforce it:**
  - Governs an action or a step in a known workflow → bake it into the relevant **skill** as an explicit step or a pre-done gate item. This is the primary target for behavior lessons, not a memory file — a memory is passive (fires only if recalled); a skill step is active (loaded and followed every time the skill runs).
  - A fact, a preference, or a worked specimen → a **memory file**, with a one-line index entry in `memory/MEMORY.md`.
  - Anything cross-cutting that changes how every session behaves → propose it to the user; don't unilaterally rewrite the operating discipline.
  - Both can apply: a behavior lesson often gets a skill step (so it actually fires) *and* a memory entry (for the why and the worked example).

## Track the rate

The success metric is a number, so measure it. Append one row per session to `wiki/Tasks/learning-ledger.md` (create it if it doesn't exist yet):

`| date | corrections (n) | novel / REPEAT | what (tags) | routed-to (layer) | caught-by (system/user) |`

- **REPEAT** = a correction in the same class as a prior lesson — meaning the lesson existed and didn't fire. A repeat is itself a detector-1 finding: why didn't the existing rule retrieve? Usually because it was written to the passive layer (memory) when it needed to be in the active layer (a skill step).
- **caught-by** = did the system's own detectors surface it, or did the user have to flag it? User-caught is the exact bottleneck this loop exists to remove.
- Surface only genuine judgment calls — anything voice-affecting, scope-affecting, or a real strategic decision.

## Why this shape, not generic "reflect"

Generic reflection is vague and easy to skip. This works because it runs specific detectors against the actual session record, by default, and acts — codifying rather than just reporting. The target is REPEAT trending to zero and user-caught trending to zero, at *growing* surface area — not fewer corrections overall, which would just reward doing less.
