---
name: asking
description: Relentless interview that stress-tests a plan, decision or idea in rounds of clickable multiple-choice questions, recommended answer first, until nothing is left silently assumed. Other Needt skills call it in a short mode for one round of clarifying questions. Use for "спроси меня", "задай вопросы", "прожарь", "опроси меня", "grill me", "/grill-me", "/needt:asking", "stress-test this", or when a plan has several open decisions only the user can make.
---

<!-- Adapted from mattpocock/skills (grill-me + grilling), MIT License, Copyright (c) 2026 Matt Pocock -->

# Needt · Asking

## Setup check

Before the first round, look back in this conversation for a line starting with `Needt ·`.
None → apply [setup](../setup/SKILL.md): its readiness line is the first line of the reply,
costs no tool calls, and tells you whether clickable questions exist. Then start. Present →
skip it.

## Sister skills

- [critic](../critic/SKILL.md) — a plan that should be checked before launch.
- [needt](../needt/SKILL.md) — finished work lands in Needt as tasks.

## Two modes

- **Full** (the user asked to be grilled or interviewed): work the whole tree below until the
  frontier is empty.
- **Short** (another Needt skill called this to clarify a task): one round, at most 4
  questions, only the ones whose answers would change the result. Everything else becomes a
  labeled assumption. Then hand control back to the calling skill.

## Grounded recommendations

- The recommended option comes from the conversation and the open project, not a generic
  default. If the project is X and the task is about promoting it, the recommendation is X.
- Never ask a question the user's message already answers; turn it into a stated assumption
  instead.
- In short mode, if no answer would change the result, ask nothing and say so in one line.

## Full mode

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the frontier as one round, then wait for the answers before the next round.

## Ask by click, not by typing

When the `AskUserQuestion` tool is available (load it via tool search if it is deferred), every round goes through it. The user should be able to answer the whole round with clicks.

- One call = one round, up to **4 questions**. A frontier larger than 4: ask the 4 that unblock the most downstream decisions now; the rest go in the next call.
- Each question: a complete question ending with "?", a `header` chip of max 12 characters, `multiSelect: false` unless the choices really combine.
- Each question has **2-4 options**. The **first option is your recommendation**, labelled with " (Recommended)" at the end. Labels are 1-5 words; put the reasoning, numbers or trade-off in the option `description` (one short line).
- Make options real alternatives that lead to different next steps (do it / do it differently / park it / not now). Never pad with filler options and never add an "Other" option: the tool adds a free-text field itself.
- Use `preview` only when comparing concrete artifacts (copy variants, mockups, code).
- Before the call, write at most 2-3 short lines of context in chat if the facts behind the questions are not already visible. Do not repeat the questions as text.

If `AskUserQuestion` is not available, fall back to text and number each question:

```
❓ **Q1** - **<question title>**: <question body, including the choices>

➡️ <your recommended answer>
```

Word each text question so "yes" accepts your recommendation.

## Between rounds

Each round's answers reshape the tree: settled decisions push the frontier outward and unblock the questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round.

After each round, state in one line per answer what is now decided (and what you will do about it, if it is an action), then call the next round.

If the user answers with free text (the "Other" field), treat it as the decision; if it is ambiguous, the clarification goes first in the next round.

## Facts vs decisions

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (files, notes, connected tools, the web), look it up; when that needs more than a couple of calls, run it in a Sonnet sub-agent per [delegation](../setup/references/delegation.md). Never turn a lookup into a question. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

Decisions the user has already recorded as settled are not reopened unless a new fact breaks them; say so once if it does.

## Done

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Then give a short list of every decision made, and do not act on irreversible ones until the user confirms you have reached a shared understanding.