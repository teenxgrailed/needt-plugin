# First-run interview — questions and options

Read by setup on the first run (no memory `fact` starting `needt plugin set up`). One round,
at most four questions, asking's short mode. Clickable when `questions: click`
(`AskUserQuestion`: header chip up to 12 characters, 2-4 options, recommended first with
" (Recommended)", reasoning in the option description). Otherwise a numbered list (never a widget), "1 =
recommended", answerable by "1, 2, 1". No "Other" option is added by hand; free text works.
Write the questions and options in the user's language; the memory line stays English.

Before the round, one line says why: a few answers make every Needt skill fit this chat.

## Q1 — Plan of this host (header: `Plan`)

"Which plan is this AI app on?" Why it matters, one phrase in the description: it sets how
much work the skills run in parallel and how deep they go.

| Option | Memory value |
|---|---|
| Claude Pro | `pro` |
| Claude Max | `max` |
| Claude Ultra | `ultra` |
| Other — Team, Enterprise or another AI app | `team` when the user names Team or Enterprise, else `other` |

Four options, always these four; the user's own text decides between `team` and `other`. Recommended: whatever the host suggests (a model or plan visible in context); unknown
→ Pro. Not asked again if the user's message already named the plan.

## Q2 — Connect now (header: `Connect`, multiSelect)

"Which of these do you want to connect now?" Offer only kinds that are not present in the
tool catalog; each description carries its free option from
[tools-help](../references/tools-help.md):

- Needt connector — comes with Needt Pro; planner skills and memory need it. Customize →
  Connectors in Claude; `claude mcp add …` in Claude Code.
- Web search — usually built in; a free extra is Tavily (1,000 credits a month).
- YouTube transcripts — free (`yt-dlp`, or Firecrawl's YouTube provider).
- GitHub — the official server with a token, or the `gh` CLI.

Plus "Skip for now". Everything present → skip this question. Chosen items: give the path or
command from tools-help in one line each after the round; connect nothing yourself. Not
chosen and not skipped → `declined`.

## Q3 — Language and tone (header: `Language`)

"Which language and tone should replies use?" Options: "Your language, casual
(Recommended)" / "Your language, professional" / "English, professional". "Your language" is
the language the user writes in. Casual is recommended when the user writes casually,
professional otherwise.

## Q4 — Memory (header: `Memory`)

"Should Needt remember preferences and project facts?" Options:

- On (Recommended) — "preferences and project facts saved in Needt, you see every save".
- Off for this chat — nothing is saved; the profile holds for this chat only.
- Skip for now — treated as on; the first `Saved:` line reminds the user once that it can be turned off.

Without the Needt connector, memory cannot persist: say once that the answers hold for this
chat only.

## After the round

Defaults when unanswered, labelled in one line: plan `unknown` (budget field `unknown`),
tools none connected, language the user's own, tone matched to how they write, memory on.
Save per setup's Save section, then continue the user's task in the same reply.
