# Delivering the prompt — one-click choice

Read when delivering (SKILL.md §7).

1. The prompt in one fenced code block, ready to paste.
2. Under it, at most three lines: size picked and why, the assumptions made, the one thing
   worth changing if the user disagrees.
3. If the user said to run it (`и запусти`, `go`, `выполни`), execute it in this chat right
   after delivering — no button.
4. Otherwise end with a **one-click choice**, in the same reply, right after the three lines:
   - Clickable questions here (`questions: click` in the setup line, `AskUserQuestion` or the
     host's equivalent): one question, `header` "Prompt", in the user's language — e.g.
     "Use this prompt now?" / "Запустить этот промт?". Options, recommended first:
     **Use prompt (Recommended)** — "Runs it here, in this chat"; **Change something** —
     "Tell me what to adjust, I rewrite it"; **Copy only** — "I'll paste it elsewhere".
     Translate labels to the user's language. When the prompt is for another product
     (ChatGPT, Gemini, a coding agent elsewhere), make **Copy only** the recommended first
     option and keep **Use prompt** second.
   - `questions: text` and `widgets: yes`: the same three choices as one small widget with
     three buttons — **Use prompt**, **Change something**, **Copy only**, recommended first by
     the same rule — that `sendPrompt` the words `go` / `change: …` (opens a field) / `copy`.
   - No clickable questions and no widgets: the same three choices in one line —
     `Use it? — "go" runs it here · "change: …" rewrites it · "copy" and I stop.` (user's language).
   - On **Use prompt** (click or "go"): execute the prompt in this chat at once, as if the user
     had pasted it, starting with its first stage. On **Change something**: ask what, in one
     line, then deliver the changed blocks and the same choice again. On **Copy only**: stop.

When the user sends their own prompt to improve, keep their intent and voice, show the
improved version, list the 2–4 changes that matter — not every edit — and end with the same
one-click choice.

When the user asks for a change to a prompt already delivered in this conversation, give the
replacement blocks only, then one full copy once they say they will paste it. Do not reprint
a long prompt for a two-line edit.

