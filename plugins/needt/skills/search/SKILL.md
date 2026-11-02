---
name: search
description: Finds the option that actually fits the user's project, verified and sourced, across web, YouTube, X and GitHub, at three depths. Triggers EN find, look up, research, what's the best way to, compare X vs Y; RU найди, поищи, загугли, ресёрч, исследуй; UK знайди, пошукай, дослідж, порівняй; DE suche, recherchiere, finde heraus, vergleiche; ES busca, investiga, encuentra, compara; FR cherche, recherche, trouve, compare; /needt:search. Not for answered questions or buy/no-buy calls (partner).
---

# Needt · Search

The job is a **find**: the one thing worth knowing that the user would not have reached with
a single search — the better library, the trick from a maintainer's comment, the competitor
that already solved it, the real number from someone who does it for a living. A pile of
links is not a result. A reworded search snippet is not research.

## Setup check

No line starting with `Needt ·` in this conversation yet → run [setup](../setup/SKILL.md), print its line first and continue the task in the same reply. Present → reuse it (its list of search tools).

## Sister skills

Who owns what and what travels between skills: [skills map](../setup/references/skills-map.md).

- [youtube](../youtube/SKILL.md) — one video per call when a source is a video.
- [critic](../critic/SKILL.md) — a plan that should be checked before launch.
- [plan](../plan/SKILL.md) — research done for a milestone of a board is logged on the plan
  page as the find, one line, and the milestone is named in the report's next step.
- [partner](../partner/SKILL.md) — a buy/no-buy or business call on what was found.
- [needt](../needt/SKILL.md) — finished work lands in Needt as tasks.
- Question is "is there a skill, plugin or tool for X": check the installed catalog first
  ([user-skills](../setup/references/user-skills.md)) before searching directories.

## 1. Frame before searching

Write down for yourself, not as a questionnaire:

- **A YouTube link in the question** is read first through [youtube](../youtube/SKILL.md)
  (its contract section) — it is a source, and the search then verifies or extends it.
- **What the user is building or deciding** — from the chat, the open project, its files and
  notes (one or two targeted looks, never a full crawl): stack, versions, constraints.
- **What a great answer looks like** — the success criterion. "A library that works with
  Next 15 + React 19, maintained in 2026, MIT" beats "a good library".
- **The 3–7 concrete sub-questions** that answer it, and **who would know** — maintainer,
  person who migrated off it, competitor's changelog, forum, docs, benchmark, regulator.
- **Which source kinds the question type requires** — see below.

Ask the user only if a missing fact would send the whole search the wrong way. Then one round
through [asking](../asking/SKILL.md) in short mode. Otherwise label the assumption and go.

## 2. Pick the depth

| Depth | When | Budget | Output |
|---|---|---|---|
| **Quick** | one fact: a price, a version, a date, a name | 1–3 calls | 1–3 lines in chat |
| **Normal** | "how best to do X", a comparison, "what's out there for Y" | 2–3 rounds, calls per the budget profile | answer + find + options in chat |
| **Deep** | a decision that matters, a market, "собери всё" | several rounds, parallel sub-agents per the budget profile ([delegation](../setup/references/delegation.md)) | cited file |

The first line of the report — after the `Needt ·` line when that one is printed in the same
reply — is the search line (Quick prints none; a run with no sub-agents ends it with `· inline`):
`Search · normal · 14 calls · sources: web, youtube, github`. The report itself is in the
user's language; the line stays in this shape. Warn before Deep that it takes several
minutes. Scale up only for a reason; the commonest failure is heavy machinery on a light question.

Read before a Normal or Deep search: [sources.md](references/sources.md) (required source
kinds by question type), [verify.md](references/verify.md) (verify rules),
[subagents.md](references/subagents.md) (when and how to delegate; read before any
delegation). Recipes for YouTube, X and GitHub: [tools.md](references/tools.md).

## 3. Wide, then narrow

- Round one is wide and parallel: short queries (2–6 words), one or more per sub-question
  and perspective, mixing source kinds; read excerpts first, open full pages only when thin
  or authoritative.
- Round two follows leads (a name, a repo, a term) with narrow queries.
- Keep 2–3 competing candidate answers and look for what rules each out.
- Stop when new searches stop changing the answer; another round needs a named gap.

## 4. Report

Lead with the answer and the **find**, then what supports it. Translate the headings into
the user's language when the report is not in English.

**Quick** — the fact, its date, the link.

**Normal** — in chat:
1. The answer / recommendation in one or two lines, applied to the user's case.
2. **Find** — the non-obvious thing worth knowing, with its source.
3. Options compared (a table when there are 3+), each with the one reason for or against.
4. **Still unclear** — one line; includes any required source kind that was skipped.

**Deep** — a file, format in [report.md](references/report.md).

When the research was for a task — a feature, a fix, a purchase — end with the concrete next
step applied to that task, and do it if it is reversible and the user asked for it.

## Widgets

With `widgets: yes` (per [widgets](../setup/references/widgets.md)), a Normal report's options
(3+) are shown as one card per option: the recommended one marked, the one reason for or
against as its subtitle. The answer, the Find and Still unclear stay text. Buttons, at most
four: `Go deeper on <option>`, `Make it a task in Needt`, `Open the source` (a link). Quick
never renders a widget. Deep's file stays a file; in chat, its `In short` numbers may be
metric cards. The search line stays the first line of text, never inside a widget. With
`widgets: no`, the report is exactly as above.

## Failing behaviors

A link dump; one search tool for everything; one long query instead of many short ones; a
price or version from memory; a source not opened; a rule taken from an excerpt; the first
plausible answer reported without looking for a better one; ignoring the user's stack;
articles only for a "how do people do it" question; a sub-agent brief without source-kind
requirements; "no examples found" without the list tried; Deep without a warning;
`Still unclear` missing or invented; fetching pages through shell commands; a widget for a
Quick answer; the search line inside a widget.
