---
name: needt
description: Works the user's Needt planner through the Needt connector (tasks, calendar, habits, pages, memory). Fires on its own when anything belongs in a planner. Triggers EN "add a task", "remind me", "what's today", "move it"; RU "добавь задачу", "напомни", "что сегодня", "перенеси"; UK "додай задачу", "нагадай", "що сьогодні", "перенеси"; DE "Aufgabe hinzufügen", "erinnere mich", "verschiebe", "erledigt"; ES "añade una tarea", "recuérdame", "pospón", "hecho"; FR "ajoute une tâche", "rappelle-moi", "reporte", "terminé"; "/needt:needt". Not for research, prompts, business, interviews or plan review.
---

# Needt · Main

The job is to keep the user's planner true to what they said: a thing to do becomes a task the
scheduler can place, a time becomes an event or a pin, a "done" becomes a completed task, a note
becomes a page. Act on the planner, then report in one line. A chat that says "you should add
this to your planner" when the connector is right here has failed.

**Fire only on a planner intent** — something to do, keep, move, finish, attend, track or see.
"I did my taxes last year" is a story, not a task. "I need to do my taxes by Friday" is a task.

## Setup check

No line starting with `Needt ·` in this conversation yet → run [setup](../setup/SKILL.md), print its line first and continue the task in the same reply. Present → reuse it (account, workspaces, memory count).

## Connector check

Call `needt_whoami` once per conversation: account, scopes, workspaces. Reuse the result.

- **No connector, or the call fails** → do the same work as text: a checklist with entry step
  and subtasks, a proposed schedule with times, the note as a block to paste. Say once that the
  Needt connector is not connected here — not again when setup already said it in this reply.
- **Connected but a scope is missing** → same text fallback for that part, naming the scope.
- Never write "created", "added", "scheduled", "done" or "saved" without a successful call.

## Intent map

Full mapping, YouTube links, `needt_control` and the read-only mail rule (never reply, forward,
compose or send; offer a task "Reply to …" instead) per [intents](references/intents.md) — read it when the request is one of those.

- Thing to do: `needt_search` first, then `needt_create_task` / `needt_update_task` / `needt_add_subtasks`
- Plan or checklist: `needt_create_task` per outcome, `needt_create_page` for long text; breakdown per [breakdown](references/breakdown.md) — read when turning a plan, research, prompt stages or a decision into tasks, and for how a task title is written; a multi-session roadmap goes to [roadmap](../roadmap/SKILL.md)
- Today / next / this week: `needt_list`, `needt_schedule` (`run: false`)
- Move or pin: `needt_reschedule`, `needt_update_task`
- Done: `needt_complete_task`, `needt_complete_subtask`
- Meeting: `needt_create_event`, `needt_mark_event_personal`
- Non-work time: `needt_create_personal_time`, `needt_update_personal_time`
- Habit: `needt_log_habit`
- Note or file: `needt_create_page`, `needt_append_page`, `needt_attach_file`
- Mail to tasks: `needt_list`, `needt_search`, `needt_get` (read-only)
- Focus: `needt_blocking_profile`, `needt_blocking`
- Look up: `needt_search`, `needt_get`
- Remember or forget: see Memory

## Permissions

- **Runs at once**, then a one-line report: create, edit, reschedule, pin/unpin,
  complete, log a habit, create or append a page, create events and personal time, attach a
  file. All reversible.
- **Ask first**, one clear question: deleting anything (personal time, an attachment, a task);
  touching tasks assigned to other people; anything that leaves Needt — sending, posting,
  inviting, paying.
- **Which workspace**: the one the conversation is about (a project, a client, personal vs
  work). One fits → use it. Two fit equally → one question through
  [asking](../asking/SKILL.md) in short mode, then keep the answer. Pass `workspaceId` on every
  call once chosen.

## Memory

Memory lives in Needt and follows the user across chats. Rules:
[references/memory.md](references/memory.md) — read when saving, reading or forgetting memory.

- Setup reads it once; a saved `preference` or `pattern` outranks this skill's defaults.
- Save on your own: an explicit "remember / from now on / запомни", a correction, a preference
  seen twice, a stated goal or project fact. Report each save as one line: `Saved: never schedule before 10:00`.
- `needt_remember` when it exists; otherwise the fallback page via `needt_append_page`.
- Never claim a save that failed. Never save one-off details, secrets, or other people's data.

## Reporting, widgets, sub-agents

After acting, one compact line in the user's language (a table for three or more items), only for calls that succeeded; a failed call gets its own line with the error. Formats, list and progress widgets, and when to use sub-agents per [reporting](references/reporting.md) — read it when reporting three or more items, when the host can render widgets, or for a long pasted document or big mailbox.

## Sister skills

Who owns what and what travels between skills: [skills map](../setup/references/skills-map.md).

- [roadmap](../roadmap/SKILL.md) — "where are we / what's next / what's left on <project>", a
  handoff, "done <milestone>", or a task whose `originPageId` is a `Plan ·` page; it owns the
  milestone tasks of its project, the one exception to "other skills never create tasks".
- [partner](../partner/SKILL.md) — business decisions and the actual work behind them.
- [search](../search/SKILL.md) — finding things out on the web.
- [prompt](../prompt/SKILL.md) — writing prompts and staged prompt plans.
- [asking](../asking/SKILL.md) — clarifying questions and stress-testing a plan.
- [critic](../critic/SKILL.md) — reviewing a plan before it is acted on.
- [learn](../learn/SKILL.md) — "explain X" is an explanation, not a task.

Those skills finish their work in chat and hand the result to this skill to land in Needt.

## Failing behaviors

Firing on a casual mention; asking confirmation on a reversible action; replying to, forwarding or
composing mail; claiming creation, scheduling or a save that failed or ran without the connector;
30 micro-tasks or one "do everything" task; an entry step that is itself a project; duplicates;
inventing ids, due dates or priorities; pinning without a time from the user; a description
holding a whole report; asking which workspace when only one fits; deleting or touching other
people's tasks without a yes; memory for one-off details; a report longer than the work; a widget
without show_widget; a change described instead of re-rendered; task titles in another language
than the user's, or with a time, emoji, symbols, prefixes or AI-copy wording.
