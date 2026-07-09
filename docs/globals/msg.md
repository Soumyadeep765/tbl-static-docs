# msg

The current message — with built-in reply, edit, and react superpowers.

## What is it?

**`msg`** is the current Telegram message, enriched with **helper methods** for replying, editing, deleting, reacting, and more. Instead of passing `chat.id` and `message_id` everywhere, you just call `msg.reply("Got it!")`.

It's [`update`](update.md)`.message` after a gym membership — same data, but it can do more.

## When would you use it?

- Reply to the message that triggered your command
- Edit the message in place
- React with an emoji
- Read text, captions, or message IDs without digging through `update`
- Delete, pin, or forward the current message

For a plain text string only, [`message`](message.md) is simpler. For raw Telegram fields with no helpers, use `update.message`. For actually *doing things* to the message, use `msg`.

!!! note "Two docs, same API"
    This page covers the **global `msg` variable**. The [msg instance](../msg-instance/index.md) page has the full method list with more examples.

---

## Try it

```js
// Read fields directly
let text = msg.text
let messageId = msg.message_id

// Reply without passing chat/message IDs
await msg.reply("Got it!")

// Short alias
await msg.r("Got it!")

// Edit the message that triggered this command
await msg.editText("Updated text")

// React with an emoji
await msg.react("👍")
```

---

## When is `msg` available?

| Update type | `msg` value |
| --- | --- |
| `message` | Message helper object |
| `business_message` | Message helper object |
| Callback query, webhook, webapp, broadcast | `null` |

Always check before calling methods. `msg.reply()` on `null` is not a fun debugging session.

---

## Common methods

| Method | Aliases | Description |
| --- | --- | --- |
| `reply(text, options?)` | `r` | Send a text reply |
| `replyPhoto(...)`, `replyVideo(...)`, etc. | `photo`, `video`, … | Send media replies |
| `editText(text, options?)` | `edit` | Edit message text |
| `editCaption(caption, options?)` | `editCap` | Edit media caption |
| `delete(messageId?)` | `del`, `remove` | Delete a message |
| `react(emoji)` | `reaction` | Add emoji reaction |
| `forward(chatId)` | `fwd` | Forward to another chat |
| `pin()`, `unpin()` | | Pin or unpin in chat |
| `getText()` | `text` | Get text or caption |
| `getMessageId()` | `id`, `messageId` | Get current message ID |
| `getChatId()` | `chatId` | Get current chat ID |
| `isBusiness()` | `isBusinessMessage` | Whether this is a business message |

Full method list: [msg instance](../msg-instance/index.md).

---

## `msg` vs `message` vs `update.message`

| Variable | What it is |
| --- | --- |
| `msg` | Message object **with helper methods** |
| [`message`](message.md) | Plain **string** of text only (or `null`) |
| [`update`](update.md)`.message` | Raw Telegram object — no helpers |

---

## Good to know

- Methods return Promises — use `await` when you need the result
- `msg` exists only during command execution
- For reply flows that wait for user input, see [Handle Need Reply](../getting-started-with-tbl/handle-need-reply.md)
