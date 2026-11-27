# Roadmap commands

Read when a `roadmap:` message or board button arrives (SKILL.md). `plan: …` is accepted as an
alias of `roadmap: …`.

**Critic before a batch.** Batch size = milestones added, or milestones whose position changes
in the final order (moving A before B changes A only). Size 3 or more, in one message, runs
[critic](../../critic/SKILL.md) in short mode on the batch first. The user's batch is applied
as asked; a finding that changes it (drops, reorders, adds a milestone) is applied only on the
user's yes, then logged with the finding as reason. One `add`, `defer`, `remove`, `done`,
`start` and `handoff` never trigger it, nor a batch taken from a result that already holds a
`Critic ·` pass (a pasted critic or partner plan). A batch the user types fresh is reviewed
even when the board was reviewed at creation. Once per batch. Reply: critic block, directly under it `Revised batch (▲) — apply?`, then the
board with the user's batch applied as asked; on yes apply the revised batch and log with the
finding as reason, no new pass.

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

