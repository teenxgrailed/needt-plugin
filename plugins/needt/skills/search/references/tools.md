# Tool routing and source recipes for Needt · Search

Names are hints. Use what the setup line says exists in this session; a tool missing here is
skipped, not faked — and named in `Still unclear` if its source kind was required. Never
fetch pages with shell commands, curl or scripts.

## Routing table

| Job | Tool (when present) | How |
|---|---|---|
| Breadth, first round | multi-query web search (Parallel `web_search`) | several short queries in one call; excerpts often answer outright |
| Hard-to-keyword ideas | Exa `web_search_exa` | describe the ideal page ("a postmortem of migrating off X"), not keywords; `category: company / people` |
| Filtered search | `firecrawl_search` | `categories: ["developer"]` for GitHub issues, PRs, READMEs; `["research"]`, `["pdf"]`; `tbs` for recent; `location` for country prices |
| Code and libraries | `firecrawl_developer_search`, GitHub MCP (`search_repositories`, `search_code`, `search_issues`), `gh` CLI | see GitHub recipe |
| Current library docs | Context7 (`resolve-library-id` → `query-docs`) | for API and version facts instead of blog posts |
| One known page | `firecrawl_scrape` / web fetch | `maxAge: 0` for live data; `formats: ["json"]` with a schema for fields |
| What pages a site has | `firecrawl_map` | before crawling, or to find a pricing / changelog page |
| Several pages of one site | `firecrawl_crawl` | small `limit`; five pages usually answer it |
| Papers | `firecrawl_research_*` | biomedical, scientific, arXiv |
| YouTube guides | youtube-transcript MCP (`youtube_search_transcript`, `youtube_get_transcript`, `youtube_batch_transcripts`, `youtube_get_channel_videos`), web search `site:youtube.com` | see YouTube recipe |
| X threads | web search / Exa with `site:x.com`, a browser or X tool when one exists | see X recipe |
| JS-heavy or logged-in pages | the browser tools | when a fetch returns an empty shell; never when the setup line forbids browsers on this machine |

## YouTube recipe — guides, teardowns, "how I do it"

Use for: how people do X, what is popular, workflows, tools practitioners actually use,
numbers they say on camera (prices, conversion, time per unit), and formats to copy.

1. **Build 3–6 queries the way a guide would be titled**, not the way the user asked:
   "how I make faceless shorts 2026", "best TTS for YouTube shorts", "X vs Y honest review",
   "<tool> tutorial", "<niche> channel breakdown". Add the year for anything that moves fast.
2. **Find candidates**: `youtube_search_transcript` or web search with `site:youtube.com` plus
   the query; for a known channel, `youtube_get_channel_videos`. Prefer videos from the last
   12 months with high views relative to the channel, and at least one small-channel video —
   big channels sell, small ones show.
3. **Pull transcripts in one batch** (`youtube_batch_transcripts`, 3–8 videos). Read the
   description too: it is where the tools, links, discount codes and the real stack are listed.
4. **Extract**, per video: the steps in order; every tool, site or product named; every
   number with its context; the thing the author says *not* to do; the hook they used in the
   first 10 seconds (useful when the question is about content itself).
5. **Cross-check**: a tool named in two unrelated videos is a lead; a number that only one
   person says stays `(1 source)`. Prices from video are old the day they are said — open
   the official page.
6. **Cite** as `video title · channel · date · ~mm:ss` with the link. Note view count as the
   page shows it, dated.

Delegate the transcript reading to a Sonnet sub-agent when there are more than three videos;
give it the extraction list above.

## X recipe — practitioners arguing in public

Use for: what is trending right now, opinions of maintainers and operators, launch reactions,
"anyone tried X?" threads, numbers people brag about, early warnings about a tool or policy.

1. **Queries**: short, with the product or term and a signal word — "<tool> switched",
   "<tool> pricing", "<trend> brands", "<term> thread", "<term> results". Run them through
   web search or Exa with `site:x.com` (and `site:twitter.com` for older posts); Exa with
   `category: tweet` where supported.
2. **Who**: prefer accounts that build or operate the thing (maintainers, founders, editors,
   marketers with a public portfolio) over commentators. A reply from the maintainer in a
   thread outranks the thread.
3. **Read the replies** when the tool can open the post: that is where the counter-evidence
   and the "this stopped working in June" live.
4. **Dates matter**: X content ages in weeks. Every cited post carries its date; anything
   older than ~90 days is context, not evidence of what is current.
5. **Cite** as `@handle · date` with the link. Quote at most one short line per post.

No X tool and no browser in this session → say so; search excerpts still give the lead, and
the find is marked `(X: excerpts only)`.

## GitHub recipe — what really breaks

Use for: choosing a library or tool, whether something is maintained, known bugs with a
version, how others integrated it, real-world configs.

1. **Find candidates**: `firecrawl_developer_search` or GitHub `search_repositories` with the
   task in plain words ("react 19 drag and drop list"), plus awesome-lists for the landscape.
2. **Health check per repo** (one look each): last release date and cadence; open issues vs
   closed in the last 90 days; stars trend only as a tie-breaker; whether the maintainer answers.
3. **Issues over README**: `search_issues` for the user's exact pain ("<lib> next 15",
   "<lib> memory leak", "<lib> typescript types") sorted by reactions. Merged PRs show what
   got fixed and when; open ones with many thumbs-up show what will not be.
4. **Code search** (`search_code`) for how others wire it: "import <lib>" in repos with a
   similar stack reveals real configs faster than docs.
5. **Versions and APIs** come from the release page or Context7, not from a blog.
6. **Cite** as `owner/repo · issue #n or release vX.Y · date`.

`gh` CLI, when present, does the same with `gh search repos|issues|code` and `gh release list`.

## Where good finds usually hide

- **"Alternatives to X" + "migrated from X"** — the people who left tell you the real weakness.
- **GitHub issues sorted by reactions** — the limitations the README does not mention.
- **Changelogs and release notes** — what is new this year that blog posts have not caught up with.
- **YouTube descriptions** — the real tool list under a guide, with versions and links.
- **X replies under a launch post** — the first honest reviews.
- **Competitors' docs and pricing pages** — how someone already solved the same problem.
- **Forums in the user's market language** — local prices, suppliers, regulations.
- **Awesome-lists and curated directories** — the landscape in one page, then verify each entry.
