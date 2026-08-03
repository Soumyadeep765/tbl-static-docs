# Docs for AI agents

This site teaches **TBL** (Tele Bot Language) on TeleBotHost: JavaScript commands for Telegram bots.

**How to use docs**

1. Find your topic in the table below (or in [/llms.txt](https://docs.telebothost.com/llms.txt)).
2. Open **one** page: `https://docs.telebothost.com` + the path.
3. Write code from that page. Open a second page only if you still need it.
4. Do **not** download or read every docs page.

Full list of every page path: [llms.txt](https://docs.telebothost.com/llms.txt)

## If you need this → open this page

| You need… | Open |
|-----------|------|
| What TBL is | [What is TBL?](about-tbl.md) |
| Language / JS rules | [The TBL Language](used-language.md) |
| First steps for humans | [Start here](start-here/index.md) |
| Command name, answer, keyboard, aliases | [Command fields](getting-started-with-tbl/command-fields.md) |
| How a command is structured | [Command structure](getting-started-with-tbl/command-structure.md) |
| Answer text / `{{user.first_name}}` | [Answer field](getting-started-with-tbl/answer-field.md) |
| Buttons under the chat input | [Adding a keyboard](getting-started-with-tbl/adding-keyboard.md) |
| Buttons inside the message (inline) | [Inline keyboards](api-instance/inline-keyboards.md) |
| Inline button presses / callbacks | [Handling callbacks](getting-started-with-tbl/handling-callbacks.md) |
| Wait for the user’s next message | [Need reply](getting-started-with-tbl/handle-need-reply.md) |
| Catch-all `*` command | [Using wildcard](getting-started-with-tbl/using-wildcard.md) |
| Which command wins when several match | [Matching order](getting-started-with-tbl/matching-order.md) |
| Extra trigger names | [Aliases](getting-started-with-tbl/adding-aliases.md) |
| Markdown / HTML in answers | [Markdown and formatting](getting-started-with-tbl/markdown-and-formatting.md) |
| Quick send to the current chat | [Bot · Sending messages](bot-instance/sending-messages.md) |
| Full Telegram methods / other chats | [Api · Sending messages](api-instance/sending-messages.md) |
| When to use Bot vs Api | [Bot vs Api](guides/bot-vs-api.md) |
| `user`, `chat`, `params`, `message`, … | [Globals](globals/index.md) |
| Save data (`db.bot` / `db.user` / `db.global`) | [Database](db-instance/index.md) |
| Call external HTTP APIs | [HTTP · Making requests](http-instance/making-requests.md) |
| Incoming webhooks | [Webhooks](webhook-instance/index.md) |
| Mini apps / public web URLs | [Webapps](webapp-instance/index.md) |
| Reply to web/webhook with HTML/JSON | [res](res-instance/index.md) |
| Photos, files, voice | [Media and files](api-instance/media-and-files.md) |
| Edit or delete a sent message | [Editing messages](api-instance/editing-messages.md) |
| Message many users | [Broadcasting](bot-instance/broadcasting.md) |
| Built-in helpers (`modules.*`) | [Modules](modules/index.md) |
| Hosted libraries (`Libs.*`) | [TBL Libraries](libs/index.md) |

## Sections (folder = topic)

| Folder | What is inside |
|--------|----------------|
| `/getting-started-with-tbl/` | Commands, answer, keyboard, matching, tutorials |
| `/globals/` | Runtime variables (`user`, `chat`, `params`, …) |
| `/bot-instance/` | Short helpers for the current chat |
| `/api-instance/` | Full Telegram Bot API wrappers |
| `/msg-instance/` | Helpers on the current message |
| `/db-instance/` | Persistent storage |
| `/http-instance/` | Outbound HTTP |
| `/webhook-instance/` | Incoming signed webhooks |
| `/webapp-instance/` | Telegram Web Apps / public routes |
| `/res-instance/` | HTTP responses for web/webhook commands |
| `/modules/` | Extra JS modules |
| `/libs/` | TeleBotHost `Libs.*` packages |

Every path under those folders is listed in [llms.txt](https://docs.telebothost.com/llms.txt).
