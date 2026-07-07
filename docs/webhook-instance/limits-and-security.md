# Limits & Security

Webhooks are signed and rate-limited. This page covers security mechanics and plan-based quotas.

---

## Signature verification

Every webhook request must include a valid `sig` query parameter.

**Algorithm:** HMAC-SHA256 with your bot token as the key.

**Payload format:**

```
{userId}:{command}:{JSON.stringify(options)}[:{expires}]
```

- User webhook: `userId` is the Telegram user ID
- Global webhook: `userId` is empty (`""`)
- Legacy signatures without `expires` are still accepted for backward compatibility

Invalid or missing signatures return **401** / **403** before your command executes.

---

## URL expiry

Pass `expiresIn` (seconds) when generating URLs:

```js
Webhook.getUrl("action", { expiresIn: 3600 })  // valid 1 hour
```

The URL includes `expires={unixTimestamp}`. Requests after that time are rejected.

---

## Payload size limits

| Field | Max encoded length |
| --- | --- |
| `options` | 5,000 characters |
| `params` | 10,000 characters |
| Request body | 1 MB (platform default) |

Oversized payloads return **413**.

---

## Webhook depth limit

User and global webhooks enforce a **chain depth limit** (default **10**, configurable via `TBH_MAX_CHAIN_DEPTH`). This prevents runaway nested webhook calls.

Webapp requests are **not** subject to this depth check.

---

## Plan-based rate limits

Each bot is limited by the owner's plan:

| Plan | Per minute | Per day |
| --- | --- | --- |
| FREE | 15 | 5,000 |
| FREEMIUM | 30 | 5,000 |
| PREMIUM | 60 | 10,000 |
| ELITE | 120 | 20,000 |

Exceeded limits return **429**:

```json
{
  "status": "error",
  "message": "Rate limit exceeded: Too many requests per minute"
}
```

(or daily quota message)

These limits apply to **webhooks**, **webapps**, and **public web** combined per bot.

---

## Redirect prefetch limits

When `redirect` is set on `getUrlFor` or `getGlobalUrl`:

- URL must be **HTTPS**
- Fetch timeout: **5 seconds**
- Response size cap applies (platform-enforced)

Prefetched content is exposed as the global [`content`](../globals/content.md) variable.

---

## `res.redirect()` security

Response redirects via `res.redirect()` accept **HTTPS URLs only**. See [Redirects](../res-instance/redirect.md).

---

## Best practices

- Use `expiresIn` for sensitive one-time links
- Keep secrets in `options` (signed), not unsigned `params`
- Use user webhooks for per-user mutations; global webhooks for system reads
- Return explicit `res.json()` errors instead of relying on the default success body
- For unsigned browser endpoints, use [Webapps](../webapp-instance/index.md) only when signing is not required

---

## See also

- [User-Based Webhooks](user-webhook.md)
- [Global Webhooks](global-webhook.md)
- [Public Web](../webapp-instance/public-web.md)
