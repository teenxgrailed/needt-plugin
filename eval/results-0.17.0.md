# Eval results - 0.17.0 (2026-11-23)

Change: critic runs inside other skills in a new short mode (`critic/references/auto.md`): partner (>3 moves or stakes), roadmap (board creation, add/reprioritize batch of 3+), prompt (L), search (Deep); needt offers it once. Recursion and double-pass rules added to critic, asking, search, roadmap, prompt, partner, needt, skills-map.
Run: three fresh Sonnet sub-agents reading the changed files and simulating K1-K7 (simulated first replies, assumed tool results), then a second fresh agent on the fixed text. A pass is simulated.

## critic wiring
- K1 partner 6-move plan: one short pass, revised plan only · PASS
- K2 partner verdict: no critic · PASS
- K3 roadmap board + single add + batch of 4: 1 pass at creation, none on single add, 1 on batch; critic never touches the board · PASS
- K4 prompt L / M: block above the fence, no triangle in the prompt; none on M · PASS
- K5 search Deep direct / inside partner / Normal: 1 / 0 / 0 · PASS
- K6 needt paste 4+ steps: tasks landed, one offer line, once · PASS
- K7 loops (critic-asking, critic-needt, critic-roadmap, roadmap-prompt): none; no second pass on a reviewed plan · PASS

## fixes made after the first runs
Full mode now prints `Critic · full · N findings` (the once-per-plan marker); roadmap and needt called as a step never run critic; needt offer is made after landing; triangle marks are stripped when a plan lands; batch size defined once; batch changes applied only on yes; creation log line carries the critic reason; search Deep chat shows heading and titles only; work is not a critic caller. Wording only, second check found only low items, fixed.

## checks
- every SKILL.md under 8000 bytes, descriptions under 600 chars, `claude plugin validate` passed, relative links resolve · PASS
- manifests at 0.17.0 · PASS
- not re-run: skills with unchanged text (learn, youtube, setup, work beyond one line)
