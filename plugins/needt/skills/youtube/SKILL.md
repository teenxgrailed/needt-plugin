---
name: youtube
description: Reads a YouTube video so Claude knows what it actually says — pulls the title, channel, date, chapters, description and the full timestamped transcript, then answers from it. Fires on its own whenever any message contains a youtube.com, youtu.be or YouTube Shorts link, whatever else the message asks (make tasks from it, critique the plan in it, compare it with X) — the link is read first, then the skill that owns the request continues with the transcript. Also for "о чем видео", "перескажи видео", "что в этом видео", "посмотри видео", "транскрипт", "расшифровка", "выжимка из видео", "summarize this video", "what does this video say", "transcript", "watch this", or when another Needt skill needs what a video says. Not for finding videos on a topic — that is search, which calls this skill for each video it picks.
---

# Needt · YouTube

The job: understand what the video says, as if you had watched it, and answer the user's real
question about it, with timestamps. A summary of the title and description is not that. A
transcript dumped into the chat is not that either.

## A link anywhere means: read it first

A YouTube link in a message is input, not a request. Whatever the message asks — «сделай
задачи из этого видео», "is the plan in this talk any good?", "compare this with Notion",
"what do people say about this?" — the video is read with section 1 before anything else, and
the skill that owns the request (needt, critic, partner, search, prompt, asking) works from
the transcript file. The user never has to say "watch it" or name this skill. Without a link,
the skill fires only on the phrases in its description.

## Used by other skills — the contract

Who calls this skill and what comes back: [skills map](../setup/references/skills-map.md).

Any Needt skill that meets a video calls this one in place (no hand-off, no user prompt):

1. Run section 1 (first route that works) → a file `<out>/<id>.md` and the header line
   `YouTube · <title> · <channel> · <duration> · captions: <lang> <manual|auto>`.
2. Print the header line once in the reply, then read the file and continue with the
   caller's own rules. Do not produce the section-3 summary unless that is what the user
   asked for.
3. Several links → one run per link, in parallel; the files stay for the whole conversation,
   so a later question about the same video is answered from the file, never refetched.
4. Nothing worked → the caller says in one line which routes failed and goes on with what it
   has (title, description) labelled as unread.

Who calls it for what:

| Caller | The video is… | What it takes from the transcript |
|---|---|---|
| [needt](../needt/SKILL.md) | a how-to, a checklist, a plan to follow | the steps in order → tasks, each with the `[mm:ss]` in the description |
| [search](../search/SKILL.md) | one of the sources it picked | tools, numbers, claims with timestamps, cross-checked against other sources |
| [critic](../critic/SKILL.md) | a plan, a strategy, a pitch | the plan as stated, then the normal critique |
| [partner](../partner/SKILL.md) | a competitor, a method, an idea the user brings | what is actually claimed vs what the user's data says |
| [prompt](../prompt/SKILL.md) | material for the prompt | the key points into `<inputs>`, cited with timestamps |
| [asking](../asking/SKILL.md) | a fact a question depends on | the fact, looked up, never asked |
| [setup](../setup/SKILL.md) | — | lists which transcript routes exist here |

## 1. Get the transcript — first route that works

1. **Bundled script (shell available).** It sits next to this file:
   `scripts/transcript.py` (use the base directory the host gave for this skill).

   ```bash
   python3 -I <skill-dir>/scripts/transcript.py "<url or id>" [--lang ru,en] [--out DIR]
   ```

   It writes `<out>/<id>.md` (default: the system temp dir, `needt-youtube/`) with the metadata,
   chapters, description and the transcript in ~30-second paragraphs `[mm:ss] …`. Always run it with `--print head` and `--out` pointing at a scratch folder: stdout then
   holds only the header, chapters and a `FILE <path>` line, and you read the file in
   pieces (a long transcript dumped into the chat is the failure this guards against).
   `--print all` only for videos under ~3 minutes. Without `--lang` it takes manual captions in the video's own language, then the
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
