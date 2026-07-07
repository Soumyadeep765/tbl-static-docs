# Handling Webhook Requests

When a webhook URL is hit, your command runs in a web context with an HTTP **`request`** object instead of a Telegram `update` payload.

---

## The `request` object

| Field | Type | Description |
| --- | --- | --- |
| `url` | string | Full request URL |
| `method` | string | `GET`, `POST`, etc. |
| `headers` | object | Request headers |
| `ip` | string | Client IP (from `x-forwarded-for` or socket) |
| `query` | object | Query string parameters |
| `body` | object \| null | POST body (when method is POST) |

### Example

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

| Global | Source |
| --- | --- |
| `options` | Decoded `options` query/body field + request metadata |
| `params` | Custom query keys (excluding `command`, `sig`, `user`, etc.) or decoded `params` field |

```js
let level = options.level        // from signed options JSON
let lang = params.lang           // from ?lang=en
```

---

## Globals available in webhooks

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
| `msg`, `TBL` | `null` | `null` |

---

## Telegram vs webhook data

| Source | Data location |
| --- | --- |
| Telegram message | `update`, `message`, `user`, `msg` |
| Webhook / webapp | `request`, `params`, `options` |

Do not expect `message` or `msg` in webhook commands.

---

## Sending Telegram messages

**User webhooks** — use `chat.id` or `user.id`:

```js
await Api.sendMessage({
  chat_id: chat.id,
  text: "Done!"
})
```

**Global webhooks** — pass `chat_id` explicitly:

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

## Error responses from the platform

Before your command runs, the platform may return:

| Status | Reason |
| --- | --- |
| 400 | Missing `command` |
| 401 | Missing `sig` |
| 403 | Invalid signature or expired URL |
| 404 | Bot not found / inactive |
| 413 | `options` or `params` payload too large |
| 429 | Rate limit exceeded |
| 403 | Bot blocked |

Your command can return its own errors via [`res`](../res-instance/index.md).

---

## See also

- [`request`](../globals/request.md)
- [`params`](../globals/params.md)
- [Limits & Security](limits-and-security.md)
- [Sending Responses](sending-webhook-response.md)
