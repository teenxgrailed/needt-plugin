# Learn widgets — the blueprints

Read [the shared widget rules](../../setup/references/widgets.md) first; `read_me` from the
host wins on anything visual (tokens, no gradients, Tabler icons, sentence case). These
blueprints say what the learn widgets *are*, so they do not degrade into a form with buttons.

## Drill — "the run"

One widget per round. The chat sees one message in (the round) and one out (the result).
Everything between happens inside the widget's own JS. No library, no timer, no explanations
inside — the "why" comes in the reply after the result.

**Shape**

```
┌──────────────────────────────────────────────────────────┐
│ ● ● ● ○ ○ ○ ○ ○ ○ ○            streak 3   <i ti-bolt>   │  ← rail: one dot per question
│                                                          │
│ 4 / 10                                                   │
│ Ich ___ gestern mit dem Zug nach Bern gefahren.          │  ← the question, 18px
│                                                          │
│ [ habe ]  [ war ]  [ bin ]  [ hatte ]        or [ field ]│  ← options as pills, keys 1–4
│                                                          │
│ ↩ Enter answers · 1–4 pick                               │  ← one hint line, 12px, muted
└──────────────────────────────────────────────────────────┘
```

**Item types** — three, mixed within a round, chosen by what the item tests:

| Type | Control | Tests | Example |
|---|---|---|---|
| `pick` | 2–4 pills, keys 1–4, random order | recognition: the right form among real mistakes | `Ich ___ nach Bern gefahren` → habe / bin / war |
| `type` | one text field, Enter | recall: produce the form | `mit ___ Freund (mein)` → meinem |
| `reorder` | the words as pills in shuffled order; click or press 1–9 appends a word to the answer line, backspace removes the last; Enter checks | structure: word order, sentence building | `[ich] [weil] [suche] [Arbeit]` → weil ich Arbeit suche |

`type` and `reorder` compare case-, space- and punctuation-insensitively against a list of
accepted forms; `type` also accepts the answer with the article or pronoun it was asked
for alone. Translate, classify, fill and apply are all one of these three.

**Behaviour**

1. The items are an array in the script: `{id, type, q, opts|words|null, a: [accepted…],
   rule}` — `rule` is the one-line reason shown on a miss, written at authoring time so
   the widget never needs the model to explain a known mistake. The whole round is in the
   widget from the start, nothing is fetched.
2. One question visible at a time; the others hidden by JS after streaming (post-streaming
   steppers are allowed; stream all questions stacked, then the script collapses them).
3. Answering: click a pill, press a number key, or type and press Enter. The widget
   checks the answer itself: the chosen control gets `border-color: var(--border-success)`
   or `var(--border-danger)`; a hit moves on after 600 ms. A miss stays: the right answer
   in `var(--text-success)` and the item's `rule` line under the question, plus two small
   buttons — `Got it` (next item) and `Why?`. `Why?` is the only `sendPrompt` allowed
   before the end of the run: it sends `Why: <q> — answered <x>, right is <y>`; the reply
   is at most three lines, renders no widget, and the user continues in the same widget.
   The next item slides in (`transform` only, 150 ms, under
   `prefers-reduced-motion: no-preference`). No "next" button after a hit.
4. The rail fills as you go: a dot turns to the success tint on a hit, the danger tint on a
   miss. `streak` counts consecutive hits and resets on a miss; at 3+ it shows with the
   bolt icon, otherwise it is hidden — no celebration text.
5. After the last question the card flips to the result:

```
│ 7 / 10                                       ← 48px, var(--font-voice)          │
│ ████████████░░░░░   hits ▍ misses                                               │
│ 3  Ich ___ gefahren        habe → bin                                            │
│ 6  mit ___ Freund          meine → meinem                                        │
│ 9  …                                                                             │
│                                   [ Send result ↗ ]  [ Replay misses ]           │
```

   `Send result` is the one button that ends the run:
   `sendPrompt('Round 1: 7/10 · missed: 3 (habe → bin), 6 (meine → meinem) · due: 3 2026-11-03, 6 2026-11-03, 1 2026-11-09, …')`
   in the user's language for the label, English keys for the line, one `due` per item
   (see Scheduling). `Replay misses` reruns the missed items inside the same widget, in a
   different order, and updates the result; the sent line then carries both scores
   (`7/10, replay 2/3`) and the due dates after the replay.
6. Size: aim under 4 KB of markup for a 10-question round. One `<style>` block of at most
   15 lines for the pill states and the rail; everything else inline.

**Scheduling — FSRS inside the widget.** Each item carries its card state from the topic
page (`{s, d, due, reps, lapses, last}` or nothing for a new item). The script loads
`import { fsrs, createEmptyCard, Rating } from 'https://esm.sh/ts-fsrs@6.0.0'` in a
`type="module"` script (esm.sh is on the allowlist) and rates each item once at the end
of the run: hit first try → `Good`; hit after `Why?` or on replay → `Hard`; miss → `Again`;
hit with the streak at 5+ and under 4 s → `Easy`. The new state and `due` go into the sent
line as `due: <id> <YYYY-MM-DD>` per item, and the compact state as `fsrs: <id> s=… d=…
reps=… lapses=…`. If the import fails (offline, blocked), the script falls back to the
ladder 1 → 2 → 4 → 8 days on hits and back to 1 on a miss, and the line says `fsrs: ladder`.
The skill then writes the states to the page and dates the review task from the earliest
`due` (§6 of the skill).

**Reply after the result** — the only text the user reads for the round: one line per miss
with the rule in the user's words (and the term in the target language for a language
drill), then the offer: another round on the misses, or stop. No restating the hits, no
repeating a `Why?` already answered.

## Study — "the lesson run"

One widget per lesson. Same chassis as the Drill run (rail, one thing visible at a time,
keys, instant tint, result screen, one `sendPrompt` at the end), with two differences:

- each step starts with its **piece** — the idea in 3–6 lines with one example, inside the
  widget, above the question (this is the one place teaching text lives in a widget, so
  the user never leaves the card);
- each question is one of the step shapes, labelled with its chip (`apply`, `find the
  error`, `pick`, `predict`, `explain back`, `what breaks`), and is of one of two kinds:
  - **checked** — built as a `pick`, `type` or `reorder` item (the Drill item types)
    with accepted forms and a `rule`; a miss shows the right form, the rule, `Got it` and
    `Why?` exactly as in the Drill run, and the step counts as *given*;
  - **open** — `explain back`, `predict` in prose: no check, the text is collected.
- checked steps are FSRS cards too (Scheduling above); open steps are not.
- the result screen lists the steps: passed · given (with the right form) · open (with
  the user's text), and the one button sends:
  `Lesson: 4 steps · passed 1,3 · given 2 (muss → machen muss) · open 4: "<user text>"`.

The reply after the run: a reaction to each open answer (substance first, no verdict
word), one rule line per given step, the recap, then the page and the review task. A
lesson run is 3–7 steps and under 6 KB; a 5-minute budget means 3–4 steps.

## Study — "the step card" (judgment-only topics)

One per step, per reply, only when the topic has no checkable answers at all. The teaching
piece is text above the widget; the card holds only:

- a chip with the question's shape (`predict`, `find the error`, `explain back`, `apply`,
  `pick`, `what breaks`), translated — it tells the user how to think before reading;
- the question;
- the controls: pills for `pick` (random order, keys 1–4), a text field for everything
  else, Enter sends;
- the step dots `● ● ○ ○ ○` with the current one accented;
- on send: `sendPrompt('Answer: <text>')` and the controls lock (opacity through a class,
  not a disabled attribute); the button and Enter call the same function; ids carry the
  step suffix (`ans_s2`, `send_s2`).

Nothing else: no timer, no score, no hints inside.

## Explain — "the mechanism"

One illustrative diagram (the `diagram` module) of how the thing works, not a flowchart of
its parts: the metaphor is the explanation. Every node is clickable and sends a question
about that part (`sendPrompt('Why does X …?')`), so the user drills into the piece they did
not get instead of asking you to repeat. The check question stays text under the diagram.

## Failing shapes

A form with a submit button; one question per widget in Drill; a step card per reply for
a lesson that could run in one widget; a miss without its rule line; a `Why?` that
re-renders the widget; a run that ends without due dates; a "Next" button between
questions; a timer; "Correct!" inside the widget; a library for a quiz; a result screen
without the misses listed; a Study card carrying the teaching text; an Explain diagram
whose nodes do nothing.
