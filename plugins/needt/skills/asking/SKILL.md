---
name: asking
description: Interviews you in rounds of clickable multiple-choice questions, recommended answer first, to stress-test a plan or decision until nothing is silently assumed; other Needt skills call it in short mode. Use for "grill me", "stress-test this", "/grill-me", "/needt:asking", "спроси меня", "задай вопросы", "прожарь", "опроси меня", "запитай мене", "допитай", "befrage mich", "löcher mich", "pregúntame", "interrógame", "interroge-moi", "pose-moi des questions". Not for reviewing a finished plan (critic).
---

<!-- Adapted from mattpocock/skills (grill-me + grilling), MIT License, Copyright (c) 2026 Matt Pocock -->

# Needt · Asking

## Setup check

No line starting with `Needt ·` in this conversation yet → run [setup](../setup/SKILL.md), print its line first and continue the task in the same reply. Present → reuse it (whether clickable questions exist).

## Sister skills

Who owns what and what travels between skills: [skills map](../setup/references/skills-map.md).

- [critic](../critic/SKILL.md) — a plan that should be checked before launch; critic sends
  its open decisions here in short mode.
- [roadmap](../roadmap/SKILL.md) — a full interview on a project with a board starts from the
  board; the decisions taken at the end become milestones or `Decide: …` milestones there.
- [partner](../partner/SKILL.md) — decisions that need numbers or the actual work.
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

Budget: two rounds, then the decisions list — a third round only when the user says to go on. Several questions that are one question applied to several items ("what does Free get" × memory, search, partner) become one question with the items as options or a short table, not four questions.

## Ask by click, not by typing

When the `AskUserQuestion` tool is available (load it via tool search if it is deferred), every round goes through it. The user should be able to answer the whole round with clicks.

- One call = one round, up to **4 questions**. A frontier larger than 4: ask the 4 that unblock the most downstream decisions now; the rest go in the next call.
- Each question: a complete question ending with "?", a `header` chip of max 12 characters, `multiSelect: false` unless the choices really combine.
- Each question has **2-4 options**. The **first option is your recommendation**, labelled with " (Recommended)" at the end. Labels are 1-5 words; put the reasoning, numbers or trade-off in the option `description` (one short line).
- Make options real alternatives that lead to different next steps (do it / do it differently / park it / not now). Never pad with filler options and never add an "Other" option: the tool adds a free-text field itself.
- Use `preview` only when comparing concrete artifacts (copy variants, mockups, code).
- Before the call, write at most 2-3 short lines of context in chat if the facts behind the questions are not already visible. Do not repeat the questions as text.

If `AskUserQuestion` is not available (and `widgets: yes` does not apply, see Widgets), fall back to text and number each question:

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

A YouTube link in the user's message is a fact source: read it through
[youtube](../youtube/SKILL.md) (its contract section) before the first round, so no question
asks what the video already answers.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (files, notes, connected tools, the web), look it up; when that needs more than a couple of calls, run it in a Sonnet sub-agent per [delegation](../setup/references/delegation.md). Never turn a lookup into a question. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

Decisions the user has already recorded as settled are not reopened unless a new fact breaks them; say so once if it does.

## Widgets

The round goes through `AskUserQuestion` whenever `questions: click` — that stays the first
choice. Only when `questions: text` and `widgets: yes` (per
[widgets](../setup/references/widgets.md)) does a round render as one elicitation widget
(`read_me` with `elicitation`, once): one form, up to 4 questions, each with 2-4 options as
pills or cards, the recommended option first and marked, an "Other" escape where a free
answer is plausible; the shell returns the answers as one line. Never both a widget and
`AskUserQuestion` in one round. The text fallback stays for `questions: text · widgets: no`.
Inside a sub-agent neither exists.

## Failing behaviors

A widget round when `AskUserQuestion` exists; two question systems in one round.

## Done

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Then give a short list of every decision made, and do not act on irreversible ones until the user confirms you have reached a shared understanding. Decisions about a project that has a board, or that form a sequence spanning sessions, are handed to [roadmap](../roadmap/SKILL.md) as milestones (open ones as `Decide: …`); the rest to [needt](../needt/SKILL.md) or [partner](../partner/SKILL.md) per the map.