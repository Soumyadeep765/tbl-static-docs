# The `update` Variable

In TBL, `update` is the **full update object** that triggered the current command. For Telegram commands it matches the [Telegram Update](https://core.telegram.org/bots/api#update) payload. For webhooks and webapps, TBL builds a synthetic update object.

## TBL-Added Fields

In addition to standard Telegram fields, TBL enriches `update` with:

| Field | Type | Description |
| --- | --- | --- |
| `user` | `Object \| null` | Resolved user (same as the `user` global) |
| `chat` | `Object \| null` | Resolved chat (same as the `chat` global) |
| `update_type` | `string` | Update type string (same as the `update_type` global) |

## Webhook / Webapp Fields

Synthetic updates for HTTP-triggered commands may also include:

| Field | Description |
| --- | --- |
| `web_request` | HTTP request wrapper with `request`, `from`, and `chat` |
| `webhook` | `true` when triggered via webhook |
| `web` | `true` for web-triggered commands |
| `webapp` | `true` for webapp-triggered commands |

## Usage

```javascript
// Access the raw Telegram message object
let photos = update.message?.photo

// Check update type from the object itself
if (update.callback_query) {
  let callbackData = update.callback_query.data
}

// Webhook: detect HTTP context
if (update.webhook) {
  let ip = update.web_request.request.ip
}
```

## Important Notes

- `update` is read-only and frozen — you cannot modify it
- It exists only during the current command execution
- For most bots, the convenience globals (`user`, `chat`, `request`, `message`) are easier than reading `update` directly
- See the [Telegram Bot API Update object](https://core.telegram.org/bots/api#update) for the full field reference
