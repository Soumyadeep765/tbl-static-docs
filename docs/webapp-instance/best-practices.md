# Webapp Best Practices

Guidelines for choosing between webapp, public web, and webhooks — and building safe public endpoints.

---

## Choose the right surface

| Need | Use |
| --- | --- |
| Static landing page, CSS, JS | [Public web](public-web.md) (`is_web=1`) |
| Dynamic API with `db` / `HTTP` | Webapp |
| Per-user signed action | [User webhook](../webhook-instance/user-webhook.md) |
| Cron / system signed job | [Global webhook](../webhook-instance/global-webhook.md) |

Do not use a webapp when public web is enough — public web is faster and cheaper (no sandbox).

Do not use a webapp when you need `user` — use a webhook.

---

## URL hygiene

- Put tracking and locale in `params`: `?ref=home&lang=en`
- Put structured config in `options` (single JSON blob)
- Never put API keys, tokens, or passwords in URLs
- Use `expiresIn` on webhooks for one-time sensitive links

---

## Security

- Webapp URLs are **unsigned** — anyone can call them
- Validate input from `params` and `request.body` inside your command
- Implement your own auth (API key in header, HMAC body, session token) for admin endpoints
- Do not rely on obscurity — command names are guessable

```js
let key = request.headers["x-api-key"]
if (key !== await db.bot.get("admin_api_key")) {
  return res.status(401).json({ error: "Unauthorized" })
}
```

---

## Public web checklist

Before marking a command `is_web = 1`:

- [ ] No secrets in the source file
- [ ] No `Api`, `db`, or server logic expected (they will not run)
- [ ] Assets use relative paths (respect injected `<base href>`)
- [ ] EJS only uses `bot`, `params`, `request` — not `user`

---

## Responses

- Always return explicit `res.json()` for APIs — do not rely on `{ "status": "success" }`
- Set CORS headers when browsers call your webapp from another origin
- Use `res.render()` to keep HTML templates as separate commands

---

## Rate limits

Webapps share per-bot limits with webhooks and public web. Cache expensive `db` reads and avoid tight polling loops from the client.

See [Limits & Security](../webhook-instance/limits-and-security.md).

---

## Related

- [Webapp Methods](webapp-methods.md)
- [Public Web](public-web.md)
- [Examples](examples.md)
