# Building Software Projects from the Brain

How to go from an idea living in the brain to a shipped, deployed piece of software — where the code lives, how the build loop runs, and how GitHub fits in.

## Where code lives

Not inside the brain repo. The brain holds the *thinking* — a `wiki/Projects/<Name>.md` page: purpose, decisions, current status, what's next. The code for that project gets its own git repository, as a sibling directory, not a subfolder of the brain.

Each project repo gets its own `CLAUDE.md`, separate from the brain's root one. This is the same split as the assistant's own operating layer: one context file for who you are and how you work in general ([constitution/assistant-constitution.md](../constitution/assistant-constitution.md)), isolated context per project so the two don't bleed into each other. A project's build instructions shouldn't have to know anything about your calendar, and your life context shouldn't leak into a code review.

## The build loop

The discipline that actually survives contact with a real session, in order:

1. **Branch from main. Never build on it directly.** `feature/x`, `fix/x` — name the branch for what it does.
2. **Commit freely on the branch.** Branch commits are cheap and reversible — they're the safety net, not a decision that needs weighing.
3. **Test before *and* after — and for anything non-trivial, write the failing test FIRST.** A test written before the implementation is your intent, pre-committed in machine-checkable form — the one artifact an AI executor can't rationalize away after the fact, and the cheapest drift-guard in the whole system (see [[Intent-Driven Development]]: the test is the executable bottom rung of the same cascade your NORTHSTAR.md tops). Confirm the baseline is green before you touch anything, then add tests alongside new features rather than after. Test at the deployed configuration — the settings and environment the live version actually runs under — not whatever's convenient on localhost, which can hide a bug that only shows up in production.
4. **Review the actual diff, not the agent's summary of it.** An agent's description of what it did is a claim, not evidence; the diff is the evidence. For anything with a rendered surface — a UI, a page — look at the rendered result, not just the file that changed.
5. **The merge is the gate.** Merging into main is an explicit decision, made with tests green and the diff reviewed — not something that happens as a side effect of finishing a task.
6. **Deploy is a separate step, after merge, never from a work-in-progress branch.** Merge and deploy are two different decisions; collapsing them means a half-finished branch can end up live.
7. **Verify at the live URL.** Confirm the deployed thing does what you meant, not just that the build succeeded.
8. **Log it on the project's wiki page.** What shipped, what changed, what's next — the brain's copy of the project should always reflect where the code actually is.

## GitHub integration

The brain repo stays **private** — it's your life. Project repos can be public or private, decided per project on its own merits.

- `gh repo create <name> --private` (or `--public`) for a new project. See [context/external-tools-and-apis.md](external-tools-and-apis.md) for the rest of the `gh` essentials.
- Use the PR flow even solo. A pull request to yourself isn't ceremony — it's a reviewable diff and a deliberate decision point, the same discipline as the merge gate above, just made visible.

## Deploying (free tiers, mid-2026 snapshot — verify current limits on the vendor's own page before relying on this)

| Target | Best for |
|---|---|
| **GitHub Pages** | Zero-setup static sites — the site lives in the same repo as the code, no separate hosting account to manage. |
| **Cloudflare Pages / Workers** | The free-tier standout as of writing: unlimited bandwidth, 500 builds/month on Pages, 100k requests/day on Workers, and KV/D1/R2 storage with zero egress cost on R2 — a full $0 stack until you hit real scale. |
| **Vercel** | Best specifically for Next.js — the framework it's built around. |
| **Netlify** | Moved to a credit-based free tier; still solid, just budget the credits. |

Recommendation shape: static and repo-native → GitHub Pages. Anything that needs more than static hosting (functions, storage, a database) → Cloudflare Pages. Next.js specifically → Vercel. Re-verify limits before committing to one — free-tier terms move faster than this document does.

## Ship propagation

The principle worth stealing regardless of stack: **a ship isn't done when the deploy lands.** Every surface that describes the project — its wiki page, the README, any status line elsewhere — updates to match ground truth once the deploy is live. And **ground truth is the live deployed thing, never the docs describing it** — corrections flow one direction, live state to documentation, never the reverse. A quick grep for old version strings across the project's surfaces is a cheap way to prove none of them are still making a current-state claim that's gone stale.

## The brain's role while building

- **Specs and decisions get written to the project's wiki page *before* building starts.** Plan-writing pays for itself roughly fivefold in agent-driven work — the plan is what keeps a multi-step build coherent instead of drifting turn by turn. See [[Plan-Writing for AI Coding Agents]].
- **State the intent, not just the task**, the same way you'd brief a person rather than hand them a checklist — what you're trying to achieve and why, so a judgment call mid-build has something to be judged against. See [[Commander's Intent]].
- **Every build session gets journaled** — what shipped, what broke, what the fix was. That record is what a later retrospective pass reads to find the pattern behind a repeated mistake.
- **Post-mortems feed back into the loop.** A bug that recurs in a new costume is an architecture smell, not a one-off — the fix belongs one level up from where the symptom showed.

## Related
- [[Plan-Writing for AI Coding Agents]] — why the spec gets written before the build starts
- [[Commander's Intent]] — briefing intent instead of just tasks
- [../constitution/assistant-constitution.md](../constitution/assistant-constitution.md) — the general-context/project-context split this doc's CLAUDE.md rule follows
- [context/external-tools-and-apis.md](external-tools-and-apis.md) — the `gh` commands and API-calling patterns used while building
- [context/loops.md](loops.md) — the reversibility and gate discipline the build loop borrows from
