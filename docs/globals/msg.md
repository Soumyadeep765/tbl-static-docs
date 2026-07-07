# The `msg` Variable

In TBL, `msg` is the **current Telegram message** enriched with built-in helper methods for replying, editing, and managing that message. It is available for normal messages and business messages.

!!! note "Global `msg` vs msg instance docs"
    This page documents the **global `msg` variable** available in every message-based command.  
    The [msg instance](../msg-instance/index.md) page covers the same API in more detail with additional examples.

## When `msg` Is Available

| Update type | `msg` value |
| --- | --- |
| `message` | Message helper object |
| `business_message` | Message helper object |
| Callback query, webhook, webapp, broadcast | `null` |

## What `msg` Contains

`msg` includes **all native Telegram message fields** (such as `message_id`, `text`, `photo`, `entities`, `reply_markup`) **plus helper methods** bound to that message.

You can read fields directly:

```javascript
let text = msg.text
let messageId = msg.message_id
```

Or call helper methods without passing chat/message IDs:

```javascript
// Reply to the current message
await msg.reply('Got it!')

// Short alias
await msg.r('Got it!')

// Edit the current message
await msg.editText('Updated text')

// React with an emoji
await msg.react('👍')
```

## Common Methods

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

See the [msg instance](../msg-instance/index.md) for the full method list including media, polls, locations, and business message support.

## `msg` vs `message` vs `update.message`

| Variable | What it is |
| --- | --- |
| `msg` | Message object **with helper methods** — use this for replying and editing |
| `message` | Plain **string** of `update.message.text` only (or `null`) |
| `update.message` | Raw Telegram message object — no helper methods |

For simple text reading, `message` or `msg.text` both work. For sending replies or edits, use `msg`.

## Important Notes

- `msg` is `null` outside message and business-message updates — check before calling methods
- Methods return Promises — use `await` or `.then()` inside async flows
- `msg` exists only during command execution
