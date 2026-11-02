---
name: setup
description: Checks what this chat can use, runs a short first-run interview (plan, tools, language, memory) and prints the `Needt ·` readiness line; other Needt skills run it on first use. Use for "/needt:setup", "set up Needt", "what can Needt do here", "what can you do", "change my plan to Max"; RU "настрой Needt", "настройка плагина", "что ты умеешь", "у меня Max"; UK "налаштуй Needt", "що ти вмієш"; DE "Needt einrichten", "was kannst du"; ES "configura Needt", "qué puedes hacer"; FR "configure Needt", "que sais-tu faire". Installs nothing, changes no settings.
---

# Set up Needt

Short, in the user's language: the readiness line, plus one round of questions on the first run.

## The readiness line

Setup always produces one line that starts exactly with `Needt ·`. Field names are in
English; values may be in the user's language. For example:

`Needt · ready · project: <name> · tone: casual · search: web, youtube, github · questions: click · agents: yes · widgets: yes · skills: 14 · budget: pro · memory: 12`

The line is the first line of the reply. It costs only the one memory read (see Memory),
made before any text; every other field comes from the tool and skill catalog already in
context — run nothing to prove it. `project` is the project the conversation is about, `none`
when the open folder is unrelated. A skill that reads this file and does not print the line
has failed the check.

Other Needt skills look for this line. One per conversation; run again only when the user
asks or the project changes. The first time, one short line in the user's language follows
it: that this is Needt's readiness check of what this chat can use.

## Establish the context

Reuse what the conversation, memory and project sources already establish. Outside the first
run's round, ask at most one question, only when the project is unknown and the task depends
on it. Match the user's tone. Never ask for secrets or credentials.

## Fields

Read them from the host's real tool and skill catalog already in context — do not assume,
and do not call tools to test them.

- **project** — the current project, or `unknown`.
- **tone** — `casual` or `professional`, matched to how the user writes.
- **search** — the source kinds that exist here (`web`, `exa`, `firecrawl`, `youtube`, `x`,
  `github`, `context7`, `papers`, `browser`, …; `none` if none), counted by what each tool
  covers per the table in [tools-help](references/tools-help.md). `x` with no X tool, browser
  or Exa is `x: web only`.
- **questions** — `click` when a clickable question tool (`AskUserQuestion`) is listed,
  including as a deferred tool; otherwise `text`. Inside a sub-agent it is never available —
  a sub-agent writes `text` even when the memory says `click`.
- **agents** — `yes` when sub-agents can be launched here (an Agent or Task tool); otherwise
  `no`. With `yes`, every Needt skill follows [delegation](references/delegation.md) for
  parallel work on cheaper models.
- **widgets** — `yes` when a `show_widget` tool (the host's `visualize` server) is listed;
  otherwise `no`. Inside a sub-agent always `no`. With `yes`, every Needt skill follows
  [widgets](references/widgets.md) for what is shown as a widget in the chat.
- **skills** — the number of skills in the host catalog that are not Needt's own (`none`
  when there are none). Every Needt skill may hand part of a task to one of them, matched by
  its installed description at that moment, per [user-skills](references/user-skills.md).
- **budget** — `pro`, `max`, `ultra`, `team`, `other` or `unknown`: the plan of this host, read
  from the `budget:` part of the memory line `needt plugin set up …`; `unknown` when there is
  none. Every Needt skill scales sub-agents and depth by it, per
  [delegation](references/delegation.md).
- **memory** — the number of memory lines read; `none` when the store is empty; `off` when
  there is no Needt connector or the user switched memory off.

Listed is not the same as working: mark anything uncertain `unverified`. Do not read
user records to test readiness or claim something enabled in another product is available.

## Memory

Read memory once per conversation, in one call, following
[the memory rules](../needt/references/memory.md): `needt_list_memories` when it exists,
else the page "Needt · Memory", else nothing (`memory: off`, said once). Do not re-read
unless the user says memory changed.

Every line read is a standing instruction for all Needt skills here (a `preference` or
`pattern` outranks a skill's default). Setup only reads; saving follows the same file.

## First run

1. After the memory read, look for a memory of kind `fact` whose content starts with
   `needt plugin set up`.
2. Found: not a first run. Print the readiness line only and go on. A later request ("у меня
   Max", "switch memory off", "change my plan") updates that line with `needt_update_memory`
   and prints the new readiness line — no interview again.
3. Not found: print the readiness line and its one explanatory line, then run the interview
   below, then save, then continue the task in the same reply.

## The interview

Read [onboarding](references/onboarding.md) on the first run (questions, options, wording).
One round, at most four questions, in [asking](../asking/SKILL.md)'s short mode: `AskUserQuestion` when
`questions: click`, recommended option first with " (Recommended)"; otherwise a numbered
list, "1 = recommended" — never a widget, whatever `widgets` says. The task runs after the
answers (or at once on defaults when the user answers with the task instead). Answers not
given become labelled defaults; the readiness line is reprinted once with the new `budget`.

- **Plan of this host** — Pro / Max / Ultra / Other (Team, Enterprise, another app).
- **Connect now** (multi-select) — Needt connector, web search, YouTube, GitHub; free options
  from [tools-help](references/tools-help.md); tools already present are not offered, and
  nothing missing means no such question (at most three questions).
- **Language and tone** — reply language, casual or professional.
- **Memory** — on (recommended) or off for this chat; "Skip for now" for tools and memory.

Without the Needt connector, add after the readiness line, two lines at most: planner skills
(needt, plan) and memory need the connector, which comes with Needt Pro (price and link:
[tools-help](references/tools-help.md)); everything else works now. A planner request is
answered as text, never with a dead end.

## Save

Save `[fact] needt plugin set up <date>; budget: <pro|max|ultra|team|other>; tools: <kinds
present>; declined: <kinds turned down, or none>` through the memory rules, and report it in
one line. Repeat run with a change: `needt_update_memory` with its id (new date), never a second
line; nothing changed → no write. "What can you do" → outcomes in six lines or fewer, no
skill list. Language or
tone that differs from the default is saved as `[preference] …`. Without a connector the
profile holds for this chat only; say so once. When the user later adds or declines a tool,
update the same line; on the fallback page append a new line.

## The other skills

Who owns which request and how skills hand work over: [skills-map](references/skills-map.md).
Setup never lists the skills to the user — they fire on their own.

## Bring back a useful start

A task given → readiness line, interview if first run, then the task in the same reply. No
task → the line and one concrete starter prompt. Setup installs, connects, schedules and
publishes nothing; it points to how, and the user does it. Never say "everything works"
from catalog discovery alone.
