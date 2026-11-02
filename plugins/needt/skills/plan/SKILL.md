---
name: plan
description: Keeps a project's roadmap alive across sessions as a board in Needt — milestones, what blocks what, what is next, a handoff for the next session — and draws it as a clickable metro map where the host renders widgets. The first call turns a goal or a pasted plan into a Needt project with one task per milestone; every later call reads the board back from Needt, works out what is next, marks a milestone done only on evidence and logs each change on the project's page. Use for "roadmap", "milestones", "plan this project", "what's next on", "where are we", "next session", "/needt:plan"; RU "роадмап", "дорожная карта", "спланируй проект", "что дальше по проекту", "на чём остановились"; UK "сплануй проєкт", "що далі"; DE "Roadmap", "Projektplan", "was steht an"; ES "hoja de ruta", "qué sigue"; FR "feuille de route", "et ensuite". Not for a day or week schedule or single tasks (needt), reviewing a plan (critic) or deciding what to do (partner).
---

# Needt · Plan

The job is that **any session, today or in a month, can open the project and know where it
stands in one call**: which milestones are done, which one is being worked on, what is
blocked, what comes next, and what the last session left for this one. The board lives in
Needt, so the app, the API and every other chat see the same thing; this chat is never the
source of truth.

## Setup check

No line starting with `Needt ·` in this conversation yet → run [setup](../setup/SKILL.md),
print its line first and continue the task in the same reply. Present → reuse it (`widgets`
decides the board's form, `memory` may name the project).

## Sister skills

- [needt](../needt/SKILL.md) — writes tasks and pages; its title rules and permissions apply
  here. A day or week plan, a single task, "what's today" are its job, not this skill's.
- [critic](../critic/SKILL.md) — a roadmap worth checking before it is built goes through it
  first when the stakes are high.
- [partner](../partner/SKILL.md) — decides the move; this skill keeps the sequence once it
  spans more than one session.

## 1. Find the board — every call

In this order, stopping at the first hit:

1. `.needt/plan.json` in the open folder: `{ "projectId", "pageId", "milestones": [{ "id",
   "title" }] }`.
2. The project's `description` in Needt, which carries `plan-page: <pageId>` — found with
   `needt_search` on the project name or `needt_list` type `project`.
3. Nothing → §2, after one `needt_search` on the name to be sure no board exists already.

Then read every milestone with `needt_get` by id (`needt_list` cannot filter tasks by
project). The board is what Needt returns now, never what this conversation or memory says.

## 2. Create — first call only

1. Milestones: 3–9 outcomes, each something that is either true or not, in the order they
   are usually done, titled by needt's "How a task is written". From the user's goal, a
   pasted plan, or a partner / critic result; a one-line summary of the goal stays with the
   user for confirmation only when the milestones were invented, not pasted.
2. `needt_create_project` with the project's name; then `needt_create_page` "Plan · <name>"
   holding the milestone table (`# · milestone · after · status`) and a `## Log` heading.
3. One `needt_create_task` per milestone: `projectId`, `autoSchedule: false` (a milestone is
   not a calendar block), `dependsOnId` = the id of the milestone it waits on (one allowed;
   further blockers go into the description as `blocked by: <titles>`), `originPageId` = the
   plan page. A goal is optional and Pro-only: `needt_create_goal` linked by `projectIds`,
   skipped silently when refused.
4. `needt_update_project` with `description: "plan-page: <pageId>"`, and in an open folder
   write `.needt/plan.json`.
5. Report the board once (§6) and the first `Log` line: `- <date> · add · <n> milestones`.

Re-running on a project that already has a board never creates a second one: §1 finds it.

## 3. State — computed, never stored

- `done` — task completed.
- `blocked` — any task it waits on (`dependsOnId` or `blocked by:`) is open.
- `current` — the one task with `status: in_progress`; at most one. Set it with
  `needt_update_task` when the user says what they are working on, or when the last handoff
  named it; ties go to board order.
- `next` — open, not blocked, not current: the first of them in board order is what the
  skill proposes.

"Where are we" is answered from these four sets and the last handoff, in four lines or fewer
above the board. Never a stored "next".

## 4. Done needs evidence

A milestone is completed (`needt_complete_task`) only on one of: a merged PR or a commit the
session can see; a file or artefact that exists; a test or check that passed in this session;
the user saying it is done. The agent's own "I finished it" is not evidence — the milestone
stays `current` and the log says `needs check: <what would prove it>`. The evidence goes into
the log line.

## 5. Log — append only

Every change goes to the plan page with `needt_append_page` (pages are never rewritten):

`- 2026-11-02 · complete · Auth flow · PR #41 merged`

Verbs: `add`, `complete`, `defer`, `remove`, `reprioritize`, `start`, each with its reason or
evidence after the last `·`. `remove` deletes the task only after the user confirms (needt's
permissions); the log keeps the line. A reorder changes `dependsOnId` with `needt_bulk`.

## 6. The board

- With `widgets: yes` (per [widgets](../setup/references/widgets.md)): one hand-written SVG,
  no library, under 4 KB — a metro map. Milestones are stations on a line, in board order,
  branches where a milestone waits on more than one; edges follow the blockers. Marks:
  `✓` done, `●` current (a pulsing ring, off under `prefers-reduced-motion`), `○` next,
  `✕` blocked. Labels are the milestone titles, shortened to fit. Every station is clickable
  and sends `plan: open <milestone title>` through `sendPrompt`; at most four buttons under
  the map: `Start <next>`, `Done: <current>`, `Where are we`, `Tilt` — the last one
  re-renders the same SVG under a CSS `perspective` with `rotateX`/`rotateZ`, still
  clickable. Colours from the host's CSS variables and ramp classes only. The explanation,
  the four state lines and the handoff stay in text above the widget. After every change the
  board is re-rendered with the same `title`.
- With `widgets: no`: one line per milestone, same marks:
  `✓ Auth flow · ● Billing · ○ Onboarding (after Billing) · ✕ Launch (blocked by Billing, Onboarding)`.
- Without a Needt connector: `PLAN.md` in the open folder (or one block in the chat) with the
  same table, `## Log` and `## Handoff` sections, kept by the same rules; the user is told
  once that the board will move to Needt when the connector is added.

`plan: open <milestone>` answers with that milestone's task (subtasks, evidence so far, what
blocks it) and offers `Start` or `Done` for it — through needt's rules, not a new board.

## 7. Handoff — end of a session

When the user says they are stopping, or asks for a handoff, append to the plan page:

```
### Handoff 2026-11-02
- next session should: <one line>
- do not repeat: <approaches that failed, or none>
- needs human: <decisions or inputs, or none>
```

Written even when the state did not change. The next session's first "where are we" quotes
it. On Claude Code a Stop hook may only remind; the skill writes the entry itself.

## 8. Memory

Only standing rules go through [memory](../needt/references/memory.md): "milestones in
English", "never mark done without a PR". Board state never goes into memory — it is in
Needt.

## Failing behaviors

Reading the board from the chat or from memory; storing "next"; two boards for one project;
a milestone completed on the agent's own claim; a rewritten or deleted log line; a day or week
schedule; milestones that are activities ("work on auth") rather than outcomes; a widget with
a library; two widgets in one reply; `.needt/plan.json` written outside an open folder; a
session ended without a handoff when the user said they are stopping.
