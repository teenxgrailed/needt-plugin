# Source kinds by question type

Read before a Normal or Deep search. Different questions live in different places. These
are minimums, not a menu; a report that skipped a required kind says so in `Still unclear`.

| Question type | Required source kinds | Why |
|---|---|---|
| How people actually do X; what is popular or trending; formats, workflows, playbooks | **YouTube guides and transcripts** + **X threads** + web | practitioners show the steps and numbers on video and argue about them on X long before articles catch up |
| Which library, tool, API, repo | **GitHub** (issues, releases, stars trend) + current docs (Context7) + web | the README sells; issues and merged PRs tell what breaks |
| What's out there, what's new, what's popular in tools or code | **GitHub discovery** — trending boards (daily/weekly), topic pages by stars, young repos gaining fast — then the health check | the best new tools show up on trending boards weeks before articles |
| A price, a plan, a limit, a date | the **official page**, opened, with the date | never recalled, never from a blog |
| A rule, a policy, a law | the **primary article, read in full**, and the exact clause quoted | an excerpt turns "X over 60 s with a claim is blocked" into "all X is blocked", and the dropped conditions decide the plan |
| A market, competitors, suppliers | competitors' own pages + forums in the market's language + X + web | what exists, what it costs, what people complain about |
| Anything scientific or medical | papers (research tools) + web | — |
| Is there a skill, plugin, MCP server or tool for X; "can my AI do X" | **the installed catalog first** (the user may already have it — [user-skills](../../setup/references/user-skills.md)), then **skill and tool directories** — the `find-skills` skill when present (`npx skills@1.7.4 find <query>`, skills.sh leaderboard), the MCP Registry, the host's own plugin/connector directory — + GitHub | a ready skill or connector beats a hand-built workflow; installs and stars show what is battle-tested |

Recipes for YouTube, X and GitHub (queries, which tool to call, what to extract, how to
cite): [tools.md](tools.md).
