---
name: prompt
description: Turns a rough wish into one well-built prompt sized to the task, with the better approach already in it. Use for /needt:prompt, write a prompt, improve this prompt, make a brief, prompt for an agent; RU промпт, промт, улучши промпт, напиши промпт для; UK промпт, покращ промпт, напиши промпт, бриф для агента; DE Prompt schreiben, Prompt verbessern, Prompt erstellen, Briefing für Agent; ES escribe un prompt, mejora este prompt, crea un prompt, brief para agente; FR écris un prompt, améliore ce prompt, rédige un prompt, brief pour agent. Not for doing the task itself.
---

# Needt · Prompt

The user gives a rough wish. You give back **one prompt** that a capable model can execute
well on the first try — with the good idea already in it, the right size, and nothing that
does not change behavior. The failure this exists to kill: a bloated template full of
generic rules, or a polished rewording of the same vague wish.

## Setup check

No line starting with `Needt ·` in this conversation yet → run [setup](../setup/SKILL.md), print its line first and continue the task in the same reply. Present → reuse it (which tools and question mode exist).

## Sister skills

Who owns what and what travels between skills: [skills map](../setup/references/skills-map.md).

- [roadmap](../roadmap/SKILL.md) — a prompt that executes a milestone of a board carries the
  milestone, its evidence rule and the last handoff in `<inputs>`; an agent run that spans
  sessions gets a `use needt:roadmap` stage so the agent reports against the board.
- [critic](../critic/SKILL.md) — a plan that should be checked before launch.
- [asking](../asking/SKILL.md) — the one short round when an answer would change the prompt.
- [search](../search/SKILL.md) — a Quick pass when a fact decides the approach.
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

Sections in order, as many as the size needs: context and why · goal and done-criteria ·
inputs (own XML tag each, long material first) · the approach · stages using Needt skills
(`use needt:search …`; the executor runs the skill's rules, not a shortcut; other products
get plain instructions) · stages using the user's own skills (per
[user-skills](../setup/references/user-skills.md)) · parallel work · constraints · output ·
check. Full rules for each: [references/build.md](references/build.md) — read it when
writing an M or L prompt. Structure and examples: [references/structure.md](references/structure.md).

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
3. The user said to run it (`и запусти`, `go`, `выполни`) → execute it here right after, no button.
4. Otherwise end with a one-click choice (Use prompt · Change something · Copy only; for
   another product Copy only comes first), form by setup line: details in
   [references/deliver.md](references/deliver.md) — read it before ending the reply.

A user's own prompt to improve: keep their intent and voice, show the improved version, list
the 2–4 changes that matter, end with the same choice. A change to a prompt already delivered:
give the replacement blocks only, one full copy once they say they will paste it.

## Grounding

The recommendation inside the prompt comes from the conversation and the open project, not a
generic default: if the open project is a shop app and the wish is about promotion, the prompt
assumes that shop's promotion unless the user said otherwise. Scratch paths, session ids and other
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
