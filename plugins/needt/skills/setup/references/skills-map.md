# Skills map — who does what, who calls whom

Shared by every Needt skill. One skill owns each kind of request; the others hand over
instead of doing a lighter version themselves. Handing over means running that skill's
rules from its file, in the same reply, and continuing with its result — not a summary of
what it would have done.

## Who owns what

| The user wants | Owner | Not this |
|---|---|---|
| A task, event, habit, page, "what's today", move, done | **needt** | plan (a milestone is a task of a board, see below) |
| A project's roadmap, "where are we", "what's next on X", "what's left", a handoff, milestones | **plan** | needt (a day or week), partner (the decision itself) |
| A business or project decision, "what should I do", money, a plan for the week | **partner** | critic (reviewing one), search (facts only) |
| Facts, options, "what's out there", "how do people do X", a price, a version | **search** | partner (the verdict), learn (an explanation) |
| One well-built prompt or brief for an agent or another product | **prompt** | — |
| Clickable questions until nothing is assumed; one short round for another skill | **asking** | critic (findings, not questions) |
| A plan taken apart before launch: problem → solution → cost → confidence | **critic** | asking (questions), partner (making the plan) |
| Understanding one thing: mechanism, example, diagram, one check question | **learn** | search (a lookup), plan (a project is not a subject) |
| What a YouTube video says | **youtube** | search (finding videos: it calls youtube per video) |

## Hand-offs — what travels between skills

| From → to | When | What is handed over |
|---|---|---|
| any → **youtube** | a YouTube link anywhere in the request | the link; back comes the transcript with `[mm:ss]` |
| any → **search** (Quick) | a fact the skill is not sure of | the fact to check; back comes value, date, link |
| any → **asking** (short) | a missing answer would change the result | at most 4 questions, recommended first; back come answers and labelled assumptions |
| partner / critic / asking → **plan** | the result is a sequence that spans sessions, with milestones that wait on each other | the milestones in order, what blocks what, open decisions as `Decide: …` milestones |
| partner / search / prompt / critic → **needt** | the result is work for one sitting or one week | outcomes, one task each, by needt's breakdown rules |
| plan → **needt** | a milestone is started, done or opened | the task id; needt's title and permission rules apply |
| plan → **critic** | a board is built from an invented plan and the stakes are high | the milestone list; back come findings and the revised sequence |
| plan → **search** | a milestone needs a fact or an option (a vendor, a library) | the question; back comes the find, logged on the plan page |
| plan → **prompt** | a milestone will be executed by a coding agent or another product | the milestone, its evidence rule and the board's handoff; back comes one prompt |
| critic → **plan** | the reviewed plan has a board | findings become `add` / `defer` / `reprioritize` log lines, with the finding as reason |
| asking (full) → **plan** / **partner** | the interview ends with decisions taken | the decisions, as milestones or as the plan's inputs |
| learn → **search** | a question that is really a lookup | the question, entirely |
| needt → **plan** | "where are we / what's next on <project>", "done <milestone>", or a task whose `originPageId` is a `Plan ·` page | the request; plan reads the board and answers |

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
- A board exists for the project (plan's §1 finds one) → every skill working on that project
  reads it before proposing work, and reports work against its milestones.
- Memory lines read at setup are standing instructions for every skill
  ([memory](../../needt/references/memory.md)).
- One widget per reply, owned by the skill that answers ([widgets](widgets.md)).
