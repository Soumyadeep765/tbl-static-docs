# update

The whole Telegram envelope — everything that just happened, delivered in one object.

## What is it?

**`update`** is the full payload that triggered your command. When someone sends a message, taps a button, or joins your group, Telegram wraps that event in an **update** object. TeleBotHost hands it to you as-is (plus a few helpful extras).

Think of it as the security camera footage of the interaction — complete, unedited, and occasionally more detail than you need.

## When would you use it?

Most of the time, you won't. The convenience globals — [`user`](user.md), [`chat`](chat.md), [`request`](request.md), [`message`](message.md) — already pull out the useful bits for you.

Reach for `update` when you need something specific that those shortcuts don't cover:

- Photos, stickers, or documents attached to a message
- Callback query data from inline buttons
- Member join/leave events
- Webhook context flags (`webhook`, `webapp`, `web_request`)

!!! tip "New to globals?"
    Start with [`user`](user.md) and [`chat`](chat.md). Come back to `update` when you need the raw data. Overview: [Global Variables](index.md).

---

## Try it

```js
// Grab photos from a message (message global won't help here)
let photos = update.message?.photo

// Handle button presses
if (update.callback_query) {
  let buttonData = update.callback_query.data
  Bot.sendMessage(update.callback_query.from.id, "You pressed: " + buttonData)
}

// Webhook command: check if this came from HTTP
if (update.webhook) {
  let clientIp = update.web_request.request.ip
  Bot.inspect("Request from: " + clientIp)
}
```

---

## Bonus fields

TeleBotHost adds a few shortcuts directly on `update` so you don't have to dig:

| Field | Type | Description |
| --- | --- | --- |
| `user` | `Object \| null` | Same as the [`user`](user.md) global |
| `chat` | `Object \| null` | Same as the [`chat`](chat.md) global |
| `update_type` | `string` | Same as [`update_type`](update_type.md) |

## Webhook and webapp extras

HTTP-triggered commands get synthetic updates with extra flags:

| Field | Description |
| --- | --- |
| `web_request` | HTTP request wrapper with `request`, `from`, and `chat` |
| `webhook` | `true` when triggered via [Webhook](../webhook-instance/index.md) |
| `web` | `true` for web-triggered commands |
| `webapp` | `true` for [Webapp](../webapp-instance/index.md) commands |

---

## Good to know

- `update` is **read-only** — you can't modify it mid-command
- It exists only while your command is running
- For the full upstream field list, see the [Telegram Bot API Update object](https://core.telegram.org/bots/api#update)
- Not sure which sub-object you need? Check [`update_type`](update_type.md) first, then [`request`](request.md)
