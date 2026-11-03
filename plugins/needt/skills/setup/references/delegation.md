# Sub-agents: when and how every Needt skill uses them

Shared by all Needt skills. The point is speed and token cost: a self-contained piece of work
runs in a sub-agent on a cheaper model while the main conversation keeps thinking; several
independent pieces run at once.

## Budget profiles

Every skill reads its sub-agent allowance from this table instead of hard-coding numbers. The
profile is the `budget:` value in the readiness line (`pro|max|ultra|team|other|unknown`, saved
by setup from the first-run interview); `unknown` behaves as `pro`.

| Profile | Sub-agents | search Normal | search Deep | critic / partner / roadmap checks | prompt stages |
|---|---|---|---|---|---|
| pro / unknown / other host | none by default; at most 2 (Sonnet or Haiku) and only for Deep on an explicit ask | inline, ≤ 8 calls, one round | only on ask; 2 agents, 1 round, warn about cost | inline, ≤ 3 calls | no parallel stages |
| team | as max, but say when a run will be long | as max | as max | as max | as max |
| max | 2-3 Sonnet in Normal when sub-questions are independent; 3-5 in Deep | ≤ 20 calls | 3-5 agents, 30+ calls | up to 3 Sonnet fact checks | parallel stages on Sonnet |
| ultra | up to 8 parallel; synthesis on the main model; Deep is the default for "a decision that matters" | ≤ 30 calls | 5-8 agents | evidence checks (PR merged, tests, prices) through agents without asking | parallel + an Opus pass for synthesis when the task is cross-cutting |

Overrides and changes:

- `agents: no` in the readiness line overrides everything: no sub-agents at all, whatever the
  profile.
- The user can change the profile by saying it ("у меня Max", "I'm on Ultra"); setup updates
  the memory.
- A skill that wants more than the profile allows says so in one line and asks ("this deserves
  a Deep run - go?") instead of running it.

## When to delegate

The profile above wins: with `pro`, `unknown`, `other` or `agents: no`, the cases below are
done inline unless the user asked for a Deep run.

Delegate when at least one is true:

- Two or more pieces are independent and each needs several tool calls (searches, reading a
  set of pages or files, checking a tool's capabilities). Run them in parallel.
- The piece would dump a lot of raw material into the conversation (page contents, transcripts,
  long listings) and only its conclusion matters here.
- The piece is mechanical: render, convert, compare, extract fields, run a check.

Do it yourself when it is a handful of tool calls, when the answer needs the whole conversation
to interpret, or when the user is deciding something and waits on you.

## Which model

| Work | Model |
|---|---|
| Web and source sweeps, transcript reading, extraction, fact checks, listing options | **Sonnet** (default) |
| Mechanical file work, renders, format conversion | **Sonnet** or **Haiku** |
| Synthesis across conflicting sources, judgment on the user's taste, final recommendation, anything the user will decide on | main model, in this conversation |

Default to Sonnet for delegated work; say in the brief's label which model ran.

## The brief

A sub-agent sees nothing of this conversation. Every brief carries:

1. **Objective** — what question it answers or what artifact it produces, and the success
   criterion.
2. **Context** — the user's project, stack, constraints and taste in a few lines; the date.
3. **Rules** — the relevant Needt skill section pasted in, or its file path. A search agent
   gets the source-kind requirements and the recipes from `skills/search/references/tools.md`;
   never assume it knows them.
4. **Tools** — which exist here (from the setup line) and which to prefer.
5. **Output format** — exact sections; which fields must carry a link and a date.
6. **Boundaries** — out of scope, what not to do (no sign-ups, no posting, no downloads, no
   writes outside its scratch), and the budget (how many calls this deserves).
7. **Gap report** — require it to list what it tried that returned nothing and every claim it
   could not verify.

## After it returns

A report is model output, not fact. Spot-check the two claims that matter most, resolve
contradictions between agents yourself, and name in the final answer what came from
sub-agents and what you verified. A report missing its gap list or a required source kind
goes back with one targeted follow-up message rather than a fresh agent.

## Failing behaviors

An agent per trivial lookup; the main model doing a 20-call sweep inline; a brief without the
skill rules; briefs that overlap so agents duplicate each other; trusting a number because an
agent wrote it confidently; running agents in sequence that could have run at once.
