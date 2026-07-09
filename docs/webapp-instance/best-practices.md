# Webapp Best Practices

Guidelines for picking the right surface — webapp, public web, or webhook — and building endpoints that won't embarrass you in production.

---

## Choose the right surface

| Need | Use |
| --- | --- |
| Static landing page, CSS, JS | [Public web](public-web.md) (`is_web=1`) |
| Dynamic API with `db` / `HTTP` | Webapp |
| Per-user signed action | [User webhook](../webhook-instance/user-webhook.md) |
| Cron / system signed job | [Global webhook](../webhook-instance/global-webhook.md) |

Three rules of thumb:

1. **Public web when static is enough** — faster, no sandbox overhead.
2. **Webapp when you need `db` or `res`** — but remember URLs are unsigned.
3. **Webhook when you need `user` or signing** — per-user actions and tamper-proof links.

---

## URL hygiene

- Put tracking and locale in `params`: `?ref=home&lang=en`
- Put structured config in `options` (single JSON blob)
- Never put API keys, tokens, or passwords in URLs
- Use `expiresIn` on webhooks for one-time sensitive links

URLs end up in browser history, server logs, and referrer headers. Treat them as public.

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

## See also

- [Webapp Methods](webapp-methods.md)
- [Public Web](public-web.md)
- [Examples](examples.md)
