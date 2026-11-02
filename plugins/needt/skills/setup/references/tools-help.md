# Tools the Needt plugin uses, and how to add them

For the first-run onboarding in setup. Each entry: what it gives, the free option, how to add
it. On claude.ai and Claude Desktop tools come from **Settings → Connectors** (a directory
connector, or "Add custom connector" with a URL). On Claude Code they come from
`claude mcp add`. Say the path; never guess a URL that is not written here.

## Needt connector — required

- Gives: the user's own tasks, projects, calendars, pages, habits, mail and memory.
- Free: included with the user's Needt account; nothing else to buy.
- claude.ai / Desktop: Settings → Connectors → add the Needt connector with the URL shown in
  the Needt app. Claude Code: `claude mcp add --transport http needt <URL from the Needt app>`.
- Memory: turn on "Let Needt learn about me" in the Needt app settings; with it off, nothing
  is saved between chats.

## Web search — usually built in

- Gives: current facts, prices, news, any page on the open web.
- Free: built into claude.ai, Claude Desktop and Claude Code on most plans.
- If missing: on claude.ai / Desktop turn on web search in the chat's tools menu; on Claude
  Code it is a built-in tool that may need permission. Nothing to install.

## YouTube transcripts

- Gives: what a video actually says, so skills can cite talks, reviews and tutorials.
- Best on a computer with a shell (Claude Code, Desktop with a terminal): `yt-dlp` — free, no
  key, not blocked like scrapers. macOS `brew install yt-dlp`, otherwise `pipx install yt-dlp`.
  The youtube skill's bundled script uses it.
- Easiest without a shell: Firecrawl (below) already includes YouTube search, transcripts, details and
  comments through its `youtube-com` provider — no separate server needed.
- Free alternative: open-source YouTube-transcript MCP servers exist and need no key, but
  YouTube blocks them from many networks (a 401 on every video means that); then use
  Firecrawl. claude.ai / Desktop: Settings → Connectors → search for "YouTube transcript".
  Claude Code: `claude mcp add` with the command from the server's README.

## Tavily — the best free extra web search

- Gives: web and news search, page extract, site map and crawl, tuned for AI agents.
- Free: 1,000 credits a month, no card (a basic search is 1 credit).
- claude.ai / Desktop: Settings → Connectors → Add custom connector → `https://mcp.tavily.com/mcp`
  (sign in with OAuth). Claude Code: `claude mcp add --transport http tavily https://mcp.tavily.com/mcp`,
  then `/mcp` to sign in.
- Zero-signup fallback on Claude Code: `claude mcp add ddg -- uvx duckduckgo-mcp-server@0.7.0`
  (free; DuckDuckGo blocks it at times and then returns nothing).

## Firecrawl

- Gives: reads full pages, whole sites and search results cleanly, including JS-heavy pages —
  plus ready data providers: YouTube, X posts, Amazon/eBay/Etsy products and prices, Google
  Maps places and reviews, Stack Exchange.
- Free: ~1,000 credits a month with an API key from firecrawl.dev; when they run out, the
  skills switch to other tools until next month.
- claude.ai / Desktop: Settings → Connectors → search for "Firecrawl".
- Claude Code: `claude mcp add firecrawl -e FIRECRAWL_API_KEY=<key> -- npx -y firecrawl-mcp@3.36.0`

## Exa

- Gives: meaning-based web search — finds similar companies, papers and posts, not keywords.
- Free: free tier with an API key from exa.ai.
- claude.ai / Desktop: Settings → Connectors → search for "Exa".
- Claude Code: add the Exa MCP server with `claude mcp add` using the command in Exa's docs.

## GitHub

- Gives: repositories, code, issues and pull requests as sources.
- Free: the official GitHub MCP server; needs a GitHub token made in GitHub settings.
- claude.ai / Desktop: Settings → Connectors → search for "GitHub".
- Claude Code: `claude mcp add --transport http github https://api.githubcopilot.com/mcp/ -H "Authorization: Bearer <token>"`,
  or simply have the `gh` CLI installed and signed in (`gh auth login`).
- The old `@modelcontextprotocol/server-github` package is archived since May 2025 and gets no
  security fixes — replace it with the server above.

## DeepWiki — how any public repo works

- Gives: answers about the inside of any public GitHub repo ("where is auth handled?").
- Free: no key, no sign-up.
- claude.ai / Desktop: Add custom connector → `https://mcp.deepwiki.com/mcp`.
  Claude Code: `claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp`.

## Papers and packages — Claude Code / Desktop with a shell

- arXiv: `claude mcp add --transport stdio --scope user arxiv -- uvx arxiv-mcp-server@0.8.2` (free).
  OpenAlex needs nothing — the skills read its free API directly.
- PyPI: `uvx mcp-pypi@4.0.1` (free; versions, changelogs, vulnerabilities).
- Plain page fetch without any key: `claude mcp add fetch -- uvx mcp-server-fetch@2026.10.28`.

## Hacker News, Stack Overflow, Reddit, X

- Hacker News and Stack Overflow: nothing to install — the skills read their free APIs.
- Reddit: closing to outside tools (RSS ends 2026-11-13, the API needs approval); the skills
  reach Reddit threads through web search. Do not install Reddit MCP servers.
- X: Firecrawl covers search and profiles without an X account. The official X API has no free
  tier — only worth it if you already pay for an X developer app.

## Anki — for users who already keep flashcards there

- Gives: the learn skill can push misses as cards into the user's Anki deck and read what
  is due, through Anki's own scheduler.
- Free: Anki is free; the MCP add-on is open source (`ankimcp/anki-mcp-server`, MIT, 0.27.0
  as of 2026-10-04). Anki desktop must be running while it is used.
- Setup: install the AnkiMCP add-on from its README, then on claude.ai / Desktop → Settings
  → Connectors → Add custom connector with the local URL the add-on shows; on Claude Code
  `claude mcp add anki -- npx -y @ankimcp/anki-mcp-server@0.27.0`.
- Without it, the learn skill keeps its own review schedule in Needt — nothing is lost.

## Context7

- Gives: current documentation for libraries, frameworks and APIs.
- Free: no key needed for basic use; a free key from context7.com raises the rate limit.
- claude.ai / Desktop: Settings → Connectors → search for "Context7".
- Claude Code: `claude mcp add --transport http context7 https://mcp.context7.com/mcp`

## SkillSpector — safety scan for skills (Claude Code / a shell)

- Gives: checks a skill, plugin or MCP server for prompt injection, data theft, dangerous code
  and vulnerable dependencies before you install it. By NVIDIA, Apache-2.0.
- Free: open source, no key for the static scan.
- Install (needs `uv` and Python 3.12+):
  `uv tool install --python 3.12 "git+https://github.com/NVIDIA/SkillSpector.git@v2.12.0"`.
  Then `skillspector scan <url or folder> --no-llm`.
- Without a shell (claude.ai): the skills read the skill's files themselves and flag the
  same risks.

## Browser

- Gives: pages that need a login, clicks or JavaScript; sites without an API (X, portals).
- Free: built into some hosts (Claude in Chrome, a browser pane in Claude Desktop).
- Setting up a browser elsewhere is a bigger setup — say so in one line and skip the details.

Tools the host does not expose are skipped by the skills, not faked.
