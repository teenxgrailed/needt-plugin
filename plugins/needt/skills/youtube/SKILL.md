---
name: youtube
description: Reads a YouTube video so Claude knows what it actually says — pulls the title, channel, date, chapters, description and the full timestamped transcript, then answers from it. Use whenever the user's message has a youtube.com or youtu.be link, or says "о чем видео", "перескажи видео", "что в этом видео", "посмотри видео", "транскрипт", "расшифровка", "выжимка из видео", "summarize this video", "what does this video say", "transcript", "watch this", or when another Needt skill needs what a video says. Not for finding videos on a topic — that is search, which calls this skill for each video it picks.
---

# Needt · YouTube

The job: understand what the video says, as if you had watched it, and answer the user's real
question about it, with timestamps. A summary of the title and description is not that. A
transcript dumped into the chat is not that either.

## Sister skills

- [search](../search/SKILL.md) — finds which videos to read; uses this skill to read them.
- [needt](../needt/SKILL.md) — steps, tools or ideas from the video land in Needt as tasks.
- [setup](../setup/SKILL.md) — lists which transcript tools exist here.

## 1. Get the transcript — first route that works

1. **Bundled script (shell available).** It sits next to this file:
   `scripts/transcript.py` (use the base directory the host gave for this skill).

   ```bash
   python3 -I <skill-dir>/scripts/transcript.py "<url or id>" [--lang ru,en] [--out DIR]
   ```

   It writes `<out>/<id>.md` (default: the system temp dir, `needt-youtube/`) with the metadata,
   chapters, description and the transcript in ~30-second paragraphs `[mm:ss] …`. Short
   videos print in full; long ones print the header and a `FILE <path>` line — then read the
   file. Without `--lang` it takes manual captions in the video's own language, then the
   original auto track. Pass `--lang` only when the user wants a specific language.
   Exit codes: `2` — no `yt-dlp`: offer `brew install yt-dlp` (macOS) or `pipx install yt-dlp`,
   run it on a yes, retry; `3` — private, removed or age-gated video: say so; `4` — the video
   has no captions in any language: say so and work from the description and chapters only,
   labelled as such.
2. **Firecrawl** (`firecrawl_scrape` with `alexandria`, provider `youtube-com`):
   `videos/video_details` and `videos/video_transcript` with `{video_id}` in one call
   (the field takes an array). ~5 credits each.
3. **A youtube-transcript MCP** (`youtube_get_transcript`). A 401 or "IP blocked" means
   YouTube blocks that scraper from this network — move on, do not retry.
4. **Nothing worked** → say which routes were tried and why each failed. Never describe a
   video from its title, thumbnail or memory as if it had been read.

Several videos: run the script once per video in parallel; more than three long ones go to
Sonnet sub-agents per [delegation](../setup/references/delegation.md), each given section 2
of this file and the file path.

## 2. Read it

Read the whole transcript, not the first screen. Note for yourself:

- what the video is (tutorial, review, talk, vlog, ad) and who is speaking;
- the main claims and the steps in order, each with its timestamp;
- every tool, product, site and number named, with its context;
- what the author says not to do, and any sponsor segment (skip it in the summary, name it);
- what is shown but not said — a transcript is speech only, so "as you can see here" means
  the answer is on screen; say that you could not see it.

Auto captions mishear names, brands and numbers. A name that looks wrong is marked `(?)`
and checked against the description or a quick search before anything depends on it.

## 3. Answer

First line, fixed shape:
`YouTube · <title> · <channel> · <duration> · captions: <lang> <manual|auto>`

Then, in the user's language:

- **The user asked something specific** ("what tool does he use", "is X covered") → answer
  that directly, with the timestamp(s), then stop or add one line of context.
- **Just a link or "о чем видео"** → one sentence on what it is and for whom; 3–7 key points
  with `[mm:ss]`; tools and numbers named; one line on whether it is worth watching in full and
  which part, tied to the user's project when one is known.
- **"Транскрипт" / "дай текст"** → give the file path; quote only the passages they need.

Cite as `[mm:ss]` linked to `https://youtu.be/<id>?t=<seconds>` where links render. Keep the
file: follow-up questions about the same video are answered from it without fetching again.
Actionable steps the user wants to do → hand them to [needt](../needt/SKILL.md).
