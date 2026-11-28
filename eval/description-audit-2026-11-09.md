# Skill descriptions — size audit (2026-11-09, v0.15.0)

Every skill description is loaded into the model's context on every turn of every chat that
has the plugin. Ten descriptions today:

| skill | chars | ~tokens | trigger phrases | languages | `/needt:x` repeated |
|---|---|---|---|---|---|
| needt | 598 | 149 | 25 | 6 | yes |
| prompt | 571 | 142 | 20 | 6 | yes |
| roadmap | 562 | 140 | 25 | 6 | yes |
| setup | 558 | 139 | 17 | 6 | yes |
| youtube | 531 | 132 | 15 | 1 | yes |
| learn | 525 | 131 | 25 | 1 | yes |
| asking | 503 | 125 | 16 | 1 | yes |
| search | 493 | 123 | 25 | 6 | yes |
| critic | 490 | 122 | 10 | 1 | yes |
| partner | 483 | 120 | 23 | 1 | yes |
| **total** | **5,314** | **~1,330** | | | |

Plus the plugin manifest description (≈250 chars) once.

## What can go without touching triggering

Ordered by bytes saved per risk. Nothing below is applied until the eval suite (`plugins/needt/evals/`)
shows the same fire rate before and after; the "with / without" delta per case is the gate.

1. **`/needt:<name>` inside the description — 10 × ~14 chars.** The slash command is derived
   from the skill name and listed by Claude Code itself; the model does not need the string to
   route `/needt:critic`. Save ≈140 chars. Risk: none for the slash path (it is an explicit
   invocation, not a match).
2. **Quotation marks around phrases — asking, critic, learn, needt, setup, youtube.** `"grill me",
   "stress-test this"` → `grill me, stress-test this`. The quotes carry no signal; partner, prompt,
   roadmap and search already list bare phrases. Save ≈200 chars. Risk: none.
3. **Per-language lists cut to the two strongest phrases.** learn carries 25 phrases across six
   languages (`почему`, `warum`, `por qué`, `pourquoi` are weak alone: a bare "why" in a question
   does not mean a lesson); needt and roadmap carry four per language where two carry the match
   (`добавь задачу`, `напомни`). Save ≈500–700 chars. Risk: real for the weakest phrases only, which
   is the point; the eval's non-English cases (`needt-what-today-ru`, `learn-ru-index`,
   `prompt-ru-landing`, `setup-ru`) are the check.
4. **"Not for …" clauses stay.** They are what stops `learn` from taking a fact question and `needt`
   from taking a prompt request; the negative cases in the suite depend on them.
5. **The first sentence stays as is.** It is the part the model reads for a fuzzy match; cutting
   it changes behaviour more than any trigger list.

Target after 1–3: ≈3,900 chars (~975 tokens), −27%, with the same fire rate on all 23 cases.

## Not a saving

- Moving triggers into the body: the body loads only after the skill fires, so it cannot help
  routing.
- One shared description for several skills: Claude Code matches each skill on its own
  description; merging means one skill fires for everything.
