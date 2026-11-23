# Critic · auto-run and short mode

Read when another Needt skill runs critic by its own rule, and before writing such a rule.
The output contract never changes: **findings first, then the revised plan with `▲`**. Short
mode only cuts everything around it. In the caller's reply the block sits directly above the
revised artifact, never after it.

## Two modes

- **Full** — the user asked (`/needt:critic`, "critique this", an accepted offer). SKILL.md §1–§5.
- **Short** — a calling skill ran critic by its own rule, inside its own reply. Rules below.

## Short mode, exactly

Input: the artifact the caller was about to hand over (a plan, a milestone list, an approach
section, a recommendation) and what the conversation already holds. Work it from zero as in
§1, silently.

1. **Heading line**, fixed English like the `Needt ·` line: `Critic · short · N findings`
   (N from 0 to 3). Full mode opens with `Critic · full · N findings` the same way. A `Critic ·`
   line is the marker the once-per-plan rule below looks for.
2. **Findings** — at most 3, by impact, one line each, all four parts:
   `**1. <title>** — <problem> → <solution> · <cost or free> · <high|medium|guess>`.
   The words around the parts follow the user's language like the full markers do. Two findings
   with one fix merge.
3. **Revised artifact** — the caller's own artifact in its own shape with the solutions
   applied; every changed or added line `▲`, a dropped step `▲ removed: <step> — <why>`.
   This is the version the caller hands over; the original is never printed beside it. N = 0:
   the artifact unchanged, no `▲`.
4. **Nothing else**: no opening summary, no `Keeps working as is`, no landing offer, no cards or
   buttons (text even with `widgets: yes`: the caller owns the reply's one widget), no
   sub-agents, no lookups (a fact that would change a finding → that finding is `guess`),
   no memory saves, no `asking`. An open decision → one line `Open: <decision>` after the
   revised artifact; the caller turns it into a labelled assumption (partner folds it into the
   plan's closing `Decisions:` line and prints no `Open:` line).
5. **Pasted deliverable** (a prompt, anything the user copies elsewhere): the artifact holds no
   `▲`; each finding line ends `· ▲ <what changed in the artifact>` instead, and the artifact
   is the revised one. The critic block sits above the artifact and is not counted in the
   caller's own line limits.
6. **Landing a revised plan** (tasks, milestones, a prompt): strip every `▲`; a
   `▲ removed:` line is never a task or a milestone.

Memory respected as in full mode: a settled point is not raised again.

## Who runs it, and when

| Caller | Trigger | Reviews | Never when |
|---|---|---|---|
| partner | handing over a plan or strategy of more than 3 moves, or any plan with real stakes (money, a public launch, a hire) | the plan | a verdict or an answer; 3 moves or fewer without stakes |
| roadmap | a board is created (before the tasks are written), unless needt routed a pasted plan there (needt offers); before an `add` / `reprioritize` batch of 3 or more milestones (size per roadmap/references/commands.md) | the milestone list or the batch | a single `add`, `defer`, `remove`, `done`, `start`; handoff |
| prompt | size **L** only, after the approach is chosen, before the prompt is built | the approach section | S or M |
| search | **Deep** only, a request the user made to search itself, before the report is written | the recommendation | Quick or Normal; no recommendation, only a map; search called by another skill |
| needt | the user pastes a plan of 4 or more steps to turn into tasks: **offer** once | offered; yes → full mode | offered once and not accepted; steps already reviewed; landing of a critic result; a plan routed to roadmap is offered too |

## Don't re-enter

- **Critic is a leaf.** It reads the conversation and calls only: youtube (a video link), search
  Quick, asking in short mode (full mode, open decisions only), roadmap (full mode: read the
  board, offer log lines). A skill called from inside critic runs with critic off. Short mode
  calls nothing. Landing through needt or roadmap, or a remake by partner, after a critique
  are steps of critic's result, never a reason to run or offer critic again. After an asking
  round, apply the answers to the revised plan (`▲`); no new findings, no second pass.
- **Only the skill that owns the user's request decides about critic.** A skill called as a
  step of another (search from partner, prompt from roadmap, partner from work, needt from
  critic's landing) never runs or offers critic itself.
- **A roadmap or needt called as a step** (by needt, partner, asking or critic) runs no critic
  and offers none: needt has already offered, or the owner already reviewed.
- **One pass per plan.** A `Critic ·` pass (or an offer made and not accepted) already covers the artifact, or the artifact this one
  was built from, in this conversation, and nothing material changed since (a step added,
  removed or reordered by the user) → no second pass. Moving a reviewed plan on (to a board, to
  tasks, into a prompt) is not a change. A review of a recommendation or an approach covers a
  plan built from it only when the plan adds no step, spend or public commitment; otherwise
  the plan is a new artifact. The critic's own output is never reviewed.
- **asking never calls critic**, and critic's asking round (full mode) is the end of the chain.
- **roadmap never re-runs critic on findings it applied**: the board's `add` / `defer` /
  `reprioritize` log lines with the finding as the reason are written by roadmap; critic called
  by roadmap does not call roadmap back.
