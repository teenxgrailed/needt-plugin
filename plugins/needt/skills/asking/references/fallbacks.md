# Asking · fallbacks when `AskUserQuestion` is missing

The round goes through `AskUserQuestion` whenever `questions: click` — that stays the first
choice. The same rules apply in every fallback: recommended option first, one " (idea)" option
per question, the gap question last, at most 4 questions a round.

## Widget (`questions: text` and `widgets: yes`)

Per [widgets](../../setup/references/widgets.md): one elicitation widget per round
(`read_me` with `elicitation`, once). One form, up to 4 questions, each with 2–4 options as
pills or cards, the recommended option first and marked, the idea option marked, an "Other"
escape where a free answer is plausible; the shell returns the answers as one line. Never both
a widget and `AskUserQuestion` in one round.

## Text (`questions: text · widgets: no`, and inside a sub-agent)

Number each question:

```
❓ **Q1** - **<question title>**: <question body, including the choices; mark (Recommended) and (idea)>

➡️ <your recommended answer>
```

Word each question so "yes" accepts your recommendation. The gap question is the last `❓`.
