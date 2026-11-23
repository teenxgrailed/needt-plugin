# Deep report format

Read before writing a Deep report. Translate the headings into the user's language when the
report is not in English.

**Critic check (Deep only, once).** Before writing, when the research ends in a recommendation
and the user asked for this search themselves, run [critic](../../critic/SKILL.md) in short
mode on that recommendation ([auto](../../critic/references/auto.md)). The file opens with
its block (`Critic · short · N findings` and the findings), then `In short` is the revised
recommendation with `▲` on every changed line. In chat the search line stays first. A finding that rests on a fact not in the
file is `guess`; critic looks nothing up. The chat summary carries only the heading and the
finding titles, one line. Skip it: no recommendation (a market map, a list of options with
no pick), search called by another skill, the recommendation already holds a `Critic ·` pass.

A markdown file: the `Critic · short` block when it ran, then `In short` (3–6 points with
numbers) → `What was found` (by question, not by source) → `Finds` → `Still unclear` (mandatory; say "none" if so) → `Sources` (numbered:
title, domain, link, what it gave, how much to trust it).

A YouTube find cites video + timestamp; an X find cites the post and its date; a GitHub find
cites the issue or release. In chat, Deep's `In short` numbers may be metric cards (see
Widgets in SKILL.md). Warn before Deep that it takes several minutes.
