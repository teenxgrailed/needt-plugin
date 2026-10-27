# Specialist skill routing

Names below are discovery hints, not guaranteed commands. The host's installed catalog and
the skills' own descriptions decide what exists. Names may be namespaced
(`marketing:campaign-plan`, `small-business:growth-pulse`) or bare.

## When to load a specialist

Load one only when the task needs its full workflow and the user is past the "where do I
start" stage (that stage stays with the partner). Short copy (one post, one DM, a caption,
a headline) is written directly by the partner — no specialist.

1. Match the task to one skill by its installed description, not by name alone.
2. Load it through the host's real mechanism (skill tool or readable `SKILL.md`). Resolve its
   relative references against its own package. Never fabricate a tool call, slash command,
   path or cross-product API.
3. Hand it a compact brief from what is already known: project, goal, audience, product,
   brand constraints, evidence, existing assets, desired output, real budget or deadline.
   Mark unknowns as assumptions instead of letting it interview the user.
4. Run the smallest complete workflow. Chain skills only when one output feeds the next.
5. Check the result against positioning, facts and economics, then deliver it in the
   partner's voice. Name the skill used in one short line only if useful.

## Precedence

The partner's rules win over a specialist's template. In practice:
- Its "ask before proceeding" lists → fill from context, label assumptions, ask at most two.
- Its calendars, milestones and SMART "time-bound" goals → keep sequence and dependencies;
  dates only if the user asked or a real commitment exists.
- Its B2B framing (MQL, pipeline, SQL) → translate to the actual business (followers,
  waitlist signups, DMs asking to buy, sales).
- Its closing "Would you like me to…" → drop; finish on the result.
- Its approval gates for sending, publishing or spending → always keep.

## Marketing plugin

| Need | Skill | Result |
|---|---|---|
| Long-form or multi-piece copy: landing page, newsletter, launch email set | `draft-content` | Ready-to-review copy |
| Adapting content across channels | `content-creation` | Channel-shaped versions |
| Launch, awareness or acquisition campaign | `campaign-plan` | Audience, message, channels, first assets, signal to watch |
| Check work against brand guidelines | `brand-review` | Specific fixes against the actual guidelines |
| Competitors and differentiation | `competitive-brief` | Sourced comparison and positioning |
| Site search visibility | `seo-audit` | Prioritized fixes for the actual site |
| Onboarding, nurture, retention emails | `email-sequence` | Sequence logic and drafts |
| Judging existing marketing results | `performance-report` | What worked, what to change |
| Diagnosing a sales or traffic drop | none without data — partner splits it into sessions × conversion × order value and names the check; with connected data use `growth-pulse` | Likely cause and the confirming check |

Do not run `draft-content` and `content-creation` on the same simple task.

## Small Business plugin

| Need | Skill | Needs |
|---|---|---|
| Is growth working, where to put money next | `growth-pulse` | Sales, funnel or channel data if connected |
| Weekly growth check incl. competitors and reviews | `marketing-monday` | Same; run once unless the user asks for a schedule |
| What to post and promote from sales evidence | `content-strategy` | Real sales data (connector or export) |
| Ongoing social posting calendar | `social-content-engine` | Brand context; staging posts needs approval |
| Visual campaign assets in Canva from an approved brief | `canva-creator` | Canva access and an approved brief |
| Visibility in search and AI answers | `seo-ai-visibility` | The actual site |
| Paid ads performance and changes | `ad-manager` | Ad account access or CSV export |
| Prospect list and outreach | `lead-finder`, `outreach-composer`, `grow-pipeline` | Sending always needs approval |
| What to reorder, slow stock | `inventory-planner` | Sales history and stock on hand |
| Cash forecast | `cash-flow-snapshot` | Ledger, processor data or upload |

A business with no sales history usually needs audience research and a first asset, not
sales analysis. A missing connector (QuickBooks, HubSpot, Canva…) means the integration is
unavailable, not that the work is impossible — prepare what can be prepared locally.

## When the specialist is absent

State it once, then do the work directly:
- Content: audience, intended action, tone, finished draft.
- Campaign: goal, audience, message, channel rationale, first asset, signal to evaluate.
- Competitors: current primary sources, comparable observations, implications.
- Results: supplied metrics, consistent periods, attribution caveats.
- Visuals: a ready brief or layout spec; claim Canva output only after it was created.

Suggest installing something only if its absence blocks a material part of the request.
Never install, connect accounts, or move private data between products on your own.

## Hosts

Claude (chat, Cowork, Claude Code): use skills exposed in the current session; a `/` menu
entry is not a tool call unless the environment provides one. ChatGPT and Codex: use skills
exposed in that host, including imported ones; do not hardcode Claude cache paths. A plugin
installed in another product is not available here.

Skill names checked against the Anthropic Marketing and Small Business packages on 2026-10-09.
Versions differ; trust the runtime catalog.
