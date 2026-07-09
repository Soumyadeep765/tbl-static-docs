# request

The active payload — already unwrapped so you don't have to.

## What is it?

**`request`** points to the specific part of the current update that matters. TeleBotHost automatically maps it for you, so you don't need to write `update.message` vs `update.callback_query` vs `update.inline_query` every time.

It's your command's "this thing right here" pointer.

## When would you use it?

- **Callback buttons** — read `request.data` for the button payload
- **Inline queries** — grab `request.query` for what the user typed
- **Member updates** — inspect who joined or left
- **Webhook commands** — `request` becomes the HTTP request object (URL, headers, body, query params)

If you already know the [`update_type`](update_type.md), `request` is usually the object you want to read from.

---

## Try it — Telegram updates

```js
// Button press? request has the callback data
if (update_type === "callback_query") {
  let data = request.data
  Bot.sendMessage(request.from.id, "You pressed: " + data)
}

// Inline search? request has the query string
if (update_type === "inline_query") {
  let query = request.query
  Bot.answerInlineQuery(request.id, [
    { type: "article", id: "1", title: "Result for " + query, input_message_content: { message_text: query } }
  ])
}
```

### What `request` equals

| `update_type` | `request` is |
| --- | --- |
| `message` | `update.message` |
| `callback_query` | `update.callback_query` |
| `inline_query` | `update.inline_query` |
| `chat_member` | `update.chat_member` |
| Other types | The matching sub-object on [`update`](update.md) |

---

## Try it — webhooks and webapps

In [Webhook](../webhook-instance/index.md) and [Webapp](../webapp-instance/index.md) mode, `request` holds **HTTP request data** instead of a Telegram sub-object:

| Field | Type | Description |
| --- | --- | --- |
| `url` | `string` | Request URL |
| `method` | `string` | HTTP method (`GET`, `POST`, etc.) |
| `headers` | `Object` | Request headers |
| `ip` | `string` | Client IP address |
| `query` | `Object` | URL query parameters |
| `body` | `Object \| null` | POST body (webhook POST requests) |

```js
// Webhook: read query params
let page = request.query.page || "1"

// Webhook POST: read body
let name = request.body?.name
Bot.sendMessage(chat.id, "Hello, " + name)
```

[`params`](params.md) may also be populated from query or body — handy for simple single-value input.

---

## Good to know

- `request` is read-only and exists only during command execution
- Its shape depends on how the command was triggered — Telegram update vs HTTP request
- For webhook routing patterns, see [Webhook](../webhook-instance/index.md) and [Public Web Commands](../getting-started-with-tbl/public-web-commands.md)
