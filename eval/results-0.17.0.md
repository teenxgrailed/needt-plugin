# Eval results - 0.17.0 (2026-11-23)

Change: critic runs inside other skills in a new short mode (`critic/references/auto.md`): partner (>3 moves or stakes), roadmap (board creation, add/reprioritize batch of 3+), prompt (L), search (Deep); needt offers it once. Recursion and double-pass rules added to critic, asking, search, roadmap, prompt, partner, needt, skills-map.
Run: K2, K3, K4, K6 are simulated (fresh Sonnet sub-agents reading the changed files, assumed tool results). K1, K5, K7 are real runs on 2026-11-23: `claude -p --model sonnet --plugin-dir plugins/needt` at 53bc42e4 (0.17.0 loaded, the synced 0.14.0 overridden), live Needt connector, writes confined to a test project `EVAL 0.17 critic test`. Raw transcripts are kept outside the repo. Re-run after the K1 fixes with `eval/run-live.sh` (Needt writes denied, leak check after each run): 0 write calls attempted or leaked.

## critic wiring
- K1 partner (real, Sonnet, read-only runner, 2 runs after the order fix): both runs answered with a plan of 3 moves or fewer, so correctly no critic. The block-order fix is not exercised yet; it needs a run that yields a 6-move plan · NOT EXERCISED
- K2 partner verdict: no critic · PASS
- K3 roadmap board + single add + batch of 4: 1 pass at creation, none on single add, 1 on batch; critic never touches the board · PASS
- K4 prompt L / M: block above the fence, no triangle in the prompt; none on M · PASS
- K5 search Deep direct / inside partner / Normal (real, Sonnet, read-only runner): 1 / 0 / 0 critic passes. Inside partner: verdict, no critic line. Normal: `Search · normal`, no critic. Direct: `Critic · short · 3 findings` with one-line findings, but in 2 of 2 runs it printed AFTER the recommendation in chat, no report file was written, and `In short` was not revised with `▲`. An earlier run (with Needt writes on) had it right · FAIL
- K6 needt paste 4+ steps: tasks landed, one offer line, once · PASS
- K7 loops (real, Sonnet, read-only runner, 4 resumed turns): `Critic · full · 5 findings`, ending with an offer to land (no unasked write, so fix 2 holds); asking short asks 2 questions with a recommended answer and calls no critic; landing as tasks: no critic, no offer; roadmap: "Critic already ran on this plan above, so I skipped it" · PASS

## fixes made after the first runs
Full mode now prints `Critic · full · N findings` (the once-per-plan marker); roadmap and needt called as a step never run critic; needt offer is made after landing; triangle marks are stripped when a plan lands; batch size defined once; batch changes applied only on yes; creation log line carries the critic reason; search Deep chat shows heading and titles only; work is not a critic caller. Wording only, second check found only low items, fixed.

## checks
- every SKILL.md under 8000 bytes, descriptions under 600 chars, `claude plugin validate` passed, relative links resolve · PASS
- manifests at 0.17.0 · PASS
- not re-run: skills with unchanged text (learn, youtube, setup, work beyond one line)
