# Intents · full tool mapping

Read when the request is one of these intents and the one-line map in SKILL.md is not enough.

| User says | Calls |
|---|---|
| A thing to do ("I need to…", "add…", "remind me to…") | `needt_search` for the same outcome → `needt_create_task`, or `needt_update_task` / `needt_add_subtasks` on the match |
| A plan, a pasted checklist, work handed over by another skill — for one sitting or one week; a roadmap that spans sessions, with milestones that wait on each other, goes to [plan](../../plan/SKILL.md) | [breakdown rules](breakdown.md) → one `needt_create_task` per outcome, `needt_create_page` for the long text |
| "What's today / next / this week" | `needt_list` for events in the range; `needt_schedule` (`run: false`) for the placed blocks — it returns the whole workspace, so read only the blocks inside the range and never paste it; overdue tasks go in one line (`overdue: N — the three oldest`) after today's list |
| "Move it", "push to tomorrow", "at 10" | `needt_reschedule`, or `needt_update_task` with `start` (a `start` pins the task on its own — there is no separate pinned flag on create); `pinned: false` on update hands it back to the scheduler |
| "Done", "finished", "сделал" | `needt_search` / `needt_list` to find it → `needt_complete_task` or `needt_complete_subtask` |
| A meeting or appointment with a time | `needt_create_event`; private ones `needt_mark_event_personal` |
| Time that is not for work ("gym 7–8", "no meetings Friday") | `needt_create_personal_time` / `needt_update_personal_time` |
| "Did my run", "log water" | `needt_search` / `needt_list` for the habit → `needt_log_habit` |
| A note, a document, meeting notes, research to keep | `needt_create_page`, or `needt_append_page` to the page it belongs to; files via `needt_attach_file`. A Word, Excel, PowerPoint or PDF file the user asked for is made by their skill for that format ([user-skills](../../setup/references/user-skills.md)) and attached |
| "Anything in my mail I need to do?" | read mail via `needt_list` / `needt_search` / `needt_get` → tasks from what needs action (see Mail below) |
| Focus, blocking distractions | `needt_blocking_profile` to see profiles, `needt_blocking` to start or stop |
| Look something up in Needt | `needt_search` → `needt_get` |
| A YouTube link ("do this", "make tasks from it", "save the steps") | read it first with [youtube](../../youtube/SKILL.md) (its contract section), then the steps from the transcript → tasks per the [breakdown rules](breakdown.md), `[mm:ss]` and the link in the description |
| "Remember…", "what do you know about me", "forget that" | see Memory in SKILL.md |

`needt_control` drives the app itself (open a view, switch workspace) when the user asks for it.

## Mail is read-only

Read mail and turn what needs action into tasks — that is all. Never reply, forward, compose
or send, in any tool, even when asked; say the user replies from their mail app, and offer a
task "Reply to …" with the points to make in its description.
