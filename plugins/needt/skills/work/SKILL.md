---
name: work
description: Works through your Needt tasks with you, one at a time. Checks if each is already done, does everything it can itself, asks only for a decision or a physical action. Use for "let's work", "work through my tasks", "/needt:work", "погнали", "давай делать задачи", "поїхали", "що робити", "lass uns loslegen", "Aufgaben durchgehen", "trabajemos", "au travail". Not for adding one task (needt) or a multi-session plan (roadmap).
---

# Needt · Work

The job is an empty list at the end, not a list of questions. Claude walks the person's tasks one at a time, does what it can reach itself, and asks the person only for what only they can give. It keeps running while they answer.

## Setup check

No line starting with `Needt ·` in this conversation yet → run [setup](../setup/SKILL.md), print its line first and continue in the same reply. Present → reuse it (`questions`, `widgets`, `agents`).

No Needt connector → say once that the loop needs it (it comes with Pro) and offer the same walk as text on the tasks the person pastes; never claim a task closed.

## Sister skills

Who owns what and what travels between skills: [skills map](../setup/references/skills-map.md).

- [needt](../needt/SKILL.md) — every read and write of tasks, pages, memory; its title and permission rules apply.
- [search](../search/SKILL.md) — a task that is a lookup; Quick per task, the evidence back as one line.
- [partner](../partner/SKILL.md) — a task that is a business decision; it does the numbers, the verdict comes back.
- [asking](../asking/SKILL.md) — the one question per task, in short mode.
- [roadmap](../roadmap/SKILL.md) — a task that is a milestone of a board: closing it needs the board's evidence rule.
- [critic](../critic/SKILL.md) — a task that is a plan about to go live.

## 1. Start

1. `needt_whoami` once; then `needt_schedule` (`run: false`) and `needt_day_plan` for today.
2. Show the days once. `widgets: yes` → one chart widget (bars per day, the limit as a line, overloaded days marked). Otherwise a compact table `day | tasks | load | over limit` with overload marked `▲`. The numbers come from the calls, never from memory.
3. One line: `Start with <task>?` — the first task of today's day plan. The person's opening message ("погнали", "let's work") already says yes: do not wait, start the loop in the same reply. The line only names the first task.

## 2. The loop: one task at a time, in day-plan order

**a. Already done?** Mandatory, before any work. Look in Needt memory, the person's decisions page if one exists, the task's history and subtasks, and every artifact Claude can reach (a merged PR, a page, mail, a connector, the live site). In a real run, 4 of 6 tasks in a row were done and not marked.

- Done with evidence → `needt_complete_task`, one line `closed: <evidence>`, next task, no question.
- Evidence partial or guessed → not done; the ask says what is missing.

**b. Not done → do everything reachable yourself.** A draft, a lookup ([search](../search/SKILL.md)), a calculation, a plan ([partner](../partner/SKILL.md)), a Needt edit, a browser or connector action inside the permissions you have. Two independent parts → sub-agents per [delegation](../setup/references/delegation.md).

Ask the person only for a login or password, money, sending or publishing, a physical action, or a decision. The ask is **one** question with 2–4 buttons (`AskUserQuestion` when `questions: click`; else one text line where "yes" accepts the recommended option), recommended option first. One open question at a time: the turn ends on the question, and the loop resumes on the answer. If the next tasks do not depend on it, do their no-question work (evidence checks, closes, drafts) before asking.

**c. Close.** The work is done → `needt_complete_task`. A decision was made → `needt_remember` (kind `fact`) or the decisions page, one line `Saved: …`.

**d. Big task.** Cannot be finished in this sitting → name a first step of 15 minutes or less (the entry step of [breakdown](../needt/references/breakdown.md)), do it now, leave the task open with that step.

**Telling the task.** The gist and what is needed from the person, one or two lines. Never retell the whole task.

## 3. Stop and continue

- Nothing left on today's list to work or close (tasks waiting on the person do not count) → `That's all for today. Take tomorrow's?` Unless the person already said "keep going": then continue into tomorrow, no question, no pause.
- Stop on "stop / enough / pause / хватит / стоп", when an ask gets no answer, or when a `/goal` target is reached.
- With a `/goal`, the goal is the stop condition; after each task, one progress line toward it.
- Every 5 tasks handled (closed or advanced), one line: `closed N, left M, ~X min saved` (X = the durations of tasks closed, whether on evidence or by Claude's work). With a `/goal`, merge it into the goal's progress line. Tomorrow's tasks: `needt_day_plan` for that date, chart not redrawn.
- Fixed markers (`Start with`, `closed:`, `Saved:`) stay English; the rest follows the person's language. The offer flag in memory is saved silently.

## Rules that never bend

- No task closed without evidence or an explicit "done" from the person.
- Money tasks (paying, charging, buying, a transfer): prepare everything, ask once; no action without the person's word.
- Sending, posting, publishing, inviting: a draft and one question, never the act.
- Deleting a task: only on a yes. Reversible edits run at once.
- Memory: [memory rules](../needt/references/memory.md).

## Failing behaviors

Working on a task before checking it is done; asking about a task that evidence already closes; closing on a guess; two questions in one message; a question that is really a lookup; retelling the whole task; acting on money, sending or deleting without a word; a big task attempted whole instead of its first 15 minutes; asking "continue?" after "keep going"; stopping with no signal; a chart that does not come from the calls; a widget without `widgets: yes`; claiming a close, edit or save with no successful call.
