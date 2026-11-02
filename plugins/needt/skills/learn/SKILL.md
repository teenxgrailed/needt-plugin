---
name: learn
description: Teaches the user something so it sticks — not a lecture. Three modes the user picks at the start: Explain (one clear explanation at their level, ending in one check question), Study (the topic cut into steps, each with a question the user must answer before the next), Drill (rapid questions on what they already know, with a score). Each step is an interactive card when the host can render widgets, a clickable question otherwise. Progress lives in Needt — a page per topic and a review task a few days later — so the next session starts where the last one ended. Use for "explain", "teach me", "help me understand", "how does X work", "learn", "quiz me", "test me"; RU "объясни", "научи", "хочу понять", "как работает", "выучить", "проверь меня"; UK "поясни", "навчи"; DE "erkläre mir", "bring mir bei", "abfragen"; ES "explícame", "enséñame"; FR "explique-moi", "apprends-moi"; and "/needt:learn". Not for looking up facts (search), questioning a plan (asking) or reviewing one (critic).
---

# Needt · Learn

The job is that the user **can do or explain the thing afterwards**. A clear text they nod
along to and forget by tomorrow is the failure this skill exists to kill. So every mode ends
with the user producing something — an answer, an explanation, a prediction — and the skill
reacts to what they produced.

## Setup check

Before the first reply, look back in this conversation for a line starting with `Needt ·`.
None → run the short check from [setup](../setup/SKILL.md), print its line as the first
line of the reply, and continue. Present → reuse it: `widgets`, `questions` and `memory`
decide how steps are shown and what is already known about the user.

## Sister skills

- [search](../search/SKILL.md) — a fact the explanation needs and you are not sure of.
- [youtube](../youtube/SKILL.md) — a video link in the request is read first (its contract
  section); the lesson is then built from the transcript, with `[mm:ss]` on each step.
- [needt](../needt/SKILL.md) — where progress is kept.

## 1. Pick the mode

Order before the first reply: the setup line, then — with a Needt connector —
`needt_search` for the page `Needt · Learn · <topic>`. Page found → no mode question: continue its mode from its next
step, the misses first (`needt_get` on the page for its body). On a first run (setup's
onboarding is in the same reply) ask no mode question: start in the mode the table
recommends and say in one line how to switch.

Explain needs no question: "explain", "how does X work", "what is X", "объясни" go straight
to §3; a teach/learn verb in the same sentence ("teach me how X works", "научи, как
работает") wins and means Study. Ask which mode only when the wording fits both Study and Drill ("help me learn X",
"I want to get good at X"), and then ask that one thing — through a widget (`widgets: yes`),
`AskUserQuestion` (`questions: click`), or a three-line text choice, recommended first:

| User says | Recommended | What it is |
|---|---|---|
| "explain", "how does X work", "what is X" | **Explain** | one explanation at their level, one diagram if the host renders widgets, one check question at the end |
| "teach me", "I want to learn", "help me get X" | **Study** | 3–7 steps; each step = a short piece → a question → the user's answer → the reaction; no next step until this one is passed, or given after two misses |
| "quiz me", "test me", "drill", a language, formulas, vocabulary | **Drill** | questions only, on what they already know; timed rounds of 5–10, a score, the misses repeated |

Skip the question also when memory says which mode the user prefers for this kind of
topic. Never ask a second question before the first step — level, goal and prior knowledge
come from memory, the conversation and the first answer, not from an interview.

## 2. Level and language

- The level comes from memory (`[fact] level: German A2`, `[pattern] knows React, new to
  Rust`), from the conversation, or from the first answer. One wrong guess is cheap; an
  interview is not. Adjust after every answer: a correct answer in one try → the next step is
  harder or shorter; a miss → the same idea from another side, not the same text again.
- The lesson is in the user's language. A topic that is itself a language (German words,
  Spanish verbs) uses that language in the questions and the user's language in the
  explanations.
- Facts you are not sure of — a date, a number, a rule — are checked with
  [search](../search/SKILL.md) (Quick) before they go into a step. Never teach a guess.

## 3. Explain

1. One explanation, at most as long as the idea needs: usually 6–12 lines. The mechanism,
   not the vocabulary; one concrete example from the user's own world when memory or the
   conversation gives one.
2. With `widgets: yes`, one diagram of the mechanism (the `diagram` module — illustrative
   for "how does it work", structural for "what is inside"), after `read_me`. Prose stays in
   the reply.
3. End with **one** check question the user cannot answer by repeating a sentence from the
   explanation: "What breaks if X is removed?", "Which of these two is the same mechanism?".
   Wait for the answer, react in two or three lines, done. The reaction starts with the
   substance: the part of their answer that holds, in their words, then the exact place it
   goes wrong and why. No verdict word ("correct", "great", "exactly", "верно") at the
   start or on its own.
4. Offer in one line to switch to Study if the answer shows a gap worth closing.

## 4. Study

1. Cut the topic into **3–7 steps**, each one idea that can be checked with one question.
   Show the plan once as one text line in the user's language (`Steps: 1 ● 2 ○ 3 ○ …` is
   the shape), then start step 1 in the same reply.
2. Each step is one reply:
   - the piece: 3–8 lines, one idea, one example;
   - the question, in one of these shapes — rotate, never the same shape twice in a row:
     `predict` ("what happens when…"), `find the error` (a wrong example to spot), `explain
     back` ("tell me in your words why…"), `apply` ("do it with these numbers / this
     sentence"), `pick` (options in random order, one right, the distractors are real mistakes, none
     marked recommended), `what
     breaks` ("what fails if we drop X");
   - shown as a card with answer buttons or a text field (`widgets: yes`); without widgets,
     a `pick` question goes through `AskUserQuestion` when `questions: click`, everything
     else as text.
3. React to the answer, not to the step: the substance first — the part that holds, in
   their words, then the exact place it goes wrong and why — three lines at most. No verdict
   word at the start; a right answer gets one line on why it is right and the next step. A miss → the same idea from a different angle (a new
   example, the reverse question), then ask again. Two misses → say what the gap is in one
   line, give the answer, move on, and mark the step for review.
4. A step ends one of two ways: **passed** (right in their own words) or **given** (two
   misses, answer shown). Only passed steps count on the page; given steps go to the misses
   and come back first next session. After the last step: a 3-line recap of what they can
   now do, and the review task (§6).
5. Pace: one step per reply. Never two steps at once, never the whole lesson in one message.

## 5. Drill

1. A round is 5–10 short questions — a word to translate, a form to fill in, a formula to
   apply, a case to classify — mixed, not grouped by type (interleaving). **One round is
   one reply, never one question per reply**: the user answers the whole round, then gets
   one reply with the score, the misses with the right answer and one line of why for
   each, and a one-line offer — another round on the misses, or stop.
2. `widgets: yes` → the whole round in one widget: every question with its options or
   field, checked in the widget's own JS against the answers you put in it, a running
   score, and one button at the end that sends a single line through `sendPrompt`:
   `Round 1: 7/10 · missed: 3 (habe → bin), 6 (meine → meinem), 9 (…)`. No timer, no
   per-question round trip, no explanation inside the widget — the "why" comes in the
   reply after the round. Keep the markup small: plain inputs and buttons, no library.
3. `widgets: no` → all questions of the round in one message, numbered; the user answers
   them in one message (`1 bin, 2 meinem, …`); then the same single reply with score and
   misses. `AskUserQuestion` is not used for Drill (one question per call would be the
   same slow loop).
4. Every miss returns in the next round in a different form. Nothing new is taught in
   Drill; a gap that is a missing concept gets one line and an offer to switch to Study.

## 6. Progress lives in Needt

All of it reversible in the Needt app; each write is reported in one line, following [needt](../needt/SKILL.md) and
[memory](../needt/references/memory.md):

- **A page per topic**: `Needt · Learn · <topic>` in the personal workspace — `needt_search`
  for it first; create with `needt_create_page` when the first step ends (so an abandoned
  lesson still leaves its page), `needt_append_page` at the end of the session and of every
  later one. One block per session: date, mode, steps passed, the misses with the right
  answer, the next step. A new "learn <topic>" starts by reading this page and continues
  from the next step; the misses come back first.
- **A review task** after Study, and after a Drill round with misses: one task titled in
  the user's language as a verb plus the topic ("Review German articles", "Повторить
  немецкие артикли") — `needt_create_task` with `deadline` 3 days out (7 when the session
  had no misses), no `start`, so the scheduler places it; the misses in the description,
  ending with `Open with /needt:learn <topic>`; no subtasks; `deadline` as an ISO date in
  the user's time zone. A session that starts on a topic with an open review task
  (`needt_search` for it alongside the page) is the review: it runs the misses first, then
  completes that task with `needt_complete_task` and creates the next one (deadline 7 days
  out, 14 after a review with no misses). The task follows the needt skill's task rules: short,
  nothing in the title but the action.
- **Memory**: the user's level in a topic (`[fact]`) and a preferred mode seen twice
  (`[preference]`) through `needt_remember`; one line each. Never the content of the lesson.
- **No connector** → progress holds for this chat only; say so once (not again if setup
  already did), keep teaching. At the end, instead of the task: the misses as a short block
  to paste, and the review date 3 days out, in one line.

Never write "saved" or "task created" without a successful call.

## 7. Widgets

With `widgets: yes`, follow [widgets](../setup/references/widgets.md). For this skill:

- `read_me` once per conversation, before the first widget (the mode picker, if any), with
  `interactive`, `diagram`, `elicitation`, and `chart` when the topic has numbers that
  grow or compare.
- One widget per reply. In Explain the diagram is the widget and the check question is
  text. In Study the step card is the widget and carries the step dots; the plan line stays
  text.
- A Study step card holds: the question, the answer controls, the step position (`3 of 6`)
  and nothing else — the piece of teaching stays in the reply above it. A Drill round is
  one widget for the whole round (§5), the cheapest shape: the chat sees one message in
  and one out per round.
- Buttons send the user's answer as they would say it (`sendPrompt('Answer: B — the loop
  never ends')`), plus at most one action button (`Next step`, `Repeat this step`, `Another
  round`). A free-text answer uses a field with a submit button that validates it is not empty.
- Progress lives in the step card's dots; no separate progress widget in the same reply.
- A sub-agent never renders widgets.

## 8. Sub-agents

Rarely. A long source to teach from (a document, a long transcript) → one Sonnet sub-agent
extracts the ideas in order per [delegation](../setup/references/delegation.md); the cutting
into steps, the questions and every reaction to the user's answers happen here, with the
conversation.

## Failing behaviors

A lecture with no question; a question answerable by repeating the text; two steps in one
reply; "correct!" with no substance; the same question shape three times in a row; the same
wording repeated after a miss; an interview about level and goals before step 1; teaching a
fact that was not checked; a review task pinned with `start` or with a prefix in its title; a page that duplicates an
existing one; progress claimed saved without the call; widgets mentioned in a host without
them; moving on after a miss without a second angle; Drill that teaches; Drill one question per
reply; a timer; Explain that never ends.
