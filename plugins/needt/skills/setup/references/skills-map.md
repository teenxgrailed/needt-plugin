# Skills map — who does what, who calls whom

Shared by every Needt skill. One skill owns each kind of request; the others hand over
instead of doing a lighter version themselves. Handing over means running that skill's
rules from its file, in the same reply, and continuing with its result — not a summary of
what it would have done.

## Who owns what

| The user wants | Owner | Not this |
|---|---|---|
| A task, event, habit, page, "what's today", move, done | **needt** | roadmap (a milestone is a task of a board, see below) |
| A project's roadmap, "where are we", "what's next on X", "what's left", a handoff, milestones | **roadmap** | needt (a day or week), partner (the decision itself) |
| A business or project decision, "what should I do" with no task list, money, a plan for the week | **partner** | critic (reviewing one), search (facts only) |
| Facts, options, "what's out there", "how do people do X", a price, a version | **search** | partner (the verdict), learn (an explanation) |
| One well-built prompt or brief for an agent or another product | **prompt** | — |
| Clickable questions until nothing is assumed; one short round for another skill | **asking** | critic (findings, not questions) |
| A plan taken apart before launch: problem → solution → cost → confidence (also run by partner, roadmap, prompt L and search Deep in short mode) | **critic** | asking (questions), partner (making the plan) |
| Understanding one thing: mechanism, example, diagram, one check question; "roadmap for learning X" | **learn** | search (a lookup), roadmap (a project is not a subject) |
| Going through the open tasks together, one at a time: "let's work", "погнали", "/needt:work" (an explicit loop request only) | **work** | needt (one task), roadmap (a board's next step) |
| What a YouTube video says | **youtube** | search (finding videos: it calls youtube per video) |

## Hand-offs — what travels between skills

| From → to | When | What is handed over |
|---|---|---|
| any → **youtube** | a YouTube link anywhere in the request | the link; back comes the transcript with `[mm:ss]` |
| any → **search** (Quick) | a fact the skill is not sure of | the fact to check; back comes value, date, link |
| any → **asking** (short) | a missing answer would change the result | at most 4 questions, recommended first; back come answers and labelled assumptions |
| partner / critic / asking → **roadmap** | the result is a sequence that spans sessions, with milestones that wait on each other | the milestones in order, what blocks what, open decisions as `Decide: …` milestones |
| partner / search / prompt / critic → **needt** | the result is work for one sitting or one week | outcomes, one task each, by needt's breakdown rules |
| roadmap → **needt** | a milestone is started, done or opened | the task id; needt's title and permission rules apply |
| partner → **critic** (short) | a plan or strategy of more than 3 moves, or with real stakes, before it is handed over | the plan; back come ≤3 findings and the revised plan with `▲`, which is what the user gets |
| roadmap → **critic** (short) | a board is created; an `add` / `reprioritize` batch of 3+ milestones | the milestone list or the batch; back come ≤3 findings and the revised list; roadmap applies and logs them |
| prompt → **critic** (short) | size L only, on the approach section | the approach; back come ≤3 findings and the revised approach; the prompt stays free of `▲` |
| search → **critic** (short) | Deep only, a request the user made to search itself, on the recommendation | the recommendation; back come ≤3 findings and the revised recommendation, above `In short` |
| needt → **critic** | the user pastes a plan of 4+ steps to turn into tasks: one-line offer, once | nothing until yes; then the plan, full mode |
| roadmap → **search** | a milestone needs a fact or an option (a vendor, a library) | the question; back comes the find, logged on the plan page |
| roadmap → **prompt** | a milestone will be executed by a coding agent or another product | the milestone, its evidence rule and the board's handoff; back comes one prompt |
| critic → **roadmap** | the reviewed plan has a board | findings become `add` / `defer` / `reprioritize` log lines, with the finding as reason |
| asking (full) → **roadmap** / **partner** | the interview ends with decisions taken | the decisions, as milestones or as the plan's inputs |
| learn → **search** | a question that is really a lookup | the question, entirely |
| needt → **work** | one line offer: 3+ overdue, an overloaded day, or "what's today"; once a day, never to a newcomer (`sessions: n` < 3, missing = 3) | nothing until the user says yes; then the day plan |
| work → **needt** | every read and write of tasks, pages, memory | the task id; needt's title and permission rules apply |
| work → **search** / **partner** / **asking** | a task is a lookup / a decision with numbers / needs the person's one answer | the task's gist; back come evidence, verdict or the answer |
| work → **roadmap** | the task is a milestone of a board | the task id; closing follows the board's evidence rule |
| needt → **roadmap** | "where are we / what's next on <project>", "done <milestone>", or a task whose `originPageId` is a `Plan ·` page | the request; roadmap reads the board and answers |

## The user's own skills

The catalog also holds skills the user installed or the host ships — document formats,
design, code review, deploy, data, marketing, a brand voice. Any Needt skill hands the part
they own to them (`skills: n` in the readiness line says how many exist), by the rules in
[user-skills](user-skills.md): match by description, brief from what is known, deliver in
the Needt skill's voice, never for what Needt owns.

## Rules that hold everywhere

- The `Needt ·` line is printed once per conversation by whichever skill runs first; every
  later skill reuses it.
- A skill that hands over says so in a few words ("checking the price first", "this spans
  sessions — keeping it as a board") and never asks the user to invoke the other skill.
- A board exists for the project (roadmap's §1 finds one) → every skill working on that project
  reads it before proposing work, and reports work against its milestones.
- **Critic is a leaf and runs once per plan** ([auto](../../critic/references/auto.md)). Only the
  skill that owns the user's request runs or offers it; a skill used as a step of another
  never does (so search Deep inside partner, prompt inside roadmap, needt inside critic never
  start critic). Critic calls only youtube, search Quick, asking (short, full mode) and
  roadmap (full mode); asking never calls critic. A plan with a `Critic ·` pass in the
  conversation, or one whose review was offered and not accepted, is not reviewed again when it moves
  on to a board, tasks or a prompt. Called by another skill, critic runs in short mode:
  `Critic · short · N findings`, ≤3 one-line findings, the caller's revised artifact with `▲`.
- Memory lines read at setup are standing instructions for every skill
  ([memory](../../needt/references/memory.md)).
- One widget per reply, owned by the skill that answers ([widgets](widgets.md)).
