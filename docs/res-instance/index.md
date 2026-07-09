# HTTP Responses (res)

Your webhook and webapp's voice — send JSON, HTML, redirects, and rendered templates back to whoever called your endpoint.

Once you call `res`, the response goes out and command execution ends. Choose wisely.

---

## What is `res`?

The **`res`** instance sends custom HTTP responses from **webhook** and **webapp** commands. Use it to build JSON APIs, HTML pages, redirects, and rendered templates.

| You get | You skip |
| --- | --- |
| Chainable methods (`res.status().json()`) | Manual header management |
| EJS templates built in | Separate templating setup |
| Auto-detected content types | Guessing MIME types |

Once a response is sent, command execution ends.

---

## How to use it

Drop this in a webhook or webapp command's **Logic** field:

```js
res.status(200).json({ ok: true, data: result })
```

Three things worth knowing upfront:

1. **`res` is only available in webhook and webapp commands** — it's `null` in normal Telegram commands.
2. **Methods chain** — `res.status(201).set("Cache-Control", "no-store").json({ ... })`.
3. **No `res` call?** The platform returns `{ "status": "success" }` with HTTP 200.

!!! tip "New to TBL?"
    `request` and `params` carry incoming HTTP data in webhook/webapp commands. Quick intro: [Learning TBL](../learning-tbl.md). Endpoint setup: [Webhooks](../webhook-instance/index.md) · [Webapps](../webapp-instance/index.md).

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

Public web pages do not run the command sandbox, so there is no `res` object. See [Public Web](../webapp-instance/public-web.md).

---

## Try it — copy-paste examples

Start simple. Each example only introduces what it needs.

### JSON API response

```js
res.json({ ok: true, message: "Hello from your bot API" })
```

### HTML page

```js
res.html("<h1>Dashboard</h1><p>Welcome!</p>")
```

### Chain status and headers

```js
res
  .status(201)
  .set("Cache-Control", "no-store")
  .json({ created: true, id: newId })
```

### Redirect (HTTPS only)

```js
res.redirect("https://example.com/done")
```

### Render another command as the response

```js
res.render("template.html", { data: { title: "My Page", items: [] } })
```

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
