# Drawing the board

Read when drawing the board (SKILL.md §6).

- With `widgets: yes` (per [widgets](../../setup/references/widgets.md)): one hand-written SVG,
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

