# Markdown & Formatting

TBL supports formatted text in command **Answers** and in messages sent from **Logic**.

---

## Answer field formatting

Every command has a **parse mode** (default: `Markdown`). It controls how the **Answer** text is rendered when sent automatically.

| Parse mode | Example in Answer |
| --- | --- |
| `Markdown` | `*bold*`, `_italic_`, `` `code` `` |
| `HTML` | `<b>bold</b>`, `<i>italic</i>`, `<code>code</code>` |
| `MarkdownV2` | Telegram [MarkdownV2](https://core.telegram.org/bots/api#markdownv2-style) rules |

```
*Welcome to my bot!*
_Pick an option below._
```

Set parse mode in the command editor. See [Command Fields](command-fields.md).

---

## Logic messages

Answers are formatted automatically, but messages you send in Logic need an explicit `parse_mode`:

```js
Bot.sendMessage("*Done!* Your settings were saved.", { parse_mode: "Markdown" })

await Api.sendMessage({
  chat_id: chat.id,
  text: "<b>Order</b> confirmed.",
  parse_mode: "HTML"
})
```

`Bot` and `Api` do not inherit the command's parse mode — set it per call.

---

## `modules.md2html` — Markdown to HTML

Convert Telegram-style Markdown to HTML inside Logic — useful before sending HTML messages or building web content:

```js
let md = "*Sale!* Visit [our site](https://example.com)"
let html = modules.md2html(md)

await Api.sendMessage({
  chat_id: chat.id,
  text: html,
  parse_mode: "HTML"
})
```

See [md2html module](../modules/md2html.md) for details and plan buffer limits.

---

## `Libs.tgutil` helpers

Escape and link helpers for safe formatting:

```js
let safe = Libs.tgutil.escapeText(userInput, "markdown")
let link = Libs.tgutil.getLinkFor(user, "markdown")
```

See [tgutil](../libs/tgutil.md).

---

## Rich messages (Api)

For tables and advanced layouts, use Api rich message fields:

```js
await Api.sendMessage({
  chat_id: chat.id,
  rich_message: {
    markdown: "# Order Summary\n\n| Item | Qty |\n| --- | --- |\n| Widget | 2 |"
  }
})
```

See [Sending Messages](../api-instance/sending-messages.md).

---

## Public web & `.md` commands

Commands with a `.md` extension served via [public web](public-web-commands.md) use content type `text/markdown`. For HTML public pages, use `.html` commands with EJS.

---

## Common mistakes

| Problem | Fix |
| --- | --- |
| Asterisks show literally | Set `parse_mode: "Markdown"` on the send call |
| HTML tags show as text | Use `parse_mode: "HTML"`, not Markdown |
| User input breaks formatting | Escape with `Libs.tgutil.escapeText()` |
| Special chars in MarkdownV2 | Escape per Telegram rules |

---

## See also

- [Command Fields](command-fields.md) — parse mode setting
- [Your First Bot](first-hello-bot.md) — formatted welcome message
- [md2html](../modules/md2html.md)
