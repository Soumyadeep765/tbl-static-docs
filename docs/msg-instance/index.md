# msg Instance

The message you're replying to — with helper methods baked in so you don't pass `chat_id` and `message_id` on every line.

Read `msg.text`, reply with `msg.reply()`, edit with `msg.editText()`. The boring IDs are already filled in.

---

## What is `msg`?

**`msg`** is the **current Telegram message** with built-in helper methods. Read message fields directly (`msg.text`, `msg.photo`) and act on the message without passing `chat_id` or `message_id` every time.

| You get | You skip |
| --- | --- |
| `msg.reply()`, `msg.editText()`, `msg.react()` | Manual `chat_id` / `message_id` |
| Raw Telegram fields (`text`, `photo`, `entities`) | Parsing `update` yourself |
| Shorthand and full API call styles | Choosing one format forever |

!!! note "Global `msg` vs this section"
    The global [`msg`](../globals/msg.md) variable **is** this instance — same object, same methods. This section documents the full API in detail.

---

## How to use it

Drop this in any command's **Logic** field (when `msg` is available):

```js
await msg.reply("Got it!")
await msg.editText("Updated.")
await msg.react("👍")
```

Three things worth knowing upfront:

1. **Check `msg` before calling methods** — it's `null` for callbacks, webhooks, and webapps.
2. **Reply methods auto-set `reply_to_message_id`** — edits and deletes auto-set `chat_id` and `message_id`.
3. **Default parse mode is Markdown** for shorthand syntax — override per call if needed.

!!! tip "New to TBL?"
    `user` and `chat` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md). For callback buttons (where `msg` is `null`), use [`Api`](../api-instance/index.md).

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

## Try it — copy-paste examples

Start simple. Each example only introduces what it needs.

### Reply to the user's message

```js
if (!msg) return
await msg.reply("Hi " + user.first_name + "!")
```

### Read message content

```js
let body = msg.text || msg.caption
if (!body) {
  return await msg.reply("Send me some text!")
}
await msg.reply("You said: " + body)
```

### Edit your reply after sending

```js
await msg.sendChatAction("typing")
await sleep(1)

let sent = await msg.reply("You said: " + msg.getText())
await sent.react("👍")
```

### Full Telegram API params

Every helper accepts shorthand strings or a full params object:

```js
await msg.reply({
  text: "Pick one:",
  parse_mode: "HTML",
  reply_markup: { inline_keyboard: [[{ text: "OK", callback_data: "/ok" }]] }
})
```

For callback buttons, use [`Api`](../api-instance/index.md) method chaining instead — see [Method Chaining](../api-instance/method-chaining.md).

---

## What `msg` contains

`msg` is the raw Telegram **Message object** plus helper methods attached on top:

| Layer | Examples |
| --- | --- |
| Telegram fields | `text`, `caption`, `photo`, `entities`, `reply_markup`, `from`, `chat`, `message_id`, `date` |
| Helper methods | `reply()`, `editText()`, `delete()`, `react()`, `pin()`, … |
| Getter helpers | `getText()`, `getMessageId()`, `getChatId()`, `isBusiness()` |

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

## `msg` vs other variables

| Variable | What it is |
| --- | --- |
| `msg` | Message object **with methods** — use for reply, edit, delete |
| `message` | Plain **string** of incoming text only (`update.message.text`) |
| `update.message` | Raw Telegram object — no helper methods |
| `chat` | Current chat info (`id`, `type`, `title`) |
| `user` | Sender info (`id`, `first_name`, `username`) |

---

## Rate limit

`msg` methods share a rate limit of **10 calls per second** (same bucket as the underlying `Api` calls they wrap).

---

## Pages in this section

| Page | Covers |
| --- | --- |
| [Replying](replying.md) | `reply`, `replyPhoto`, `replyVideo`, media, polls, dice |
| [Editing](editing.md) | `editText`, `editCaption`, `editMedia`, keyboards, live location |
| [Actions](actions.md) | Delete, pin, react, forward, copy, chat actions, business read |
| [Message Data](message-data.md) | Fields, getters, business messages, availability |
