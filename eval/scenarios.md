# Scenarios — three per skill

Host state unless stated: Needt connector present, `questions: click`, `agents: yes`,
`widgets: yes`, memory has 3 lines (`[preference] tasks in English`, `[fact] project: Acme
shop`, `[preference] answer short`), no `Needt ·` line in the conversation yet.

## needt
- **N1** "add: call the printer about the banner, by Friday" → `Needt ·` line first; one
  `needt_search` then `needt_create_task` with `deadline`; one-line report; no question.
- **N2** no connector; "what's on today?" → `Needt ·` line with `memory: off`; one line that
  the connector is missing and comes with Pro; the day answered as text from the chat, no
  dead end; nothing claimed as created.
- **N3** "done: Creem review approved" where that title is a milestone with `originPageId` on
  a `Plan ·` page → hands to plan; the milestone is gated by Creem, so plan asks for or finds the artefact (the approval email), not completed on the word alone.

## plan
- **P1** "roadmap for launching the Acme shop" (no board exists) → `needt_search` on the name
  first; project, page, 3–9 milestone tasks with `dependsOnId`, pointer; the board shown once;
  no question about scope unless the milestones were invented.
- **P2** "where are we" with an existing board → reads tasks by id, four state lines + last
  handoff, the metro map; nothing stored as "next".
- **P3** "I'm stopping for today" → Handoff block appended to the plan page, even with no state
  change; the reply quotes it in three lines.

## partner
- **R1** "should I buy 40 vintage jackets at €18 each to resell?" → numbers executed on labelled
  assumptions, verdict `take / take if X / walk`, no interview; lands in Needt only on ask.
- **R2** "help me think about the next three months for the shop" with a board → reads the
  board, proposes the move against its milestones, hands the sequence to plan.
- **R3** "write a LinkedIn post about the launch" → written directly, no specialist, no
  question; a user-installed brand-voice skill is used when the catalog has one.

## search
- **S1** "what does Vercel Pro cost now?" → Quick: 1–3 calls, the price, its date, the link;
  no widget.
- **S2** "best way to add i18n to a Next 15 app" → Normal: search line first, Find, options as
  cards, Still unclear; GitHub among the sources.
- **S3** "is there a skill for making slide decks?" → the installed catalog is checked before
  any directory; an installed one is named with what it does and offered; it runs only when the user asks for a deck.

## prompt
- **M1** "write a prompt for a coding agent to add dark mode" → one fenced prompt, size M,
  three lines under it, then the one-click choice (AskUserQuestion since `questions: click`).
- **M2** "…и запусти" → the prompt is executed at once, no choice offered.
- **M3** a prompt for a milestone of a board → `<inputs>` carries the milestone, its evidence
  rule and the last handoff.

## asking
- **A1** "grill me on my plan to open a second shop" → first round of ≤4 clickable questions,
  recommended first, no prose interview.
- **A2** short mode called by prompt → at most one round (none when nothing would change the result), control handed back.
- **A3** the interview ends with decisions about a project that has a board → decisions go to
  plan as milestones; irreversible ones not acted on.

## critic
- **C1** a pasted launch plan → 2–3 line summary, ≤7 findings each with Problem / Solution /
  Cost / Confidence, Keeps working as is, revised plan with `▲`.
- **C2** the plan has a board → read first; findings offered as log lines.
- **C3** "that's fine for us, we never do X" → saved as a `preference` and reported in one line.

## learn
- **L1** "explain how OAuth refresh tokens work" → one explanation at the level memory shows,
  one example from the Acme shop, a diagram, one check question, no level question.
- **L2** "statistics for a first course" → the subject map with `•` on the current item,
  no diagram in the same reply.
- **L3** "roadmap for learning Rust" → learn's map, not a plan board.

## youtube
- **Y1** a youtu.be link + "make tasks from this" → transcript read first, then needt with
  `[mm:ss]` in descriptions.
- **Y2** "what does this video say" → title, chapters, the answer with timestamps.
- **Y3** no transcript available → says so once, falls back per its contract, never invents.

## setup
- **T1** first run with everything present → the readiness line + the one explanatory line
  + the `set up` memory save; nothing else.
- **T2** first run without a connector → the Pro line first (two lines at most), then the
  free skills work; the task continues.
- **T3** a second skill in the same conversation → no new readiness line.

## plan + needt + partner together
- **X1** "продолжаем магазин, что дальше?" → plan answers (board), in Russian, fixed markers
  English.
- **X2** "add milestone 'photos shot' after 'samples received'" → plan: new task with
  `dependsOnId`, log `add`, board re-rendered with the same title.
- **X3** `widgets: no`, same as X2 → the same change, the board as the one-line list.
