---
name: setup
description: Internal — other Needt skills run it automatically on first use. Checks Needt readiness in the current conversation — the project, the preferred tone, which tools and skills are actually exposed (search tools, clickable questions, sub-agents, chat widgets, Marketing and Small Business skills), and the user's Needt memory. On the first run it also tells the user, in a few lines, which tools the plugin uses and how to get the missing ones for free. Every other Needt skill runs this check first when the conversation has no Needt readiness line yet. Use directly for "set up Needt", "настрой Needt", "проверь что подключено", "what can Needt use here". Does not install plugins, connect accounts, or change settings.
---

# Set up Needt

Short, useful, in the user's language. Not an interview. Normally three to six lines; a first
run adds at most six more.

## The readiness line

Setup always produces one line that starts exactly with `Needt ·`. Field names are in
English; values may be in the user's language. For example:

`Needt · ready · project: <name> · tone: casual · search: web, youtube, github · questions: click · agents: yes · widgets: yes · memory: 12`

The line is the first line of the reply. It costs only the one memory read
(see Memory), made before any text — plus loading that tool if the host defers it; every
other field comes from the tool and skill catalog already in context — run nothing to prove
it. `project` is the project the conversation is about, `none` when the open folder is
unrelated to the task. A skill that reads this file and does not
print the line has failed the check.

That line is the marker other Needt skills look for in the conversation. One per
conversation; run again only when the user asks or the project changes. The first time it is
printed in a conversation, one short line in the user's language follows it, once: that it is
Needt's readiness check showing what this chat can use.

## Establish the context

Reuse what the conversation, memory and accessible project sources already establish: the
current project, what the user wants, how they write. Do not interrogate: at most one
question, and only when the project is unknown and the task depends on it. If the user writes
casually, match it; otherwise default to friendly-professional and do not ask
about tone. Never ask for secrets or credentials.

## Fields

Read them from the host's real tool and skill catalog already in context — do not assume,
and do not call tools to test them.

- **project** — the current project, or `unknown`.
- **tone** — `casual` or `professional`, matched to how the user writes.
- **search** — the source kinds that exist here, from this set: `web` (a web search tool),
  `exa`, `firecrawl`, `youtube` (transcript tools, or a shell with `yt-dlp` for the bundled script), `x` (an X tool or a browser),
  `github` (GitHub MCP, developer search or `gh`), `deepwiki`, `context7`, `papers` (a paper
  index or arXiv MCP), `tavily`, `fetch`, `skills` (the `find-skills` skill), `skillspector`
  (the safety scanner on PATH), `browser`.
  `none` if none. Hacker News, Stack Exchange and OpenAlex need no tool (free APIs read by web
  fetch) and are not listed. Count what a tool covers, not only its name: Firecrawl with
  `firecrawl_developer_search` also gives `github`, with `firecrawl_research_*` gives
  `papers`, with its `youtube-com` provider gives `youtube`; Exa gives `x` when it can search
  tweets. `x` without an X tool, browser or Exa is `x: web only` — say so, do not list it as a
  full source.
- **questions** — `click` when a clickable question tool (`AskUserQuestion`) is listed,
  including as a deferred tool; otherwise `text`. Inside a sub-agent it is never available —
  a sub-agent writes `text` even when the memory says `click`.
- **agents** — `yes` when sub-agents can be launched here (an Agent or Task tool); otherwise
  `no`. With `yes`, every Needt skill follows [delegation](references/delegation.md) for
  parallel work on cheaper models.
- **widgets** — `yes` when a `show_widget` tool (the host's `visualize` server) is listed;
  otherwise `no`. Inside a sub-agent always `no`. With `yes`, every Needt skill follows
  [widgets](references/widgets.md) for what is shown as a widget in the chat.
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

1. After the memory read, look for a memory of kind `fact` whose content starts with
   `needt plugin set up`.
2. Found: this is not a first run. Print the readiness line only and go on.
3. Not found: print the readiness line, then the onboarding, then continue with the task.
4. Onboarding is at most six lines in chat, in the user's language:
   - one line per missing tool kind: what it adds, that a free option exists, and the link or
     command from [tools-help](references/tools-help.md);
   - a kind that is a bigger setup gets one line saying so, without details;
   - one closing line naming the one tool to add first, with its link or command; the rest
     can wait.
   Nothing else — no list of what is already present beyond the readiness line, no tour.
5. Without the Needt connector, its line comes first: it is the one tool the plugin needs.
6. Save `[fact] needt plugin set up <date>; tools: <kinds present>; declined: <kinds the
   user turned down, or none>` through the memory rules, and report it in one line. Without
   a connector the line holds for this chat only; say so once.
7. When the user later adds or declines a tool, update that memory with `needt_update_memory`
   and its id instead of adding another; on the fallback page append a new line.

## Bring back a useful start

If a task is already given, print the readiness line first and continue straight into that
task in the same reply. If no task is given, print the line and offer one concrete starter
prompt.

Setup authorizes no installation, account connection, global setting change, scheduling or
publication; it points to how, and the user does it. Never say "everything works" based only
on catalog discovery.
