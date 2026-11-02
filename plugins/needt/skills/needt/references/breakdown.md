# Breakdown rules (tasks)

Read when turning a plan, checklist, research, prompt stages or a decision into tasks.

- **One task per outcome** — something either done or not. Usually 1–7; more means the
  outcomes are too small or belong in subtasks.
- **`entry`** = the first small concrete step, doable in one sitting without deciding anything
  ("open the supplier sheet and list the three quotes"), not "start working on it".
- **`subtasks`** in the order they are done. The task itself is the closing step, so the last
  subtask is never "finish" or "done".
- **A step that needs the user's decision** is its own subtask naming the decision:
  "Decide: Stripe or Paddle for checkout".
- **Estimates** in minutes only with a basis in the conversation. **Priority** only with a
  reason (deadline, blocker, "this first"). **Due date** only when the user named one — never
  from "soon".
- **`start` + pinned** only when the user said when ("tomorrow at 10"). Everything else goes to
  the scheduler unpinned.
- **No duplicates**: `needt_search` per outcome first, batched. Same open outcome → update it.
  Similar but different → create, and mention the near-match.
- **Documents are pages**: a report, brief, spec or notes go to a page linked from the task.
  A task description holds a few lines and links, never the whole text.
- **How a task is written** — like a person jotting it on paper, not like an AI:
  - **The user's language, always.** The language they write to you in, even if the source
    (mail, research, a prompt) is in another one. Never mix languages in one title. One
    exception: a memory line that names a task language ("write tasks in English") wins —
    memory outranks this default, as everywhere in the plugin.
  - **Short and plain**: verb first, 2–6 words, the user's own words where possible —
    "Call the print shop", "Позвонить в типографию". Not "Reach out to the print shop to
    discuss and finalize the order details".
  - **Nothing in the title but the action**: no time or date ("at 14:00", "tomorrow" — that is
    `start` or the due date), no emoji, no symbols or brackets, no prefixes or tags ("TODO:",
    "[Work]", "Step 1:", "#marketing", "Task:"), no priority words ("URGENT", "!!!"), no trailing
    period.
  - **No AI slop**: no filler verbs ("leverage", "optimize", "streamline", "ensure",
    "оптимизировать процессы"), no vague outcomes ("Work on strategy", "Improve marketing"),
    no motivational wording, no restating the project name in every task.
  - **Description only when it adds something** the title cannot: a link, a number, who, the
    one-line reason. Empty is fine.
  - Subtasks follow the same rules.

| Material | Becomes |
|---|---|
| Research from [search](../../search/SKILL.md) | the recommendation is the task; options are short notes in the description; sources linked |
| Stages from [prompt](../../prompt/SKILL.md) | one task per stage, the stage's prompt in the description |
| A [partner](../../partner/SKILL.md) session | each "actual work" item one task; advice stays in chat |
| A pasted checklist | grouped into outcomes; items become subtasks; nothing dropped silently |
| A decision just made | one task to carry it out; the decision and its reason in one line |
