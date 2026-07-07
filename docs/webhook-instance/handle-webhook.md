# Handling Webhook Requests

When someone hits a webhook URL, your command runs in a **web context** — with an HTTP `request` object instead of a Telegram `update` payload.

Same sandbox, different front door.

---

## The `request` object

Your command gets a snapshot of the incoming HTTP call:

| Field | Type | Description |
| --- | --- | --- |
| `url` | string | Full request URL |
| `method` | string | `GET`, `POST`, etc. |
| `headers` | object | Request headers |
| `ip` | string | Client IP (from `x-forwarded-for` or socket) |
| `query` | object | Query string parameters |
| `body` | object \| null | POST body (when method is POST) |

### Example — guard by method

```js
let method = request.method
let ip = request.ip
let ref = params.ref || request.query.ref

if (method !== "GET") {
  return res.status(405).json({ error: "GET only" })
}
```

Typical `request.query` for a user webhook:

```json
{
  "command": "syncGameData",
  "options": "{\"level\":10}",
  "sig": "...",
  "user": "987654321",
  "ref": "profile",
  "lang": "en"
}
```

Parsed `options` are also available on the global [`options`](../globals/options.md) object. Custom URL params appear in [`params`](../globals/params.md).

---

## `options` and `params`

Two globals, two jobs:

| Global | Source |
| --- | --- |
| `options` | Decoded `options` query/body field + request metadata |
| `params` | Custom query keys (excluding `command`, `sig`, `user`, etc.) or decoded `params` field |

```js
let level = options.level        // from signed options JSON
let lang = params.lang           // from ?lang=en
```

Put secrets and tamper-sensitive data in `options` (signed). Put marketing tags and filters in `params` (visible in the URL).

---

## What's available in webhooks

| Global / Instance | User webhook | Global webhook |
| --- | --- | --- |
| `bot`, `owner`, `plan` | ✓ | ✓ |
| `user`, `chat` | ✓ | `null` |
| `User` | ✓ | `null` |
| `res` | ✓ | ✓ |
| `Api`, `Bot`, `db`, `HTTP` | ✓ | ✓ |
| `modules`, `Libs` | ✓ | ✓ |
| `Webhook`, `Webapp` | ✓ | ✓ |
| `request`, `params`, `options` | ✓ | ✓ |
| `content` | ✓ (if `redirect` prefetch) | ✓ |
| `msg` | `null` | `null` |
| Platform utilities | `null` | `null` |

`msg` only exists when Telegram sends a message update — webhooks don't have one. **Platform utilities** (internal helpers tied to Telegram message context) are likewise unavailable here.

---

## Telegram vs webhook data

| Source | Data location |
| --- | --- |
| Telegram message | `update`, `message`, `user`, `msg` |
| Webhook / webapp | `request`, `params`, `options` |

Do not expect `message` or `msg` in webhook commands. If your logic branches on update type, check `request` instead.

---

## Sending Telegram messages

**User webhooks** — `chat.id` is right there:

```js
await Api.sendMessage({
  chat_id: chat.id,
  text: "Done!"
})
```

**Global webhooks** — you're on your own for `chat_id`:

```js
await Api.sendMessage({
  chat_id: 123456789,
  text: "Cron job finished."
})
```

---

## Command aliases

Webhooks resolve command names through the same alias system as Telegram commands. The `command` query value can be a primary name or any registered alias.

---

## Errors before your command runs

The platform may reject a request before your Logic field executes:

| Status | Reason |
| --- | --- |
| 400 | Missing `command` |
| 401 | Missing `sig` |
| 403 | Invalid signature, expired URL, or bot blocked |
| 404 | Bot not found / inactive |
| 413 | `options` or `params` payload too large |
| 429 | Rate limit exceeded |

Your command can return its own errors via [`res`](../res-instance/index.md).

---

## See also

- [`request`](../globals/request.md)
- [`params`](../globals/params.md)
- [Limits & Security](limits-and-security.md)
- [Sending Responses](sending-webhook-response.md)
