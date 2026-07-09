# Webhooks

Let the outside world poke your bot — signed HTTP URLs that trigger commands from websites, cron jobs, payment providers, or your own backend.

Every URL carries an HMAC signature tied to your bot token. Tampered requests get rejected before your command even runs.

---

## What are webhooks?

**Webhooks** are signed HTTP endpoints that trigger TeleBotHost commands from external systems — websites, cron jobs, payment providers, or your own backend.

| You get | You skip |
| --- | --- |
| Signed, tamper-proof URLs | Building your own auth layer |
| Full command sandbox (`Bot`, `Api`, `db`, `HTTP`) | Separate webhook server |
| Per-user or system-wide triggers | Polling Telegram for updates |

Each URL includes an HMAC signature tied to your bot token. Modified or forged requests are rejected before your command runs.

---

## How to use them

Generate a signed URL inside any command's **Logic** field:

```js
let syncUrl = Webhook.getUrl("syncData", {
  options: { level: 10 },
  params: { ref: "profile" }
})
```

Three things worth knowing upfront:

1. **`Webhook` is available in normal commands** — use it to generate links you send to users or external systems.
2. **User webhooks include `user` and `chat`** — global webhooks do not.
3. **Respond with [`res`](../res-instance/index.md)** — JSON, HTML, or redirects instead of the default `{ "status": "success" }`.

!!! tip "New to TBL?"
    `user`, `params`, and `options` are globals available in webhook commands. Quick intro: [Learning TBL](../learning-tbl.md). For unsigned public endpoints, see [Webapps](../webapp-instance/index.md).

---

## Webhook, webapp, or public web?

| Feature | User webhook | Global webhook | Webapp | Public web |
| --- | --- | --- | --- | --- |
| **Signed** | Yes | Yes | No | No |
| **`user` / `chat`** | Yes | `null` | `null` | N/A |
| **Runs command sandbox** | Yes | Yes | Yes | No |
| **`res` available** | Yes | Yes | Yes | No |
| **`msg` available** | No | No | No | No |
| **Depth limit** | Yes | Yes | No | N/A |
| **Best for** | Per-user actions | Cron, system APIs | Public dynamic APIs | Static `is_web` pages |

Use **webhooks** when you need signing, user context, or trusted external triggers.  
Use **webapps** for unsigned public dynamic logic.  
Use **public web** for fast static pages — see [Public Web](../webapp-instance/public-web.md).

---

## Try it — copy-paste examples

Start simple. Each example only introduces what it needs.

### Generate a user webhook URL

```js
let url = Webhook.getUrl("confirmPayment", {
  params: { orderId: "12345" },
  expiresIn: 3600  // URL expires in 1 hour
})
Bot.sendMessage(chat.id, "Confirm here: " + url)
```

### Generate a global (system) webhook

No user context — good for cron jobs:

```js
let cronUrl = Webhook.getGlobalUrl("dailySync", {
  params: { source: "cron" }
})
```

### Handle the incoming request

Inside your webhook command, read the HTTP data:

```js
let method = request.method
let body = request.body

res.json({ ok: true, received: method })
```

Incoming request shape: [`request`](../globals/request.md) · Responses: [`res`](../res-instance/index.md)

---

## HTTP route

```
GET | POST | PUT | PATCH | DELETE | OPTIONS | HEAD
/webhook/{bot_id}?command={name}&sig={hash}&...
```

All HTTP methods are accepted. Query parameters and (for POST) body fields carry `options`, `params`, and `redirect`.

---

## URL structure

```
https://{domain}/webhook/{bot_id}
  ?command={commandName}
  &options={urlEncodedJson}
  &sig={hmacSha256}
  &user={telegramUserId}      ← user webhooks only
  &expires={unixTimestamp}    ← optional
  &redirect={httpsUrl}        ← optional (getUrlFor / getGlobalUrl)
  &{customParams...}
```

- **`options`** — JSON object passed to your command (max **5,000** chars encoded)
- **`params`** — extra query key/value pairs (max **10,000** chars encoded)
- **`sig`** — required; HMAC-SHA256 of `user:command:JSON(options)[:expires]`
- **`expires`** — optional Unix timestamp; expired URLs are rejected

---

## Instance methods

| Method | Purpose |
| --- | --- |
| [`getUrl(command, opts)`](user-webhook.md#geturlcommand-options-params-expiresin) | Signed URL for **current user** |
| [`getUrlFor({ ... })`](user-webhook.md#geturlfor) | Signed URL for a **specific user** |
| [`getGlobalUrl(command, opts)`](global-webhook.md) | Signed URL with **no user** |
| `validate(...)` | Server-side signature check (advanced) |

`Webhook` is available inside webhook, webapp, and normal commands when generating links.

---

## What runs in your command

Webhook commands receive the full command sandbox except `msg`:

| Available | Not available |
| --- | --- |
| `res`, `Api`, `Bot`, `db`, `HTTP`, `modules`, `Libs` | `msg` |
| `user`, `chat`, `User` (user webhooks) | `user` in global webhooks |
| `request`, `params`, `options` | — |
| `Webhook`, `Webapp` | — |

See [Handling Requests](handle-webhook.md) for the `request` object shape.

---

## Responses

- Default: `{ "status": "success" }` with HTTP 200
- Custom: use [`res`](../res-instance/index.md) — `res.json()`, `res.html()`, etc.
- Redirect: `res.redirect("https://...")` (HTTPS only)

---

## Pages in this section

- [Webhook Types](webhook-types.md) — user vs global
- [User-Based Webhooks](user-webhook.md) — `getUrl`, `getUrlFor`
- [Global Webhooks](global-webhook.md) — `getGlobalUrl`
- [Handling Requests](handle-webhook.md) — `request`, globals, sending messages
- [Limits & Security](limits-and-security.md) — rate limits, signatures, depth
- [Sending Responses](sending-webhook-response.md) — link to `res`

---

## Related

- [Webapps](../webapp-instance/index.md)
- [HTTP Responses (res)](../res-instance/index.md)
- [`request`](../globals/request.md)
- [`params`](../globals/params.md)
