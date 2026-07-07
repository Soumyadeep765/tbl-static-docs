# md2html

`modules.md2html` converts **Telegram-style Markdown** to **Telegram-compatible HTML**. Use it when you have Markdown text and need to send with `parse_mode: "HTML"`.

```js
let html = modules.md2html("**Bold** and *italic* text")
Bot.sendMessage(chat.id, html, { parse_mode: "HTML" })
```

Powered by [telegram-md2html](https://www.npmjs.com/package/telegram-md2html).

---

## Basic usage

```js
modules.md2html("**Hello** *world*!")
// "<b>Hello</b> <i>world</i>!"

modules.md2html("Visit [Google](https://google.com)")
// 'Visit <a href="https://google.com">Google</a>'
```

Pass the result directly to `Bot.sendMessage` or `Api.sendMessage` with `parse_mode: "HTML"`.

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

## Full message example

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
Bot.sendMessage(chat.id, html, { parse_mode: "HTML" })
```

---

## With user content

Escape is handled automatically when `escapeHtml` is enabled (default). For mixed user input, still validate content before converting:

```js
let userText = modules.tgutil.escapeText(params, "html")
let html = modules.md2html("**You wrote:**\n" + userText)
Bot.sendMessage(chat.id, html, { parse_mode: "HTML" })
```

Or use [tgutil](../libs/tgutil.md) for Telegram-specific escaping.

---

## Limits

| Limit | Value |
| --- | --- |
| Input size | Plan buffer size (512 KB – 10 MB) |
| Method | Sync function call |

Input exceeding the plan buffer throws: `Markdown input exceeds plan limit (N bytes)`.

---

## md2html vs manual HTML

| Approach | When to use |
| --- | --- |
| `modules.md2html(text)` | You have Markdown and want HTML parse mode |
| `parse_mode: "Markdown"` | Simple Telegram Markdown — no conversion needed |
| `parse_mode: "MarkdownV2"` | Full MarkdownV2 — escape with [tgutil](../libs/tgutil.md) |
| Manual HTML | Full control over tags |

---

## Notes

- Returns a **string** — sync, no `await`
- Output is safe for Telegram `parse_mode: "HTML"`
- HTML special characters in plain text are escaped by default
- For date formatting in messages, see [dayjs](dayjs.md) or [Libs.dateTimeFormat](../libs/date-time-format.md)
- Package docs: [telegram-md2html on npm](https://www.npmjs.com/package/telegram-md2html)
