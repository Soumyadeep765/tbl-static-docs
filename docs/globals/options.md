# The `options` Variable

In TBL, `options` carries **context passed between commands** or **results returned from API calls**. It helps share state without using persistent storage.

## How `options` Gets Its Value

| Source | What `options` contains |
| --- | --- |
| `Bot.run('/next', { step: 2 })` | The object you passed as the second argument |
| Telegram API callback | Full API JSON response (`{ ok, result, ... }`) |
| Webhook command | Merged webhook options and HTTP request metadata |

## Custom Data (Bot.run)

When chaining commands with [Bot.run](../bot-instance/running-commands.md):

```javascript
// In /start
Bot.run('/onboard', { step: 1, name: user.first_name })

// In /onboard
let step = options.step    // 1
let name = options.name    // user's first name
```

## API Callback Result

When a command runs as the callback of an [Api](../api-instance/index.md) call, `options` contains the Telegram API response:

```json
{
  "ok": true,
  "result": {
    "message_id": 42,
    "chat": { "id": 123 },
    "text": "Hello!"
  }
}
```

```javascript
if (options.ok) {
  let messageId = options.result.message_id
}
```

## Webhook Merge

In webhook commands, `options` may combine custom options with HTTP metadata from the incoming request.

## `options` vs `tbl_options`

| Variable | Purpose |
| --- | --- |
| `options` | General context — `Bot.run` payloads, API results, webhook merge |
| `tbl_options` | Explicitly passed via `tbl_options` in HTTP/API callback options |

See [tbl_options](tbl_options.md) when you need to pass your own data through HTTP or API callbacks.

## Important Notes

- `options` is `null` when nothing was passed
- It exists only during command execution
- For long-lived state, use [`db.user`](../db-instance/user.md) or [`db.bot`](../db-instance/bot.md)
