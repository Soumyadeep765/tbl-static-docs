# Webapp Examples

Practical patterns for webapp commands and URL generation.

---

## JSON API (webapp)

Webapps have no `user` context — design APIs around `params`, `db.bot`, or tokens you validate yourself.

```js
let id = params.id
if (!id) {
  return res.status(400).json({ error: "id required" })
}

let record = await db.bot.get("item:" + id)
res
  .set("Access-Control-Allow-Origin", "*")
  .json({ ok: true, record: record || null })
```

---

## HTML dashboard via `res.render()`

**Handler command (`showDashboard`):**

```js
let stats = {
  visitors: await db.bot.get("visitors") || 0,
  updated: Date.now()
}
res.render("dashboard.html", { data: { stats } })
```

**Template command (`dashboard.html`):**

```html
<!DOCTYPE html>
<html>
<body>
  <h1>Stats</h1>
  <p>Visitors: <%= stats.visitors %></p>
</body>
</html>
```

---

## Send a webapp link in Telegram

```js
let url = Webapp.getUrl("dashboard", {
  params: { ref: "telegram", lang: "en" }
})

await Api.sendMessage({
  chat_id: chat.id,
  text: "Open dashboard: " + url
})
```

---

## Public landing page link

For static `is_web` commands — no sandbox, no `res`:

```js
let home = Webapp.getUrl("index.html", { public: true })

await Api.sendMessage({
  chat_id: chat.id,
  text: "Visit our site: " + home
})
```

The `index.html` command should contain static HTML (optionally with EJS for `bot.username` and `params`). See [Public Web](public-web.md).

---

## User-specific action (use webhook, not webapp)

When you need `user` context and signing:

```js
let syncUrl = Webhook.getUrl("syncProgress", {
  options: { source: "app" },
  expiresIn: 3600
})
```

Inside `syncProgress`:

```js
let progress = await db.user.get("level", 0)
res.json({ ok: true, user_id: user.id, level: progress })
```

---

## Health check endpoint

```js
res.json({
  ok: true,
  bot: bot.username,
  uptime: process.uptime()
})
```

---

## Related

- [Webapp Methods](webapp-methods.md)
- [Public Web](public-web.md)
- [HTTP Responses (res)](../res-instance/index.md)
- [User-Based Webhooks](../webhook-instance/user-webhook.md)
