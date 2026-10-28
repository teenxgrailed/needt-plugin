# Memory — shared by every Needt skill

Memory lives in Needt, not in the chat: what the user asked never to do, how they like things
done, their goals, facts about their projects. It follows them across chats and products.

## Where it is

1. **`needt_remember`** (Needt connector; `content` 1–500 characters, `kind: preference |
   pattern | goal | fact`, default `preference`; no `workspaceId` — the workspace comes from
   the connection) — the primary store. Returns `{id, kind, content, source: "assistant",
   createdAt, updated}`; `updated: true` means a near-duplicate line was refreshed instead of
   added. Errors: memory switched off in the app → 400; sensitive content → 400 (do not
   retry with a rewording); more than 500 assistant lines → 409, offer to clean old ones with
   `needt_forget_memory`. Read with `needt_list_memories`, edit with `needt_update_memory`,
   remove with `needt_forget_memory`.
2. **Fallback — the page "Needt · Memory"** in the personal workspace, when the connector is
   present but `needt_remember` is not: find it with `needt_search` (create once with
   `needt_create_page` if missing), append one line per item with `needt_append_page`:
   `- [preference] 2026-10-28 · never post without asking`. Read it at setup like the list.
3. **No connector** — memory holds for this chat only, inside the `Needt ·` line; say so once.

Never claim something was saved when the call did not succeed. If the connector says memory
is switched off, say that it is turned on in the Needt app, and keep the item for this chat.

## Read

Setup reads memory once per conversation (one call), puts `memory: 12` in the `Needt ·`
line, and every skill treats the lines as standing instructions: a `preference` or `pattern`
outranks a skill's own default. Re-read only when the user says memory changed.

## Write — the plugin saves on its own

Save without asking, then report in one line (`Saved: never schedule before 10:00`):

- An explicit ask: "remember", "don't ever", "from now on", "запомни", "больше так не делай".
- A correction of how something was done ("no, shorter", "use the other workspace") — as a
  `preference`, worded as the rule, not the incident.
- A stable preference noticed twice in the conversation (format, language, tone, tools).
- A `goal` the user states as theirs, a `fact` about their project that later work depends on.

Wording: one line, present tense, the user's own terms, no reasoning. One item per call.
Update an existing line instead of adding a near-duplicate.

## Never save

Secrets and credentials; health, finances or legal details of the person beyond what they
asked to keep; other people's private data; one-off details (a date, a draft); anything the
user asked to forget — that goes to `needt_forget_memory` at once.
