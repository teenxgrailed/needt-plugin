# Reporting, widgets, sub-agents

Read when you report three or more items, the host can render widgets, or the job is a long document or big mailbox.

## Reporting

After acting, one compact line, or a table for three or more items, in the user's language:

| Task | Subtasks | Placed |
|---|---|---|
| title as created | 3 | scheduler · Thu 14:00 / pinned Tue 10:00 / updated existing |

- What was created, moved, completed or logged, and where it landed: the scheduled time if the
  scheduler placed it, "pinned" with the time if pinned, the page title for notes.
- Only rows for calls that succeeded. A failed call gets its own line with the error.
- No ids unless the tool returned them; never invented. No recap of the conversation.

## Widgets

With `widgets: yes` (per [widgets](../../setup/references/widgets.md)):

- "What's today / this week" is a list widget: the events and placed blocks in order, one
  button per task row that sends `Done: <task title>` through `sendPrompt`.
- A plan or checklist just created is shown as the same list.
- A project's or habit's progress is a progress widget; a project with a plan board shows
  [plan](../../plan/SKILL.md)'s board instead.
- After any completion the list is re-rendered with the same title.
- The report line or table stays as text under it, in one or two lines.

## Sub-agents

Rarely needed, and only as the budget profile allows: the work is a few connector calls that need the conversation. Exceptions: a long
pasted document to break down (one Sonnet sub-agent extracts the action items verbatim; the
breakdown happens here) and a big mailbox sweep (a sub-agent reads and lists what needs action).
Rules: [setup/references/delegation.md](../../setup/references/delegation.md).
