# Eval results - 0.17.0 (2026-11-23)

Change: critic runs inside other skills in a new short mode (`critic/references/auto.md`): partner (>3 moves or stakes), roadmap (board creation, add/reprioritize batch of 3+), prompt (L), search (Deep); needt offers it once. Recursion and double-pass rules added to critic, asking, search, roadmap, prompt, partner, needt, skills-map.
Run: K2, K3, K4, K6 are simulated (fresh Sonnet sub-agents reading the changed files, assumed tool results). K1, K5, K7 are real runs on 2026-11-23: `claude -p --model sonnet --plugin-dir plugins/needt` at 53bc42e4 (0.17.0 loaded, the synced 0.14.0 overridden), live Needt connector, writes confined to a test project `EVAL 0.17 critic test`. Raw transcripts are kept outside the repo. Final run on 27.11 at skills head 5534e0b (runner 83190c5): `eval/run-live.sh` with Needt writes denied under both connector prefixes, `--setting-sources project,local` so the runner's personal CLAUDE.md cannot drive writes, and a leak and exit check after each run. All 8 transcripts: 0 non-read Needt calls succeeded.

## critic wiring
- K1 partner (real, Sonnet, 5534e0b): `Critic · short · 3 findings` directly above the revised plan, one-line findings `title — problem → solution · cost · confidence`, `▲` on changed steps, original not printed, open points inside the closing `Decisions:` line, no `Open:` line; ends with one offer to land as tasks or a board, nothing written · PASS
- K2 partner verdict: no critic · PASS
- K3 roadmap board + single add + batch of 4: 1 pass at creation, none on single add, 1 on batch; critic never touches the board · PASS
- K4 prompt L / M: block above the fence, no triangle in the prompt; none on M · PASS
- K5 search Deep direct / inside partner / Normal (real, Sonnet, 5534e0b): direct writes the report file opening with the search line, `## Critic · short · 3 findings`, then `## In short` with `▲`; chat shows one critic line with the titles. Inside partner: search is not loaded, partner reviews its own plan once (`Critic · short`), no critic from search. Normal: no critic · PASS
- K6 needt paste 4+ steps: tasks landed, one offer line, once · PASS
- K7 loops (real, Sonnet, 5534e0b, 4 resumed turns): `Critic · full · 6 findings` ends with an offer and writes nothing; asking short asks the open decisions, no critic; "land it as tasks" lands (as [would call] lines) with no critic or offer; roadmap: "Critic already reviewed this plan earlier", no second pass · PASS

## fixes made after the first runs
Full mode now prints `Critic · full · N findings` (the once-per-plan marker); roadmap and needt called as a step never run critic; needt offer is made after landing; triangle marks are stripped when a plan lands; batch size defined once; batch changes applied only on yes; creation log line carries the critic reason; search Deep chat shows heading and titles only; work is not a critic caller. Wording only, second check found only low items, fixed.

## checks
- every SKILL.md under 8000 bytes, descriptions under 600 chars, `claude plugin validate` passed, relative links resolve · PASS
- manifests at 0.17.0 · PASS
- not re-run: skills with unchanged text (learn, youtube, setup, work beyond one line)
