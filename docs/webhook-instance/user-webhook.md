# User-Based Webhooks

Signed URLs that run a command **as a specific Telegram user**. Inside the command, `user`, `chat`, and the `User` instance are all there — just like a normal message handler, except the caller is an HTTP client instead of Telegram.

---

## What you get

| In the command | Available? |
| --- | --- |
| `user`, `chat` | ✓ |
| `User.get()` / `User.set()` | ✓ (deprecated — prefer `db.user`) |
| `db.user` | ✓ — scoped to the webhook user |
| `request`, `params`, `options` | ✓ |
| `res` | ✓ |

Three things worth knowing upfront:

1. **`getUrl()` is for the current user** — the one whose update triggered the command you're running now.
2. **`getUrlFor()` targets any user ID** — use this from admin commands or backend jobs.
3. **`redirect` only works on `getUrlFor()` and `getGlobalUrl()`** — not on plain `getUrl()`.

---

## `getUrl(command, { options, params, expiresIn })`

Creates a webhook URL for the **current user** — whoever triggered the command you're writing (e.g. a `/share` command in Telegram).

| Parameter | Type | Description |
| --- | --- | --- |
| `command` | string | Command name or alias to run |
| `options` | object | Data passed to the command (signed) |
| `params` | object | Extra query parameters (visible in URL) |
| `expiresIn` | number | Optional seconds until URL expires |

`redirect` is **not** supported here. Use [`getUrlFor()`](#geturlfor-user_id-command-redirect-options-params-expiresin) or [`getGlobalUrl`](global-webhook.md) if you need redirect prefetch.

### Example — share a sync link

```js
let syncUrl = Webhook.getUrl("syncGameData", {
  options: { level: 10 },
  params: { ref: "profile", lang: "en" },
  expiresIn: 3600
})

await Api.sendMessage({
  chat_id: chat.id,
  text: "Sync your data: " + syncUrl
})
```

---

## `getUrlFor({ user_id, command, redirect, options, params, expiresIn })`

Creates a webhook URL for a **specific user ID**. Use when you know the target user but they didn't trigger the current command — admin panels, email links, backend jobs.

| Parameter | Type | Description |
| --- | --- | --- |
| `user_id` | number | Target Telegram user ID |
| `command` | string | Command to execute |
| `redirect` | string | Optional HTTPS URL — prefetched into [`content`](../globals/content.md) |
| `options` | object | Signed options object |
| `params` | object | Extra query parameters |
| `expiresIn` | number | Optional expiry in seconds |

### Example — admin-generated upgrade link

```js
let upgradeUrl = Webhook.getUrlFor({
  user_id: 123456789,
  command: "applyUpgrade",
  redirect: "https://api.example.com/plan-status",
  options: { plan: "pro" },
  params: { ref: "email" },
  expiresIn: 600
})
```

When the webhook fires, the platform fetches `redirect` (HTTPS only) and exposes the response body as the global `content` variable before your command runs.

---

## What the URL looks like

```
https://{domain}/webhook/{bot_id}
  ?command=syncGameData
  &options=%7B%22level%22%3A10%7D
  &sig=a1b2c3...
  &user=987654321
  &expires=1710000000
  &ref=profile
  &lang=en
```

- Changing `command`, `options`, `user`, or `expires` invalidates `sig`
- Expired URLs (when `expires` is set) return **403**

---

## Inside the command

```js
// user and chat are populated — use them freely
let name = user.first_name
let saved = await db.user.get("progress", 0)

// Read HTTP details
let ref = params.ref || request.query.ref
let ip = request.ip

// Respond to the HTTP caller
res.json({
  ok: true,
  user_id: user.id,
  progress: saved,
  ref
})
```

---

## Sending Telegram messages

User webhooks have user context, but there is still no `msg` helper. Use `Api` with explicit IDs or resolve chat from `chat`:

```js
await Api.sendMessage({
  chat_id: chat.id,
  text: "Webhook processed for " + user.first_name
})
```

---

## See also

- [Webhook Types](webhook-types.md)
- [Handling Requests](handle-webhook.md)
- [HTTP Responses (res)](../res-instance/index.md)
