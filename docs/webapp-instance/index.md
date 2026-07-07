# Webapps

**Webapps** are unsigned HTTP endpoints that run full TBL commands — dynamic pages, lightweight APIs, and dashboards without cryptographic signing.

```js
let url = Webapp.getUrl("dashboard", {
  params: { ref: "home", lang: "en" }
})
```

Anyone with the URL can trigger the command. Use webapps for public dynamic logic; use [webhooks](webhook-instance/index.md) when you need signing or per-user context.

---

## HTTP route

```
GET | POST | PUT | PATCH | DELETE | OPTIONS | HEAD
/webapp/{bot_id}/{command}?options={json}&{params...}
```

The command name is in the **path**, not the query string.

---

## Webapp vs Webhook vs Public Web

| | Webapp | User webhook | Global webhook | Public web |
| --- | --- | --- | --- | --- |
| **URL signed** | No | Yes | Yes | No |
| **Runs TBL sandbox** | Yes | Yes | Yes | **No** |
| **`res` available** | Yes | Yes | Yes | No |
| **`user` / `chat`** | `null` | Yes | `null` | N/A |
| **`Api`, `db`, `HTTP`** | Yes | Yes | Yes | No |
| **Command in URL** | Path (`/webapp/.../cmd`) | Query (`?command=`) | Query | Path (`/public/.../file`) |
| **`is_web` flag required** | No | No | No | **Yes** |
| **Best for** | Dynamic APIs, dashboards | Secure user actions | Signed system jobs | Static HTML/CSS/JS |

---

## When to use a Webapp

- Public JSON API that needs `db`, `HTTP`, or `Api`
- Server-rendered dashboard with `res.render()`
- Embeddable pages where signing is impractical
- Endpoints that read/write **bot-level** data, not per-user secrets

!!! warning
    Webapp URLs are public. Do not expose admin actions or user-specific secrets without your own auth layer inside the command.

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
| `res`, `Api`, `Bot`, `db`, `HTTP`, `modules`, `Libs` | `msg`, `TBL` util |
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
