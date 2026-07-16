# Northstar

> Filled by `/setup-brain`. If your exports are already in `raw/inbox/`, setup drafts these answers from your own data and asks you to confirm-and-correct — drop data in first for a smarter setup. The private-forever section is always yours to state explicitly; it is never inferred.

The single anchor document for this second brain. Filled in once at setup (typically by the `/setup-brain` interview), revisited whenever the answers stop feeling true. This is the one file every other piece of substrate points back to — when in doubt about scope, tone, or what belongs in the wiki, the answer is here.

## First: what a Northstar even is

If you've never used the term: a **Northstar is the fixed point you steer by** — a short, honest statement of what a system is *for*, written down so that every later decision can be checked against it instead of re-argued from scratch. It's not a mission statement for show; it's a working tool. When you're unsure whether something belongs in your wiki, whether a feature is worth building, or whether the system has drifted — you read the Northstar and the answer is usually obvious. A system without one slowly becomes everything, which is the same as nothing.

Its counterpart, the **constitution** (see [constitution/](constitution/)), covers the other half: the Northstar says what the system is *for*; the constitution says how it *behaves* while getting there — the standing rules that hold from session to session so nothing important gets re-decided (or quietly forgotten) each time. Direction and discipline. You need both, and one page of each is enough.

## The worked example: the second brain's own Northstar

This kit ships with its own Northstar, so you can see the shape before writing yours:

> **Every session starts from everything you've ever fed it.** The second brain exists so that your AI reasons from your accumulated context — your thinking, decisions, sources, and history — instead of starting from zero every conversation. It must be **compounding** (each session leaves it richer than it found it), **trustworthy** (verified, contradiction-flagged, never letting opinion harden into fact), and **owned** (plain files on your machine, readable without any tool, exportable in one copy-paste). The human does judgment and direction; the AI does the maintenance that killed every second brain before it — and it **minimizes the human's load**: it does what it can before involving you, sizes what remains (is this big or small?), and presents it so the decision is easy to make. And it is **always learning**: every correction, miss, and insight gets folded back into how it works, so it keeps getting better the more you use it. The test that matters: you stop re-explaining yourself — whenever that milestone actually arrives for you.

Everything in this kit serves that statement, and anything that doesn't serve it stays out. That's a Northstar doing its job. Yours, below, *specializes* it: same system purpose, pointed at your particular life and work.

## Who this is for

{{USER_NAME}} — {{USER_ONE_LINE_DESCRIPTION}}

## What this second brain is for

{{PURPOSE_SUMMARY}}

What kind of work does this need to support — recurring deep research on a narrow set of topics? A running record of decisions on a long project? A personal archive of health/finance/life knowledge? Name it specifically; "everything" is not a scope.

## What it must do well

{{SUCCESS_CRITERIA}}

The 2-4 things that, if this second brain does them well, make the whole project worth the maintenance cost. Be concrete — "answer questions about my own past reasoning without me re-explaining it" is a criterion; "be useful" is not.

## What is private-forever

{{PRIVACY_BOUNDARIES}}

Anything that must never leave this local vault, never get pasted into a public artifact, never get summarized into a shareable form. Name categories, not just examples — the categories are what future sessions need to check against.

## The 6-level choice

Every second brain sits somewhere on a spectrum of how much is delegated to the AI vs. kept as manual practice — from pure manual note-taking up through fully autonomous ingestion and lint passes running on a schedule. See [context/the-6-levels.md](context/the-6-levels.md) for the full comparison.

**Current level**: {{CURRENT_LEVEL}}

**Why this level, not more or less**: {{LEVEL_RATIONALE}}

## Milestones — not a calendar

Progress here is checked by what's actually happened, not by how many days have passed. Some builds hit these in a week; others take longer, depending on how much you bring in and how deep the domain is — there's no clock to watch, only these to check off:

- [ ] **Setup complete** — this file written, `CLAUDE.md` filled in, a first profile page exists.
- [ ] **First real ingest** — your first genuine export (not just what was on hand at setup) processed into the wiki.
- [ ] **First re-use** — a session opens *from* something already compiled, instead of you re-explaining it. This is the core signal that it's working.
- [ ] **First self-made connection** — two sources link up on their own, something you didn't have to notice yourself. The compounding effect showing up for real.
- [ ] **First maintenance catch** — `/wiki-lint` or `/retro` catches a real gap or drift without you pointing it out.

If a milestone is taking a long time to hit, that's the thing to look at — usually it means not enough has been ingested yet, not that the system has failed. See [context/why-a-second-brain.md](context/why-a-second-brain.md) for the honest cost accounting (one documented build found time-invested roughly equaled time-saved around a month in — a data point about someone else's pace, not a schedule for yours).

## Related

- [CLAUDE.md](CLAUDE.md) — the operating schema this Northstar directs
- [context/why-a-second-brain.md](context/why-a-second-brain.md) — why this approach, and its honest costs
- [context/the-6-levels.md](context/the-6-levels.md) — the delegation-level spectrum referenced above
- [constitution/assistant-constitution.md](constitution/assistant-constitution.md) — how the assistant behaves in service of this Northstar
