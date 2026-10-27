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
- Free: several open-source YouTube-transcript MCP servers exist; none needs a paid key.
- claude.ai / Desktop: Settings → Connectors → search for "YouTube transcript", or add a
  local MCP server on Desktop. Claude Code: add the chosen server with `claude mcp add`
  using the command from its README.

## Firecrawl

- Gives: reads full pages, whole sites and search results cleanly, including JS-heavy pages.
- Free: free tier with an API key from firecrawl.dev.
- claude.ai / Desktop: Settings → Connectors → search for "Firecrawl".
- Claude Code: `claude mcp add firecrawl -e FIRECRAWL_API_KEY=<key> -- npx -y firecrawl-mcp`

## Exa

- Gives: meaning-based web search — finds similar companies, papers and posts, not keywords.
- Free: free tier with an API key from exa.ai.
- claude.ai / Desktop: Settings → Connectors → search for "Exa".
- Claude Code: add the Exa MCP server with `claude mcp add` using the command in Exa's docs.

## GitHub

- Gives: repositories, code, issues and pull requests as sources.
- Free: the official GitHub MCP server; needs a GitHub personal access token.
- claude.ai / Desktop: Settings → Connectors → search for "GitHub".
- Claude Code: `claude mcp add --transport http github https://api.githubcopilot.com/mcp/ -H "Authorization: Bearer <token>"`,
  or simply have the `gh` CLI installed and signed in (`gh auth login`).

## Context7

- Gives: current documentation for libraries, frameworks and APIs.
- Free: no key needed for basic use.
- claude.ai / Desktop: Settings → Connectors → search for "Context7".
- Claude Code: `claude mcp add --transport http context7 https://mcp.context7.com/mcp`

## Browser

- Gives: pages that need a login, clicks or JavaScript; sites without an API (X, portals).
- Free: built into some hosts (Claude in Chrome, a browser pane in Claude Desktop).
- Setting up a browser elsewhere is a bigger setup — say so in one line and skip the details.

Tools the host does not expose are skipped by the skills, not faked.
