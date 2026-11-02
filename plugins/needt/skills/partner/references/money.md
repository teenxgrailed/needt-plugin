# Partner · money and verdicts

Read when the question is about money: cost, margin, price, break-even, a buy or commit decision.

## Money

Use the economics of the business type; resale, production and software differ.
For goods, read [resale.md](resale.md) or [production.md](production.md) when relevant.
When a prompt or another skill names partner for a stage, run these rules in full: executed
numbers, a downside case, a verdict (take / take if X / walk). An inline estimate labelled
"rough" does not satisfy a partner stage.

- Compute in code or a calculator every number a decision rests on (cost, margin, break-even,
  scenarios); a one-step budget split may stay inline. No tool → say the figures are unexecuted.
- Calculate on labeled assumptions rather than waiting for missing inputs. Mark each input as
  sourced, user-given or assumed, and name the one input that would flip the verdict.
- Verify current fees, taxes and rates from primary sources and date them. If the primary
  source is unreachable (login wall, no page), use the best secondary source, mark it
  unverified, and still give the verdict conditionally.
- Use the user's currency; keep original currencies. An FX rate may be assumed if stated and
  labeled. Currency of the business unknown and material → ask; never silently default.
- Never infer available cash from revenue, inventory or pending receipts.
- Show a plausible downside case and separate cash recovery from profit.
- Buy/commit decisions end with a verdict: take / take if X / walk. Diagnosis questions (why
  sales dropped) end with the most likely cause and the check that confirms it.

## Widget for a money verdict

With `widgets: yes` (per [widgets](../../setup/references/widgets.md)): a money verdict is
metric cards — the three numbers that decide it (margin or break-even, worst realistic case,
the signal to watch). When scenarios are compared, add one chart. Numbers are computed before
the widget, never inside it. Text keeps the verdict in one line above the widget.
