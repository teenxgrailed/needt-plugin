# Building the prompt — section details

Read when writing the prompt (SKILL.md §5). Structure and examples: [structure.md](structure.md).

Use the sections the size needs, in this order. Structure and examples:
[references/structure.md](structure.md).

1. **Context and why** — the situation, the project, who it is for, and the reason behind the
   task. Executors generalize from the reason far better than from bare rules.
2. **Goal and done-criteria** — the outcome, and how anyone can tell it is done.
3. **Inputs** — data, files, links, previous findings, each in its own XML tag, long material
   at the top and the request after it.
4. **The approach** — the chosen direction and the ideas from step 2. Steps only where order
   matters; otherwise describe the goal and let the executor plan.
5. **Stages using Needt skills**, when the executor is Claude with this plugin: name them —
   `use needt:search (normal depth) to find …`, `use needt:asking in short mode if …`,
   `use needt:partner to check the economics of …`. A stage that names a skill means the
   executor runs that skill's rules, not an inline shortcut: a search stage delegated to
   sub-agents hands them the skill's source-kind requirements and recipes
   ([search/references/tools.md](../../search/references/tools.md)); a partner stage produces
   executed numbers, not a funnel guessed in a table. For a "how do people do it / what is
   popular" question, the search stage names YouTube guides with transcripts and X threads as
   required sources, plus GitHub for anything about tools or code. For other products,
   replace each skill with plain instructions that do the same job
   ([references/structure.md](structure.md), portable version).
5b. **Stages using the user's own skills**, when the executor is this host and the catalog
   has a skill for a stage (their deploy runbook, their pptx skill, their code-review
   checklist): name it the way the catalog lists it, per [user-skills](../../setup/references/user-skills.md); for another product, plain
   instructions that do the same job.
6. **Parallel work** — say which stages are independent and may run as parallel sub-agents
   on a cheaper model, and which need the main model (synthesis, taste, the final call).
   Rules: [setup/references/delegation.md](../../setup/references/delegation.md).
7. **Constraints** — what to keep, what is out of scope, what needs permission (sending,
   paying, publishing, deleting). Say what to do instead of only what not to do. Permission
   lists are short and exact; everything reversible the executor does on its own,
   including waking an agent or bot that the user has already authorized.
8. **Output** — format, length, language, where it goes. Deliverables the user will want
   later (a video, a report, a dataset) go to a durable place the user can open — a project
   folder, Drive, a doc; a temp or scratch directory holds only intermediates.
9. **Check** — how the executor verifies its own result before handing it over. For media:
   what was actually checked (frames, audio) and what was not.

Write the prompt in the language the executor should work in — the user's language by
default; English for code agents only if the user's other prompts to them are in English.

