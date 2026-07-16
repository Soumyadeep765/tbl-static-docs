# md2html

Write Markdown, send HTML — Telegram's picky parser will thank you.

## What is it?

**md2html** converts **Telegram-style Markdown** into **Telegram-compatible HTML**. When you want bold, links, and spoilers in a message but `parse_mode: "HTML"` is easier to debug than MarkdownV2 escaping, this module does the translation for you.

Access it as `modules.md2html` — a single sync function.

Powered by [telegram-md2html](https://www.npmjs.com/package/telegram-md2html).

---

## How to use

Pass Markdown, get HTML:

```js
let html = modules.md2html("**Bold** and *italic* text")
Bot.sendMessage(html, { parse_mode: "HTML" })
```

Send the result to [Bot](../bot-instance/index.md) with `parse_mode: "HTML"`. That's the whole pipeline.

---

## Supported syntax

| Markdown | HTML output |
| --- | --- |
| `**text**` | `<b>text</b>` |
| `*text*` or `_text_` | `<i>text</i>` |
| `__text__` | `<u>text</u>` |
| `~~text~~` | `<s>text</s>` |
| `\|\|text\|\|` | `<tg-spoiler>text</tg-spoiler>` |
| `` `code` `` | `<code>code</code>` |
| ` ```lang\ncode\n``` ` | `<pre><code>code</code></pre>` |
| `[text](url)` | `<a href="url">text</a>` |
| `> quote` | `<blockquote>quote</blockquote>` |
| `**> quote**` | expandable blockquote |
| `## heading` | `<b>▎ heading</b>` |
| `### heading` | `<b>▎ heading</b>` |

---

## Username protection

Underscores in Telegram usernames are **not** treated as italic:

```js
modules.md2html("Hello @my_telegram_bot")
// "Hello @my_telegram_bot" — preserved, no <i> tags

modules.md2html("This is *italic* text")
// "This is <i>italic</i> text"
```

---

## md2html vs manual HTML

| Approach | When to use |
| --- | --- |
| `modules.md2html(text)` | You have Markdown and want HTML parse mode |
| `parse_mode: "Markdown"` | Simple Telegram Markdown — no conversion needed |
| `parse_mode: "MarkdownV2"` | Full MarkdownV2 — escape with [tgutil](../libs/tgutil.md) |
| Manual HTML | Full control over tags |

---

## Try it

### Format a daily update

[Bot](../bot-instance/index.md) sends to [chat](../globals/chat.md):

```js
let markdown = [
  "## Daily Update",
  "",
  "**New features:**",
  "• *Faster* responses",
  "• ~~Old bug~~ fixed",
  "• ||Secret beta||",
  "",
  "Visit [our docs](https://docs.example.com)",
  "",
  "> Questions? Contact @support_bot"
].join("\n")

let html = modules.md2html(markdown)
Bot.sendMessage(html, { parse_mode: "HTML" })
```

### Mix Markdown with user input

When [user](../globals/user.md) content is involved, escape it first with [Libs.tgutil](../libs/tgutil.md):

```js
let userText = Libs.tgutil.escapeText(params, "html")
let html = modules.md2html("**You wrote:**\n" + userText)
Bot.sendMessage(html, { parse_mode: "HTML" })
```

---

## Notes

- **Sync** — returns a string, no `await`
- Input size is limited by your plan's buffer size (512 KB – 10 MB). Exceeding it throws: `Markdown input exceeds plan limit (N bytes)`
- HTML special characters in plain text are escaped by default (`escapeHtml` enabled)
- Output is safe for Telegram `parse_mode: "HTML"`
- For date formatting in messages, see [dayjs](dayjs.md)
- Package docs: [telegram-md2html on npm](https://www.npmjs.com/package/telegram-md2html)
