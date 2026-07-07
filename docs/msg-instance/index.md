# msg Instance

`msg` is the **current Telegram message** with built-in helper methods. Read message fields directly (`msg.text`, `msg.photo`) and act on the message without passing `chat_id` or `message_id` every time.

```js
await msg.reply("Got it!")
await msg.editText("Updated.")
await msg.react("👍")
```

!!! note "Global `msg` vs this section"
    The global [`msg`](../globals/msg.md) variable **is** this instance — same object, same methods. This section documents the full API in detail.

---

## When `msg` is available

| Context | `msg` |
| --- | --- |
| `message` update | Message helper object |
| `business_message` update | Message helper object |
| Callback query | `null` — use [`Api`](../api-instance/index.md) or `query` |
| Inline query | `null` |
| `edited_message` | `null` — no helper on edits alone |
| Channel post (`channel_post`) | `null` |
| Webhook / webapp commands | `null` |
| Broadcast commands | `null` |

Always check before calling methods:

```js
if (!msg) return
await msg.reply("Hello!")
```

---

## What `msg` contains

`msg` is the raw Telegram **Message object** plus helper methods attached on top:

| Layer | Examples |
| --- | --- |
| Telegram fields | `text`, `caption`, `photo`, `entities`, `reply_markup`, `from`, `chat`, `message_id`, `date` |
| Helper methods | `reply()`, `editText()`, `delete()`, `react()`, `pin()`, … |
| Getter helpers | `getText()`, `getMessageId()`, `getChatId()`, `isBusiness()` |

```js
// Read data
let body = msg.text || msg.caption
let sender = msg.from.first_name

// Act on the message
await msg.reply("Hi " + sender + "!")
```

---

## Two call styles

Every helper accepts **string arguments** (shorthand) or a **full params object** (Telegram API format):

```js
// Shorthand — chat_id and reply_to_message_id filled automatically
await msg.reply("Hello!", { parse_mode: "HTML" })

// Full object — pass any Telegram sendMessage param
await msg.reply({
  text: "Hello!",
  parse_mode: "HTML",
  reply_markup: { inline_keyboard: [[{ text: "OK", callback_data: "/ok" }]] }
})
```

Reply methods automatically set `reply_to_message_id` to the current message. Edit/delete/pin methods automatically set `chat_id` and `message_id`.

---

## Default parse mode

Text replies and edits default to `parse_mode: "Markdown"` when using shorthand syntax. Override per call:

```js
await msg.reply("**bold**", { parse_mode: "HTML" })
await msg.editText("Updated", { parse_mode: "MarkdownV2" })
```

---

## Short aliases

Every method has short aliases. All names are **case-insensitive**:

| Method | Aliases |
| --- | --- |
| `reply` | `r` |
| `replyPhoto` | `photo` |
| `replyVideo` | `video` |
| `replyDocument` | `doc`, `document` |
| `replySticker` | `sticker` |
| `replyAnimation` | `gif`, `animation` |
| `editText` | `edit` |
| `delete` | `del`, `remove` |
| `react` | `reaction` |
| `forward` | `fwd` |
| `copy` | `cp` |
| `sendChatAction` | `action`, `typing` |
| `getMessageId` | `id`, `messageId` |
| `getChatId` | `chatId` |
| `getText` | `text` |

```js
await msg.r("Quick reply")
await msg.photo("https://example.com/img.jpg", { caption: "Photo" })
```

---

## Rate limit

`msg` methods share a rate limit of **10 calls per second** (same bucket as the underlying `Api` calls they wrap).

---

## `msg` vs other variables

| Variable | What it is |
| --- | --- |
| `msg` | Message object **with methods** — use for reply, edit, delete |
| `message` | Plain **string** of incoming text only (`update.message.text`) |
| `update.message` | Raw Telegram object — no helper methods |
| `chat` | Current chat info (`id`, `type`, `title`) |
| `user` | Sender info (`id`, `first_name`, `username`) |

For callback buttons, use [`Api`](../api-instance/index.md) method chaining on the sent message instead — see [Method Chaining](../api-instance/method-chaining.md).

---

## Pages in this section

| Page | Covers |
| --- | --- |
| [Replying](replying.md) | `reply`, `replyPhoto`, `replyVideo`, media, polls, dice |
| [Editing](editing.md) | `editText`, `editCaption`, `editMedia`, keyboards, live location |
| [Actions](actions.md) | Delete, pin, react, forward, copy, chat actions, business read |
| [Message Data](message-data.md) | Fields, getters, business messages, availability |

---

## Quick example

```js
// /start command — user sent a message, msg is available
if (!msg.hasText()) {
  await msg.reply("Send me some text!")
  return
}

await msg.sendChatAction("typing")
await sleep(1)

let sent = await msg.reply("You said: " + msg.getText())
await sent.react("👍")
```
