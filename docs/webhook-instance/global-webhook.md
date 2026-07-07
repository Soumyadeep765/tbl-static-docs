# Global Webhooks

Signed URLs that run commands **without binding a Telegram user**. `user` and `chat` are `null`; the `User` instance is not available.

Think of them as system-level triggers — cron jobs, monitoring hooks, account-wide reads, and backend integrations that don't act on behalf of one person.

---

## What you get (and don't)

| In the command | Available? |
| --- | --- |
| `bot`, `owner`, `plan`, `db`, `HTTP`, `modules` | ✓ |
| `user`, `chat`, `User` | `null` |
| `request`, `params`, `options`, `res` | ✓ |
| `msg` | `null` |

!!! warning "No default chat"
    Without `user` or `chat`, you must pass `chat_id` explicitly to `Api.sendMessage()` and friends.

---

## `getGlobalUrl(command, { options, redirect, params, expiresIn })`

| Parameter | Type | Description |
| --- | --- | --- |
| `command` | string | Command name or alias |
| `options` | object | Signed data passed to the command |
| `redirect` | string | Optional HTTPS URL — prefetched into [`content`](../globals/content.md) |
| `params` | object | Extra query parameters |
| `expiresIn` | number | Optional seconds until URL expires |

### Example — cron stats job

```js
let statsUrl = Webhook.getGlobalUrl("aggregateStats", {
  options: { days: 30 },
  redirect: "https://api.example.com/metrics.json",
  params: { ref: "cron" },
  expiresIn: 300
})
```

---

## What the URL looks like

```
https://{domain}/webhook/{bot_id}
  ?command=aggregateStats
  &options=%7B%22days%22%3A30%7D
  &sig=d4e5f6...
  &expires=1710000300
  &ref=cron
```

Note: there is **no** `user` parameter. The signature is computed with an empty user segment.

---

## Inside the command

Design for `user` being `null`:

```js
let total = await db.bot.get("total_users") || 0

// content may hold prefetched redirect body
let external = content || {}

res.json({
  ok: true,
  total_users: total,
  external_keys: Object.keys(external)
})
```

---

## Sending Telegram messages

No `chat`? Store an admin chat ID in bot storage, or pass one you know:

```js
let adminChat = await db.bot.get("admin_chat_id")
if (adminChat) {
  await Api.sendMessage({
    chat_id: adminChat,
    text: "Daily stats job completed."
  })
}
```

---

## Global vs user webhook — quick picker

| Scenario | Use |
| --- | --- |
| Action for one logged-in user | [User webhook](user-webhook.md) |
| Nightly stats aggregation | Global webhook |
| User-specific payment callback | User webhook with `getUrlFor` |
| Signed public API, no user data | Global webhook |
| Unsigned browser-facing API | [Webapp](../webapp-instance/index.md) |
| Static landing page | [Public web](../webapp-instance/public-web.md) |

---

## See also

- [Webhook Types](webhook-types.md)
- [Handling Requests](handle-webhook.md)
- [Limits & Security](limits-and-security.md)
