# Eval — the release gate

No release of `needt` ships until every scenario in `scenarios.md` has a PASS in
`results-<version>.md`. The gate is `release.sh`: it refuses to build when that file is
missing or holds a FAIL.

## How a run works

One fresh Sonnet sub-agent per skill (ten in parallel), each given:

1. the skill's `SKILL.md` and the files under its `references/`, plus the shared references
   `setup/references/{skills-map,widgets,user-skills,delegation}.md` and
   `needt/references/memory.md`;
2. the three scenarios for that skill from `scenarios.md`;
3. this instruction: *"You are the model that received this skill and this user message
   in a chat with the stated host state (connector, widgets, questions, agents). Write the
   first reply you would give, verbatim, including tool calls as `[call: tool(args)]`.
   Then judge it against the scenario's checks, one line per check, PASS or FAIL with the
   reason."*

The runner (a person or the main agent) collects the lines into `results-<version>.md`:

```
## needt
- N1 add a task · PASS
- N2 no connector · PASS
- N3 done milestone → plan · FAIL: created the task itself instead of handing over
```

A FAIL blocks the release; fix the skill text, re-run that skill only, update the file.

## Expected in every first reply

The host state has no `needt plugin set up` memory, so setup's first run adds its onboarding
lines (none when nothing is missing) and the `set up` save. That is expected, not a FAIL. A scenario that states `budget: …` in its host state means the
set-up memory line exists with that value: no plan question, no first-run interview.

## What every scenario checks

- The `Needt ·` line is the first line when the conversation has none, and is not printed
  again when it exists.
- No question is asked when the skill's rules say to assume and go.
- The hand-off goes to the skill the map names, in the same reply, not as "run X".
- Nothing is reported as created, saved or done without a successful call.
- Fixed strings stay English; everything else is in the user's language.
- With `widgets: no` the answer is the same, as text.
