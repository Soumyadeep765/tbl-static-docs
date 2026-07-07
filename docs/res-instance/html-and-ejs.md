# HTML & EJS

Send HTML pages with automatic EJS rendering and platform HTML injection.

---

## `html(content)`

Sets `Content-Type: text/html`, renders EJS if needed, injects platform tags, and sends the response.

```js
res.html("<h1>Welcome</h1><p>Bot: <%= bot.username %></p>")
```

### Automatic EJS

If the string contains `<%`, it is processed as an EJS template before sending:

```js
res.html(`
  <h1>Hello <%= user?.first_name || "Guest" %></h1>
  <% if (params.debug) { %>
    <pre><%= JSON.stringify(params) %></pre>
  <% } %>
`)
```

### HTML injection

For HTML responses, the platform automatically injects:

- `<base href>` — correct asset paths for webapp or public URLs
- `<meta name="tbh-bot-id">` — bot identifier
- TeleBotHost attribution comment block

Injection runs once per response. See [Defaults & Protection](defaults-and-protection.md) for the HTML age-gate.

---

## `renderEJS(template, data)`

Explicit EJS render with an optional data object merged into the template context.

```js
res.renderEJS(`
  <html>
    <body>
      <h1><%= title %></h1>
      <p>Items: <%= items.length %></p>
    </body>
  </html>
`, {
  title: "Dashboard",
  items: stats
})
```

Same HTML protection and injection as `html()`.

---

## EJS syntax

| Tag | Meaning |
| --- | --- |
| `<% code %>` | Run JavaScript (no output) |
| `<%= expr %>` | Output escaped HTML |
| `<%- expr %>` | Output raw (unescaped) |
| `<%# comment %>` | Comment |

---

## Template context

Variables available inside `html()`, `text()`, `renderEJS()`, and `render()` templates:

| Variable | Description |
| --- | --- |
| `bot` | Current bot object |
| `user` | User object — **user webhooks only**; `null` in global webhook / webapp |
| `chat` | Chat object — **user webhooks only** |
| `owner` | `{ id, username, plan }` |
| `params` | URL query / body params |
| `request` | `{ url, method, query, ip }` |
| `update_type` | Update type string (if set) |
| Custom `data` | Fields from `render()` / `renderEJS()` second argument |

```js
res.html(`
  <p>Bot: <%= bot.username %></p>
  <p>Query ref: <%= params.ref || "none" %></p>
  <p>IP: <%= request.ip %></p>
`)
```

!!! note "User in templates"
    `user` is populated only in **user-based webhooks**. In global webhooks and webapps, use `params`, `db`, or signed tokens — not URL guesswork.

---

## `text()` with EJS

`text()` also auto-renders EJS when `<%` is present:

```js
res.text("Status: <%= status %>, updated: <%= Date.now() %>")
```

---

## See also

- [res.render()](render.md) — render a whole command file
- [Defaults & Protection](defaults-and-protection.md)
- [Public Web](../webapp-instance/public-web.md) — EJS on static `is_web` commands (no `res`)
