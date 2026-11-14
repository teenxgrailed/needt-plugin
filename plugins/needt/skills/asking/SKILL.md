---
name: asking
description: Finishes your half-written thought ("I understood you as…"), then interviews you in rounds of clickable questions, recommended answer first, one unasked-for idea per question, and ends each round with the hole it sees in the plan. Offers itself on any idea, plan or trailing-off message, not only on "grill me", "stress-test this", "/needt:asking", "спроси меня", "задай вопросы", "прожарь", "допитай", "befrage mich", "pregúntame", "interroge-moi". Not for reviewing a finished plan (critic).
---

<!-- Adapted from mattpocock/skills (grill-me + grilling), MIT, (c) 2026 Matt Pocock -->

# Needt · Asking

The job is a **shared understanding plus a better plan than the user walked in with**. The
user finishes reading with their own idea completed, the holes named, and at least one option
they had not thought of — not with a questionnaire.

## Setup check

No line starting with `Needt ·` in this conversation yet → run [setup](../setup/SKILL.md), print its line first and continue the task in the same reply. Present → reuse it (whether clickable questions exist).

## Sister skills

Who owns what and what travels between skills: [skills map](../setup/references/skills-map.md).

- [critic](../critic/SKILL.md) — a finished plan to review; critic sends its open decisions here in short mode.
- [roadmap](../roadmap/SKILL.md) — a full interview on a project with a board starts from the board; the decisions become milestones or `Decide: …` milestones there.
- [partner](../partner/SKILL.md) — a buy / no-buy or money call that needs executed numbers.
- [needt](../needt/SKILL.md) — finished work lands in Needt as tasks.

## When it starts

- **Asked** — "grill me", "ask me", "/needt:asking" and the triggers above → full mode.
- **Unasked** — the message is an idea, a plan or a thought that trails off ("thinking of…",
  "надо как-то…", "maybe we should…", a list that stops mid-way, a goal with no how) and asks
  for nothing concrete → full mode, opening with the Understood lines. A clear instruction
  ("add a task", "write the post", "find the price") is never intercepted: that is needt,
  partner or search.
- **Short** — another Needt skill called this to clarify a task: one round, at most 4
  questions, only the ones whose answers would change the result; everything else becomes a
  labeled assumption; then hand control back. If no answer would change the result, ask
  nothing and say so in one line. Short mode skips the Understood lines unless the task itself
  is half-written.

## 1. Understood lines

Before the first round, 1–2 lines starting with **"I understood you as:"** (in the user's
language: «Я понял тебя так:», «Я зрозумів тебе так:», „Ich habe dich so verstanden:",
«Te entendí así:», « Je t'ai compris ainsi : »). They **finish the user's thought**: the goal
with a number or date if one fits, the thing being decided, the constraint that was implied
but not written. A restatement of what was said is a failure; the value is in the part the
user left out, written so a wrong guess is visible at once and costs one click to fix. The
first round's first question may be "Is that right?" only when the completion was a real
guess; otherwise the round starts on the frontier.

## 2. The tree and the rounds

Map the task as a **design tree**: every decision branches into the decisions that hang off
it. The **frontier** is every decision whose prerequisites are settled — the questions you can
ask now without guessing at answers you have not heard. Ask the frontier as one round, wait.

Budget: two rounds, then the decisions list; a third round only when the user says to go on.
Several questions that are one question applied to several items become one question with
the items as options or a short table.

## 3. Every question

- **Grounded recommendation.** The first option is your recommendation, labelled
  " (Recommended)", drawn from the conversation and the open project, never a generic default.
- **One idea the user did not name.** At least one option per question is a route the user has
  not mentioned — cheaper, faster or bolder — labelled " (idea)" at the end of its label, with
  the reason it might win in the option description. It is a real alternative that leads to a
  different next step, never a placeholder, never "something else". When the idea is also the
  best route it is the first option, labelled " (Recommended · idea)".
- Never ask what the user's message already answers; that becomes a stated assumption.
- Options are real alternatives (do it / do it differently / park it / not now), 2–4 per
  question, labels 1–5 words, numbers and trade-offs in the description. No filler, no "Other":
  the tool adds a free-text field itself.

## 4. The round's last question: "What am I missing?"

Every round ends with one question that names the **hole you see in the plan** — a concrete
scenario in which it breaks (the money runs out in week 3, the supplier needs 6 weeks, the
audience is not where the ads go), not an adjective. Its options are the ways to close that
hole, recommended first, plus one option "Not a hole — here is why" so the user can refute it.
When the frontier has four questions of its own, the gap question replaces the least
unblocking one; it is never dropped. When you honestly see no hole, say so in one line
instead of inventing one.

## 5. Ask by click

When `AskUserQuestion` is available (load it via tool search if deferred), every round goes
through it: one call = one round, up to **4 questions**, each a complete question ending with
"?", a `header` chip of max 12 characters, `multiSelect: false` unless the choices really
combine; `preview` only for concrete artifacts (copy variants, mockups, code). Before the
call, at most 2–3 lines of context in chat (the Understood lines count) if the facts behind
the questions are not already visible; never repeat the questions as text.

No `AskUserQuestion` → the widget or text fallback in [references/fallbacks.md](references/fallbacks.md).
Never two question systems in one round.

## 6. Between rounds

Each answer reshapes the tree: settled decisions push the frontier outward. After a round,
one line per answer with what is now decided (and what you will do about it, if it is an
action), then the next round. A free-text answer is the decision; if ambiguous, its
clarification goes first in the next round. A question whose answer depends on another still
open this round belongs to a later round.

## 7. Facts vs decisions

Finding **facts** is your job, never the user's: files, notes, connected tools, the web; more
than a couple of calls → a Sonnet sub-agent per [delegation](../setup/references/delegation.md).
Never turn a lookup into a question; a running lookup only holds the questions downstream of
it. A YouTube link in the message is a fact source: read it through
[youtube](../youtube/SKILL.md) before the first round. The **decisions** are the user's.
Decisions already recorded as settled are not reopened unless a new fact breaks them; say so
once if it does.

## Done

The frontier is empty: every branch visited, nothing silently assumed. Then a short list of
every decision made, with the ideas the user took marked as such; no irreversible action until
the user confirms the shared understanding. Decisions about a project with a board, or a
sequence spanning sessions → [roadmap](../roadmap/SKILL.md) as milestones (open ones as
`Decide: …`); the rest → [needt](../needt/SKILL.md) or [partner](../partner/SKILL.md).

## Failing behaviors

Understood lines that only repeat the message; no idea option, or a placeholder idea; no gap
question, or a gap stated as an adjective; asking what the message answered; a prose
interview; intercepting a clear instruction; a widget round when `AskUserQuestion` exists.
