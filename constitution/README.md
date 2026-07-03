# The constitution — what it is, and this system's own

## What a constitution even is

If the term is new: a **constitution is the set of standing rules a system runs on** — the decisions made *once*, written down, so they don't get re-decided (or silently forgotten) every session. Where the [Northstar](../NORTHSTAR.md) says what the system is *for*, the constitution says how it *behaves* on the way there. Anything an AI assistant has to "remember to do" without a written rule will eventually not be done — a constitution turns "remember to" into "this is how it works here."

## The second brain's own constitution, in six rules

This is the worked example — the standing law this kit's whole design enforces:

1. **Raw is immutable.** Original sources land in `raw/` and are never edited. The wiki is a *derived* artifact — rebuildable, auditable, always traceable back to the originals.
2. **One door in.** Everything enters through `raw/inbox/` and gets logged. No side-channel edits that the record doesn't know about.
3. **Trust is earned per claim.** Load-bearing claims get verified before they're stated as fact; evidence gets labeled (research / opinion / speculation); contradictions between sources get *named*, not silently resolved.
4. **The human judges; the AI maintains.** You curate sources, set direction, and make the calls. The AI does the filing, cross-referencing, updating, and consistency-checking — the maintenance labor that killed every pre-AI second brain.
5. **You own the artifact.** Plain markdown, git-versioned, local-first. Whatever is marked private-forever never leaves `raw/` on this machine. No platform can reprice, lock, or lose your brain.
6. **Changes are reversible and the system improves itself.** Every automated pass logs what it changed; git can undo any of it. The retro and lint loops mean the system catches its own drift instead of waiting for you to notice.

## The three files that implement it

| File | Half of the job |
|---|---|
| [assistant-constitution.md](assistant-constitution.md) | How the assistant **behaves**: lead with a recommendation, handle routine silently, never delete without asking, know which calls are yours alone |
| [epistemic-layer.md](epistemic-layer.md) | How it **thinks**: the 11 reasoning moves (steelman, red-team, verify, surface assumptions…) that keep the wiki's content honest |
| [verification.md](verification.md) | How it **checks**: the concrete workflow for testing claims before they land as fact |

Read once at setup; the assistant re-reads them at session start. Change them deliberately — editing the constitution *is* how you tune your system's character over time.
