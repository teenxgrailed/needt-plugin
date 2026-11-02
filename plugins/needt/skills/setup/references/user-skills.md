# The user's own skills — shared by every Needt skill

The host's catalog usually holds skills the user installed themselves or that the host
ships: document formats (docx, pptx, xlsx, pdf), design and front-end taste, code review,
deploy and infrastructure, data analysis, a brand or style guide, marketing and
small-business workflows, language or domain skills. Needt skills use them the way they use
each other: hand over for the part they own, keep the thread, deliver in the Needt skill's
voice. A user who installed a skill expects it to be used, not reinvented inline.

## What setup records

Setup counts the skills in the catalog that are not Needt's own and puts `skills: 14` in
the readiness line (`skills: none` when there are none). Names are not listed in the line;
each skill matches at hand-off time, by the installed description, not by name.

## When to hand over

- **A format or artefact Needt does not own**: a Word, PowerPoint, Excel or PDF file; a
  slide deck; a chart image; a UI mock; a diagram file. The user's skill for that format
  makes it; the Needt skill supplies the content.
- **A workflow the user already has a skill for**: their code-review checklist, their deploy
  runbook, their SEO audit, their brand voice, their meeting-notes format, their research
  method for a domain. Use it when the task is that workflow and the user is past "where do
  I start" (that stage stays with the Needt skill).
- **The host's own skills** for the host's own features (a design tool, a data tool, an
  artifact or document type) when the output should live there.
- **Never** for what Needt owns: the planner, memory, the board, the readiness line, the
  verdict in partner, the find in search. A user's skill that overlaps a Needt skill (their
  own grill-me, their own researcher) runs only when the user names it; Needt's fires on its
  triggers.

## How

1. Match by the installed description, in the catalog that is in context. Never assume a
   skill from its name alone, and never fabricate a slash command, tool call, path or API.
2. Load it through the host's real mechanism (the skill tool, or its readable `SKILL.md`),
   and resolve its relative references against its own package.
3. Hand it a compact brief from what is already known: project, goal, audience, constraints,
   evidence, existing assets, desired output, memory lines that apply. Mark unknowns as
   assumptions instead of letting it re-interview the user.
4. Run the smallest complete workflow. Chain two skills only when one output feeds the next.
5. Check the result against the facts and the user's rules, then deliver it in the Needt
   skill's voice. Say in a few words that the user's skill was used ("made with your pptx
   skill"), never "now I'll run X".
6. In a sub-agent, pass the skill's file path in the brief; sub-agents do not see the
   catalog.

## Precedence

1. The user's latest explicit instruction.
2. Project instructions and memory lines.
3. The Needt skill that owns the request (how many questions, reply length, how it ends,
   what lands in Needt).
4. The user's skill's own template, checklists and formats.

A user's skill contributes method, format and checklists. It never changes what lands in
Needt or how the reply ends.

## Not installed

A task that clearly wants a skill the user does not have → do the plain version inline and
say in one line which kind of skill would do it better; recommending or installing one goes
through the safety check in [search/references/tools.md](../../search/references/tools.md)
first. Never claim a skill ran when it did not.
