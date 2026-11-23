# Eval results - 0.17.0 (2026-11-23)

Change: critic runs inside other skills in a new short mode (`critic/references/auto.md`): partner (>3 moves or stakes), roadmap (board creation, add/reprioritize batch of 3+), prompt (L), search (Deep); needt offers it once. Recursion and double-pass rules added to critic, asking, search, roadmap, prompt, partner, needt, skills-map.
Run: K2, K3, K4, K6 are simulated (fresh Sonnet sub-agents reading the changed files, assumed tool results). K1, K5, K7 are real runs on 2026-11-23: `claude -p --model sonnet --plugin-dir plugins/needt` at 53bc42e4 (0.17.0 loaded, the synced 0.14.0 overridden), live Needt connector, writes confined to a test project `EVAL 0.17 critic test`. Raw transcripts are kept outside the repo.

## critic wiring
- K1 partner 6-move plan (real, Sonnet): one pass, `Critic · short · 3 findings`, one-line findings, revised plan with `▲`, original not printed; but the critic block came after the plan instead of before it, and a separate `Open:` line was printed instead of folding into Decisions · FAIL
- K2 partner verdict: no critic · PASS
- K3 roadmap board + single add + batch of 4: 1 pass at creation, none on single add, 1 on batch; critic never touches the board · PASS
- K4 prompt L / M: block above the fence, no triangle in the prompt; none on M · PASS
- K5 search Deep direct / inside partner / Normal (real, Sonnet): 1 / 0 / 0. Direct: the file opens `Search · deep` then `Critic · short · 3 findings`, `In short` is the revised recommendation with `▲`. Inside partner: no critic line anywhere, but partner did the research with its own agents and never loaded search, so the step rule was only weakly exercised. Normal: `Search · normal`, no critic · PASS
- K6 needt paste 4+ steps: tasks landed, one offer line, once · PASS
- K7 loops (real, Sonnet, 4 turns resumed): `/needt:critic full` gives `Critic · full · 6 findings` plus Open decisions; "settle them now" starts an asking short round (3 questions, recommended answer first), no critic; the answers are landed as 10 tasks through needt, `▲` stripped, no critic offer; "send to roadmap" builds a 9-milestone board, saying "no second critic pass, the plan already had one". Side issues outside K7: turn 1 landed a task unasked (critic §5 says offer), and turn 3 saved the eval decisions to real Needt memory · PASS

## fixes made after the first runs
Full mode now prints `Critic · full · N findings` (the once-per-plan marker); roadmap and needt called as a step never run critic; needt offer is made after landing; triangle marks are stripped when a plan lands; batch size defined once; batch changes applied only on yes; creation log line carries the critic reason; search Deep chat shows heading and titles only; work is not a critic caller. Wording only, second check found only low items, fixed.

## checks
- every SKILL.md under 8000 bytes, descriptions under 600 chars, `claude plugin validate` passed, relative links resolve · PASS
- manifests at 0.17.0 · PASS
- not re-run: skills with unchanged text (learn, youtube, setup, work beyond one line)
