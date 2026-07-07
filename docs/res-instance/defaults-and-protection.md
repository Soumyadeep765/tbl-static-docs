# Defaults & Protection

How `res` behaves when you send nothing, how HTML pages are protected, and what gets injected automatically. The safety net under every webhook and webapp response.

---

## Default response

If your webhook or webapp command **does not** call any `res` send method, the platform returns:

```json
{ "status": "success" }
```

with HTTP status **200**.

Fine for fire-and-forget cron triggers. Not fine when your caller parses the body — use explicit `res.json()` or `res.html()`.

---

## Sending ends execution

Once `res.json()`, `res.html()`, `res.send()`, `res.redirect()`, or `res.render()` delivers a response, **no further code output is processed** for that request. Treat response calls as `return` points.

```js
res.json({ ok: true })
// Code below still runs in JavaScript — but the HTTP response is already sent.
// Don't send twice.
```

---

## HTML age-gate protection

HTML responses (`.html` commands, `res.html()`, `res.render()` on HTML) may show a **verification warning page** before the real content when:

- HTML protection is enabled (default)
- The visitor has not passed verification

Visitors verify via a cookie (`tbh_verified`) or header (`x-tbh-verified`). After verification, the actual page is served.

This applies to:

- `res.html()`, `res.renderEJS()`, `res.render()` on HTML commands
- [Public web](../webapp-instance/public-web.md) HTML commands

---

## Automatic HTML injection

For HTML content, the platform injects:

| Injection | Purpose |
| --- | --- |
| `<base href="...">` | Correct relative asset paths per bot (`/webapp/{bot_id}/` or `/public/{bot_id}/`) |
| `<meta name="tbh-bot-id" content="...">` | Bot identification |
| Attribution comment | TeleBotHost hosting notice |

Injection runs once per response. `res.html()` and `res.render()` on HTML commands include it automatically.

---

## Unknown methods

`res` is wrapped in a proxy. Calling an undefined method name returns **404 JSON**:

```json
{
  "error": "Method not found",
  "message": "Method \"foo\" is not supported"
}
```

Stick to documented methods: `set`, `status`, `send`, `json`, `html`, `xml`, `text`, `redirect`, `render`, `renderEJS`, `end`.

---

## Redirect rules

`res.redirect()` accepts **HTTPS URLs only**. Invalid URLs return **400 JSON**. See [Redirects](redirect.md).

---

## JSON errors

| Situation | Status | Body |
| --- | --- | --- |
| `JSON.stringify` fails in `json()` | 500 | `{ error: "JSON serialization failed", ... }` |
| Invalid redirect URL | 400 | `{ error: "Invalid redirect", ... }` |
| Unknown `res` method | 404 | `{ error: "Method not found", ... }` |
| `render()` command missing | 404 | `{ error: "Command not found", ... }` |

---

## See also

- [Overview](index.md)
- [Public Web](../webapp-instance/public-web.md) — static serving without `res`
- [Limits & Security](../webhook-instance/limits-and-security.md) — rate limits and payload sizes
