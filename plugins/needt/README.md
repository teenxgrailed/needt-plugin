# Needt

**Think together. Write the right prompt. Find the good stuff.**

## Skills

| Skill | Command | Purpose |
|---|---|---|
| Needt · Main | `/needt:needt` | Works your planner through the Needt connector: tasks, plans broken into tasks, today/next, reschedule, done, events, habits, pages, mail read into tasks, memory. Fires on its own on planner intents in EN/RU/UK/DE/ES/FR |
| Partner | `/needt:partner` | Main skill #2: a partner in everything — plans, moves, ideas, decisions, money. Uses every other skill and every tool the host exposes, does the work instead of advising, lands it in Needt |
| Prompt | `/needt:prompt` | Turns a rough wish into one prompt sized to the task, with ideas and Needt skill stages built in |
| Search | `/needt:search` | Researcher that finds the non-obvious good option for your project — wide then narrow, mixed sources, verified, cited |
| YouTube | `/needt:youtube` | Reads a video — metadata, chapters, timestamped transcript through a bundled `yt-dlp` script, Firecrawl as fallback — and answers from what it actually says. Fires on any YouTube link |
| Asking | `/needt:asking` | Stress-tests a plan in rounds of clickable questions; other skills use its short mode to clarify |
| Learn | `/needt:learn` | Explains one thing at the user's level: the mechanism, one example from their world, one clickable diagram or subject map where widgets exist, one check question. No quiz mode |
| Critic | `/needt:critic` | Reviews a plan before launch from scratch: Problem → Solution → Cost → Confidence, then the revised plan |
| +Setup | `/needt:+setup` (internal) | Onboards on first run, checks project, tone, tools and memory; prints the `Needt ·` readiness line |

Every skill looks for the `Needt ·` readiness line in the conversation first. If it is
missing, the skill runs the short setup check, prints the line and continues the task in the
same reply — setup never blocks work.

The plugin is included with the Needt subscription and works in any language: fixed markers
such as `Needt ·` and `Search ·` stay as they are, everything else follows the user's language.

The main skill acts on its own on anything reversible (create, move, complete, schedule);
deleting and anything that leaves Needt ask first. Other skills finish in chat and hand the
result to the main skill to land in Needt.

**Memory.** The plugin saves preferences, "never do X" rules, goals and project facts on its
own and reports each in one `Saved:` line. It writes through `needt_remember` when the connector
offers it, otherwise to a "Needt · Memory" page in Needt, otherwise keeps it in the chat only.
Setup reads memory once per conversation and shows the count as `memory: n` in the `Needt ·`
line. Rules: `skills/needt/references/memory.md`.

**Widgets.** Where the host renders chat widgets (Claude Desktop's `visualize` tool), the
readiness line says `widgets: yes` and skills show what has a shape — today's list with Done
buttons, option cards, money metrics, finding cards, a mechanism diagram — as a widget, with the
same answer in text everywhere else. Rules: `skills/setup/references/widgets.md`.

**Sub-agents.** Skills run independent sweeps (searches, transcript reading, extraction) in
parallel sub-agents on a cheaper model, following `skills/setup/references/delegation.md`.
The main model keeps synthesis and decisions.

Skills call each other through relative links (`../search/SKILL.md`), so the package works
wherever the host can read skill files. Marketing and Small Business are optional external
plugins that Partner uses when present. No MCP servers, hooks, schedulers or agents are bundled; the only script is the youtube
skill's transcript fetcher (Python standard library + `yt-dlp`).

**Required and optional tools.** The Needt connector is required for the main skill and for
memory; without it they fall back to text in the chat. Everything else — web search, YouTube
transcripts, X, GitHub, Marketing, Small Business — is optional; setup lists what is missing on
first run with free options and a link or one command for each.

## Install in Claude

Customize > Plugins > upload `needt.plugin`. Remove the older `needt-partner` plugin so its
skills do not appear twice. Local test without installing:

```sh
claude --plugin-dir /absolute/path/to/needt
```

First run: connect the Needt connector (Customize > Connectors), then say anything planner-like
or run `/needt:+setup`. Setup onboards once and records "set up" in memory so it does not repeat.

## ChatGPT and Codex

The root `plugin.json` carries the portable manifest with the OpenAI interface extension.
Upload flows differ between hosts; a valid package does not prove an account has an upload
control. Not submitted to any public directory; do not present it as an official Anthropic or
OpenAI plugin.

## Data and limits

Installing Needt connects no accounts and authorizes no messages, orders, spending,
publication or scheduled sends. No telemetry. Memory lives in your Needt account (or only in the
conversation without the connector); the plugin keeps no copy of its own. No business outcome is guaranteed; final decisions stay with the user.

## Changelog

0.9.0 (2026-11-02)

- learn is Explain only: one explanation, one diagram or a clickable subject map with
  `✓` on what is passed (state in one memory line), one check question, one reaction.
  Study, Drill, the lesson/drill widgets, FSRS, progress pages, review tasks and the Anki
  entry are removed — a lesson loop in chat was slow and expensive in live use.

0.8.0 (2026-11-02)

- learn: three item types in a run (`pick`, `type`, `reorder`); a miss shows the rule and a
  `Why?` button (the only mid-run message); FSRS scheduling (ts-fsrs 6) inside the widget,
  card states on the topic page, the review task dated by the earliest due; a Reference
  page per topic; the mission (why the user learns) steers examples; Anki connector in
  tools-help for users who keep Anki.

0.7.3 (2026-11-02)

- learn: with widgets, a Study lesson is one widget ("the lesson run": pieces, questions
  and checks inside, one summary line back), like the Drill round; a time in the request is
  a budget for one run; fewer setup calls; unique ids per widget.

0.7.2 (2026-11-02)

- learn: blueprints for its three widgets in `learn/references/blueprints.md` — the Drill run
  (one question at a time inside the widget, keys 1–4, instant tint, rail, streak, result
  screen with Send result / Replay misses), the Study step card, the Explain mechanism
  diagram with clickable parts.

0.7.1 (2026-11-02)

- learn Drill: one round = one widget (or one message) with all questions, scored inside;
  one summary line back to the chat. No per-question round trips, no timer.
- widgets.md: many small answers go into one widget that sends one summary line.

0.7.0 (2026-11-02)

- New skill `learn`: Explain / Study / Drill, one step per reply, the user answers before the
  next step; progress page `Needt · Learn · <topic>` and a `Review: <topic>` task in Needt.
- Chat widgets: readiness line gains `widgets: yes|no`; shared rules in
  `setup/references/widgets.md`; hooks in needt (today's list with Done buttons), partner
  (metric cards, move cards), search (option cards), asking (elicitation form when no
  AskUserQuestion), critic (finding cards with Accept fix), prompt (Use / Change / Copy
  buttons when no AskUserQuestion). Same answer in text where the host has no widgets.

0.6.6 (2026-11-02)
- youtube is now a service skill: any YouTube link in any message is read first, whatever the message asks, and the owning skill (needt, search, critic, partner, prompt, asking) continues from the transcript file. A contract section defines the one-call interface; every other skill names when it calls youtube and what it takes from the video.

0.6.5 (2026-11-02) — fixes from a live test of every skill
- search: OSS Insight marked dead (empty since 2026-03-01), Trendshift numbers unlabeled → names only, keyless GitHub API fallback when the GitHub MCP fails, no pasting of a tool's billing link, HN limit unverified, Jina wording.
- setup: the readiness line's one allowed call is the memory read (was contradictory with partner); `project: none` for an unrelated folder; sub-agents always report `questions: text`.
- needt: a memory line about task language outranks "user's language"; `needt_schedule` is read for the range only; overdue in one line; `start` pins on create.
- prompt: the text fallback offers all three choices (go / change / copy).
- asking: two rounds by default, one question per decision instead of one per item.
- youtube: always `--print head` + `--out`, read the file in pieces.
- critic: the fresh-route summary opens the reply.

0.6.4 (2026-11-02)
- Prompt ends with a one-click choice right after the prompt: **Use prompt** (runs it in this chat), **Change something**, **Copy only**. Copy only is recommended when the prompt is for another product. Without clickable questions it offers `go` in one line.

0.6.3 (2026-11-02)
- The plugin passes its own SkillSpector scan: risk 91 → 25 (CAUTION, no HIGH findings). Every `npx`/`uvx` install line is pinned to a version, no text names credential files, and reversible actions are described as "runs, then reports". The remaining findings are the documented API URLs, the onboarding skill path and the YouTube script's argument-list `subprocess` call.

0.6.2 (2026-11-02)
- Safety check before installing any skill, plugin or MCP server: NVIDIA SkillSpector scan when present (`skillspector scan <src> --no-llm`; risk 51+ = do not install), otherwise a manual read of SKILL.md and scripts for the known red flags. Search and partner both run it; setup lists how to install SkillSpector.

0.6.1 (2026-11-02)
- Search has a GitHub discovery recipe: GitHub Trending, OSS Insight trends API, Trendshift, gitdebt and whatstrending star-velocity boards, topic pages and `created:`/`pushed:` searches — popular and rising checked separately, then a health check.

0.6.0 (2026-11-02)
- Search knows many more sources, all checked 2026-11-02: Tavily (1,000 free credits, OAuth), DuckDuckGo fallback, DeepWiki and GitMCP for repo internals, the official GitHub MCP (old package archived), PyPI/npm package tools, arXiv MCP and the OpenAlex API, Jina Reader and fetch MCP, Hacker News (Algolia) and Stack Exchange APIs, Firecrawl providers for X, Amazon/eBay/Etsy, Google Maps, Bing places, Instagram/TikTok.
- Reddit is closing to outside tools (RSS ends 2026-11-13) — search reaches it through web search only.
- A spent tool (Firecrawl 402, any 429) switches to the next one instead of retrying.
- `find-skills` routes "is there a skill or MCP for X" questions.
- Setup onboarding lists the new free options.

0.5.4 (2026-11-02)
- Setup counts what a tool covers, not only its name: Firecrawl also gives github (developer search), papers and youtube; X without a dedicated tool is reported as `x: web only`.

0.5.3 (2026-10-28)
- Needt tasks are written like a person would: the user's language only, short and plain, no time, emoji, symbols, prefixes or AI filler in titles; descriptions only when they add something.

0.5.2 (2026-10-28)
- New `youtube` ("Needt · YouTube"): reads a video from a link — title, channel, date, chapters,
  description and a timestamped transcript via the bundled `scripts/transcript.py` (`yt-dlp`,
  manual captions first, rolling auto-caption repeats removed), then Firecrawl, then a
  transcript MCP. Answers the user's question with `[mm:ss]` citations. Search uses it to read
  videos; setup counts `yt-dlp` as a YouTube source.

0.5.1 (2026-10-28)
- Partner rewritten as the second main skill: a 5-step loop (situation → real question → better move → work → land in Needt), routes to every skill and reads every host MCP, ideas as 2–4 grounded moves with a first step, plans that start today; money rigor kept in full.
- memory.md carries the final `needt_remember` signature (no workspaceId; 400/400/409 errors; `updated` flag).

0.5.0 (2026-10-28)
- New main skill `needt` ("Needt · Main"): works the planner through the Needt connector —
  tasks, plans broken into tasks, today/next, reschedule, done, events, habits, pages, mail
  read into tasks, memory. Fires on its own on planner intents in EN/RU/UK/DE/ES/FR.
  Everything reversible runs at once and is reported; deleting and anything leaving Needt asks.
  The `tasks` skill (0.4.0) is merged into it and removed.
- Memory (`skills/needt/references/memory.md`): saves preferences, "never do X", goals and
  project facts on its own with a one-line `Saved:` report, through `needt_remember` when the
  connector offers it, otherwise a "Needt · Memory" page, otherwise chat-only. Setup reads
  memory once per conversation (`memory: n` in the `Needt ·` line).
- New `critic` ("Needt · Critic"): reviews a plan before launch from scratch; every finding is
  Problem → Solution → Cost → Confidence, then the revised plan; soft in tone, hard on outcomes.
- Setup onboards on first run: which source tools exist, free options for missing ones, links
  or one command; records "set up" in memory so it runs once.

0.4.0 (2026-10-27)
- New: `tasks` turns plans, research, prompt stages and partner outcomes into Needt tasks
  through the Needt connector (checks for duplicates, pages for documents); plain checklist
  without the connector.
- Search: required source kinds per question type, YouTube transcript, X and GitHub recipes,
  mandatory `Search ·` first line.
- Sub-agent delegation rules shared by all skills (`setup/references/delegation.md`).
- Setup line is now the mandatory first line and carries an `agents` field.
- Prompt: stages that name a skill must run it; deliverables go to durable places.
- Asking: recommendations grounded in the project.
- All fixed strings in English, text in the user's language; owner-specific content removed.

0.3.0 (2026-10-27)
- Plugin renamed `needt-partner` → `needt`.
- New: `prompt` (prompt builder with S/M/L sizing and skill stages), `search` (researcher
  built on Anthropic's multi-agent research lessons: wide-then-narrow, effort budgets,
  perspectives, two-source verification), `asking` (adapted from mattpocock/skills grill-me,
  MIT, with a short mode for other skills).
- Setup prints a `Needt ·` readiness line, records search tools and question mode; every
  skill checks for it first.
- Partner links to search, asking and prompt.

0.2.0 (2026-10-09)
- Rule priority, work-first, casual register, brand-voice fallback, money checks, specialist
  routing; see git history of the previous package.

## Maintainer notes

Keep root `plugin.json` and `.claude-plugin/plugin.json` name and version aligned.
Project-specific taste belongs in user context, not in shared plugin instructions.
