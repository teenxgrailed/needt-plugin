---
name: prompt
description: Turns a rough wish ("хочу сделать это, это и это, и поищи") into one well-built prompt sized to what the task really needs — a few lines for a small job, a structured brief for an agent run. Thinks of ideas and the better approach first, asks only what would change the prompt, and wires in the other Needt skills (search, asking, partner) where the task needs them. Use for "/needt:prompt", "промт", "промпт", "сделай промт", "улучши промт", "напиши промт для", "improve this prompt", "write a prompt for", "make a brief for an agent". Not for doing the task itself unless the user says to run the prompt.
---

# Needt · Prompt

The user gives a rough wish. You give back **one prompt** that a capable model can execute
well on the first try — with the good idea already in it, the right size, and nothing that
does not change behavior. The failure this exists to kill: a bloated template full of
generic rules, or a polished rewording of the same vague wish.

## Setup check

Before the first reply, look back in this conversation for a line starting with `Needt ·`.
None → run the short check from [setup](../setup/SKILL.md), print its line as the first
line of the reply, and continue. Present → reuse it (it says which tools and question mode
exist). Reading the setup file and not printing the line is the failure this guards against.

## Sister skills

- [critic](../critic/SKILL.md) — a plan that should be checked before launch.
- [needt](../needt/SKILL.md) — finished work lands in Needt as tasks.

## 1. Understand the wish

Pull out, from the wish, the chat and the open project (one or two targeted looks at most):

- **Outcome** — what exists or is decided when the task is done.
- **Who runs it** — this chat, a coding agent, a sub-agent, another product (ChatGPT,
  Gemini, Mistral). Unknown → this chat.
- **Context the executor will not have** — the project, stack, constraints, what was tried,
  the user's taste. This is usually the most valuable part of the prompt.
- **A YouTube link in the wish** — read it now through [youtube](../youtube/SKILL.md) (its
  contract section); the key points go into `<inputs>` with timestamps, so the executor does
  not have to watch it again.
- **Parts that need other skills** — "и поищи" → a search stage; money or business calls →
  partner; open decisions → asking.

## 2. Think of the better move

Before writing, spend a moment on the task itself, not the prompt:

- Generate 2–3 ways to approach it. Pick the strongest and say why in one line; the others
  may go into the prompt as options to consider, if that helps the executor.
- Add the ideas the user did not ask for but would want — a missing step, a check, a nicer
  outcome, a risk. Keep only ones inside the user's goal and style.
- If facts decide the approach (a current price, whether a library exists), run a Quick pass
  of [search](../search/SKILL.md) now, or build the search stage into the prompt.

## 3. Ask only what changes the prompt

If a missing answer would change the prompt materially, run [asking](../asking/SKILL.md) in
short mode: one round, at most 4 clickable questions, recommended option first. Everything
else becomes a labeled assumption written into the prompt. A wish that is already clear gets
no questions.

## 4. Pick the size

| Size | When | Shape |
|---|---|---|
| **S** | one clear action, little context needed | 2–8 lines of plain prose |
| **M** | a task with context, constraints and a defined output | short sections, ~15–60 lines |
| **L** | an agent run, multi-stage work, research + build, long-lived instructions | XML-tagged brief, ~60–200 lines |

Pick the smallest size that carries the needed context. Longer is not better; every sentence
must change what the executor does.

## 5. Build it

Use the sections the size needs, in this order. Structure and examples:
[references/structure.md](references/structure.md).

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
   ([search/references/tools.md](../search/references/tools.md)); a partner stage produces
   executed numbers, not a funnel guessed in a table. For a "how do people do it / what is
   popular" question, the search stage names YouTube guides with transcripts and X threads as
   required sources, plus GitHub for anything about tools or code. For other products,
   replace each skill with plain instructions that do the same job
   ([references/structure.md](references/structure.md), portable version).
6. **Parallel work** — say which stages are independent and may run as parallel sub-agents
   on a cheaper model, and which need the main model (synthesis, taste, the final call).
   Rules: [setup/references/delegation.md](../setup/references/delegation.md).
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

## 6. Self-check before delivering

- Would a smart newcomer with only this prompt do the right thing? What would they guess?
- Each sentence changes behavior; delete the generic ones ("be thorough", "think step by step").
- No contradictions; no rule that a later rule silently overrides.
- Assumptions are marked; nothing invented about the user's project.
- Skill stages point at skills that exist (check the setup line).

## 7. Deliver

1. The prompt in one fenced code block, ready to paste.
2. Under it, at most three lines: size picked and why, the assumptions made, the one thing
   worth changing if the user disagrees.
3. If the user said to run it (`и запусти`, `go`, `выполни`), execute it in this chat right
   after delivering — no button.
4. Otherwise end with a **one-click choice**, in the same reply, right after the three lines:
   - Clickable questions here (`questions: click` in the setup line, `AskUserQuestion` or the
     host's equivalent): one question, `header` "Prompt", in the user's language — e.g.
     "Use this prompt now?" / "Запустить этот промт?". Options, recommended first:
     **Use prompt (Recommended)** — "Runs it here, in this chat"; **Change something** —
     "Tell me what to adjust, I rewrite it"; **Copy only** — "I'll paste it elsewhere".
     Translate labels to the user's language. When the prompt is for another product
     (ChatGPT, Gemini, a coding agent elsewhere), make **Copy only** the recommended first
     option and keep **Use prompt** second.
   - `questions: text` and `widgets: yes`: the same three choices as one small widget with
     three buttons — **Use prompt**, **Change something**, **Copy only**, recommended first by
     the same rule — that `sendPrompt` the words `go` / `change: …` (opens a field) / `copy`.
   - No clickable questions and no widgets: the same three choices in one line —
     `Use it? — "go" runs it here · "change: …" rewrites it · "copy" and I stop.` (user's language).
   - On **Use prompt** (click or "go"): execute the prompt in this chat at once, as if the user
     had pasted it, starting with its first stage. On **Change something**: ask what, in one
     line, then deliver the changed blocks and the same choice again. On **Copy only**: stop.

When the user sends their own prompt to improve, keep their intent and voice, show the
improved version, list the 2–4 changes that matter — not every edit — and end with the same
one-click choice.

When the user asks for a change to a prompt already delivered in this conversation, give the
replacement blocks only, then one full copy once they say they will paste it. Do not reprint
a long prompt for a two-line edit.

## Grounding

The recommendation inside the prompt comes from the conversation and the open project, not a
generic default: if the project is Needt and the wish is about promotion, the prompt assumes
Needt promotion unless the user said otherwise. Scratch paths, session ids and other
ephemeral details go into the prompt only when the executor is this same session.

## Widgets

With `widgets: yes` in the setup line (per [widgets](../setup/references/widgets.md)), the only
widget here is the three-button choice in §7 step 4, and only when `questions: text`;
`AskUserQuestion` stays first when it exists, and the reply never carries both. The prompt
itself is always a fenced code block, never inside a widget — the user pastes it. With
`widgets: no`, §7 applies unchanged.

## Failing behaviors

A questionnaire instead of a prompt; a template with empty placeholders; a giant prompt for a
small task; generic best-practice filler; losing the user's actual goal while polishing
wording; referencing Needt skills in a prompt meant for another product; inventing facts
about the project; running the prompt when the user only asked for it; the prompt inside a widget; two choice systems in one reply.
