# About These Docs

This kit treats its own documentation as part of the culture of learning it asks you to run — see [[Culture of Learning]] (`wiki/Topics/Culture of Learning.md`). Docs that quietly drift from what the code does are the same failure mode as a lesson nobody wrote down: something was learned once and then lost. So the goals below are written down, not assumed.

## Primary goal: time-to-working-brain

The number that matters most is how long it takes a new user to reach a functioning, personalized second brain **with zero outside help** — no Discord question, no support ticket, no "wait, what do I do with this file." The docs succeed when the Quickstart in `README.md` and the first `/setup-brain` + `/ingest-source` pass happen without a single question needing to be asked. Everything else below is in service of that, or it's secondary.

## Secondary goals

1. **Self-serve depth.** Any operational question — "what does this folder do," "how do I automate ingestion," "which model for which job" — should be answerable within two hops of the README: one link to the right doc, at most one more link inside it. If answering a real question takes three hops or more, that's a docs bug, not a reader failing to look hard enough.
2. **Teach the concepts by worked example, not abstraction alone.** Northstar, constitution, culture of learning — these are unfamiliar terms to most people. Every place they're introduced, this kit ships its *own* filled-in version alongside the explanation, so the reader sees the shape before writing theirs. `NORTHSTAR.md` doesn't just define what a Northstar is — it *is* one, filled in for this kit, sitting right above the template fields waiting for yours.
3. **The docs improve themselves.** A user hitting a gap is a signal, not a failure to route around silently: open an issue, and repeated questions get folded into the docs. The retro loop (`.claude/skills/retro/`) applies to documentation exactly like it applies to everything else this kit maintains — month two's docs should answer questions month one's docs didn't. A doc that never changes after it ships is a doc nobody is actually using to learn from.

## The organizing frame: Diátaxis

Documentation here follows [Diátaxis](https://diataxis.fr) — a framework built on one observation: readers approach docs in four distinct modes, each with a different need, and mixing modes inside one document serves nobody.

| Mode | Need | Where it lives here |
|---|---|---|
| **Tutorial** | Learning by doing | The README Quickstart, `/setup-brain` |
| **How-to guide** | A recipe for a specific task | The skills, `export-handout.md`, the how-to context docs |
| **Reference** | Precise, look-up-able description | `CLAUDE.md`, `wiki/_schema.md`, the `constitution/` files |
| **Explanation** | Understanding *why* | The `context/` concept docs, the `wiki/Topics/` seed pages |

**The rule: one file, one mode.** A how-to that stops mid-recipe to explain the theory behind it makes the reader lose their place; a reference doc that turns into a tutorial buries the fact someone came to look up. A tutorial that hedges with caveats and alternatives stops being something a beginner can follow blind. When a doc needs to do more than one job, it does one and *links* to the others rather than blending them — this file is itself an explanation, so it links out to the README and the constitution rather than re-teaching either.

## Design rules

- **One obvious next step per page.** Every doc ends pointing at exactly one place to go next, not a menu. This is progressive disclosure — Sweller's cognitive-load research is the underlying reason: working memory is small, and a page that reveals depth only as it's needed keeps the reader inside their capacity instead of front-loading everything they might eventually want.
- **Docs are code.** A doc-only change still goes through review; if the code and the doc disagree, that disagreement is a bug, not a style question, and gets fixed the same session it's found.
- **Trust mechanics.** A guide that fails once stops being trusted — the reader stops following steps and starts second-guessing every one. So quickstarts get tested against a real clone, not just read over. Numbers that go stale fast (model names, pricing, export-format specifics) say "verify against the vendor's page" rather than asserting a figure that will quietly rot.

## Related

- [README.md](../README.md) — the front door this document exists behind
- [constitution/README.md](../constitution/README.md) — the standing rules the docs describe
- `wiki/Topics/Culture of Learning.md` — the underlying discipline this page applies to documentation specifically
