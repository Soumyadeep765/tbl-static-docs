# Headers & Status

Control HTTP status codes and response headers before sending the body.

---

## `set(key, value)`

Sets a response header. Headers can be chained.

```js
res
  .set("Content-Type", "application/json")
  .set("Cache-Control", "no-cache")
  .set("X-Request-Id", String(Date.now()))
```

`set()` applies headers to the outgoing HTTP response.

---

## `status(code)`

Sets the HTTP status code. Default is **200**.

```js
res.status(404).json({ error: "Not found" })
res.status(201).json({ created: true })
res.status(500).text("Internal error")
```

Chain `status()` before any body method:

```js
res.status(403).json({ error: "Forbidden" })
```

---

## `end()`

Returns the stored response state. Most commands should use `json()`, `html()`, or another send method directly — you rarely need `end()`.

Possible return shapes:

| Situation | Return value |
| --- | --- |
| Response already sent | `{ sent: true }` |
| Redirect stored | `{ redirect: "https://..." }` |
| Body stored | `{ __response: { status, headers, body } }` |
| Nothing sent yet | `{ __response: { status: 200, headers: {}, body: null } }` |

In normal webhook and webapp commands you rarely need `end()` — the platform calls it automatically after your script finishes.

---

## Common patterns

### CORS for a JSON API

```js
res
  .status(200)
  .set("Access-Control-Allow-Origin", "*")
  .set("Access-Control-Allow-Methods", "GET, POST")
  .json({ data: payload })
```

### Custom content type with `send()`

```js
res
  .status(200)
  .set("Content-Type", "text/csv")
  .send("id,name\n1,Alice\n2,Bob")
```

### Error response

```js
if (!params.id) {
  return res.status(400).json({
    error: "Missing id",
    message: "Pass ?id= in the query string"
  })
}
```

---

## See also

- [JSON, Text & XML](send-json-text-xml.md)
- [Defaults & Protection](defaults-and-protection.md)
