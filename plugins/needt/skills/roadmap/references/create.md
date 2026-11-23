# Creating the board

Read on the first call, when no board exists (SKILL.md §2).

1. Milestones: 3–9 outcomes, each something that is either true or not, in the order they
   are usually done, titled by needt's "How a task is written". From the user's goal, a
   pasted plan, or a partner / critic result; a one-line summary of the goal stays with the
   user for confirmation only when the milestones were invented, not pasted.
1b. **Critic, once.** Run [critic](../../critic/SKILL.md) in short mode
   ([auto](../../critic/references/auto.md)) on the milestone list, and build the board from
   its revised list. Skip it when the list comes from a plan that already holds a `Critic ·`
   pass in this conversation (a critic or partner result) or whose review was offered and not accepted, or when roadmap was called as a step
   of another skill (needt, partner, asking, critic). Strip every `▲` from the revised list; a
   `▲ removed:` line is not a milestone. Show critic's block (heading, findings) above the
   board, plus one line `Changed: <titles>` when a milestone was dropped, added or reordered.
   The board is created from the revised list; no `defer`, `reprioritize` or `remove` lines at
   creation (nothing existed yet): the one log line carries the reason, see step 5.
2. `needt_create_project` with the project's name; then `needt_create_page` "Plan · <name>"
   holding the milestone table (`# · milestone · task id · after · status` — the ids are how a
   chat without an open folder finds the tasks) and a `## Log` heading.
3. One `needt_create_task` per milestone: `projectId`, `autoSchedule: false` (a milestone is
   not a calendar block), `dependsOnId` = the id of the milestone it waits on (one allowed;
   further blockers go into the description as `blocked by: <titles>`), `originPageId` = the
   plan page. A goal is optional and Pro-only: `needt_create_goal` linked by `projectIds`,
   skipped silently when refused.
4. `needt_update_project` with `description: "plan-page: <pageId>"`, and in an open folder
   write `.needt/plan.json`.
5. Report the board once (§6) and the first `Log` line: `- <date> · add · <n> milestones`, with
   ` · critic: <changed or dropped titles, a phrase each>` appended when critic changed the list.

Re-running on a project that already has a board never creates a second one: §1 finds it.

