---
name: plan
description: Keeps a project roadmap alive across sessions as a board in Needt, with next steps computed and done marked only on evidence. Use for /needt:plan, roadmap, milestones, where are we, what's left, what's next on, handoff, plan commands; RU роадмап, вехи, где мы, что осталось, на чём остановились; UK роудмап, віхи, де ми, що залишилось; DE Roadmap, Meilensteine, wo stehen wir, Übergabe; ES hoja de ruta, hitos, dónde estamos, qué falta; FR feuille de route, jalons, où en est-on, passation. Not for day or week schedules, plan review or learning a subject.
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
- The user's own skills ([user-skills](../setup/references/user-skills.md)) — a milestone that is their workflow (deploy, review,
  a deck) runs through their skill; the evidence rule still decides done.

## Commands

`plan: where are we` · `open` · `start` · `done` · `add … after …` · `defer` / `remove` ·
`handoff`, in any language; the table of what each does:
[references/commands.md](references/commands.md) — read when a `plan:` message or board button arrives.

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

3–9 outcome milestones, then project, plan page, one task per milestone (`autoSchedule: false`,
`dependsOnId`), `plan-page:` in the project description, `.needt/plan.json`, first log line.
Steps: [references/create.md](references/create.md) — read on the first call. Re-running on a
project that already has a board never creates a second one: §1 finds it.

## 3. State — computed, never stored

- `done` — task completed.
- `blocked` — any task it waits on (`dependsOnId` or `blocked by:`) is open.
- `current` — the one task with `status: in_progress`; at most one. Set it with
  `needt_update_task` when the user says what they are working on, or when the last handoff
  named it; ties go to board order.
- `next` — open, not blocked, not current: the first of them in board order is what the
  skill proposes.

"Where are we" is answered from these four sets and the last handoff, in four lines or fewer
above the board. Never a stored "next": the handoff's "next session should" is advice,
re-checked against these sets each time.

## 4. Done needs evidence

A milestone is completed (`needt_complete_task`) only on one of: a merged PR or a commit the
session can see; a file or artefact that exists; a test or check that passed in this session;
the user saying it is done — for a milestone with no external gate. A milestone gated by
someone else (a review, a payment, an approval, a merge) needs the artefact or one confirming
question ("the approval email arrived?") even when the user says done. The agent's own "I
finished it" is not evidence — the milestone
stays `current` and the log says `needs check: <what would prove it>`. The evidence goes into
the log line.

## 5. Log — append only

Every change goes to the plan page with `needt_append_page` (pages are never rewritten):

`- 2026-11-02 · complete · Auth flow · PR #41 merged`

Verbs: `add`, `complete`, `defer`, `remove`, `reprioritize`, `start`, each with its reason or
evidence after the last `·`. `remove` deletes the task only after the user confirms (needt's
permissions); the log keeps the line. A reorder changes `dependsOnId` with `needt_bulk`.

## 6. The board

Marks: `✓` done, `●` current, `○` next, `✕` blocked.

- `widgets: yes` → one SVG metro map, clickable stations, re-rendered with the same `title`
  after every change; spec in [references/board.md](references/board.md) — read when drawing the board.
- `widgets: no` → one line per milestone, same marks:
  `✓ Auth flow · ● Billing · ○ Onboarding (after Billing) · ✕ Launch (blocked by Billing, Onboarding)`.
- No Needt connector → `PLAN.md` in the open folder (or one block in the chat) with the same
  table, `## Log` and `## Handoff`, same rules; tell the user once that the board moves to
  Needt when the connector is added.

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
