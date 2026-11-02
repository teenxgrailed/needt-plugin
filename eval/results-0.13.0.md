# Eval results — 0.13.0 (2026-11-03)

Run: five Sonnet sub-agents, two skills each, on the text as of this release. Six failures in
the first pass; every one was fixed in the skill text (or the scenario, where the scenario
was wrong) and re-judged against the changed lines.

## needt
- N1 add a task · PASS
- N2 no connector · PASS
- N3 done milestone → plan · PASS (after: plan §4 — an externally gated milestone needs the artefact or one confirming question even on the user's word)

## plan
- P1 roadmap, no board · PASS
- P2 where are we · PASS (plan page table now carries task ids for chats without an open folder)
- P3 stopping for today · PASS

## partner
- R1 jackets resale · PASS
- R2 three months, board exists · PASS (partner step 5 now says when plan is called at once vs offered)
- R3 LinkedIn post · PASS (partner: short copy in the user's brand-voice skill when present)

## search
- S1 Vercel Pro price · PASS
- S2 i18n for Next 15 · PASS
- S3 skill for slide decks · PASS (scenario corrected: named and offered; used only on a deck request)

## prompt
- M1 dark-mode prompt · PASS
- M2 "…и запусти" · PASS
- M3 prompt for a milestone · PASS

## asking
- A1 grill me · PASS
- A2 short mode · PASS (scenario corrected: at most one round)
- A3 decisions → plan · PASS

## critic
- C1 pasted plan · PASS
- C2 plan has a board · PASS (after: findings offered as log lines, written on Accept; board looked for first)
- C3 "we never do X" · PASS

## learn
- L1 OAuth refresh tokens · PASS
- L2 statistics map · PASS
- L3 roadmap for learning Rust · PASS (skills-map now routes "roadmap for learning X" to learn)

## youtube
- Y1 link + make tasks · PASS
- Y2 what does this video say · PASS (after: youtube has a Setup check; `Needt ·` line first, `YouTube ·` header after it)
- Y3 no transcript · PASS (after: `captions: none` in the header)

## setup
- T1 first run, everything present · PASS (after: no onboarding lines when nothing is missing)
- T2 first run, no connector · PASS
- T3 second skill, same conversation · PASS

## together
- X1 продолжаем магазин · PASS
- X2 add milestone after · PASS
- X3 same with widgets: no · PASS

Open notes carried to the next eval: asking's "two rounds" budget vs "frontier empty"; prompt's
"one or two targeted looks" vs a board read; the handoff's "next session should" is advice,
stated in plan §3.
