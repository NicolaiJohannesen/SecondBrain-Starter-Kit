# Loop Engineering for a Second Brain

The discipline of building autonomous loops that let maintenance work run itself, so you stay at the judgment layer instead of doing the same mechanical task by hand every session. The shift: you stop prompting an AI assistant turn-by-turn for routine work and start writing the loop that runs the workflow on its own — the harness, not any single prompt, becomes the thing that compounds.

## What a loop is made of

A loop is a repeatable unit of work the system runs without a human in the inner cycle. The building blocks:

- **Scheduled agents** — work that fires on a timer (an inbox sweep, a health-check pass) rather than on a human prompt.
- **Verifier / checker sub-agents** — a second, independent pass checks the first pass's output against an objective standard, so quality doesn't depend entirely on the first pass being right. The checker should not be the same run that produced the work.
- **Skills** — versioned, callable workflows, so a recurring procedure (how to ingest a source, how to run a health check) is written once and invoked by name instead of re-derived from scratch each session.
- **The persistent-state substrate** — the wiki itself, which the loop reads from and writes back to, so knowledge compounds across runs instead of resetting each time.
- **Objective gates** — an automated check (a test, a count, a predicate) that passes or fails a step deterministically, replacing manual review on the routine, low-stakes cases.

The irreducible human job across all of this: set the direction, make the calls a gate can't make for you, and curate what the loop is allowed to feed on.

## The autonomy spectrum

Loops aren't one shape — they span a spectrum, and placing a task on it tells you which mechanism to build:

1. **Research-frontier loops** — experiment-driven systems that try something, measure the result, and keep what worked. Highest autonomy, least predictable outcome per run.
2. **Bounded multi-day goals** — a single, verifiable end condition the system works toward over hours or days. Reliable specifically *because* the end state is checkable in the transcript.
3. **Interval exploration or polling** — re-running a prompt on a schedule, either checking a state (is the deploy healthy?) or exploring an open-ended question you wouldn't have thought to ask yourself.
4. **Daily minutiae automation** — the low end: inbox triage, routine document generation, repetitive scans. Scheduled, repetitive, high-volume, low-stakes per run.

**Autonomy is a dial, not a switch.** A loop doesn't have to run start-to-finish unattended. Draft-not-send — have the loop prepare an email, a message, a page edit, and hold the final irreversible action for a human to approve — is the same discipline as keeping a human on the one step in any process that can't be undone. Automate up to the last reversible step; keep a person on the irreversible one.

## The 4-condition test — when a loop actually pays off

Building a loop has a fixed setup cost. It only pays back when the task is loop-shaped — meaning **all four** of the following hold:

1. **It repeats.** The task recurs, ideally at least weekly, so the build cost amortizes over enough runs.
2. **The output is gate-able.** Something objective can check whether the output is acceptable — not just human taste, which a script can't evaluate.
3. **Inputs are stable.** The shape of what comes in doesn't change every single run, or the loop breaks more often than it saves you work.
4. **Failure is tolerable.** A bad run gets caught by the gate, or is cheap to revert — not catastrophic and not silent.

If any one of these fails, do the task manually. Building the loop first burns exactly the attention it was supposed to save you.

## Manual first, then processize, then loop

The correct build sequence — and the standard mistake is skipping straight to step three:

1. **Manual.** Do the task by hand a handful of times. Learn its real shape: what varies, what's actually fixed, where the edge cases live.
2. **Processize.** Once the shape is stable, write it down as a repeatable procedure — a skill, a checklist, a script — so it stops being re-derived from memory each time.
3. **Loop.** Automate it behind a schedule and a gate, but only after it passes the 4-condition test above.

This mirrors the general pattern of proving something works by hand before productizing it. It's also why the first pass at anything genuinely new in a second brain — a new data source, a new kind of page, a new cross-referencing convention — should be done manually a few times before any of it gets automated.

## The concrete mechanics in Claude Code

Claude Code ships several native mechanisms for keeping work going without prompting each step. Which one to reach for comes down to three questions:

1. **What starts the next unit of work?** A condition being unmet, a fixed time interval, or an external event.
2. **Does it need to survive the session — or the machine — being closed?** In-session only, versus something durable that keeps running unattended.
3. **Does it need your local files?** Local execution versus a fresh, isolated clone with no access to your working directory.

Answering those three picks the mechanism:

- **A goal-style command** sets a completion condition and the assistant keeps taking turns until it's met, without you re-prompting each step. The critical design constraint: the condition must be something the assistant's own output can *demonstrate in the transcript* — a test passing, a file count, an empty queue — not something unverifiable like "the writing is good." Add a turn or time cap in the condition itself to bound runaway cases ("...or stop after 20 turns").
- **An interval-based loop command** re-runs a prompt on a schedule while a session stays open — either a fixed interval you set, or one the assistant picks dynamically based on how active the situation looks. This is the right tool for polling something (is the deploy still healthy?) or for running a broad, open-ended exploration prompt at intervals and letting the assistant surface directions you might not have thought to look in yourself.
- **Cloud-managed scheduled routines** run on the provider's infrastructure rather than your machine, so they keep working when your laptop is closed. The tradeoff: each run works from a fresh clone with no access to your local files, so anything that needs to read or write your actual wiki repository needs that repository configured as a routine target, not assumed to be the local folder on your desk.
- **Local scheduled tasks** run on your own machine on a timer, with full access to local files, but only while the machine is on.

A useful practitioner finding, independently reported by more than one source: bounded, verifiable goal-style loops are the more reliable mechanism of the two, and can reliably run for multiple days at a stretch — provided the completion condition is genuinely checkable, which circles back to the 4-condition test above. Verification is what makes a long-running loop trustworthy; two independent lines of practice converge on that same point.

## The maintenance loops a second brain needs

These are the recurring jobs worth wiring up once each has been done manually a few times and passes the 4-condition test:

| Loop | Cadence | Mechanism |
|---|---|---|
| Inbox sweep and ingest | daily, or every session start | manual first → a named skill → a scheduled task once proven |
| Daily journal | continuous, every session | written as part of normal session work, not a separate automation |
| Health check (orphaned pages, stale claims, contradictions, gaps) | every 5–10 sessions | a skill — the only real defense against a wiki going silently stale |
| Re-export reminders | quarterly | a calendar reminder, or a cloud-scheduled routine (survives the machine being off) |
| Self-improvement review | end of every substantive session | a skill that reviews what corrections you had to give the assistant and codifies the pattern so it doesn't recur |

## The reversibility rule

Every autonomous run should log what it changed. Git makes any of it revertible essentially for free — commit after every session, or have the loop itself commit its own changes with a clear message. Anything outward-facing (a message to another person, a public post) should be drafted and held for your review, never sent automatically — the same discipline as the merge gate in software development: automate all the way up to the last reversible step, and keep a human on the one action that can't be taken back.

## Related
- [context/how-to-build.md](how-to-build.md) — Step 5 wires these loops into the build; Step 6 is the compounding discipline they support
- [context/model-routing.md](model-routing.md) — which model tier a loop's sub-agents should run on, since nobody is watching the spend turn by turn on a scheduled run
