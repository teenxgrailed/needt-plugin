# Needt for Claude, Codex and other MCP clients

[Needt](https://needt.app) is the place you keep everything you are working on — tasks, calendar, docs, habits, goals — with a scheduling engine that plans your day. This repository holds the official Needt plugin and the listing files for MCP directories.

## What is here

- `plugins/needt/` — the Needt plugin: the main `needt` skill (your planner and memory in any chat) plus `partner`, `prompt`, `search`, `asking`, `critic` and `setup` skills. It connects to the Needt MCP server.
- `server.json` — the MCP Registry entry.
- `.claude-plugin/marketplace.json`, `.agents/plugins/marketplace.json` — plugin marketplaces for Claude Code and Codex.

## What the plugin runs and where data goes

The plugin is instructions (Markdown skills) plus one MCP connection to `https://mcp.needt.app/mcp`. It runs no local scripts and has no hooks. When you use it, your assistant reads and writes your own Needt data through that server after you sign in with OAuth; nothing is sent anywhere else by the plugin. Needt's privacy policy: https://use.needt.app/privacy

## Install

Claude Code:

```bash
claude plugin marketplace add teenxgrailed/needt-plugin
claude plugin install needt@needt
```

Codex:

```bash
codex plugin marketplace add teenxgrailed/needt-plugin
```

Any MCP client: add the remote server `https://mcp.needt.app/mcp` (streamable HTTP, OAuth).

## Support

hello@needt.app · https://needt.app/resources/mcp/ · Terms: https://use.needt.app/terms
