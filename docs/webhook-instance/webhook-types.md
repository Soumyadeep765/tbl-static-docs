# Webhook Types

Two flavors of signed webhook, one URL pattern. Both hit `/webhook/{bot_id}` — the difference is whether a Telegram user rides along for the trip.

---

## What are the two types?

| | User webhook | Global webhook |
| --- | --- | --- |
| **Who it's for** | One specific Telegram user | Nobody in particular |
| **`user` in URL** | `?user={telegramUserId}` | Omitted |
| **`user` / `chat` in command** | Loaded and enriched | `null` |
| **`User` instance** | Available | `null` |
| **`update.webhook`** | `true` | `false` |
| **`update.web`** | `false` | `true` |

Both require a valid signature. Both respect depth limits. Both run your command in the full sandbox.

---

## User-based webhook

A **user webhook** runs a command **as a specific Telegram user** — the same `user`, `chat`, and `User` you'd get from a normal message.

**Reach for this when:**

- A website action should run on behalf of a logged-in user
- You need `user`, `chat`, or per-user `db.user` data
- The link is personalized (upgrade flow, sync, account settings)

**Generate with:**

```js
Webhook.getUrl("myCommand")           // current user
Webhook.getUrlFor({ user_id: 123, command: "myCommand" })
```

Full guide: [User-Based Webhooks](user-webhook.md)

---

## Global webhook

A **global webhook** runs a command **without any user context**. `user` and `chat` are `null`; the `User` instance is not available.

**Reach for this when:**

- Cron jobs or backend services trigger bot logic
- Public read-only APIs (still signed, but no user)
- Account-level operations that do not target one user

**Generate with:**

```js
Webhook.getGlobalUrl("getStats", { options: { days: 30 } })
```

!!! warning "No default chat"
    In global webhooks, `Api.sendMessage()` and `Bot` helpers need an explicit `chat_id` — there is no default user chat to fall back on.

Full guide: [Global Webhooks](global-webhook.md)

---

## Still not sure?

| Scenario | Pick |
| --- | --- |
| "Sync this user's game progress" | User webhook |
| "Run nightly stats for the whole bot" | Global webhook |
| "Payment callback for user #123" | User webhook via `getUrlFor` |
| "Signed API, no user data needed" | Global webhook |
| "Anyone can hit this from a browser" | [Webapp](../webapp-instance/index.md) (unsigned) |
| "Static landing page" | [Public web](../webapp-instance/public-web.md) |

---

## Not the same as Webapp or Public Web

Webhooks always run signed and sandboxed. Webapps and public web are a different story:

| | Webhook (both types) | Webapp | Public web |
| --- | --- | --- | --- |
| Signed | Yes | No | No |
| Runs sandbox | Yes | Yes | No |
| `res` | Yes | Yes | No |

Webapps and public web: [Webapps](../webapp-instance/index.md).

---

## See also

- [User-Based Webhooks](user-webhook.md)
- [Global Webhooks](global-webhook.md)
- [Limits & Security](limits-and-security.md)
