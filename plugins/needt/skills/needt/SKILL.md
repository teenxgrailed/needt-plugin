---
name: needt
description: Works the user's Needt planner through the Needt connector (tasks, calendar, habits, pages, memory). Fires on its own when anything belongs in a planner. Triggers EN "add a task", "remind me", "what's today", "move it"; RU "добавь задачу", "напомни", "что сегодня", "перенеси"; UK "додай задачу", "нагадай", "що сьогодні", "перенеси"; DE "Aufgabe hinzufügen", "erinnere mich", "verschiebe", "erledigt"; ES "añade una tarea", "recuérdame", "pospón", "hecho"; FR "ajoute une tâche", "rappelle-moi", "reporte", "terminé"; "/needt:needt". Not for research, prompts, business, interviews or plan review.
---

# Needt · Main

The job: keep the user's planner true to what they said: a thing to do becomes a task the
scheduler can place, a time an event or a pin, a "done" a completed task, a note a page. Act on
the planner, then report in one line; "you should add this to your planner" with the connector
right here is a failure.

**Fire only on a planner intent** — something to do, keep, move, finish, attend, track or see.
"I did my taxes last year" is a story; "I need to do my taxes by Friday" is a task.

## Setup check

No line starting with `Needt ·` in this conversation yet → run [setup](../setup/SKILL.md), print its line first and continue in the same reply. Present → reuse it (account, workspaces, memory count).

## Connector check

Call `needt_whoami` once per conversation (account, scopes, workspaces); reuse the result.

- **No connector, or the call fails** → do the same work as text: a checklist with entry step
  and subtasks, a proposed schedule with times, the note as a block to paste. Say once that the
  connector is not connected — not again when setup already said it in this reply.
- **A scope is missing** → the same text fallback for that part, naming the scope.
- Never write "created", "added", "scheduled", "done" or "saved" without a successful call.

## Intent map

Full mapping, YouTube links, `needt_control` and the read-only mail rule (never reply, forward,
compose or send; offer a task "Reply to …"): [intents](references/intents.md) — read it for those.

- Thing to do: `needt_search` first, then `needt_create_task` / `needt_update_task` / `needt_add_subtasks`
- Plan or checklist: `needt_create_task` per outcome, `needt_create_page` for long text; [breakdown](references/breakdown.md) — read when turning a plan, research, prompt stages or a decision into tasks, and for how a title is written; a multi-session roadmap goes to [roadmap](../roadmap/SKILL.md)
- Today / next / this week: `needt_list`, `needt_schedule` (`run: false`)
- Move or pin: `needt_reschedule`, `needt_update_task` · Done: `needt_complete_task`, `needt_complete_subtask`
- Meeting: `needt_create_event`, `needt_mark_event_personal` · Non-work time: `needt_create_personal_time`, `needt_update_personal_time`
- Habit: `needt_log_habit` · Note or file: `needt_create_page`, `needt_append_page`, `needt_attach_file`
- Mail to tasks and look up: `needt_list`, `needt_search`, `needt_get` (read-only)
- Focus: `needt_blocking_profile`, `needt_blocking` · Remember or forget: see Memory

## Permissions

- **Runs at once**, then a one-line report: create, edit, reschedule, pin, complete, log a
  habit, create or append a page, create events and personal time, attach a file.
- **Ask first**, one question: deleting anything; others' tasks; anything that leaves Needt —
  sending, posting, inviting, paying.
- **Which workspace**: the one the conversation is about. One fits → use it. Two fit equally →
  one question through [asking](../asking/SKILL.md) in short mode, then keep the answer. Pass
  `workspaceId` on every call once chosen.

## Memory

Memory lives in Needt and follows the user across chats: [references/memory.md](references/memory.md) — read to save, read or forget.

- Setup reads it once; a saved `preference` or `pattern` outranks these defaults.
- Save on your own: "remember / from now on / запомни", a correction, a preference seen twice,
  a stated goal or project fact. Report each save in one line: `Saved: never schedule before 10:00`.
- `needt_remember` when it exists, else the fallback page via `needt_append_page`.
- Never claim a failed save; never save one-off details, secrets or other people's data.

## Reporting, widgets, sub-agents

After acting, one compact line in the user's language (a table for three or more items), only for calls that succeeded; a failed call gets its own line with the error. Formats, widgets, sub-agents: [reporting](references/reporting.md) — read it for three or more items, a widget-capable host, or a long pasted document or big mailbox.

## Offering the work loop

After reading the day (`needt_list` / `needt_schedule`), offer [work](../work/SKILL.md) in one line — "Work through them together? (/needt:work)" — when all hold:

- the connector exists;
- there is a signal: 3 or more overdue tasks, a day planned past its limit, or the user asked "what's today" ("let's go" or an explicit loop request already is a yes);
- not offered yet today: one line `[fact] needt work offered <date>` in memory, created once, then updated by id (`needt_list_memories`) with the new date, saved silently with no `Saved:` report;
- not a newcomer: `sessions: n` in the `needt plugin set up` memory line is at least 3 (a missing field means 3).

One line, never repeated, never in a reply that already does the work.

## Offering critic

4+ pasted steps toward one goal, to turn into tasks or a roadmap → land them as pasted, always end with one line: "Check the plan first? (/needt:critic)". Yes → full [critic](../critic/SKILL.md) shows findings and the revised plan; the tasks or board just made change, by id, only on a second yes. No or no answer → never offer again here. Never offered: a plan with a `Critic ·` pass (a landing critic result too), needt as a step of another skill, an errand list, 3 steps or fewer.

## Sister skills

Who owns what and what travels between skills: [skills map](../setup/references/skills-map.md).

- [work](../work/SKILL.md) — "let's work", "погнали": walks the open tasks one at a time, closes the done ones, does the rest itself.
- [roadmap](../roadmap/SKILL.md) — "where are we / what's next / what's left on <project>", a
  handoff, "done <milestone>", or a task whose `originPageId` is a `Plan ·` page; it owns its
  project's milestone tasks, the one exception to "other skills never create tasks".
- [partner](../partner/SKILL.md) — business decisions and the work behind them.
- [search](../search/SKILL.md) — finding things out on the web.
- [prompt](../prompt/SKILL.md) — prompts and staged prompt plans.
- [asking](../asking/SKILL.md) — clarifying questions, stress-testing a plan.
- [critic](../critic/SKILL.md) — reviewing a plan before it is acted on; offered, never forced (below).
- [learn](../learn/SKILL.md) — "explain X" is an explanation, not a task.

Those skills finish in chat and hand the result here to land in Needt.

## Failing behaviors

Offering `/needt:work` to a newcomer, twice a day or without a signal; offering critic twice, on a reviewed plan or on chores; none on a pasted 4+ step plan; firing on a casual mention; confirming a reversible action; replying to, forwarding or composing mail; claiming a write that failed or ran without the connector; 30 micro-tasks or one "do everything" task; an entry step that is itself a project; duplicates; invented ids, due dates or priorities; pinning without the user's time; a description holding a whole report; asking which workspace when one fits; touching other people's tasks without a yes; memory for one-off details; a report longer than the work; a widget without show_widget; a change described instead of re-rendered; titles in another language, or with a time, emoji, symbols, prefixes or AI-copy wording.
