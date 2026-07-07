# Sending Webhook Responses

Webhooks are HTTP endpoints — callers expect a body, not silence. Use the [`res`](../res-instance/index.md) instance to control exactly what goes back.

---

## Quick start

```js
res.json({ ok: true, processed: true })
```

The response is sent immediately and command execution stops. Treat every `res.*()` send call like a `return`.

---

## Default behavior

If you do not call `res`, the platform returns:

```json
{ "status": "success" }
```

with HTTP **200**. Fine for fire-and-forget triggers. Bad for API integrations that parse the response body — use explicit `res.json()` so callers get predictable output.

---

## Common patterns

### JSON API

```js
res.status(200).json({
  status: "success",
  data: result,
  timestamp: Date.now()
})
```

### HTML page

```js
res.render("report.html", {
  data: { rows: reportData }
})
```

### Redirect browser

```js
res.redirect("https://myapp.com/done")
```

### Error to caller

```js
if (!options.token) {
  return res.status(401).json({ error: "Unauthorized" })
}
```

---

## Full `res` reference

| Topic | Page |
| --- | --- |
| Overview & availability | [res Overview](../res-instance/index.md) |
| `set()`, `status()` | [Headers & Status](../res-instance/headers-and-status.md) |
| `json()`, `text()`, `xml()` | [JSON, Text & XML](../res-instance/send-json-text-xml.md) |
| `html()`, EJS | [HTML & EJS](../res-instance/html-and-ejs.md) |
| `redirect()` | [Redirects](../res-instance/redirect.md) |
| `render()` | [res.render()](../res-instance/render.md) |
| Defaults, HTML protection | [Defaults & Protection](../res-instance/defaults-and-protection.md) |

---

## Webapp responses

The same `res` API applies to [webapp commands](../webapp-instance/index.md). Public web pages do **not** use `res` — see [Public Web](../webapp-instance/public-web.md).

---

## See also

- [Handling Requests](handle-webhook.md)
- [res Overview](../res-instance/index.md)
