# Message Data

`msg` is both an **action API** and a **data object**. All standard Telegram [Message](https://core.telegram.org/bots/api#message) fields are readable directly, plus helper getters for common values.

```js
let id = msg.message_id
let text = msg.text
let chatType = msg.chat.type
let isBiz = msg.isBusiness()
```

---

## Core fields

| Field | Type | Description |
| --- | --- | --- |
| `message_id` | `number` | Unique message ID in this chat |
| `text` | `string` | Text content (text messages only) |
| `caption` | `string` | Media caption |
| `date` | `number` | Unix timestamp |
| `chat` | `object` | Chat the message was sent in |
| `from` | `object` | Sender (may be absent in channels) |
| `entities` | `array` | Text formatting entities |
| `reply_markup` | `object` | Inline or reply keyboard attached |

### Media fields (when present)

| Field | Message type |
| --- | --- |
| `photo` | Array of PhotoSize objects |
| `video` | Video object |
| `audio` | Audio object |
| `voice` | Voice object |
| `document` | Document object |
| `sticker` | Sticker object |
| `animation` | Animation (GIF) object |
| `location` | Location object |
| `contact` | Contact object |
| `poll` | Poll object |
| `dice` | Dice object |

```js
if (msg.photo) {
  let fileId = msg.photo[msg.photo.length - 1].file_id
  await msg.replyPhoto(fileId, { caption: "Same image back" })
}

if (msg.document) {
  await msg.reply("Received file: " + msg.document.file_name)
}
```

---

## Helper getters

| Method | Alias | Returns |
| --- | --- | --- |
| `getText()` | `text` | `msg.text` or `msg.caption`, or `null` |
| `hasText()` | — | `true` if text or caption is non-empty |
| `getMessageId()` | `id`, `messageId` | Current `message_id` |
| `getChatId()` | `chatId` | Current `chat.id` |
| `getBusinessConnectionId()` | `businessConnectionId` | Business connection ID or `null` |
| `isBusiness()` | `isBusinessMessage` | `true` for business messages |

```js
if (msg.hasText()) {
  await msg.reply("You wrote: " + msg.getText())
}

let chatId = msg.getChatId()
let msgId = msg.getMessageId()
```

Note: `getText` as a **method** returns text/caption. The `text` **alias** calls the getter — but `msg.text` as a **property** is the raw Telegram text field only (not caption).

---

## Chat and sender

### `msg.chat`

| Field | Description |
| --- | --- |
| `id` | Chat ID |
| `type` | `"private"`, `"group"`, `"supergroup"`, `"channel"` |
| `title` | Group/channel title |
| `username` | Public @username |

```js
if (msg.chat.type === "private") {
  await msg.reply("This is a private chat.")
}
```

### `msg.from`

| Field | Description |
| --- | --- |
| `id` | User ID |
| `first_name` | First name |
| `last_name` | Last name |
| `username` | @username |
| `is_bot` | Whether sender is a bot |

```js
await msg.reply("Hello " + msg.from.first_name + "!")
```

---

## Business messages

When the update type is `business_message`, `msg` is built from `update.business_message`:

| Extra behaviour | Detail |
| --- | --- |
| `isBusiness()` | Returns `true` |
| `getBusinessConnectionId()` | Returns the connection ID |
| `read()` | Available — marks message as read |
| Auto-injected params | `business_connection_id` added to API calls |

```js
if (msg.isBusiness()) {
  await msg.read()
  await msg.reply("Thanks for your business inquiry!")
}
```

---

## Reply context

| Field | Description |
| --- | --- |
| `reply_to_message` | Message this is a reply to (full object) |
| `reply_to_message_id` | ID only (legacy) |

```js
if (msg.reply_to_message) {
  await msg.reply("Replied to: " + (msg.reply_to_message.text || "[media]"))
}
```

---

## `msg` vs `message` vs `update.message`

| Variable | Type | Use for |
| --- | --- | --- |
| `msg` | Message + methods | Replying, editing, reading all fields |
| `message` | `string` or `null` | Quick read of incoming **text only** |
| `update.message` | Raw object | Advanced access without helpers |

```js
// These are equivalent for plain text:
let a = message
let b = msg.text

// Caption-only messages have no msg.text — use getText():
let c = msg.getText()  // returns caption
```

---

## Availability rules

`msg` is created only when the update contains:

| Source | Field checked |
| --- | --- |
| Normal message | `update.message` |
| Business message | `update.business_message` |

`msg` is **`null`** when:

- Callback query (`callback_query`) — use `query` global instead
- Inline query
- Edited message only (`edited_message`)
- Channel post (`channel_post`)
- Webhook or webapp command
- Broadcast command

```js
if (!msg) {
  // Fallback for callbacks
  if (query) {
    await Api.answerCallbackQuery({ text: "OK" })
  }
  return
}
```

---

## Case insensitivity

Method names work in any casing — `msg.replyPhoto()`, `msg.replyphoto()`, and `msg.REPLYPHOTO()` all work.

---

## Notes

- `msg` exists only during command execution — not stored between updates
- Do not confuse with [Libs](../libs/index.md) or [modules](../modules/index.md) — unrelated
- For sending without a triggering message, use [`Bot`](../bot-instance/index.md) or [`Api`](../api-instance/index.md)
- Entity parsing for formatted text: [tgutil](../libs/tgutil.md) `parseEntities()`
