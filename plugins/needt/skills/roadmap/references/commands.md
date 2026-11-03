# Roadmap commands

Read when a `roadmap:` message or board button arrives (SKILL.md). `plan: …` is accepted as an
alias of `roadmap: …`.

Buttons and short messages the board understands, in any language (the English form is
what the widget sends):

| Message | Does |
|---|---|
| `roadmap: where are we` / "где мы", "status" | §3 state in four lines, the last handoff, the board |
| `roadmap: open <milestone>` | the milestone's task: subtasks, evidence so far, what blocks it; offers Start or Done |
| `roadmap: start <milestone>` | sets it `in_progress` (one at a time), log `start` |
| `roadmap: done <milestone>` | asks for or finds the evidence (§4), completes, log `complete`, re-renders |
| `roadmap: add <milestone> after <other>` | new task with `dependsOnId` = other; "between A and B" also moves B's `dependsOnId` to the new task; the page table gets its row; log `add` |
| `roadmap: defer <milestone>` / `remove` | log `defer` with reason; `remove` deletes after the user confirms |
| `roadmap: handoff` / "I'm stopping" | §7 block appended |

