---
name: setup
description: Checks Needt readiness in the current conversation — the project, the preferred tone, which tools and skills are actually exposed (search tools, clickable questions, sub-agents, Marketing and Small Business skills), and the user's Needt memory. On the first run it also tells the user, in a few lines, which tools the plugin uses and how to get the missing ones for free. Every other Needt skill runs this check first when the conversation has no Needt readiness line yet. Use directly for "set up Needt", "настрой Needt", "проверь что подключено", "what can Needt use here". Does not install plugins, connect accounts, or change settings.
---

# Set up Needt

Short, useful, in the user's language. Not an interview. Normally three to six lines; a first
run adds at most six more.

## The readiness line

Setup always produces one line that starts exactly with `Needt ·`. Field names are in
English; values may be in the user's language. For example:

`Needt · ready · project: <name> · tone: casual · search: web, youtube, github · questions: click · agents: yes · memory: 12`

The line is the first line of the reply. Its only tool call is the one memory read (see
Memory), made before any text; every other field comes from the tool and skill catalog
already in context — load nothing to prove it. A skill that reads this file and does not
print the line has failed the check.

That line is the marker other Needt skills look for in the conversation. One per
conversation; run again only when the user asks or the project changes.

## Establish the context

Reuse what the conversation, memory and accessible project sources already establish: the
current project, what the user wants, how they write. Do not interrogate: at most one
question, and only when the project is unknown and the task depends on it. If the user writes
casually, match it without asking; otherwise default to friendly-professional and do not ask
about tone. Never ask for secrets or credentials.

## Fields

Read them from the host's real tool and skill catalog already in context — do not assume,
and do not call tools to test them.

- **project** — the current project, or `unknown`.
- **tone** — `casual` or `professional`, matched to how the user writes.
- **search** — the source kinds that exist here, from this set: `web` (a web search tool),
  `exa`, `firecrawl`, `youtube` (transcript tools), `x` (an X tool or a browser),
  `github` (GitHub MCP, developer search or `gh`), `context7`, `papers` (a paper index),
  `browser`. `none` if none.
- **questions** — `click` when a clickable question tool (`AskUserQuestion`) is listed,
  including as a deferred tool; otherwise `text`.
- **agents** — `yes` when sub-agents can be launched here (an Agent or Task tool); otherwise
  `no`. With `yes`, every Needt skill follows [delegation](references/delegation.md) for
  parallel work on cheaper models.
- **specialists** — Marketing / Small Business skills, matched by description, only if present.
- **memory** — the number of memory lines read; `none` when the store is empty; `off` when
  there is no Needt connector or the user switched memory off.

Listed is not the same as working: mark anything uncertain `unverified`. Do not read
transactions or customer records to test readiness, and do not claim something enabled in
another product is available here.

## Memory

Read memory once per conversation, in one call, following
[the memory rules](../needt/references/memory.md): `needt_list_memories` when it exists,
else the page "Needt · Memory", else nothing (`memory: off`, said once). Do not re-read
unless the user says memory changed.

Every line read is a standing instruction for all Needt skills in this conversation: a
`preference` or `pattern` outranks a skill's own default, a `goal` or `fact` is context the
user does not have to repeat. Setup only reads here; saving follows the same rules file.

## First run

1. After the memory read, look for a line `[fact] needt plugin set up <date>; …`.
2. Found: this is not a first run. Print the readiness line only and go on.
3. Not found: print the readiness line, then the onboarding, then continue with the task.
4. Onboarding is at most six lines in chat, in the user's language:
   - one line per missing tool kind: what it adds, that a free option exists, and the link or
     command from [tools-help](references/tools-help.md);
   - a kind that is a bigger setup gets one line saying so, without details;
   - one closing line: "Say which you want and I'll walk you through it."
   Nothing else — no list of what is already present beyond the readiness line, no tour.
5. Without the Needt connector, its line comes first: it is the one tool the plugin needs.
6. Save `[fact] needt plugin set up <date>; tools: <kinds present>; declined: <kinds the
   user turned down, or none>` through the memory rules, and report it in one line. Without
   a connector the line holds for this chat only; say so once.
7. When the user later adds or declines a tool, update that line instead of adding another.

## Bring back a useful start

If a task is already given, print the readiness line first and continue straight into that
task in the same reply. If no task is given, print the line and offer one concrete starter
prompt.

Setup authorizes no installation, account connection, global setting change, scheduling or
publication; it points to how, and the user does it. Never say "everything works" based only
on catalog discovery.
