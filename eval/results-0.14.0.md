# Eval results — 0.14.0 (2026-11-03)

Run: two Sonnet sub-agents on the new scenarios (T1–T6, B1–B4) plus S2, C1, R2 as regression.
Two failures in the first pass, fixed in the skill text and re-judged against the changed lines.

## setup
- T1 first run, all present, click · PASS
- T2 first run, no connector, text · PASS
- T3 second skill, same conversation · PASS
- T4 "у меня Max" later · PASS
- T5 no AskUserQuestion, widgets: yes · PASS (after: "never a widget, whatever `widgets` says" in setup and onboarding)
- T6 repeated /needt:setup · PASS (after: "what can you do" → outcomes in ≤ 6 lines; no write when nothing changed)

## budget profiles
- B1 search Normal, pro · PASS (after: a run with no sub-agents ends the search line with `· inline`)
- B2 search Normal, ultra · PASS
- B3 critic, pro · PASS (critic §6 now names the "deserves a Deep check — go?" line)
- B4 critic, ultra, board · PASS

## regression
- S2 search Normal · PASS
- C1 critic pasted plan · PASS
- R2 partner with a board · PASS

Carried notes: the `Needt ·` line is reprinted once after a plan change (README wording
updated); partner's "write only what was asked" vs the at-once hand-off to plan when a board
exists — read as hand-off.
