# Verification

How claims get checked before they land in the wiki as settled fact. This operationalizes Move #7 (verify the facts) from `epistemic-layer.md` specifically for wiki-writing work. Accuracy matters more than the token cost of checking — verify by default, not only when something feels suspicious.

## Verify by default, escalate only the ambiguous middle

- Use fast, cheap sub-agents in parallel as the first-pass verifier for straightforward fetch-and-compare checks (does this study exist, does this quote match, is this figure right). This is retrieval work, not deep reasoning — a lightweight model handles it well, and cheapness is what makes liberal verification affordable at all.
- Escalate to a stronger model only when the first pass comes back *partially verified*, *contested*, or *unclear* on a load-bearing claim, or when sources genuinely conflict and provenance is unclear. Clean verifications and clear contradictions don't need a second look — the escalation budget is for the ambiguous middle specifically.
- For a large verification pass (more than ~10 claims, or a full lint sweep across many pages), state the scope up front before running it.

## Two passes on load-bearing claims

A single verification pass catches whether a citation exists. It routinely misses whether the source actually supports the claim as framed. Run both passes on anything load-bearing:

**Pass 1 — citation is real, numbers are right.** Does the cited study/paper/figure exist, with the stated author, year, journal, and magnitude? This catches wrong-who, wrong-how-much, wrong-year, wrong-journal — the class of error where the citation exists but some detail was misremembered or transposed.

**Pass 2 — the source actually supports the framing.** Read what the source *says*, not just confirm that it exists, and check whether its actual content supports the claim as written. This catches a different class of error: a source cited as playing one role (e.g., "an independent re-analysis") when it actually played a different one (e.g., a discussion piece referencing someone else's re-analysis), a polemical framing presented as settled fact, or an interpretation of a finding presented as if it were the finding itself.

Pass 2 is the meaningfully harder pass — it requires reading the source, not just confirming it exists. Don't skip it on load-bearing claims even when Pass 1 comes back clean; a citation being real says nothing about whether it's being used honestly.

## Paired-agent dispatch on contested topics

Single-agent verification is fine for attribution-layer facts: does the paper exist, who's the lead author, what year, what's the specific number. It is not reliable for framing-layer facts on genuinely contested topics — a single agent tends to reproduce whatever framing is most prevalent in its training data and in default search-engine ranking, and that reproduction can feel like independent verification when it isn't.

For contested topics — where reasonable, well-informed people from different starting positions would frame the question differently — run two agents in parallel instead of one:

- **Agent A**: "Find the strongest case *for* [position]. Cite specific sources, including ones skeptical of the mainstream framing if applicable."
- **Agent B**: "Find the strongest case *against* [position]. Cite specific sources, including ones skeptical of the dissenting framing if applicable."

Synthesize from both reports at write time. Don't hand synthesis to a single agent on a contested topic — that's exactly where the single-agent framing bias re-enters.

**Then verify the paired output itself.** Paired-agent dispatch fixes the framing problem, but both outputs still need attribution-axis fact-checking — overstated effect sizes, miscited journals, misattributed institutional roles, and polemic-dressed-as-fact show up reliably in agent-generated research even when the framing balance is good. Dispatch a lightweight verification pass on the most load-bearing 6-8 assertions in each report before treating either as ground truth.

**Diagnostic for whether a topic counts as contested**: would thoughtful people from genuinely different starting premises land on different framings here? If yes, paired-agent dispatch. If the only open questions are attribution details (dates, names, specific figures), single-agent verification is enough.

## Evidence labeling

Distinguish, in the prose itself, between empirical (research-backed), expert opinion, and speculation. Use qualifying language for anything resting on a single source or a single study: "X argues...", "one study found...", "reportedly...". Don't let a claim harden into unqualified fact over time just because it's been sitting on a page unchallenged.

## Contradiction flagging

When sources disagree, the correct move is not to silently pick the more recent or more authoritative-sounding one, and not to present both without comment either. Add a small in-page section that names the contradiction explicitly, states both claims, cites both sources, and notes any relevant differences in recency or evidence quality. This is especially important on any topic where someone might encounter an older, superseded figure later and need to understand how the picture changed.

## Related

- [epistemic-layer.md](epistemic-layer.md) — Move #7 (verify the facts) and Move #8 (symmetric application), which this page operationalizes for wiki content
- [assistant-constitution.md](assistant-constitution.md) — the behavioral layer this verification discipline runs inside
- [../wiki/_schema.md](../wiki/_schema.md) — where evidence labeling and contradiction flagging show up in the actual page format
