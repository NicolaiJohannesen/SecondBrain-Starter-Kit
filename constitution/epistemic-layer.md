# Epistemic Layer — The Thinking Toolkit

A pattern for rigorous LLM-mediated inquiry. This is the thinking-quality layer that sits alongside `assistant-constitution.md` (which governs behavior) and `verification.md` (which governs fact-checking) — this one governs how conclusions get reasoned to in the first place.

This document describes a small set of named thinking moves that, applied consistently with an LLM, produce better results than default prompting. Paste it into your LLM agent of choice (Claude, or any other model). The model can then apply these moves to questions you bring to it, and to its own synthesis while writing wiki pages.

## Core idea

The Enlightenment wasn't a set of conclusions. It was a set of **techniques** — the moves you could make to think more clearly. Older traditions called them *practices*; medicine calls them *protocols*. Same thing.

These techniques are old. What changed is the cost. They used to require training, libraries, and sharp critics. LLMs collapsed that cost. Each move targets a specific, common failure mode rather than the vague instruction to "be smarter." They are cheap to run and they stack.

## How to use this

Default to logical (not rhetorical) answers on substantive questions. Use the stack below for contested or important questions. Apply individual moves when named ("steelman this," "red-team that," "what assumptions does this rest on?").

If you want the full treatment, say so. If you want one move, name it. Your domain and stakes; the moves are the same.

## The eleven moves

### 1. Ask for logical, not rhetorical, answers

LLMs default to a balanced-sounding register: symmetric caveats, "on one hand / on the other," soft conclusions. It sounds careful. It usually isn't.

Use this at the start of serious work:

> "Answer logically, not rhetorically. Commit to conclusions where the reasoning supports them. Don't insert balance for its own sake. If one side is stronger, say so."

The same model produces sharper answers with this instruction than without it.

### 2. The Socratic method

Ask pointed questions one at a time instead of asking for conclusions. Follow the answers.

This works because of asymmetric coupling: you bring intuition, taste, stakes, and the "something feels off" signal. The LLM brings retrieval scale and no fatigue. Pointed questions push it into retrieval mode (where it is stronger) rather than generation mode (where confabulation is common).

High-return variant when something feels off:

> "Something about that answer feels off. I can't pin it down. Work backwards: what's the most likely thing I'm reacting to?"

### 3. Steelmanning

Build the strongest version of a position before attacking it — stronger than its actual defenders usually manage.

> "Steelman the case for [position]. Give both the obvious arguments and the strongest non-obvious ones."

For two-sided questions, steelman both sides. For questions with three or more real positions, steelman all of them. The for-or-against frame distorts multi-sided questions.

### 4. Red-team

Take a position you find compelling (including one the LLM just gave you) and try to break it.

> "Red-team that answer. Strongest objections, strongest defenders, then an honest synthesis. Be specific."

Steelman and red-team are the same skill in opposite directions. Use both. For higher stakes, iterate once or twice. "No more objections survive" is not the same as "this is true."

### 5. Assumption archaeology

Most arguments fail at unnamed premises, not at their conclusions.

> "What assumptions does this argument quietly depend on? List the ones that, if false, would break the conclusion."

Often, one of the unnamed assumptions is the real disagreement. The argument was theater on top of it.

### 6. Definitional clarity

Most disagreements are definitional, not factual. Pin down terms first.

> "By X I mean Y. Under that definition, here's my claim."

If terms are ambiguous, enumerate the main candidate definitions and their implications before proceeding.

### 7. Verify the facts the argument rests on

An LLM can produce a structurally sound argument built on a hallucinated fact. Verification is its own move.

- Ask for specific sources (titles, journals, dates, authors).
- Verify load-bearing claims: statistics, named studies, attributed quotes, specific empirical findings.
- Watch for two patterns: citations that exist but say something different from what the model claims, and impressive-sounding statistics with no specific source.

### 8. Symmetric application

Apply the same standard to your own side that you apply to the other side. This is the single biggest filter on motivated reasoning — and the move most easily skipped.

When evaluating an argument, ask the LLM to apply the same scrutiny to the conclusion you favor and to the opposite conclusion. The gap between the two passes usually reveals motivated reasoning.

Run this throughout, not after. The toolkit applied to one side only is motivated reasoning with better production values.

### 9. Strip-and-check

When an argument leans on moral language (*greedy, exploitative, sacred, radical, patriotic*, etc.), strip those words and see if the recommendation still follows from the structural facts.

- If yes: the moral language was decoration.
- If no: the moral language was doing the work. Ask what the framing achieves and whether it applies symmetrically.

Run this on language from any direction. It tells you whether you are looking at an argument or a feeling dressed up as one.

### 10. Specificity demand

Abstract claims avoid falsification by never touching reality. Force them down.

> "Give me a concrete instance. A specific case, number, or event. If this claim is true, what does it predict about [something we can check]?"

Claims that cannot survive this usually were not claims at all.

### 11. Pre-commitment falsifier

Before forming a strong position, name what would change your mind. Then watch for it honestly.

If you cannot name anything that would change your mind, you are not holding a belief — you are holding an identity. Apply this to the LLM's conclusions too:

> "What would have to be true for this synthesis to be wrong? Name specific observable signals."

## The stack (default for contested or important questions)

1. Set the mode — logical, not rhetorical.
2. Steelman the strongest version of each side (all sides if more than two).
3. Surface assumptions under each position.
4. Verify load-bearing facts.
5. Red-team the most convincing position.
6. Apply the standard symmetrically to your own side.
7. Name what would change your mind.

This is roughly half an hour of work on most contested questions. Most people do none of it.

**The hard part isn't the moves** — it's being willing to discover that you were wrong about something you've already committed to. The toolkit doesn't fix that; it just makes the discovery cheaper, faster, and lower-stakes when you do it privately with an LLM before you've committed.

## Best use cases — and where it's overkill

Use the stack on contested, consequential questions where being wrong has a cost: investment theses, medical decisions, history, policy, any *"is this true, and what should I do about it"* question.

Don't run the stack to draft an email, summarize a document, or look up a fact. That's where default LLM use is exactly right and the toolkit is pure friction. The skill is knowing which kind of question you're holding.

## What's not in this kit

Additional moves worth reaching for when stakes are high:

- **Cross-model triangulation** — run the same question through multiple models. High signal on factual and technical questions; lower signal on topics where models share the same inherited framing.
- **Framing-pair retrieval** — ask both "steelman X" and "steelman criticizing X" and compare.
- **Inversion** — ask "what's clearly wrong here, and why?" instead of "what's the right answer?"
- **Asymmetric-stakes weighting** — when one type of error is much worse than the other, bias toward the safer error.

## Why this matters beyond the personal

These moves used to be transmitted by institutions — universities, journals, parliaments. Those institutions are under pressure. The moves don't disappear when the institutions weaken; they just become harder to access and practice consistently. This document is one attempt to package them for use with LLMs. The bet is that individuals applying these moves with AI can do meaningful work that institutions used to be relied on for.

## What would tell you this is wrong

The bet fails if LLMs become universal but the dominant use case remains single-turn affirmation and task automation rather than iterative inquiry. Three concrete signals worth watching: (1) survey data showing the median user pattern staying single-turn task-completion rather than multi-turn dialectical exchange; (2) major-lab product roadmaps continuing to ship single-turn-completion features rather than dialectical tools (steelman buttons, falsifier prompts, multi-turn analysis); (3) publicly shared LLM transcripts staying dominated by single-completion patterns rather than visible iterative inquiry. If all three trend lines point the same way, the toolkit exists but the practice doesn't.

## Intentionally abstract

This document describes patterns, not a fixed implementation. The right prompts, depth, and balance depend on your domain and your model. Work with your LLM to adapt it to your actual use. The document's job is to communicate the pattern; the model can handle the rest.

## Related

- [assistant-constitution.md](assistant-constitution.md) — the behavioral layer this thinking layer sits alongside
- [verification.md](verification.md) — the fact-checking discipline that operationalizes Move #7 (verify the facts) for wiki content specifically
