# Prompt structure — reference for Needt · Prompt

Distilled from Anthropic's prompting guidance (platform.claude.com prompting best practices,
"Effective context engineering for AI agents", "How we built our multi-agent research
system"), checked 2026-10-27.

## Principles that matter most

- **Context beats commands.** Explain the situation and why the task exists; a model that
  knows the reason makes better calls in cases the prompt did not foresee.
- **Be explicit about the outcome.** Describe what done looks like. If you want ambitious
  work, say so ("include as many relevant features as you can").
- **Minimal complete set.** The smallest set of information that fully specifies the
  behavior. Generic advice ("think step by step", "be thorough") adds noise on current models.
- **Positive instructions.** "Write flowing prose paragraphs" works better than "no markdown".
- **Style follows style.** A prompt in heavy markdown tends to produce heavy markdown.
- **Goal over procedure.** "Think it through carefully" usually beats a hand-written
  step list; give steps only where order truly matters.
- **Examples are strong signals.** 1–5 examples in `<example>` tags, varied so the model
  does not copy surface details.
- **Long material first, question last.** In long prompts put documents at the top and the
  request at the end.
- **Delegation briefs** need: objective, output format, tools and sources to use, and clear
  boundaries — otherwise agents duplicate work or leave gaps.
- **Effort budgets.** Tell an agent how much work the task deserves (a quick check vs. a deep
  run) — models tend to over- or under-invest without it.

## Tag names (use consistently)

`<context>`, `<goal>`, `<inputs>` with `<document index="n">` inside, `<approach>`,
`<stages>`, `<constraints>`, `<output>`, `<check>`, `<examples>` / `<example>`.

Examples are in English; the prompt itself is written in the language the executor should
work in.

## Size S example

Wish: "make me a post about the sale"

```text
Write a short Instagram post for a vintage-sneaker shop: 20% off everything until Sunday.
Tone: cocky, no exclamation marks, 2–3 lines plus one line inviting people to the profile.
Give three versions.
```

## Size M example

Wish: "I want to understand why sales dropped and what to do"

```text
Context: an online clothing store; October sales fell about 30% against September.
Data: the order export is below; GA4 traffic is available through the connected tool.

Goal: name the most likely cause of the drop and the check that would confirm it, plus one
step that can be taken this week.

<inputs>
<orders>{paste the export}</orders>
</inputs>

Approach: first split the drop into traffic × conversion × average order value and find
which factor fell. Then look for the cause of that factor only. Use needt:partner to check
the economics of the proposed step.

Constraints: change nothing in the store or the ads — analysis and recommendation only.
Output: 5–10 lines in chat, numbers from the calculation, not eyeballed.
```

## Size L skeleton

```text
<context>
Who the user is, the project, the stack or market, what was tried, why this task now.
</context>

<goal>
The outcome in one or two sentences.
Done when: concrete, checkable criteria.
</goal>

<inputs>
<document index="1"><source>…</source><content>…</content></document>
</inputs>

<approach>
The chosen direction and why. Ideas to include. Options to weigh, if any.
</approach>

<stages>
1. Research — use needt:search (normal depth): sub-questions …, source kinds …
2. Decide — if X is unclear, use needt:asking in short mode.
3. Build — …
4. Verify — …
</stages>

<constraints>
Keep: … Out of scope: … Needs the user's permission: sending, paying, publishing, deleting.
</constraints>

<output>
Format, length, language, destination.
</output>

<check>
How to verify the result before handing it over.
</check>
```

## Portable version (another product, no Needt plugin)

Replace skill stages with plain instructions:

- **search** → "Research before answering: run many short web searches across docs, GitHub
  issues, forums and competitors; open the authoritative pages; confirm key facts in two
  independent sources; cite each fact with a link and date; say what stayed unclear."
- **asking** → "If a decision only I can make blocks you, ask me up to four multiple-choice
  questions at once with your recommended answer first; otherwise state assumptions and go."
- **partner** → "Calculate every number the decision rests on, show a downside case, and end
  with a verdict: take / take if X / walk."
