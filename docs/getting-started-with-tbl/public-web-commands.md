# Public Web Commands

Mark commands as **public web** resources to serve static pages, assets, and templates at a per-bot URL — without running Logic or the TBL sandbox.

---

## Enable public web

In the command editor, enable **Public web** (`is_web = 1`) on the command.

Only flagged commands are served. Others return **403** if accessed via the public URL.

---

## URL format

```
https://{domain}/public/{bot_id}/{command_name}
```

Generate links in Logic:

```js
let home = Webapp.getUrl("index.html", { public: true })
let css = Webapp.getUrl("styles.css", { public: true })

await Api.sendMessage({
  chat_id: chat.id,
  text: "Visit: " + home
})
```

---

## What to put in the command

Public web serves the command **source** directly — not the Answer field.

| Command name | Use for |
| --- | --- |
| `index.html` | Landing page (default for `/public/{bot_id}/`) |
| `about.html` | Info page |
| `styles.css` | Stylesheet |
| `app.js` | Client-side script |
| `data.json` | Static JSON |
| `readme.md` | Markdown content |

### Example `index.html` command

```html
<!DOCTYPE html>
<html>
<head>
  <title><%= bot.username %></title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Welcome to @<%= bot.username %></h1>
  <% if (params.ref) { %>
    <p>Ref: <%= params.ref %></p>
  <% } %>
  <script src="app.js"></script>
</body>
</html>
```

EJS tags (`<%`, `<%=`) work with limited context: `bot`, `params`, `request`. No `user`, `Api`, or `db`.

---

## Answer vs source

| Field | Telegram command | Public web command |
| --- | --- | --- |
| **Answer** | Sent as chat message | Ignored |
| **Logic** | Runs in sandbox | **Not executed** |
| **Command source** | Logic code | **Served as file content** |

Build the page in the command editor body (the code/source area), not in Answer.

---

## Public web vs webapp

| | Public web (`is_web`) | Webapp |
| --- | --- | --- |
| URL | `/public/{bot_id}/page.html` | `/webapp/{bot_id}/api` |
| Logic runs | No | Yes |
| `db`, `Api`, `res` | No | Yes |
| Best for | Static HTML/CSS/JS | Dynamic APIs, DB-backed pages |

Need server logic? Use a [webapp](../webapp-instance/index.md). Need a fast landing page? Use public web.

---

## Default home page

Name a command `index.html` (or alias `index` / `app`) with `is_web` enabled:

```
https://{domain}/public/{bot_id}/
```

Empty path resolves to `index.html`.

---

## Full guide

For routing, assets, rate limits, and EJS context, see the complete [Public Web](../webapp-instance/public-web.md) reference.

---

## See also

- [Command Fields](command-fields.md)
- [Webapp Methods](../webapp-instance/webapp-methods.md)
- [Execution Flow](execution-flow.md)
