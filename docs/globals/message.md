# The `message` Variable

In TBL, `message` is a **plain string** containing the text of the current message — nothing more.

It is extracted from `update.message.text` only. It is **not** the full Telegram message object.

## How `message` Works

| Situation | `message` value |
| --- | --- |
| User sent a text message | The message text (e.g. `"Hello bot"`) |
| Photo, sticker, voice, document | `null` |
| Callback query, inline query | `null` |
| Channel post (non-text) | `null` |
| Webhook or webapp command | Usually `null` |

```javascript
// Simple echo for text messages
if (message) {
  Bot.sendMessage(chat.id, `You said: ${message}`)
}
```

## `message` vs `msg` vs `update.message`

| Variable | Type | Use for |
| --- | --- | --- |
| `message` | `string \| null` | Quick text-only checks |
| `msg` | Message helper object | Replying, editing, reactions |
| `update.message` | Raw Telegram object | Full message metadata |

For text with captions on media, use `msg.getText()` or read `update.message.caption` — `message` only covers `.text`.

## Important Notes

- `message` contains **text only** — no media, no metadata
- It is `null` for non-text updates
- Exists only during command execution
