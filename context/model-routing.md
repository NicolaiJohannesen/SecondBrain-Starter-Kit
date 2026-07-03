# Model Routing for a Second Brain

Which model to use for which job, when running this kit with Claude Code. Getting this right matters for two reasons: cost, and — on a subscription plan rather than pay-per-token API access — staying inside your rate-limit window during a long build or a heavy ingest session.

## Two independent axes

Model selection has two dimensions that are easy to conflate but should be set separately:

- **Tier** — which model family: a fast/cheap tier for lookup work, a mid tier for action work, a top tier for hard reasoning.
- **Effort** — how much of that tier's ceiling to spend on a given call. A capable model run at low effort is still fast and cheap; the tier sets the ceiling, the effort setting decides how close to it you actually go.

Set both deliberately per task. Don't let a sub-agent inherit the main session's model by default — that silently sends lookup work through your most expensive tier.

## Tier routing table

| Job | Model | Why |
|---|---|---|
| Read-only lookup, file/codebase search, fact retrieval, grading, classification, verification | **Fast/cheap tier** ("Haiku"-class) | This is fetch-and-compare work, not deep reasoning. A small model handles it well, and because it's cheap you can afford to run it liberally and in parallel. No adaptive/extended thinking needed for most of this work. |
| Page authoring, ingest workflows, code modification, multi-step formatted output | **Mid tier** ("Sonnet"-class) | The default for actually doing the work: writing wiki pages, running an ingest pass, editing files, producing structured output. This is where most of a build session's token spend should land. |
| Multi-file architectural reasoning, novel synthesis across disparate sources, adversarial red-teaming, hard tradeoff evaluation | **Top tier** ("Opus"-class), thinking mode explicitly enabled | Reserve this tier for work where its extra capability genuinely changes the outcome — deep cross-file reasoning, synthesizing ideas that don't share an obvious frame, evaluating a decision with real tradeoffs. Enable extended/adaptive thinking explicitly; it is often off by default on the top tier and has to be turned on. |
| Long-horizon autonomous work spanning many hours or days | **The highest available tier**, run at maximum effort | Reserve for genuinely long-horizon autonomous runs where the mid or standard top tier is measurably insufficient — this is the exception, not the default, and costs meaningfully more per token than the standard top tier. |

Rough decision test: if the task is "go find/check/confirm X," route it to the fast tier. If the task is "produce a finished artifact by following a known pattern," route it to the mid tier. If the task is "figure out how these five things relate, or which of two flawed options is less bad," route it to the top tier with thinking explicitly on.

## Sub-agent dispatch: verify liberally, escalate the ambiguous middle

The single highest-value pattern for keeping a second brain accurate without burning your budget:

1. **First-pass verification always runs on the fast/cheap tier, in parallel.** Dispatch several fast-tier sub-agents at once to fact-check claims, confirm citations exist, or classify incoming material. Because each one is cheap, you can afford to verify far more than you would if every check ran on a capable model.
2. **Escalate to the mid tier only for the ambiguous middle** — claims the fast-tier check comes back "partially verified," "contested," or "unclear" on, specifically when the claim is load-bearing (something the wiki's synthesis depends on) or when sources genuinely conflict and the fast-tier pass can't resolve which is right.
3. **Don't re-run clean results on a more expensive tier.** If the fast-tier check comes back clearly verified or clearly contradicted, that's the answer — spending more compute on an already-resolved question is waste, not rigor.

This turns verification from an expensive thing you do occasionally into a cheap thing you do by default. A second brain that only spot-checks itself will accumulate confidently-stated errors over time; one that verifies liberally at the cheap tier and escalates selectively stays trustworthy at a sustainable cost.

## Rate-limit hygiene on a subscription plan

If you're running this kit under a subscription (rather than metered API billing), token spend maps to your usage window, not your invoice — but the discipline is the same either way. Cheaper models and lower effort settings leave more headroom for the work that actually needs the top tier. Before fanning out several parallel sub-agents at the top tier, ask whether the task genuinely needs that ceiling, or whether it's lookup/action work that the fast or mid tier would handle just as well for a fraction of the spend. A build session that routes ingest and verification work correctly can run for hours; one that defaults everything to the top tier will exhaust its window in minutes.

## Related
- [context/how-to-build.md](how-to-build.md) — the ingest workflow this routing table supports
- [context/loops.md](loops.md) — scheduled and autonomous work, where routing discipline matters most because nobody is watching the spend turn by turn
