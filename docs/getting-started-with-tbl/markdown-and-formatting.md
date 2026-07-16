# Markdown & Formatting

Plain text works. *Bold welcome messages* work better. TBL lets you format command **Answers** and messages sent from **Logic** — but Telegram is picky about syntax, and the two places behave slightly differently.

Concept first, then examples.

---

## Answer field formatting

Every command has a **parse mode** setting (default: **Markdown**). It controls how the **Answer** text renders when TBL sends it automatically — you don't pass `parse_mode` yourself for Answer.

| Parse mode | Example in Answer |
| --- | --- |
| `Markdown` | `*bold*`, `_italic_`, `` `code` `` |
| `HTML` | `<b>bold</b>`, `<i>italic</i>`, `<code>code</code>` |
| `MarkdownV2` | Telegram [MarkdownV2](https://core.telegram.org/bots/api#markdownv2-style) rules |

```
*Welcome to my bot!*
_Pick an option below._
```

Set parse mode in the command editor — [Command Fields](command-fields.md).

---

## Logic messages — you're on your own

Answers are formatted automatically. Messages **you** send in Logic need an explicit `parse_mode` on each call — the command setting does **not** carry over.

[`Bot`](../bot-instance/index.md) for quick sends:

```js
Bot.sendMessage("*Done!* Your settings were saved.", { parse_mode: "Markdown" })
```

[`Api`](../api-instance/index.md) when you need full control:

```js
await Api.sendMessage({
  chat_id: chat.id,
  text: "<b>Order</b> confirmed.",
  parse_mode: "HTML"
})
```

Forget `parse_mode` and asterisks show up literally. Telegram's favorite prank.

---

## `modules.md2html` — Markdown to HTML

Convert Telegram-style Markdown to HTML inside Logic — handy before sending HTML messages or building web content:

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

User input plus raw Markdown equals broken messages. Escape and link helpers keep things safe:

```js
let safe = Libs.tgutil.escapeText(userInput, "markdown")
let link = Libs.tgutil.getLinkFor(user, "markdown")
```

See [tgutil](../libs/tgutil.md).

---

## Rich messages (Api)

Tables and advanced layouts? Api rich message fields:

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

Start with plain **Markdown** in Answer. Level up to HTML and md2html when you need links and tables.

---

## See also

- [Command Fields](command-fields.md) — parse mode setting
- [Your First Bot](first-hello-bot.md) — formatted welcome message
- [md2html](../modules/md2html.md)
