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
  - Sub-agents
  - Subagents
  - Claude Code subagents
  - Agent Teams
  - Claude Code Agent Teams
  - Multi-agent orchestration
  - Subagent vs Agent Team
  - Custom subagents
  - Built-in subagents
  - Claude Code agents
  - Paired-agent dispatch
  - Sub-agent dispatch
  - Sub-agent isolation
---

# Sub-agents and Agent Teams

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

Three coordination primitives cover almost every multi-agent need: **sub-agents** delegate a task within a single session and return a summary; **agent teams** coordinate across separate parallel sessions with shared state; **dynamic workflows** write a deterministic script that fans out tens-to-hundreds of parallel sub-agents in one session. All three are instances of the broader pattern covered in [[Multi-Agent Systems]].

## Sub-agents

A sub-agent is a specialized assistant invoked from a main session to handle a specific task. Each runs in its own context window with its own instructions, its own restricted tool set, and its own permissions — and returns only a summary to the main session. The structural value: the main session's context stays clean even when a sub-agent reads fifty files or runs a hundred searches. That work happens in the sub-agent's separate window; the main session only sees the final output.

**Compression is the actual value.** Only the result comes back to the parent — not the reasoning, not the intermediate steps. You're distilling a large amount of exploration into a clean signal without polluting the parent's context. Sub-agents can't spawn further sub-agents and can't talk to each other directly; this isn't a limitation, it's what makes the compression honest. You always know where decisions get made: the parent. Sub-agents are leaves; the parent is the root.

Sub-agents are defined as a markdown file with a name, a description, and optional fields for allowed tools, model choice, and permissions. The **description field is the routing signal** — the parent decides which sub-agent to invoke by matching the description to the task, so a vague description breaks routing. Built-in sub-agents ship ready to use: a fast read-only search agent for codebase exploration, a read-only research agent for planning, a general-purpose agent for complex multi-step tasks, and narrow config-generation agents for specific commands.

**When to reach for one**: a side task would flood the main conversation with search results, logs, or file contents you won't reference again — codebase research, a focused review, an isolated validation pass, anything that requires reading many files for a single decision.

## Agent teams

Agent teams are a different mechanism: multiple sessions running in parallel, each in its own context window, coordinating through a shared task list on disk rather than through direct messages. One session acts as team lead; the others are teammates that pick up tasks, report progress, and can challenge each other's findings. This is genuinely concurrent (several sessions actually running at once) rather than sequential (a sub-agent runs, returns, the main session resumes). Use agent teams when teammates need to share findings and coordinate on their own — parallel research and review, new modules where teammates own separate pieces, or debugging with competing hypotheses tested side by side. Use sub-agents instead when you just need a quick, focused worker that reports back.

## Dynamic workflows — the orchestration-scale primitive

Dynamic workflows are a step up again: instead of delegating one sub-agent at a time or running a few parallel sessions, the model writes an orchestration *script* that fans out tens-to-hundreds of parallel sub-agents in a single session, checks their work adversarially, and folds in only what survives. The defining move is coordination living outside the conversation, in deterministic code rather than turn-by-turn improvisation — which is what lets a workflow span hours to days and resume cleanly after an interruption. A flagship real-world case: an engineer used this pattern to port a large codebase from one systems language to another — roughly 750,000 lines, eleven days from first commit to merge, with parallel agents writing behavior-identical ports of hundreds of files and two independent reviewers checking each one.

## Split by context, not by role — the critical anti-pattern

The common failure mode in multi-agent design is splitting work by role — planner, implementer, tester. It feels organized but creates a telephone game where information degrades at every handoff. Split by context instead: the question isn't what role work belongs to, but what information a subtask actually needs. If two subtasks need deeply overlapping context, they belong to the *same* agent; only split where the interfaces are genuinely clean.

## When not to use multi-agent

Many elaborate multi-agent pipelines have been replaced by better prompting on a single agent with equivalent results. Start with one agent; add complexity only when you can measure that it's needed. Multi-agent is the wrong call when agents constantly need to share context (the handoff cost exceeds the parallelism gain), when the task is simple enough for one well-prompted agent, or — for coding work specifically — when parallel agents would write code simultaneously and make incompatible assumptions that conflict at merge time. The safer split for coding: sub-agents explore and answer questions; the main session writes the code.

## Distinguishing sub-agents, skills, and slash commands

Three mechanisms that look similar but solve different problems:

| Mechanism | Triggered by | Best for |
|---|---|---|
| Slash commands | The user typing a command | Deliberate, repeatable user-invoked actions |
| Skills (see [[Agent Skills]]) | The agent judging task relevance | On-demand workflows that load progressively |
| Sub-agents | The agent delegating a sub-task | Context-isolated focused work that returns a summary |

A skill *teaches* the agent how to do something; a sub-agent *delegates the doing* to a separate context; a slash command *gives the user a button* for a known operation. In practice all three compose — a command can invoke a skill that delegates parts of its work to sub-agents.

## Common failure modes

Vague task descriptions cause sub-agents to duplicate each other's work or take the wrong task — give each one a clear objective, expected output format, and explicit boundaries on what *not* to cover. A verification sub-agent that produces approval without actually running checks is worse than no verification at all, because it manufactures false confidence — write explicit instructions ("run the full suite, cover these specific cases, don't mark complete until each passes"). And token cost compounds faster than expected in multi-agent workflows — route routine work to faster, cheaper models and watch the spend.

## Related
- [[Multi-Agent Systems]] — the broader architectural pattern this page is one implementation of
- [[Agent Skills]] — the on-demand workflow layer, a complementary mechanism
- [[Agent Orchestration]] — coordinating multiple agents once more than one is in play
- [[Context Engineering]] — sub-agent isolation is a canonical context-isolation technique
- [[Agent Failure Modes]] — the broader taxonomy these common failure modes belong to
- [[The Harness Is the Product]] — sub-agent isolation as one row of a full agent harness
