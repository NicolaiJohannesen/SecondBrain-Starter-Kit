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
  - AI agent
  - LLM agent
  - autonomous agent
  - agentic system
  - Agent loop
  - Tool use
  - Tool calling
  - Agentic workflow
  - Augmented LLM
  - Agent architecture
---

# AI Agents

> Kit-seed page — shipped with the Starter Kit as part of your brain's starting knowledge. It is yours now: edit, extend, or delete it freely.

An AI agent is a software system that independently accomplishes tasks on a user's behalf. Unlike a chatbot that answers single queries, or a script that executes fixed steps, an agent combines a large language model with tools, persistent memory, and structured instructions to reason, plan, and act autonomously over multi-step workflows — deciding its own next action at each step based on the current state, looping until an exit condition is reached.

## Core architecture

Every agent rests on three pillars:

**Model** — the reasoning engine. Handles task decomposition, tool selection, error recovery, and final synthesis. The canonical approach is to prototype with the most capable model available to establish a performance ceiling, then replace individual steps with smaller, faster models where accuracy allows.

**Tools** — the effectors. Agents call external functions and services to retrieve information or take action. Three types recur: *data tools* (retrieve context — search, database queries, document retrieval), *action tools* (change state — send a message, update a record, run code), and *orchestration tools* (other agents, exposed as callable functions). Tools should be documented as clearly as a public API, because the model reads the description to decide when and how to use it — ambiguous tool definitions are a leading cause of agent failure (see [[Agent Failure Modes]]).

**Instructions** — the behavioral specification, best written as numbered lists with explicit conditional logic for edge cases. Dense policy documents should be distilled into step-by-step routines rather than fed to the model verbatim.

## The agent loop

An agent run is a loop: the model receives inputs (the request, tool results, memory), produces a response or a tool call, the tool executes, the result comes back, and the cycle repeats. Common exit conditions: a designated "final output" is invoked, the model responds without calling any tool, an unrecoverable error occurs, or a maximum iteration count is reached. This loop structure is the same whether the system is a single agent or a coordinated network of agents (see [[Multi-Agent Systems]]).

## When to use an agent

Agents earn their overhead on three problem types: **complex decision-making** that requires contextual reasoning rather than rule lookup; **unmanageable rule systems** with too many exceptions to codify deterministically; and **unstructured data** — natural language, varied document types, images. Agents are the *wrong* choice for simple, deterministic tasks — a scheduled message, a fixed database insert — where the overhead of a reasoning loop adds cost and latency without benefit. Start with a single call and good prompting; add agentic complexity only when simpler approaches measurably fall short.

## Workflow patterns

Five building-block patterns appear across production systems and can be combined:

| Pattern | Structure | When to use |
|---|---|---|
| Prompt chaining | Sequential calls; each processes the prior output | Task decomposes into fixed, ordered subtasks |
| Routing | A classifier directs input to a specialized handler | Distinct input categories need different handling |
| Parallelization | Concurrent subtasks aggregated programmatically | Independent subtasks, or multiple perspectives wanted |
| Orchestrator-workers | A central agent dynamically decomposes and delegates | Subtasks aren't predictable upfront |
| Evaluator-optimizer | A generator and an evaluator loop until quality holds | Iterative refinement against clear criteria |

## Single-agent vs multi-agent

Single-agent systems handle surprisingly complex tasks by accumulating tools, and are simpler to evaluate, debug, and maintain — maximize a single agent's capabilities before splitting. Splitting pays off when prompts with many conditional branches become unmanageable, tool sets grow too large for reliable selection, or genuinely parallel specialized execution is needed. Two patterns dominate: a **manager** pattern, where a central agent coordinates specialists via tool calls and retains context throughout; and a **handoff** pattern, where agents transfer full ownership of a task to a peer. See [[Multi-Agent Systems]] and [[Agent Orchestration]] for the deeper treatment.

## Personal AI systems and context isolation

A distinct failure mode shows up in personal setups where one person uses the same agent across multiple long-running projects: **context bleed**. Without isolation, one project's vocabulary, recent decisions, and tone requirements pollute another session. The bleed compounds — as the agent accumulates more context across more projects, reliability degrades exactly when accumulated knowledge should be making it better. The structural fix is per-project instruction files that isolate context at the session level, with one root-level file carrying identity and global conventions. See [[Personal Context Layer]] for the memory architecture this operates within.

## Guardrails and safety

Autonomous agents can compound errors, expose private data, or take irreversible harmful actions. Effective guardrails are layered: a relevance classifier keeps responses in scope, a safety classifier detects jailbreaks and prompt injection, a PII filter prevents exposing personal data, tool risk scoring rates each tool by reversibility and impact and triggers human approval for high-risk actions, and output validation checks responses against a schema. Human-in-the-loop escalation is essential for repeated failures below a confidence threshold, high-stakes actions, and agent-flagged ambiguity.

## Interoperability infrastructure

Two open protocols are becoming the plumbing of the multi-agent ecosystem: the [[Model Context Protocol (MCP)]] standardizes how agents connect to data sources and tools, replacing bespoke integrations with a universal client-server protocol; the Agent2Agent Protocol (A2A) standardizes how agents from different vendors hand off tasks to each other. MCP handles the agent-to-world connection; A2A handles agent-to-agent collaboration.

## Practical applications

Customer support (classify intent, query knowledge bases, escalate to humans), coding agents (plan edits across files, run tests, iterate), research and analysis (multi-source gathering, synthesis, report generation), and business-process automation (onboarding, compliance review, procurement) are the recurring production categories.

## Related
- [[The Harness Is the Product]] — the synthesis frame: the operational substrate around the model is the moat, not the model alone
- [[Multi-Agent Systems]] — when splitting into multiple agents pays off, and when it breaks
- [[Agent Orchestration]] — coordination patterns once you have more than one agent
- [[Agent Failure Modes]] — the named taxonomy of production failures
- [[Personal Context Layer]] — the memory architecture agents read from and write to
- [[Model Context Protocol (MCP)]] — the standard for connecting an agent to tools and data
