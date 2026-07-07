# HTTP Responses (res)

The **`res`** instance sends custom HTTP responses from **webhook** and **webapp** commands. Use it to build JSON APIs, HTML pages, redirects, and rendered templates.

```js
res.status(200).json({ ok: true, data: result })
```

Once a response is sent, command execution ends.

---

## When `res` is available

| Context | `res` |
| --- | --- |
| User webhook | Available |
| Global webhook | Available |
| Webapp command | Available |
| Public web (`/public/...`) | **Not available** — raw command code is served directly |
| Telegram message commands | `null` |
| Broadcast commands | `null` |

Public web pages do not run the TBL sandbox, so there is no `res` object. See [Public Web](../webapp-instance/public-web.md).

---

## Method overview

| Method | Purpose | Chains? |
| --- | --- | --- |
| [`set(key, value)`](headers-and-status.md#setkey-value) | Set response headers | Yes |
| [`status(code)`](headers-and-status.md#statuscode) | Set HTTP status (default **200**) | Yes |
| [`send(body)`](send-json-text-xml.md#sendbody) | Send any body (auto-detects HTML) | Yes |
| [`json(obj)`](send-json-text-xml.md#jsonobj) | Send `application/json` | Yes |
| [`text(content)`](send-json-text-xml.md#textcontent) | Send `text/plain` (EJS if `<%` present) | Yes |
| [`xml(content)`](send-json-text-xml.md#xmlcontent) | Send `application/xml` | Yes |
| [`html(content)`](html-and-ejs.md#htmlcontent) | Send `text/html` with EJS + injection | Yes |
| [`redirect(url)`](redirect.md) | HTTPS redirect only | Yes |
| [`render(path, options)`](render.md) | Render another command as the response | Yes |
| [`renderEJS(template, data)`](html-and-ejs.md#renderejstemplate-data) | Explicit EJS → HTML | Yes |
| [`end()`](headers-and-status.md#end) | Return stored response state (advanced) | No |

Unknown method names (via chaining proxy) return **404 JSON**.

---

## Method chaining

All response methods except `end()` return `res`, so you can chain:

```js
res
  .status(201)
  .set("Cache-Control", "no-store")
  .json({ created: true, id: newId })
```

---

## Default response

If your command finishes **without** calling `res`, the platform returns:

```json
{ "status": "success" }
```

with HTTP **200**. See [Defaults & Protection](defaults-and-protection.md).

---

## Choosing a method

| Goal | Method |
| --- | --- |
| REST / API JSON | `res.json()` |
| Plain text or logs | `res.text()` |
| Full HTML page | `res.html()` or `res.render("page.html")` |
| Reuse another command's code | `res.render("template.html", { data: { ... } })` |
| Send user elsewhere | `res.redirect("https://example.com/done")` |
| Custom headers / status | `res.set()` + `res.status()` + `res.send()` |

---

## Pages in this section

- [Headers & Status](headers-and-status.md) — `set()`, `status()`, `end()`
- [JSON, Text & XML](send-json-text-xml.md) — `send()`, `json()`, `text()`, `xml()`
- [HTML & EJS](html-and-ejs.md) — `html()`, `renderEJS()`, template syntax
- [Redirects](redirect.md) — `redirect()` rules
- [res.render()](render.md) — render commands, content types, data passing
- [Defaults & Protection](defaults-and-protection.md) — fallbacks, HTML age-gate, injection

---

## Related

- [Webhooks](../webhook-instance/index.md) — signed HTTP endpoints
- [Webapps](../webapp-instance/index.md) — unsigned dynamic endpoints
- [Public Web](../webapp-instance/public-web.md) — static `is_web` pages (no `res`)
- [`request`](../globals/request.md) — incoming HTTP data in webhook/webapp commands
