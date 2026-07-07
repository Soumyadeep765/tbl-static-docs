# Webhook Types

TBL supports two signed webhook modes. Both use the same per-bot route (`/webhook/{bot_id}`) but differ in whether a Telegram user is bound to the request.

---

## User-based webhook

A **user webhook** runs a command **as a specific Telegram user**.

| Field | Value |
| --- | --- |
| URL includes | `user={telegramUserId}` |
| `update.webhook` | `true` |
| `update.web` | `false` |
| `user` / `chat` | Loaded from database and enriched |
| `User` instance | Available |

**Use when:**

- A website action should run on behalf of a logged-in user
- You need `user`, `chat`, or per-user `db.user` data
- The link is personalized (upgrade flow, sync, account settings)

**Generate with:**

```js
Webhook.getUrl("myCommand")           // current user
Webhook.getUrlFor({ user_id: 123, command: "myCommand" })
```

---

## Global webhook

A **global webhook** runs a command **without any user context**.

| Field | Value |
| --- | --- |
| URL omits | `user` parameter |
| `update.globalWebhook` | `true` |
| `update.web` | `true` |
| `user` / `chat` | `null` |
| `User` instance | `null` |

**Use when:**

- Cron jobs or backend services trigger bot logic
- Public read-only APIs (still signed, but no user)
- Account-level operations that do not target one user

**Generate with:**

```js
Webhook.getGlobalUrl("getStats", { options: { days: 30 } })
```

!!! warning
    In global webhooks, `Api.sendMessage()` and `Bot` helpers need an explicit `chat_id` — there is no default user chat.

---

## Comparison

| | User webhook | Global webhook |
| --- | --- | --- |
| Signature | Required | Required |
| `user` in command | Yes | `null` |
| `User.set()` / `User.get()` | Yes | No default user |
| `update.webhook` flag | `true` | `false` |
| `update.web` flag | `false` | `true` |
| Depth limit | Yes | Yes |
| Typical source | User dashboard, email link | Cron, monitoring, admin panel |

---

## Not the same as Webapp or Public Web

| | Webhook (both types) | Webapp | Public web |
| --- | --- | --- | --- |
| Signed | Yes | No | No |
| Runs sandbox | Yes | Yes | No |
| `res` | Yes | Yes | No |

Webapps and public web are documented under [Webapps](../webapp-instance/index.md).

---

## See also

- [User-Based Webhooks](user-webhook.md)
- [Global Webhooks](global-webhook.md)
- [Limits & Security](limits-and-security.md)
