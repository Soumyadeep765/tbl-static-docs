# Actions

Delete, pin, react, forward, copy, and send chat actions on the **current message** or chat.

```js
await msg.delete()
await msg.react("👍")
await msg.pin()
await msg.forward(user.id)
```

---

## Delete

### `delete(messageId?)` — alias: `del`, `remove`

Delete a message in the current chat. Defaults to the current message.

```js
await msg.delete()              // delete the message that triggered the command
await msg.delete(msg.message_id) // same — explicit id
await msg.del(otherMessageId)   // delete a different message in this chat
```

---

## Reactions

### `react(emoji, isBig?)` — alias: `reaction`

Add an emoji reaction to the current message:

```js
await msg.react("👍")
await msg.react("🔥", true)   // large animation
await msg.reaction("❤️")
```

| Param | Default | Description |
| --- | --- | --- |
| `emoji` | required | Single emoji string |
| `isBig` | `false` | Show large reaction animation |

### `removeReaction(options?)` — alias: `unreact`

Remove the bot's reaction from the current message:

```js
await msg.removeReaction()
await msg.unreact()
```

---

## Pin and unpin

### `pin(disableNotification?)`

Pin the current message in the chat:

```js
await msg.pin()           // with notification
await msg.pin(true)       // silently
```

Requires bot admin rights with `can_pin_messages` in groups.

### `unpin(messageId?)`

Unpin a message. Defaults to the current message:

```js
await msg.unpin()
await msg.unpin(specificMessageId)
```

---

## Forward and copy

### `forward(toChatId, options?)` — alias: `fwd`

Forward the current message to another chat:

```js
await msg.forward(user.id)
await msg.fwd(chat.id, { disable_notification: true })
```

### `copy(toChatId, options?)` — alias: `cp`

Copy (send without forward header) to another chat:

```js
await msg.copy(user.id)
await msg.cp(chat.id, { caption: "Copied for you" })
```

| Param | Description |
| --- | --- |
| `toChatId` | Destination chat ID or `@username` |
| `options` | Extra `forwardMessage` / `copyMessage` params |

---

## Chat actions

### `sendChatAction(action, options?)` — alias: `action`, `typing`

Show a status indicator in the chat:

```js
await msg.sendChatAction("typing")
await msg.typing()
await msg.action("upload_photo")
```

| Action | Shows |
| --- | --- |
| `typing` | Typing… |
| `upload_photo` | Sending photo… |
| `record_video` | Recording video… |
| `upload_video` | Sending video… |
| `record_voice` | Recording voice… |
| `upload_voice` | Sending voice… |
| `upload_document` | Sending file… |
| `choose_sticker` | Choosing sticker… |
| `find_location` | Finding location… |
| `record_video_note` | Recording video note… |
| `upload_video_note` | Sending video note… |

Chat actions expire after ~5 seconds. Send again for longer operations.

```js
await msg.sendChatAction("typing")
await sleep(2)
await msg.reply("Here's the answer...")
```

---

## Business messages

### `read(options?)` — alias: `markRead`, `markAsRead`

Mark the current **business message** as read. Only works when `msg.isBusiness()` is `true`.

```js
if (msg.isBusiness()) {
  await msg.read()
}
```

Throws `read is only available for business messages` on normal messages.

---

## Method reference

| Method | Alias | Telegram API |
| --- | --- | --- |
| `delete(id?)` | `del`, `remove` | `deleteMessage` |
| `react(emoji, big?)` | `reaction` | `setMessageReaction` |
| `removeReaction(opts?)` | `unreact` | `deleteMessageReaction` |
| `pin(silent?)` | — | `pinChatMessage` |
| `unpin(id?)` | — | `unpinChatMessage` |
| `forward(chatId, opts?)` | `fwd` | `forwardMessage` |
| `copy(chatId, opts?)` | `cp` | `copyMessage` |
| `sendChatAction(action, opts?)` | `typing`, `action` | `sendChatAction` |
| `read(opts?)` | `markRead` | `readBusinessMessage` |

---

## Examples

### Self-destructing command response

```js
let notice = await msg.reply("Processing...")
// ... do work ...
await notice.delete()
await msg.reply("Done!")
```

### Forward user message to admin

```js
let adminId = process.env.ADMIN_CHAT_ID
await msg.forward(adminId)
await msg.reply("Reported to admin.")
```

### React to confirm

```js
await msg.react("✅")
await msg.reply("Marked as complete.")
```

### Typing indicator during slow work

```js
await msg.sendChatAction("typing")
let result = await HTTP.get("https://api.example.com/data")
await msg.reply("Result: " + result.data.value)
```

---

## Notes

- `delete()` can remove the triggering message or any message in the same chat (with permission)
- Reactions require Telegram Premium in some private chat contexts
- `forward` shows "Forwarded from" header; `copy` does not
- Rate limit: **10 msg method calls per second**
- For actions on messages sent via `Api`, use [method chaining](../api-instance/method-chaining.md) on the returned object
