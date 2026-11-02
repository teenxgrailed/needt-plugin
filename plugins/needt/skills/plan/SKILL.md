---
name: plan
description: Keeps a project's roadmap alive across sessions as a board in Needt — milestones, blockers, what is next, a handoff — drawn as a clickable metro map where widgets render. First call builds the board from a goal or a pasted plan; later calls read it back from Needt, compute next, mark done only on evidence, log each change. Use for "roadmap", "milestones", "plan this project", "where are we", "what's next on", "what's left", "project status", "pick up where we left off", "handoff", "next session", "plan:" commands, "/needt:plan"; RU "роадмап", "дорожная карта", "вехи", "спланируй проект", "где мы", "что дальше по", "что осталось", "статус проекта", "на чём остановились", "хэндофф"; UK "сплануй проєкт", "де ми", "що далі"; DE "Roadmap", "Meilensteine", "wo stehen wir", "Übergabe"; ES "hoja de ruta", "hitos", "dónde estamos"; FR "feuille de route", "jalons", "où en est-on". Not for a day or week schedule (needt), reviewing a plan (critic), deciding what to do (partner) or learning a subject (learn).
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

Who owns what and what travels between skills: [skills map](../setup/references/skills-map.md).

- [needt](../needt/SKILL.md) — writes tasks and pages; its title rules and permissions apply
  here. A day or week plan, a single task, "what's today" are its job. It hands "where are
  we / what's next on <project>" and "done <milestone>" here.
- [partner](../partner/SKILL.md) — decides the move; hands over the sequence once it spans
  more than one session. "Should we do X" on a board's milestone goes back to it.
- [critic](../critic/SKILL.md) — a board built from an invented plan goes through it first
  when the stakes are high; its findings come back as `add` / `defer` / `reprioritize` log
  lines with the finding as reason.
- [asking](../asking/SKILL.md) — short mode when the milestones cannot be cut without the
  user (scope, order); a full interview's decisions become milestones or `Decide: …` ones.
- [search](../search/SKILL.md) — a milestone that needs a fact or an option; the find is
  logged on the plan page.
- [prompt](../prompt/SKILL.md) — a milestone that a coding agent or another product will
  execute gets one prompt carrying the milestone, its evidence rule and the last handoff.
- [learn](../learn/SKILL.md) — "roadmap for learning X" is a subject map there, not a board.

## Commands

Buttons and short messages the board understands, in any language (the English form is
what the widget sends):

| Message | Does |
|---|---|
| `plan: where are we` / "где мы", "status" | §3 state in four lines, the last handoff, the board |
| `plan: open <milestone>` | the milestone's task: subtasks, evidence so far, what blocks it; offers Start or Done |
| `plan: start <milestone>` | sets it `in_progress` (one at a time), log `start` |
| `plan: done <milestone>` | asks for or finds the evidence (§4), completes, log `complete`, re-renders |
| `plan: add <milestone> after <other>` | new task with `dependsOnId`, log `add` |
| `plan: defer <milestone>` / `remove` | log `defer` with reason; `remove` deletes after the user confirms |
| `plan: handoff` / "I'm stopping" | §7 block appended |

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
