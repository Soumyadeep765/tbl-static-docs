# JSON, Text & XML

Send structured or plain-text HTTP bodies with `json()`, `text()`, `xml()`, or the generic `send()`.

---

## `json(obj)`

Sets `Content-Type: application/json` and sends JSON.

```js
res.json({
  status: "success",
  user: user?.id ?? null,
  count: items.length
})
```

**String passthrough** — if you pass a string, it is sent as-is (useful for pre-serialized JSON):

```js
res.json('{"ok":true}')
```

**Serialization errors** — if `JSON.stringify` fails, `res` returns **500** with:

```json
{ "error": "JSON serialization failed", "message": "..." }
```

---

## `text(content)`

Sets `Content-Type: text/plain` and sends plain text.

```js
res.text("Hello, world!")
```

If the string contains EJS tags (`<%`), it is rendered first:

```js
res.text("Hello <%= bot.username %>, request from <%= request.ip %>")
```

---

## `xml(content)`

Sets `Content-Type: application/xml` and sends the body unchanged.

```js
res.xml('<?xml version="1.0"?><response><status>ok</status></response>')
```

---

## `send(body)`

Generic send method. Uses whatever `Content-Type` you set with `set()`, or auto-detects HTML when the body looks like HTML.

```js
res.send("raw body")

res.set("Content-Type", "application/octet-stream").send(binaryData)
```

For HTML bodies, `send()` applies the same HTML access protection as `html()`. Prefer `html()` or `json()` when the content type is known.

---

## Examples

### JSON API with validation

```js
let id = params.id
if (!id) {
  return res.status(400).json({ error: "id required" })
}

let record = await db.bot.get("records:" + id)
res.json({ ok: true, record })
```

### Plain-text health check

```js
res.text("ok")
```

### XML feed snippet

```js
let items = await db.bot.get("feed") || []
let xml = '<?xml version="1.0"?><rss><channel>'
for (let item of items) {
  xml += `<item><title>${item.title}</title></item>`
}
xml += "</channel></rss>"
res.xml(xml)
```

---

## See also

- [HTML & EJS](html-and-ejs.md) — templated HTML responses
- [res.render()](render.md) — serve another command (e.g. `api.json`)
- [Headers & Status](headers-and-status.md)
