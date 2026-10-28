---
name: needt
description: Works the user's Needt planner through the Needt connector — tasks and subtasks, projects, calendar and auto-scheduling, personal time, habits, pages, read-only mail, memory. Fires on its own in any conversation whenever the user mentions something that belongs in a planner, without being asked to use Needt: a thing to do, a deadline, a meeting, a reminder, a habit, a note to keep, "what's on today", moving or finishing something, mail to turn into tasks. Triggers in any language, e.g. EN "add a task", "remind me", "what's today", "move it", "done", "plan my day"; RU "добавь задачу", "напомни", "что сегодня", "перенеси", "сделал", "запланируй"; UK "додай задачу", "нагадай"; DE "Aufgabe hinzufügen", "erinnere mich"; ES "añade una tarea", "recuérdame"; FR "ajoute une tâche", "rappelle-moi"; and "/needt". Not for research (search), prompts (prompt), business moves (partner), interviews (asking) or plan review (critic) — those hand finished work to this skill to land it in Needt.
---

# Needt · Main

The job is to keep the user's planner true to what they said: a thing to do becomes a task the
scheduler can place, a time becomes an event or a pin, a "done" becomes a completed task, a note
becomes a page. Act on the planner, then report in one line. A chat that says "you should add
this to your planner" when the connector is right here has failed.

**Fire only on a planner intent** — something to do, keep, move, finish, attend, track or see.
"I did my taxes last year" is a story, not a task. "I need to do my taxes by Friday" is a task.

## Setup check

Before anything else, look back in this conversation for a line starting with `Needt ·`.
None → run the short check from [setup](../setup/SKILL.md), print its line as the first line
of the reply, and continue. Present → reuse it (account, workspaces, memory count).

## Connector check

Call `needt_whoami` once per conversation: account, scopes, workspaces. Reuse the result.

- **No connector, or the call fails** → do the same work as text: a checklist with entry step
  and subtasks, a proposed schedule with times, the note as a block to paste. Say once that the
  Needt connector is not connected here.
- **Connected but a scope is missing** → same text fallback for that part, naming the scope.
- Never write "created", "added", "scheduled", "done" or "saved" without a successful call.

## Intent map

| User says | Calls |
|---|---|
| A thing to do ("I need to…", "add…", "remind me to…") | `needt_search` for the same outcome → `needt_create_task`, or `needt_update_task` / `needt_add_subtasks` on the match |
| A plan, a pasted checklist, work handed over by another skill | breakdown rules below → one `needt_create_task` per outcome, `needt_create_page` for the long text |
| "What's today / next / this week" | `needt_list` (tasks due and scheduled, events) for the range → a short ordered view; `needt_schedule` if unscheduled tasks need placing |
| "Move it", "push to tomorrow", "at 10" | `needt_reschedule`, or `needt_update_task` with `start` (pins it); `pinned: false` hands it back to the scheduler |
| "Done", "finished", "сделал" | `needt_search` / `needt_list` to find it → `needt_complete_task` or `needt_complete_subtask` |
| A meeting or appointment with a time | `needt_create_event`; private ones `needt_mark_event_personal` |
| Time that is not for work ("gym 7–8", "no meetings Friday") | `needt_create_personal_time` / `needt_update_personal_time` |
| "Did my run", "log water" | `needt_search` / `needt_list` for the habit → `needt_log_habit` |
| A note, a document, meeting notes, research to keep | `needt_create_page`, or `needt_append_page` to the page it belongs to; files via `needt_attach_file` |
| "Anything in my mail I need to do?" | read mail via `needt_list` / `needt_search` / `needt_get` → tasks from what needs action |
| Focus, blocking distractions | `needt_blocking_profile` to see profiles, `needt_blocking` to start or stop |
| Look something up in Needt | `needt_search` → `needt_get` |
| "Remember…", "what do you know about me", "forget that" | see Memory below |

`needt_control` drives the app itself (open a view, switch workspace) when the user asks for it.

### Breakdown rules (tasks)

- **One task per outcome** — something either done or not. Usually 1–7; more means the
  outcomes are too small or belong in subtasks.
- **`entry`** = the first small concrete step, doable in one sitting without deciding anything
  ("open the supplier sheet and list the three quotes"), not "start working on it".
- **`subtasks`** in the order they are done. The task itself is the closing step, so the last
  subtask is never "finish" or "done".
- **A step that needs the user's decision** is its own subtask naming the decision:
  "Decide: Stripe or Creem for checkout".
- **Estimates** in minutes only with a basis in the conversation. **Priority** only with a
  reason (deadline, blocker, "this first"). **Due date** only when the user named one — never
  from "soon".
- **`start` + pinned** only when the user said when ("tomorrow at 10"). Everything else goes to
  the scheduler unpinned.
- **No duplicates**: `needt_search` per outcome first, batched. Same open outcome → update it.
  Similar but different → create, and mention the near-match.
- **Documents are pages**: a report, brief, spec or notes go to a page linked from the task.
  A task description holds a few lines and links, never the whole text.
- **How a task is written** — like a person jotting it on paper, not like an AI:
  - **The user's language, always.** The language they write to you in, even if the source
    (mail, research, a prompt) is in another one. Never mix languages in one title.
  - **Short and plain**: verb first, 2–6 words, the user's own words where possible —
    "Call the print shop", "Позвонить в типографию". Not "Reach out to the print shop to
    discuss and finalize the order details".
  - **Nothing in the title but the action**: no time or date ("at 14:00", "tomorrow" — that is
    `start` or the due date), no emoji, no symbols or brackets, no prefixes or tags ("TODO:",
    "[Work]", "Step 1:", "#marketing", "Task:"), no priority words ("URGENT", "!!!"), no trailing
    period.
  - **No AI slop**: no filler verbs ("leverage", "optimize", "streamline", "ensure",
    "оптимизировать процессы"), no vague outcomes ("Work on strategy", "Improve marketing"),
    no motivational wording, no restating the project name in every task.
  - **Description only when it adds something** the title cannot: a link, a number, who, the
    one-line reason. Empty is fine.
  - Subtasks follow the same rules.

| Material | Becomes |
|---|---|
| Research from [search](../search/SKILL.md) | the recommendation is the task; options are short notes in the description; sources linked |
| Stages from [prompt](../prompt/SKILL.md) | one task per stage, the stage's prompt in the description |
| A [partner](../partner/SKILL.md) session | each "actual work" item one task; advice stays in chat |
| A pasted checklist | grouped into outcomes; items become subtasks; nothing dropped silently |
| A decision just made | one task to carry it out; the decision and its reason in one line |

### Mail is read-only

Read mail and turn what needs action into tasks — that is all. Never reply, forward, compose
or send, in any tool, even when asked; say the user replies from their mail app, and offer a
task "Reply to …" with the points to make in its description.

## Permissions

- **Runs without asking**, then one-line report: create, edit, reschedule, pin/unpin,
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
[references/memory.md](references/memory.md).

- Setup reads it once (`needt_list_memories`, or the "Needt · Memory" page as fallback); a
  saved `preference` or `pattern` outranks this skill's defaults.
- Save on your own, without asking: an explicit "remember / from now on / запомни", a
  correction of how something was done, a preference seen twice, a stated goal or project fact.
- Report each save as one line: `Saved: never schedule before 10:00`.
- `needt_remember` when it exists; otherwise the fallback page via `needt_append_page`.
- Never claim a save that failed. Never save one-off details, secrets, or other people's data.

## Reporting

After acting, one compact line, or a table for three or more items, in the user's language:

| Task | Subtasks | Placed |
|---|---|---|
| title as created | 3 | scheduler · Thu 14:00 / pinned Tue 10:00 / updated existing |

- What was created, moved, completed or logged, and where it landed: the scheduled time if the
  scheduler placed it, "pinned" with the time if pinned, the page title for notes.
- Only rows for calls that succeeded. A failed call gets its own line with the error.
- No ids unless the tool returned them; never invented. No recap of the conversation.

## Sub-agents

Rarely needed: the work is a few connector calls that need the conversation. Exceptions: a long
pasted document to break down (one Sonnet sub-agent extracts the action items verbatim; the
breakdown happens here) and a big mailbox sweep (a sub-agent reads and lists what needs action).
Rules: [setup/references/delegation.md](../setup/references/delegation.md).

## Sister skills

- [partner](../partner/SKILL.md) — business decisions and the actual work behind them.
- [search](../search/SKILL.md) — finding things out on the web.
- [prompt](../prompt/SKILL.md) — writing prompts and staged prompt plans.
- [asking](../asking/SKILL.md) — clarifying questions and stress-testing a plan.
- [critic](../critic/SKILL.md) — reviewing a plan before it is acted on.

Those skills finish their work in chat and hand the result to this skill to land in Needt; they
never create tasks on their own.

## Failing behaviors

Firing on a casual mention that is not a planner intent; asking for confirmation on a
reversible action; replying to, forwarding or composing mail; claiming creation, scheduling or
a save that failed or ran without the connector; a wall of 30 micro-tasks; one task "do
everything"; an entry step that is itself a project; duplicating a task that already exists;
inventing ids, due dates or priorities; pinning without a time from the user; a description
holding a whole report; asking which workspace when only one fits; deleting or touching other
people's tasks without asking; saving memory for one-off details; a report longer than the work;
task titles in another language than the user's, with a time, emoji, symbols or prefixes in
them, or written like AI copy instead of a short human note.
