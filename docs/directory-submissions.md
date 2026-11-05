# Directory submissions — texts and status (2026-11-03)

## 1. Official MCP Registry — `io.github.teenxgrailed/needt`

`server.json` in the repo root. Publish: `mcp-publisher login github` (device code, account
teenxgrailed) → `mcp-publisher publish` from the repo root. Glama and PulseMCP ingest the
registry on their own.

## 2. Anthropic directory (claude.ai/directory/manage) — owner, paid plan, browser

Two submissions from the same organization: the **MCP connector** (`https://mcp.needt.app/mcp`)
first, then the **plugin bundle** (repo `teenxgrailed/needt-plugin`, folder `plugins/needt`).
Pre-check: `claude plugin validate plugins/needt --strict` — run before submitting.

**Plugin name:** Needt

**Description (50–100 words):**
Needt gives Claude your planner and nine working skills. `/needt` adds, moves and finishes
tasks, reads your day across calendars, logs habits, writes pages and turns mail into tasks
through the Needt connector. Partner thinks through a business move and does the work. Search
finds the good option with sources. Prompt writes one well-built prompt. Asking stress-tests
a plan with clickable questions, Critic reviews it, Roadmap keeps a project roadmap alive across
sessions, Learn explains one thing so it sticks, YouTube reads a video. Memory follows you
across chats. Works in English, Russian, Ukrainian, German, Spanish and French.

**Three use cases:**
1. "What's on today?" → the day's events and scheduled tasks from Needt, Done buttons per task.
2. "Roadmap for launching my shop" → a Needt project with milestones and blockers, "where are
   we" answered in any later chat, a clickable map in Claude Desktop.
3. "Should I buy 40 jackets at €18 to resell?" → numbers executed on labelled assumptions and a
   verdict: take / take if X / walk.

**Platform:** Claude (web, Desktop), Claude Code, Cowork. **Org URL:** https://needt.app
**Contact:** hello@needt.app **Repo:** https://github.com/teenxgrailed/needt-plugin

## 3. awesome-claude-code (hesreallyhim) — owner, web issue form

Rules: issue form only (no PR, no `gh`), "created by people", repo ≥ 14 days old with
activity or ≥ 100 stars, one resource at a time, one-line description without a pitch.
Form: https://github.com/hesreallyhim/awesome-claude-code/issues/new?template=recommend-resource.yml

**Name:** Needt
**Category:** Plugins / Skills
**Link:** https://github.com/teenxgrailed/needt-plugin
**One line:** Ten skills for Claude Code and Claude — planner, business partner, research, prompt
builder, grill-me, critic, project roadmap, explainer, YouTube reader — with memory kept in the
Needt app.
**License:** MIT

## 4. Form directories — any browser, free tier

| Where | URL | What to enter |
|---|---|---|
| mcp.so | https://mcp.so/submit | repo URL, type "remote server" + "agent skill", description below |
| Plug and Ship | https://plugandship.dev/submit | repo URL (plugin for Claude Code) |
| claudemarketplaces.com, SkillsMP, skills.sh | automatic from GitHub / installs | nothing |

**Short description (≤160):** Needt plugin: your planner in every chat plus partner, search,
prompt, asking, critic, plan, learn and YouTube skills; memory that follows you. MIT.

## Status

- [x] MCP Registry — listed as `io.github.teenxgrailed/needt` 1.0.0, active since 2026-10-27 (https://registry.modelcontextprotocol.io/v0/servers?search=needt); bump `server.json` version before any re-publish
- [ ] Anthropic directory — owner
- [ ] awesome-claude-code — web form only (gh/PR → account restricted); repo created 2026-10-27, bot needs ≥ 14 days → submit from 2026-11-10 (Needt task set)
- [x] Plug and Ship — submitted 2026-11-05, free queue, launch 2026-11-27: https://plugandship.dev/p/needt (badge: https://plugandship.dev/badge/needt.svg)
- [ ] mcp.so — paid only, parked
