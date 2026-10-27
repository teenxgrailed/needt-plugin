---
name: search
description: Smart researcher that finds the good option, not just the first one — the library, approach, tool, supplier, fact or example that actually fits the user's project, verified and sourced. Starts from the user's context, fans out many short queries across different kinds of sources (web, YouTube guides and their transcripts, X threads, GitHub), follows the leads that matter, and comes back with a recommendation. Three depths, picked from the question. Use for "найди", "поищи", "загугли", "что есть для", "как лучше сделать", "как делают", "что сейчас популярно", "собери всю инфу", "ресёрч", "исследуй", "find", "look up", "research", "what's the best way to", "how do people do X", "compare X vs Y", or when another Needt skill needs facts from the web. Not for questions already answered in the conversation, and not for buy/no-buy money calls — that is partner.
---

# Needt · Search

The job is a **find**: the one thing worth knowing that the user would not have reached with
a single search — the better library, the trick from a maintainer's comment, the competitor
that already solved it, the real number from someone who does it for a living. A pile of
links is not a result. A reworded search snippet is not research.

## Setup check

Before the first search, look back in this conversation for a line starting with `Needt ·`.
None → run the short check from [setup](../setup/SKILL.md) (it lists the search tools that
really exist here), print its line as the first line of the reply, and continue. Present →
reuse its tool list.

## Sister skills

- [critic](../critic/SKILL.md) — a plan that should be checked before launch.
- [needt](../needt/SKILL.md) — finished work lands in Needt as tasks.

## 1. Frame before searching

Write down for yourself, not as a questionnaire:

- **What the user is actually building or deciding** — from the chat, the open project, its
  files and notes (one or two targeted looks, never a full crawl). Research for "my app"
  starts by knowing what the app already uses: stack, versions, constraints, what was tried.
- **What a great answer looks like** — the success criterion. "A library that works with
  Next 15 + React 19, maintained in 2026, MIT" beats "a good library".
- **The 3–7 sub-questions** that answer it. Concrete ones: "which libraries do X for React 19,
  and which are maintained" — not "what about X".
- **Who would know** — the perspectives that see different truths: the maintainer, the person
  who migrated off it, the competitor's changelog, the frustrated user on a forum, the docs,
  the benchmark, the regulator. Each perspective is a query direction.
- **Which source kinds the question type requires** — see §3. A question about how people
  do something or what is popular is not answered by articles alone.

Ask the user only if a missing fact would send the whole search the wrong way. Then one round
through [asking](../asking/SKILL.md) in short mode. Otherwise label the assumption and go.

## 2. Pick the depth

| Depth | When | Budget | Output |
|---|---|---|---|
| **Quick** | one fact: a price, a version, a date, a name | 1–3 calls | 1–3 lines in chat |
| **Normal** | "how best to do X", a comparison, "what's out there for Y" | 2–3 rounds, ~8–20 calls | answer + find + options in chat |
| **Deep** | a decision that matters, a market, "собери всё" | several rounds, 3–5 parallel sub-agents when available, 30+ calls | cited file |

The first line of the report is the search line:
`Search · normal · 14 calls · sources: web, youtube, github`. The report itself is in the
user's language; the line stays in this shape. Warn before Deep that it
takes several minutes. Scale up only for a reason; the commonest failure is heavy machinery
on a light question.

## 3. Source kinds by question type

Different questions live in different places. These are minimums, not a menu; a report that
skipped a required kind says so in `Still unclear`.

| Question type | Required source kinds | Why |
|---|---|---|
| How people actually do X; what is popular or trending; formats, workflows, playbooks | **YouTube guides and transcripts** + **X threads** + web | practitioners show the steps and numbers on video and argue about them on X long before articles catch up |
| Which library, tool, API, repo | **GitHub** (issues, releases, stars trend) + current docs (Context7) + web | the README sells; issues and merged PRs tell what breaks |
| A price, a plan, a limit, a date | the **official page**, opened, with the date | never recalled, never from a blog |
| A rule, a policy, a law | the **primary article, read in full**, and the exact clause quoted | an excerpt once turned "shorts over 60 s with a claim are blocked" into "all shorts are blocked" and that decided a whole plan wrongly |
| A market, competitors, suppliers | competitors' own pages + forums in the market's language + X + web | what exists, what it costs, what people complain about |
| Anything scientific or medical | papers (research tools) + web | — |

Recipes for YouTube, X and GitHub are in [references/tools.md](references/tools.md): how to
build the queries, which tool to call, what to extract, how to cite.

## 4. Search: wide, then narrow

- **Round one is wide and parallel.** Short, broad queries — 2–6 words — one or more per
  sub-question and per perspective, batched into as few calls as the tools allow. Long, overly
  specific queries return nothing; start broad and see what the landscape is.
- **Mix source kinds** — this is where the good finds come from. Docs and changelogs for
  what is true now; GitHub issues and merged PRs for what actually breaks; forums, Reddit,
  HN and X for lived experience; YouTube transcripts for numbers practitioners say but never
  write; competitors' pages for what already exists; papers for anything scientific.
- **Read excerpts first.** Open a full page only when the excerpt is thin, contradictory, or
  the source is the authoritative one — and always for a rule or a price that decides something.
- **Follow leads.** A name, a repo, a term you did not know — that is round two. Narrow
  queries now, aimed at the leads.
- **Hypotheses, not just notes.** Keep 2–3 competing candidate answers and look for what
  would rule each one out, including evidence against the one you like.
- **Stop** when new searches stop changing the answer. Another round needs a named gap.

## 5. Delegating to sub-agents

Rules for all skills: [setup/references/delegation.md](../setup/references/delegation.md).
For search specifically: a Normal search with two or more independent sub-questions runs them
as parallel Sonnet sub-agents (one per sub-question or per source kind); Deep always does.
Quick never does. Sub-agents do not see this file unless you give it to them:

- Each brief contains: the objective and the sub-question it owns; the user's context and
  success criterion; the **required source kinds from §3 and the recipes for them** (paste the
  relevant part of `references/tools.md` or its path); which tools exist here (from the
  setup line); the output format; what is out of scope.
- Each sub-agent reports, besides findings: which source kinds it tried, which queries
  returned nothing, and every claim it could not verify. "No live examples found" without
  the list of what was tried is not a result — send it back for the missing kinds.
- Merge yourself: dedupe, resolve contradictions, keep the better-sourced version, and say
  when two agents disagreed.

## 6. Verify

- Every number, price, date, version and availability claim carries a link and its date.
  Prices, versions, "who maintains this", rates and laws are searched, never recalled.
- Anything that decides money, a dependency or a commitment needs two independent sources;
  one source is a lead — mark it `(1 source)`.
- A policy that decides a choice: open the primary article, read the whole section, quote
  the clause with its conditions (duration, account type, region). A second page that says
  something else means both are quoted and the difference is named.
- View counts, follower counts and "went viral" come from the platform page or a dated
  report; say which. Unverified counts are marked `UNVERIFIED`, never rounded into facts.
- Sources disagree → show the range and say so. Old source → say how old.
- Code-level claims ("works with React 19") get checked against the repo, issues or changelog,
  not a blog post.
- Never invent a URL. Never cite a page you did not open or read an excerpt of.

## 7. Report

Lead with the answer and the **find**, then what supports it. Translate the headings below
into the user's language when the report is not in English.

**Quick** — the fact, its date, the link.

**Normal** — in chat:
1. The answer / recommendation in one or two lines, applied to the user's case.
2. **Find** — the non-obvious thing worth knowing, with its source.
3. Options compared (a table when there are 3+), each with the one reason for or against.
4. **Still unclear** — one line; includes any required source kind that was skipped.

**Deep** — a markdown file: `In short` (3–6 points with numbers) → `What was found` (by
question, not by source) → `Finds` → `Still unclear` (mandatory; say "none" if so) →
`Sources` (numbered: title, domain, link, what it gave, how much to trust it).

A YouTube find cites video + timestamp; an X find cites the post and its date; a GitHub find
cites the issue or release. When the research was for a task — a feature, a fix, a purchase —
end with the concrete next step applied to that task, and do it if it is reversible and the
user asked for it.

## Failing behaviors

A link dump; one search tool for everything; one long query instead of many short ones; a
price or version from memory; a source not opened; a rule taken from an excerpt; the first
plausible answer reported without looking for a better one; ignoring the user's stack or
constraints; articles only for a "how do people do it" question; a sub-agent brief without
the source-kind requirements; "no examples found" without the list of what was tried; Deep
without a warning; `Still unclear` missing or invented; fetching pages through shell
commands.
