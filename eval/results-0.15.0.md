# Eval results — 0.15.0 (2026-11-03)

Change: the skill `plan` is renamed `roadmap` (Claude Code's built-in `/plan` shadowed it).
Run: one fresh Sonnet sub-agent on the roadmap scenarios and the hand-offs into it (P1–P3,
N3, X1–X3), plus a link and name sweep. Everything else carries over from 0.14.0 unchanged.

## roadmap
- P1 roadmap for launching the Acme shop (no board) · PASS
- P2 where are we (board exists) · PASS
- P3 I'm stopping for today · PASS

## hand-offs into roadmap
- N3 done: Creem review approved → roadmap asks for the artefact · PASS
- X1 продолжаем магазин, что дальше? · PASS
- X2 add milestone after another · PASS
- X3 same with widgets: no · PASS

## sweep
- no link to `../plan/SKILL.md`, `../../plan/SKILL.md`, `/needt:plan`, `skills/plan` left · PASS
- every relative link under `skills/roadmap/` resolves · PASS
- no skill-name "plan" left (after: `skills-map.md` asking → **roadmap**) · PASS

## carried over from 0.14.0
- needt N1–N2, partner R1–R3, search S1–S3, prompt M1–M3, asking A1–A3, critic C1–C3, learn L1–L3, youtube Y1–Y3, setup T1–T6, budget B1–B4 · PASS (text unchanged except the name)
