# Eval results - 0.16.0 (2026-11-22)

Change: new skill `work` (`/needt:work`); needt offers it; setup counts `sessions: n`.
Run: fresh Sonnet sub-agents on the final text (simulated first replies, judged per check).
Skills changed in this release, so re-run: work, needt, setup. Not changed, not re-run:
partner, search, prompt, asking, critic, learn, youtube, roadmap (see the last section).
A pass is simulated, with assumed tool results.

## work
- W1 six tasks (2 already done closed with no question, 1 money question only and deferred to the end, 1 big task first step, 2 ordinary; `closed 3, left 3, ~50 min saved` after task 5) · PASS
- W2 offer only with signal, sessions >= 3, once a day, flag silent · PASS
- W3 keep going / statement / stop / goal · PASS

## setup
- T1 first run, everything present · PASS
- T2 first run, no connector, text questions · PASS
- T7 sessions counter (1 -> 2, 3 no write, missing field = 3, first run writes 1) · PASS

## needt
- N1 add a task · PASS
- N2 no connector, "what's on today?" · FAIL: with no connector and an empty chat there is no day to lay out, so the reply ends by asking for a paste, which setup calls a dead end. Not caused by this change (needt text unchanged here); left open for the owner.
- N3 done milestone -> roadmap · PASS

## fixes made after the run
Skill-text gaps the runs found were fixed afterwards: count of "handled" tasks and "left M", the end-of-list statement with a question outstanding, creating the offer flag when missing, and the silent-save carve-out in memory.md. Wording only; not re-run.

## not re-run
Text unchanged in 0.16.0, so nothing is claimed for them: partner R1-R3, search S1-S3, prompt M1-M3, asking A1-A3, critic C1-C3, learn L1-L3, youtube Y1-Y3, roadmap P1-P3, X1-X3, setup T3-T6, budget B1-B4, needt N1-N3 beyond the above.

## checks
- every SKILL.md under 8000 bytes, work description under 600 chars · PASS
- manifests at 0.16.0, descriptions of both plugin.json match marketplace.json · PASS
