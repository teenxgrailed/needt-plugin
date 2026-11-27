# Eval results - 0.17.0 (2026-11-23)

Change: critic runs inside other skills in a new short mode (`critic/references/auto.md`): partner (>3 moves or stakes), roadmap (board creation, add/reprioritize batch of 3+), prompt (L), search (Deep); needt offers it once. Recursion and double-pass rules added to critic, asking, search, roadmap, prompt, partner, needt, skills-map.
Run: K2 and K4 are simulated (fresh Sonnet sub-agents reading the changed files, assumed tool results). K1, K3, K5, K6, K7 are real runs: `claude -p --model sonnet` through `eval/run-live.sh` (plugin loaded with `--plugin-dir`, live Needt connector read-only: write tools denied under both connector prefixes, user-level settings and instruction files kept out, leak and exit check after each run). A landing is judged on the `[would call: …]` lines and the reply text. Raw transcripts are kept outside the repo. Runs on 27.11: K6 and K7 at bc006b3 (the final skills head); K1, K3 and K5 at 3738d61, whose skills differ from bc006b3 only in needt/SKILL.md, which those scenarios don't use. All 24 transcripts: 0 non-read Needt calls succeeded.

## critic wiring
- K1 partner (real, 3738d61): `Critic · short · 3 findings` directly above the revised plan, one-line findings `title — problem → solution · cost · confidence`, `▲` on changed steps, original not printed, open points in the closing `Decisions:` line, no `Open:` line; ends with one offer ("put it on a roadmap board?"), nothing written · PASS
- K2 partner verdict: no critic · PASS
- K3 roadmap (real, 3738d61, 5 turns): no board → `Critic · short · 3 findings`, revised list with `▲` and `▲ removed:`, `Changed:` line, `Build from the revised list?`, nothing written; "yes" → board from the revised list ([would call] project, page, tasks, log with critic's reason); single add → no critic (asked where, since "samples received" did not exist); batch of 4 → critic once, `Revised batch (▲) — apply?` directly under it, then the board with the 4 as asked; "yes" → revised batch applied, log lines with the finding as reason, no new pass. Note: before the yes the user's batch was shown on the board but not written · PASS
- K4 prompt L / M: block above the fence, no triangle in the prompt; none on M · PASS
- K5 search Deep direct / inside partner / Normal (real, 3738d61): direct writes the report file opening with the search line, `## Critic · short · 3 findings`, then `## In short` with `▲`; chat shows one critic line with the titles. Inside partner: search not loaded, partner reviews its own plan once, no critic from search. Normal: no critic · PASS
- K6 needt (real, bc006b3): 6 pasted steps → 6 [would call] creates and one closing offer line ending `(/needt:critic)` (wording paraphrased); "yes" → `Critic · full · 6 findings` with the revised plan, tasks untouched, one offer to apply; second "yes" → tasks created/updated, no `▲`, no new offer. Separate run: "no" → never offered again, a later 4-step paste got no offer; a 3-step paste → no offer · PASS
- K7 loops (real, bc006b3, 4 turns): `Critic · full · 7 findings` ends with an offer, nothing written; asking short asks the open decisions with a recommended answer, no critic; "land it as tasks" lands with no critic or offer; roadmap: "Critic already ran on this plan", no second pass · PASS

## fixes made after the first runs
Full mode now prints `Critic · full · N findings` (the once-per-plan marker); roadmap and needt called as a step never run critic; needt offer is made after landing; triangle marks are stripped when a plan lands; batch size defined once; batch changes applied only on yes; creation log line carries the critic reason; search Deep chat shows heading and titles only; work is not a critic caller. Wording only, second check found only low items, fixed.

## checks
- every SKILL.md under 8000 bytes, descriptions under 600 chars, `claude plugin validate` passed, relative links resolve · PASS
- manifests at 0.17.0 · PASS
- not re-run: skills with unchanged text (learn, youtube, setup, work beyond one line)
