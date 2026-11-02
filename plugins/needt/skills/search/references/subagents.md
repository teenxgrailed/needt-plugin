# Sub-agent brief rules

Read before delegating a Normal or Deep search. General rules for all skills:
[setup/references/delegation.md](../../setup/references/delegation.md).

Sub-agent counts follow the budget profile in
[delegation.md](../../setup/references/delegation.md): where it allows agents, independent
sub-questions of a Normal or Deep search run as parallel Sonnet sub-agents (one per
sub-question or per source kind); Quick never does. With `agents: no` or a profile that allows
none, the same sub-questions run inline, one round at a time. Sub-agents do not see SKILL.md unless you give it to them:

- Each brief contains: the objective and the sub-question it owns; the user's context and
  success criterion; the **required source kinds from [sources.md](sources.md) and the
  recipes for them** (paste the relevant part of `tools.md` or its path); which tools exist
  here (from the setup line); the output format; what is out of scope.
- Each sub-agent reports, besides findings: which source kinds it tried, which queries
  returned nothing, and every claim it could not verify. "No live examples found" without
  the list of what was tried is not a result — send it back for the missing kinds.
- Merge yourself: dedupe, resolve contradictions, keep the better-sourced version, and say
  when two agents disagreed.
