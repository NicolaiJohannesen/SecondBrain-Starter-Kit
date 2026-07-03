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
  - Context window management
  - Context rot
  - Attention budget
  - Curating LLM context
  - Just-in-time retrieval
  - Compaction
  - Beyond prompt engineering
---

# Context Engineering

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

> Identify the smallest possible set of high-signal tokens that maximize the likelihood of the desired outcome — and curate that set continuously as the agent runs.

Context engineering is the discipline that comes after prompt engineering. Where prompt engineering optimizes a single instruction at a single inference call, context engineering manages the entire token state of an agent across many turns — treating context as a finite resource with diminishing returns, not an unlimited input. Long-running agents accumulate state: message history, tool outputs, file contents, intermediate reasoning. That accumulated state actively degrades model performance unless deliberately curated.

## The structural problem: context rot

As the number of tokens in the context window increases, the model's ability to accurately recall information decreases. Two compounding causes: transformer attention is roughly quadratic in pairwise token relationships, so every new token competes for attention with every existing one; and training data skews toward shorter sequences, so deep-context recall is statistically out of distribution for the model. The practical consequence is an attention budget that depletes with each new token — the job of context engineering is spending that budget on the highest-signal tokens available.

The degradation is measured, not theoretical. Multi-hop needle-in-haystack benchmarks show frontier models losing tens of percentage points of accuracy well before advertised context limits are reached. Separately, research on "lost in the middle" effects shows a U-shaped accuracy curve across input position — content buried in the middle of a long context is structurally underweighted versus content at the start or end. A further finding: even with perfect retrieval (irrelevant tokens masked out entirely), performance still degrades as raw input length increases — the sheer length of the input impairs generation independent of content quality. Long context windows solve *retrieval* failures; they do not by themselves solve *generation* failures.

## Named techniques

| Technique | What it does | When it helps |
|---|---|---|
| System prompt calibration | Balance brittle hardcoded logic against vague guidance | Always — it's the most expensive context you pay for every turn |
| Tool design | Minimize overlap between tools, return token-efficient outputs | When many tools make selection ambiguous |
| Few-shot curating | A few diverse canonical examples, not exhaustive edge cases | Teaching a pattern rather than a lookup table |
| Just-in-time retrieval | Keep lightweight identifiers; load full data via tools only when needed | Any data you might need but rarely do |
| Compaction | Summarize conversation approaching context limits | Long sessions where early history is no longer load-bearing |
| Structured note-taking | Agent writes to external memory files | Multi-session, long-horizon tasks |
| Sub-agent architectures | Specialized agents return condensed summaries, not raw exploration | Long-horizon tasks where exploration would pollute the main context |

The same budget logic explains why on-demand [[Agent Skills]], an always-loaded project-conventions file, and [[Sub-agents and Agent Teams]] exist as separate mechanisms rather than one big prompt: each is a different way to keep the high-signal set small while still having access to everything else when it's actually needed.

## Failure modes to watch for

Hardcoding brittle logic into the system prompt; the opposite failure of vague guidance with no concrete signal; bloated overlapping tool sets; a "laundry list" of edge cases instead of curated canonical examples; overly aggressive compaction that discards subtle but critical context; and agents burning context chasing dead ends without guidance. The pattern across all of them: too much undifferentiated context is as bad as too little. Curation — what stays, what goes, what gets summarized, what gets offloaded — is the actual work.

## Prompt caching is part of the same discipline

Treating prompt caching as separate from context engineering is a common mistake. The same skill — identifying the stable/volatile boundary in your content and structuring around it — drives both. Cached reads cost a fraction of full input price, so at high hit rates the savings compound across a session. A common structural bug: dynamic content (working memory, timestamps, per-step state) sitting *between* cache breakpoints invalidates everything downstream of it on every turn. Moving volatile content out of the stable prefix — appending it as a clearly-marked dynamic block instead — is often the single highest-leverage fix available in a long-running agent's cost profile.

## Practical threshold

There is no single sharp cliff, but a practical zone — roughly in the hundreds-of-thousands-of-tokens range for current frontier models — where active management stops being optional. Below it, an agent can often get away with dumping everything into context. Above it, curation (clearing, compaction, sub-agent isolation, structured notes) becomes necessary just to keep the session coherent.

## Related

- [[The Harness Is the Product]]
- [[Multi-Agent Systems]]
- [[Agent Skills]]
- [[Sub-agents and Agent Teams]]
- [[Personal Context Layer]]
- [[Agent Failure Modes]]
