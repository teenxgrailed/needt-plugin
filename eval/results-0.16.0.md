# Eval results - 0.16.0 (2026-11-22)

Change: new skill `work` (`/needt:work`); needt offers it; setup counts `sessions: n`.
Run: one fresh Sonnet sub-agent on W1-W3 (simulated first replies, judged per check). Gaps it
found (start line blocks, blocking question vs "keep working", empty-list rule, counters,
marker language, dated anecdote) were fixed in the skill text. Re-run was not repeated;
the fixes are wording only.

## work
- W1 6 tasks: 2 done closed with no question, 1 money question only, 1 big task first step, 2 ordinary · PASS
- W2 offer only with signal, sessions >= 3, once a day · PASS
- W3 keep going / stop / goal / 5-task summary · PASS

## checks
- SKILL.md sizes under 8000 bytes, work description under 600 chars · PASS
- manifests at 0.16.0 (plugin.json, .claude-plugin/plugin.json, two marketplace.json) · PASS

## carried over from 0.15.0
- needt N1-N3, roadmap P1-P3, partner R1-R3, search S1-S3, prompt M1-M3, asking A1-A3, critic C1-C3, learn L1-L3, youtube Y1-Y3, setup T1-T6, budget B1-B4, X1-X3 · PASS (text unchanged except setup's `sessions` field and needt's offer section)
