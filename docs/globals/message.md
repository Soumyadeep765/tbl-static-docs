# message

Just the text. No metadata, no drama.

## What is it?

**`message`** is a plain **string** — the text the user typed in their message. That's it. Not the full Telegram message object, not the caption on a photo, not the button label. Just the words.

If someone sends `"Hello bot"`, then `message` is `"Hello bot"`. If they send a cat sticker instead, `message` is `null`. Stickers are many things. Text they are not.

## When would you use it?

Perfect for quick, text-only logic:

- Echo bots ("you said X")
- Simple keyword checks
- Commands where [`params`](params.md) isn't set but you still want the full message text

When you need to **reply, edit, or react** to the message, switch to [`msg`](msg.md). When you need photos, captions, or entities, use [`update`](update.md) or `msg.getText()`.

---

## Try it

```js
// Simple echo
if (message) {
  Bot.sendMessage("You said: " + message)
} else {
  Bot.sendMessage("I only understand text messages right now.")
}
```

---

## When is `message` set?

| Situation | `message` value |
| --- | --- |
| User sent a text message | The message text (e.g. `"Hello bot"`) |
| Photo, sticker, voice, document | `null` |
| Callback query, inline query | `null` |
| Channel post (non-text) | `null` |
| Webhook or webapp command | Usually `null` |

For text in **media captions**, use `msg.getText()` or read `update.message.caption` — `message` only covers `.text`.

---

## `message` vs `msg` vs `update.message`

Three variables, three jobs. Pick the right tool:

| Variable | Type | Use for |
| --- | --- | --- |
| `message` | `string \| null` | Quick text-only checks |
| [`msg`](msg.md) | Message helper object | Replying, editing, reactions |
| [`update`](update.md)`.message` | Raw Telegram object | Full message metadata |

Rule of thumb: reading text? `message` or `msg.text`. Doing something *to* the message? `msg`.

---

## Good to know

- `message` contains **text only** — no media, no metadata
- It is `null` for non-text updates — always check before using it
- Exists only during command execution
