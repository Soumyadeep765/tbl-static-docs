# Docs for AI agents

TeleBotHost docs are large. Agents should **not** load the whole site.

Use this page (or [`/llms.txt`](https://docs.telebothost.com/llms.txt)) as a **router**: pick one topic → open **one** URL → write TBL code.

## Rules

1. Open **one** docs page for the current task.
2. Prefer this map / [`llms.txt`](https://docs.telebothost.com/llms.txt) over guessing APIs.
3. Open a second page only if needed.
4. In a VS Code / Cursor bot workspace, also follow local `AGENTS.md` (command headers, `id:`, upload flow).

## What is what

| Need | Open this |
|------|-----------|
| What is TBL / language | [What is TBL?](about-tbl.md), [The TBL Language](used-language.md) |
| Command header fields | [Command Fields](getting-started-with-tbl/command-fields.md) |
| Answer text / `{{user…}}` | [Answer Field](getting-started-with-tbl/answer-field.md) |
| Reply keyboard (bottom buttons) | [Adding a Keyboard](getting-started-with-tbl/adding-keyboard.md) |
| Inline buttons (in message) | [Inline Keyboards](api-instance/inline-keyboards.md) |
| Callbacks / `callback_query` | [Handling Callbacks](getting-started-with-tbl/handling-callbacks.md) |
| Wait for next user message | [Need Reply](getting-started-with-tbl/handle-need-reply.md) |
| Wildcard `*` command | [Using Wildcard](getting-started-with-tbl/using-wildcard.md) |
| Matching order / priority | [Matching & Priority](getting-started-with-tbl/matching-order.md) |
| Quick send in current chat | [Bot · Sending Messages](bot-instance/sending-messages.md) |
| Full Telegram API / other chats | [Api · Sending Messages](api-instance/sending-messages.md) |
| Bot vs Api | [Bot vs Api](guides/bot-vs-api.md) |
| `user` / `chat` / `params` | [Globals](globals/index.md) |
| Store data | [db](db-instance/index.md) → `db.bot` / `db.user` / `db.global` |
| Outbound HTTP | [HTTP](http-instance/making-requests.md) |
| Incoming webhooks | [Webhooks](webhook-instance/index.md) |
| Webapp / public URL | [Webapps](webapp-instance/index.md), [Public Web Commands](getting-started-with-tbl/public-web-commands.md) |
| `res.send` / HTML for web | [res](res-instance/index.md) |
| Built-in modules (`modules.*`) | [Modules](modules/index.md) |
| Hosted libs (`Libs.*`) | [TBL Libraries](libs/index.md) |
| Photos / files | [Media and Files](api-instance/media-and-files.md) |
| Edit / delete messages | [Editing Messages](api-instance/editing-messages.md) |
| Broadcast | [Broadcasting](bot-instance/broadcasting.md) |

## Machine index

Plain-text URL list for crawlers and agents:

**https://docs.telebothost.com/llms.txt**

## Tutorials

| Lesson | Page |
|--------|------|
| 1 — First bot | [First Hello Bot](getting-started-with-tbl/first-hello-bot.md) |
| 2 — Keyboard | [Adding a Keyboard](getting-started-with-tbl/adding-keyboard.md) |
| 3 — Aliases | [Adding Aliases](getting-started-with-tbl/adding-aliases.md) |
| 4 — User input | [Need Reply](getting-started-with-tbl/handle-need-reply.md) |
| 5 — Callbacks | [Handling Callbacks](getting-started-with-tbl/handling-callbacks.md) |
| 6 — Wildcard `*` | [Using Wildcard](getting-started-with-tbl/using-wildcard.md) |
