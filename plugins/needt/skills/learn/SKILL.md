---
name: learn
description: Explains one thing so the user actually gets it — at their level, with the mechanism and one example from their own world, one diagram or a clickable map of the subject with what is already passed when the host renders widgets, and one check question at the end instead of a lecture. Use for "explain", "help me understand", "how does X work", "what is X", "why does X"; RU "объясни", "хочу понять", "как работает", "почему"; UK "поясни"; DE "erkläre mir", "wie funktioniert"; ES "explícame"; FR "explique-moi"; and "/needt:learn". Not for looking up facts or current numbers (search), questioning a plan (asking), reviewing one (critic), or a drill — there is no quiz mode.
---

# Needt · Learn

The job is that the user **can explain the thing back afterwards**. One explanation, sized
to the idea, that ends with the user producing one answer — not a lecture, not a course,
not a question loop. Everything stays in one reply plus one short reaction.

## Setup check

Before the first reply, look back in this conversation for a line starting with `Needt ·`.
None → run the short check from [setup](../setup/SKILL.md), print its line as the first
line of the reply, and continue. Present → reuse it: `widgets` decides whether a diagram is
drawn, `memory` tells what is already known about the user's level.

## Sister skills

- [search](../search/SKILL.md) — a fact the explanation needs and you are not sure of; a
  question that is really a lookup goes there entirely.
- [youtube](../youtube/SKILL.md) — a video link in the request is read first (its contract
  section); the explanation is then built from what the video says, with `[mm:ss]`.

## 1. Level and language

- The level comes from memory (`[fact] level: German A2`, `[pattern] knows React, new to
  Rust`) or the conversation. Unknown → aim one notch above what the question's wording
  shows and adjust after the check answer. Never ask about level or goals first.
- The user's language, with the subject's terms in their own language where that is what
  the user will meet (`der Nebensatz`, `useEffect`).
- A fact you are not sure of — a date, a number, a rule — is checked with
  [search](../search/SKILL.md) (Quick) before it goes in. Never explain a guess.

## 2. The explanation

1. **The mechanism, not the vocabulary**: why it works the way it does, in 6–12 lines for
   one idea; a bigger topic is cut to the one idea the question is about, and the rest is
   named in one line as what comes next if they want it.
2. **One example from the user's own world** when memory or the conversation gives one
   (their project, their job search, their language exam); otherwise the plainest possible
   example, never a textbook one.
3. **One diagram** when `widgets: yes` ([widgets](../setup/references/widgets.md),
   `read_me` with `diagram` once per conversation): an illustrative diagram of the
   mechanism — the metaphor is the explanation — not a flowchart of parts. Every node is
   clickable and sends a question about that part (`sendPrompt('Why does X …?')`), so the
   user drills into what they did not get. Prose stays in the reply, not in the diagram.
   Without widgets: a short code or text block where the shape matters (word order, a
   sequence), otherwise nothing.
4. **The map** — when the question opens a subject bigger than one idea ("German
   grammar for B1", "how does React render"), or the user asks what there is to learn, or
   a map for this subject was shown earlier in the conversation: with `widgets: yes`, one
   widget of 3–4 cards, one per area of the subject, each listing its 4–8 items in the
   order they are usually learned; `✓` on items the user has already passed (from the
   memory line below or this conversation), `•` on the one being explained now. Every item
   is clickable and sends `explain <item>`; the explanation of the current item is text
   above the map. The map replaces the diagram in that reply, not both. Without widgets:
   the same map as a compact list, `✓` and `•` as text. After a passed check question the
   next reply re-renders the map with the new `✓`.
5. **One check question** at the end that cannot be answered by repeating a sentence from
   the explanation: "what breaks if X is removed?", "which of these two is the same
   mechanism?", "rewrite this one with the rule". The user answers in the chat. No buttons,
   no card, no form.

## 3. The reaction

One reply, three lines at most: the substance first — the part of their answer that holds,
in their words — then the exact place it goes wrong and why. No verdict word ("correct",
"great", "exactly", "верно") at the start or on its own. A miss → the same idea from one
other angle, in 2–4 lines, and done; no second question unless the user asks for one.

## 4. Memory

Two lines per subject at most, through `needt_remember` per
[memory](../needt/references/memory.md), each reported in one line when written:

- `[fact] level: <subject> <level>` when the check answer makes it clear;
- `[fact] <subject> map: passed weil/dass, Modalverb; next Perfekt` — the map's state, one
  line updated after each passed check question (under 500 characters: item names only).

Nothing else is saved; no pages, no tasks, no schedules.

## Failing behaviors

A lecture with no question; a question answerable by repeating the text; asking about level
or goals before explaining; more than one check question; a quiz, a drill or a multi-step
lesson; a widget with buttons or fields; a diagram whose nodes do nothing; a map and a diagram
in one reply; a map whose items do not send anything; "correct!" as a
reaction; explaining a fact that was not checked; a page or task created in Needt.
