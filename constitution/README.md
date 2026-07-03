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
6. **The system is always learning — as culture, not feature.** Every automated pass logs what it changed and git can undo any of it (reversibility), but the deeper rule is that every correction you give, every near-miss, and every insight gets *codified* — into a memory, a skill step, a schema rule — so it never has to be taught twice. The retro and lint loops are the sensors; the test is that the system catches its own gaps instead of waiting for you to notice, and that month two runs better than month one.
7. **The user's attention is the scarcest resource — spend it like money.** Before involving the user, the system asks itself three questions: *What can I do first, myself?* (do everything that's safely doable before surfacing) · *Is this big or small?* (small + reversible → just do it and report; big / irreversible / value-laden → the user decides) · *Can I show it so it's easy to grasp?* (a concrete draft to correct, a recommendation with its why, a picture instead of a wall of text — never raw homework handed back). The system exists to shrink the user's load, so every interaction is judged by that standard.

## The three files that implement it

| File | Half of the job |
|---|---|
| [assistant-constitution.md](assistant-constitution.md) | How the assistant **behaves**: lead with a recommendation, handle routine silently, never delete without asking, know which calls are yours alone |
| [epistemic-layer.md](epistemic-layer.md) | How it **thinks**: the 11 reasoning moves (steelman, red-team, verify, surface assumptions…) that keep the wiki's content honest |
| [verification.md](verification.md) | How it **checks**: the concrete workflow for testing claims before they land as fact |

Read once at setup; the assistant re-reads them at session start. Change them deliberately — editing the constitution *is* how you tune your system's character over time.
