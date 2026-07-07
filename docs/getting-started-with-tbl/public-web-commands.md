# Public Web Commands

Want a landing page for your bot without spinning up a separate website? **Public web commands** serve HTML, CSS, JS, and JSON at a per-bot URL — no Logic execution, no sandbox, no cold start drama.

Static files. Fast. Good enough for docs, link-in-bio pages, and simple mini-sites.

---

## What is public web?

Normally, command **Logic** runs in a sandbox when someone interacts with your bot. Public web is different:

- You mark a command with **Public web** (`is_web`)
- The command **source** (what you write in the editor) is served as a file
- **Answer** and **Logic** are ignored — they never run

Think of it as hosting static assets under `/public/{bot_id}/...`.

---

## Enable public web

In the command editor, turn on **Public web** (`is_web = 1`).

Only flagged commands are served. Hit a non-public command's URL and you get **403**. Security by opt-in.

---

## URL format

```
https://{domain}/public/{bot_id}/{command_name}
```

Generate links in Logic when you want to share them in chat:

```js
let home = Webapp.getUrl("index.html", { public: true })
let css = Webapp.getUrl("styles.css", { public: true })

await Api.sendMessage({
  chat_id: chat.id,
  text: "Visit: " + home
})
```

[`Api`](../api-instance/index.md) sends the message; `Webapp.getUrl` builds the link.

---

## What to put in the command

Public web serves the command **source** directly — **not** the Answer field.

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

EJS tags (`<%`, `<%=`) work with limited context: `bot`, `params`, `request`. No `user`, [`Api`](../api-instance/index.md), or `db` — this is static serving, not Logic.

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

Need server logic? Use a [webapp](../webapp-instance/index.md). Need a fast landing page? Public web.

---

## Default home page

Name a command `index.html` (or alias `index` / `app`) with `is_web` enabled:

```
https://{domain}/public/{bot_id}/
```

Empty path resolves to `index.html`. Your bot's front door on the web.

---

## Full guide

Routing, assets, rate limits, and EJS context — [Public Web](../webapp-instance/public-web.md).

---

## See also

- [Command Fields](command-fields.md) — `is_web` toggle
- [Webapp Methods](../webapp-instance/webapp-methods.md)
- [Execution Flow](execution-flow.md) — public web skips the sandbox
