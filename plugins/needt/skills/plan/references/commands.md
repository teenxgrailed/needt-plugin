# Plan commands

Read when a `plan:` message or board button arrives (SKILL.md).

Buttons and short messages the board understands, in any language (the English form is
what the widget sends):

| Message | Does |
|---|---|
| `plan: where are we` / "где мы", "status" | §3 state in four lines, the last handoff, the board |
| `plan: open <milestone>` | the milestone's task: subtasks, evidence so far, what blocks it; offers Start or Done |
| `plan: start <milestone>` | sets it `in_progress` (one at a time), log `start` |
| `plan: done <milestone>` | asks for or finds the evidence (§4), completes, log `complete`, re-renders |
| `plan: add <milestone> after <other>` | new task with `dependsOnId` = other; "between A and B" also moves B's `dependsOnId` to the new task; the page table gets its row; log `add` |
| `plan: defer <milestone>` / `remove` | log `defer` with reason; `remove` deletes after the user confirms |
| `plan: handoff` / "I'm stopping" | §7 block appended |

