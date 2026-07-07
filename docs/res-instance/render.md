# res.render()

Render another command's source code as the HTTP response. Ideal for separating API logic from HTML/JSON templates.

```js
res.render("dashboard.html", {
  data: {
    stats: statsData,
    title: "My Dashboard"
  }
})
```

Execution ends as soon as the rendered content is sent.

---

## Basic usage

```js
// Render by exact command name
res.render("profile.html")

// Pass template data
res.render("api-response.json", {
  data: { ok: true, result: computed }
})

// Override content type
res.render("export", {
  contentType: "text/csv",
  data: { rows: csvRows }
})
```

If the command name is not found, `res` returns **404 JSON**:

```json
{ "error": "Command not found", "message": "Command \"...\" not found" }
```

---

## Automatic content type

`res.render()` sets `Content-Type` from the command name extension, unless you pass `options.contentType`.

| Extension | Content-Type |
| --- | --- |
| `.html`, `.htm` | `text/html` |
| `.css` | `text/css` |
| `.js`, `.mjs` | `application/javascript` |
| `.json`, `.jsonld` | `application/json` |
| `.xml` | `application/xml` |
| `.csv` | `text/csv` |
| `.yaml`, `.yml` | `application/x-yaml` |
| `.md`, `.markdown` | `text/markdown` |
| `.svg` | `image/svg+xml` |
| `.ts`, `.tsx`, `.jsx`, `.vue`, … | Matching script types |
| *(no extension)* | `text/plain` |

```js
res.render("page.html")      // text/html
res.render("data.json")      // application/json
res.render("styles.css")     // text/css
res.render("readme")         // text/plain
```

---

## Data passing

Pass custom fields via `options.data`. They are merged into the EJS template context alongside globals.

```js
// URL: /webapp/{bot_id}/showProfile?section=settings

res.render("profile-template.html", {
  data: {
    profile: userProfile,
    section: params.section || "overview"
  }
})
```

Inside `profile-template.html`:

```html
<h1>Section: <%= section %></h1>
<p>Ref from URL: <%= params.ref %></p>
```

### Available in rendered templates

| Source | Variables |
| --- | --- |
| Platform | `bot`, `user`, `chat`, `owner`, `params`, `request`, `update_type` |
| `options.data` | Any keys you pass (e.g. `profile`, `stats`) |
| Parent command | Full TBL sandbox — `Api`, `Bot`, `db`, `HTTP`, `modules`, etc. run **before** render; the template only sees template context |

!!! note
    `user` is available in templates only when the parent command runs in a **user webhook** context.

---

## EJS in rendered commands

For `.html` and `.text` commands, if the command code contains `<%`, it is EJS-rendered with `options.data` before sending.

HTML commands also receive platform HTML injection (`<base>`, meta tag, attribution).

---

## Practical examples

### Separate API logic from HTML

**Handler command (`showDashboard`):**

```js
let stats = {
  users: await db.bot.get("user_count") || 0,
  revenue: await db.bot.get("revenue") || 0
}
res.render("dashboard.html", { data: { stats } })
```

**Template command (`dashboard.html`):**

```html
<!DOCTYPE html>
<html>
<body>
  <h1>Dashboard</h1>
  <p>Users: <%= stats.users %></p>
  <p>Revenue: <%= stats.revenue %></p>
</body>
</html>
```

### JSON via template command

```js
res.render("user-payload.json", {
  data: {
    id: user.id,
    name: user.first_name,
    premium: user.premium || false
  }
})
```

**`user-payload.json` command:**

```json
{
  "ok": true,
  "user": {
    "id": <%= id %>,
    "name": "<%= name %>",
    "premium": <%= premium %>
  }
}
```

### JSON API without a template file

For simple APIs, `res.json()` is often enough:

```js
res.status(200)
   .set("Access-Control-Allow-Origin", "*")
   .json({ status: "success", data: userData })
```

---

## See also

- [HTML & EJS](html-and-ejs.md) — `html()`, `renderEJS()`
- [JSON, Text & XML](send-json-text-xml.md)
- [Defaults & Protection](defaults-and-protection.md)
