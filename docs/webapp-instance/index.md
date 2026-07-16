# Webapps

Your bot's public front door — unsigned HTTP endpoints that run full commands for dynamic pages, JSON APIs, and dashboards.

No cryptographic signing required. Anyone with the URL can trigger the command — design accordingly.

---

## What are webapps?

**Webapps** are unsigned HTTP endpoints that run full TeleBotHost commands — dynamic pages, lightweight APIs, and dashboards without cryptographic signing.

| You get | You skip |
| --- | --- |
| Full sandbox (`db`, `HTTP`, `Api`, `res`) | Building a separate backend |
| Server-rendered pages via `res.render()` | Static file hosting setup |
| Command logic you already know | Learning a new framework |

Anyone with the URL can trigger the command. Use webapps for public dynamic logic; use [webhooks](../webhook-instance/index.md) when you need signing or per-user context.

---

## How to use them

Generate a webapp URL inside any command's **Logic** field:

```js
let url = Webapp.getUrl("dashboard", {
  params: { ref: "home", lang: "en" }
})
```

Three things worth knowing upfront:

1. **`user` and `chat` are always `null`** — pass IDs via `params` or look up data in `db.bot`.
2. **Respond with [`res`](../res-instance/index.md)** — JSON, HTML, redirects, or rendered templates.
3. **URLs are public** — don't expose admin actions without your own auth layer.

!!! tip "New to TBL?"
    `params`, `request`, and `bot` are globals available in webapp commands. Quick intro: [Learning TBL](../learning-tbl.md). For signed per-user endpoints, see [Webhooks](../webhook-instance/index.md).

!!! warning
    Webapp URLs are public. Do not expose admin actions or user-specific secrets without your own auth layer inside the command.

---

## Webapp, webhook, or public web?

| | Webapp | User webhook | Global webhook | Public web |
| --- | --- | --- | --- | --- |
| **URL signed** | No | Yes | Yes | No |
| **Runs command sandbox** | Yes | Yes | Yes | **No** |
| **`res` available** | Yes | Yes | Yes | No |
| **`user` / `chat`** | `null` | Yes | `null` | N/A |
| **`Api`, `db`, `HTTP`** | Yes | Yes | Yes | No |
| **Command in URL** | Path (`/webapp/.../cmd`) | Query (`?command=`) | Query | Path (`/public/.../file`) |
| **`is_web` flag required** | No | No | No | **Yes** |
| **Best for** | Dynamic APIs, dashboards | Secure user actions | Signed system jobs | Static HTML/CSS/JS |

---

## When to use a webapp

- Public JSON API that needs `db`, `HTTP`, or `Api`
- Server-rendered dashboard with `res.render()`
- Embeddable pages where signing is impractical
- Endpoints that read/write **bot-level** data, not per-user secrets

---

## Try it — copy-paste examples

Start simple. Each example only introduces what it needs.

### Generate a webapp URL

```js
let apiUrl = Webapp.getUrl("getStats", { params: { period: "week" } })
Bot.sendMessage("Live stats: " + apiUrl)
```

### Return JSON from a webapp command

Inside your webapp command's **Logic** field:

```js
let stats = await db.bot.get("weekly_stats", {})
res.json({ ok: true, data: stats })
```

### Render an HTML page

```js
res.render("dashboard.html", { data: { title: "My Bot Dashboard" } })
```

Responses: [`res`](../res-instance/index.md) · Static pages: [Public Web](public-web.md)

---

## HTTP route

```
GET | POST | PUT | PATCH | DELETE | OPTIONS | HEAD
/webapp/{bot_id}/{command}?options={json}&{params...}
```

The command name is in the **path**, not the query string.

---

## Instance methods

| Method | Description |
| --- | --- |
| `Webapp.getUrl(command, config)` | Standard webapp URL |
| `Webapp.get(command, config)` | Alias for `getUrl` |

See [Webapp Methods](webapp-methods.md) and [Public Web](public-web.md) for URL variants.

---

## Globals in webapp commands

| Available | Not available |
| --- | --- |
| `res`, `Api`, `Bot`, `db`, `HTTP`, `modules`, `Libs` | `msg` |
| `bot`, `owner`, `plan`, `request`, `params`, `options` | `user`, `chat`, `User` (always `null`) |
| `Webhook`, `Webapp` | — |

Design commands to work without `user`. Pass IDs via `params` or look up data in `db.bot`.

---

## Responses

Use [`res`](../res-instance/index.md) for JSON, HTML, redirects, and templates. Default response if nothing sent:

```json
{ "status": "success" }
```

---

## Pages in this section

- [Webapp Methods](webapp-methods.md) — `getUrl`, options, params, public URLs
- [Public Web](public-web.md) — static `is_web` pages (detailed guide)
- [Examples](examples.md)
- [Best Practices](best-practices.md)

---

## Related

- [Webhooks](../webhook-instance/index.md)
- [HTTP Responses (res)](../res-instance/index.md)
- [`request`](../globals/request.md)
