# The `request` Variable

In TBL, `request` points to the **active payload** for the current update. TBL automatically maps the relevant part of the update so you don't have to dig through the full `update` object.

## Telegram Updates

For normal Telegram commands, `request` is the sub-object that triggered the command:

| `update_type` | `request` equals |
| --- | --- |
| `message` | `update.message` |
| `callback_query` | `update.callback_query` |
| `inline_query` | `update.inline_query` |
| `chat_member` | `update.chat_member` |
| Other types | The matching sub-object on `update` |

```javascript
// Handle callback queries without parsing update manually
if (update_type === 'callback_query') {
  let data = request.data
  Bot.sendMessage(request.from.id, `You pressed: ${data}`)
}
```

## Webhook and Webapp Mode

When a command runs via [Webhook](../webhook-instance/index.md) or [Webapp](../webapp-instance/index.md), `request` contains **HTTP request data** instead of a Telegram sub-object.

| Field | Type | Description |
| --- | --- | --- |
| `url` | `string` | Request URL |
| `method` | `string` | HTTP method (`GET`, `POST`, etc.) |
| `headers` | `Object` | Request headers |
| `ip` | `string` | Client IP address |
| `query` | `Object` | URL query parameters |
| `body` | `Object \| null` | POST body (webhook POST requests) |

```javascript
// Webhook command: read query params
let page = request.query.page || '1'

// Webhook POST: read body
let name = request.body?.name
```

## Important Notes

- `request` is read-only and exists only during command execution
- Its structure depends on how the command was triggered (Telegram update vs HTTP request)
- For webhook routing details, see [Webhook](../webhook-instance/index.md)
