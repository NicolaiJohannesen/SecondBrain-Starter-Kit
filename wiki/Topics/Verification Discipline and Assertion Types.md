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
  - Assertion types
  - Verification by assertion type
  - Type-aware verification
  - Verification fetish
  - Assertion-type framework
  - Two-pass verification
  - Attribution-axis verification
  - Citation-loading
  - Paired-agent dispatch
---

# Verification Discipline and Assertion Types

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

A framework for applying verification with the right amount of discrimination: **not all assertions are the same kind of thing, and the discipline has to be matched to the type before it's applied.** A flat rule — "verify everything or downweight it" — produces a bias of its own: it systematically underweights claims that are highly likely true but not empirically checkable for reasons that have nothing to do with their truth (a valid logical inference, say, or a reasonable projection about the future). Call this the **verification-fetish** failure mode: verification standards applied so uniformly that they end up filtering out claims by demanding evidence they structurally cannot produce.

## The six assertion types and their disciplines

| Type | Defining feature | Appropriate discipline |
|---|---|---|
| **Empirical-verifiable** | Data exists and can be checked | Verify against the data directly. Mark verified / partial / unverified. |
| **Empirical-in-principle-verifiable** | Data could exist but doesn't yet | Mark `[in-principle verifiable, data unavailable]`. Don't treat as confirmed or disconfirmed. |
| **Inferential** | Conclusion follows from verified premises via a logical chain | Verify the premises and the validity of the chain — not the conclusion directly. A valid inference from verified premises carries real weight even though it isn't itself "verified." |
| **Counterfactual / future projection** | About a non-actualized possibility | Surface what evidence would shift confidence either way. Mark `[inherently uncertain — counterfactual]` while preserving the likelihood assessment. |
| **Logical / structural** | True by structure given stated premises | Assess validity given the premises, not empirical support. Mark `[logically valid, premise-dependent]`. |
| **Conventional / common-sense** | A widely shared assumption among informed people | Mark `[conventional]` and check whether the convention is genuinely shared or is doing rhetorical work as if it were. |

The failure this table exists to prevent: an inferential claim with a sound chain, or a well-supported counterfactual, getting quietly demoted to "speculative" just because it can't be empirically verified in the strict sense — when its actual epistemic support is strong. Naming the type makes the appropriate confidence visible instead of collapsing everything into "verified" or "unverified."

## Single-agent vs. paired-agent verification

**Single-agent verification** is the right tool for attribution-layer facts: does this source exist, who's the author, what year, what's the specific figure. It is cheap, fast, and reliable for lookups with a checkable answer.

It is **not** reliable for framing-layer facts on genuinely contested topics — questions where reasonable, well-informed people from different starting positions would frame things differently. A single verification agent tends to reproduce whatever framing dominates its training data and default search rankings, and a structured-looking report can make that reproduction feel like independent verification when it isn't.

The fix is **paired-agent dispatch**: run two agents in parallel with opposing briefs —

```
Agent A: "Find the strongest case FOR [position]. Cite specific sources,
including ones skeptical of the mainstream framing if applicable."

Agent B: "Find the strongest case AGAINST [position]. Cite specific
sources, including ones skeptical of the dissenting framing if
applicable."
```

Synthesize from both reports at write time — never hand synthesis to a single agent on a contested topic, since that reintroduces the same single-framing bias one layer downstream.

## Two-pass discipline on load-bearing claims

A single verification pass tends to catch whether a citation exists; it routinely misses whether the source actually supports the claim as framed. Run both passes on anything load-bearing:

- **Pass 1 — the citation is real and the numbers are right.** Does the study/paper/figure exist with the stated author, year, and magnitude? Catches wrong-author, wrong-year, wrong-magnitude errors.
- **Pass 2 — the source actually supports the framing.** Read what the source *says*, not just confirm it exists, and check whether its content backs the claim as written. Catches a source cited as playing one role (e.g. "an independent re-analysis") when it actually played a narrower one (e.g. a discussion piece), or an interpretation of a finding presented as if it were the finding itself.

Pass 2 is the harder pass — it requires reading the source, not confirming its existence. Skipping it on load-bearing claims is where confident-sounding but subtly wrong specifics get into a wiki and stay there.

## Confidence stratification

Independent of assertion type, tag conclusions by confidence so a later reader (or a later session) can tell load-bearing from provisional at a glance: `[would-bet-on]` for well-supported claims, `[verify-before-using]` for anything that hasn't cleared both passes, `[contested]` for genuinely disputed ground, `[dialogue-internal]` for something surfaced in conversation that hasn't been checked at all. The two axes cross-cut: an inferential claim tagged `[would-bet-on]` is a strong claim with a sound chain behind it, not a weak one just because it isn't empirically verifiable in the strict sense.

## Related

- [[Commander's Intent]] — the doer/checker adversarial pattern this discipline formalizes for claims specifically
- [[Feedback Loops (Universal Pattern)]] — verification is the comparator step of a feedback loop applied to knowledge
- [constitution/verification.md](../../constitution/verification.md) — this kit's operational verification protocol
- [[Agent Failure Modes]] — confident-but-wrong output is the failure mode this whole framework exists to catch
- [[Agent Orchestration]] — paired-agent dispatch as a specific orchestration pattern
