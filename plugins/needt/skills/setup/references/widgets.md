# Widgets — shared by every Needt skill

Some hosts (Claude Desktop with the `visualize` tool) can render a widget inside the chat:
HTML or SVG that becomes a checklist with checkboxes, a chart, a step with answer buttons, a
diagram. The setup line says whether this host can: `widgets: yes` means `show_widget` is in
the tool catalog; anything else means `no`. Inside a sub-agent it is always `no`.

A widget is a better way to show the same answer, never a different answer. Every skill
produces the same decisions, numbers and files with `widgets: no`; the widget only changes
how they are shown and how the user answers back.

## When a widget, when text

With `widgets: yes`, show as a widget what has a shape:

| Shape | Widget |
|---|---|
| A list the user acts on — today's tasks, a checklist, a plan's steps | list with a checkbox or button per row |
| A choice between options | one card per option, the recommended one marked |
| Numbers that compare or move — money, scenarios, a trend | metric cards + a chart |
| A step the user answers — a quiz question, a decision | question with answer buttons |
| A process, a structure, how something works | diagram |
| Progress — steps done of total, a streak, a project | progress bar or step dots |

Stays text in every host: answers of one or two lines, code, prose explanations, a search
line or readiness line, anything the user will paste elsewhere (a prompt, a task list for
another tool), tables of more than five columns.

## How

1. Before the first widget of the conversation call `read_me` once with every module the
   conversation will need — `interactive` for lists, cards and progress, `chart` for
   numbers, `diagram` for structure, `elicitation` for a form of questions; a module not
   loaded yet is loaded once when its shape first comes up. Its rules win over this file
   on anything visual.
2. One widget per reply, holding one thing. Two shapes in one reply → the more useful one is
   the widget, the other is text.
3. Explanation goes outside the widget, in the reply. The widget holds the object — rows,
   cards, a question and its options, a chart — not paragraphs of teaching or reasoning.
   The reply carries in one line what the user needs if the widget fails to render: the
   question asked, the count of findings, the number of items.
4. Buttons are the skill's own next actions, worded as the user would say them and in the
   user's language — "Done: Call the print shop", "Go deeper on X", "Accept fix 2", "Next
   step" are English examples to translate — sent through `sendPrompt` with the same words
   as the label, plus the item's title where one is needed to tell items apart. No "OK",
   no "Close", no decorative buttons. At most four action buttons per widget; one button
   per row of a list does not count toward that.
5. When the data changes (a task completed, a number recomputed), show a new widget with the
   same `title`, not a description of the change.
6. A widget never stores anything. What must survive — a completed task, a saved
   preference, a learning step passed — is written to Needt by the skill, then the widget
   reflects it.
7. State the user changed inside a widget (a slider, a selection) is read with
   `read_widget_context` before acting, never asked again.
8. Scripts only from the CDN allowlist in `read_me`; no `localStorage`, no network calls
   from the widget, no fullscreen.
9. Many small answers — a quiz round, a form, a batch of yes/no decisions — go into one
   widget that collects or scores them in its own JS and sends one summary line through
   `sendPrompt`, never one widget per answer: every round trip costs the user a click and
   the chat a reply. Keep markup lean — plain inputs and buttons, no library unless the
   shape is a chart.

## Fallback

With `widgets: no`: a choice goes through `AskUserQuestion` when the setup line says
`questions: click`, else as a numbered list where "1" picks the recommended option (a quiz question keeps its
options unmarked); a list
is a markdown table or checklist; a chart is the three numbers that matter in a table;
progress is `step 3 of 7`. The skill never mentions widgets, never says "I would show this as
a widget", never apologizes for text.

## Failing behaviors

A widget for a two-line answer; two widgets in one reply; one widget per small answer; prose inside the widget; a button
that says "OK"; describing a change instead of re-rendering; claiming a widget saved
something; a widget mentioned in a host without `show_widget`; a sub-agent rendering widgets;
a different answer with and without widgets.
