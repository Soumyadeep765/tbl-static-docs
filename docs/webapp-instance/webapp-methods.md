# Webapp Methods

Generate webapp and public web URLs with `Webapp.getUrl()` (alias: `Webapp.get()`).

---

## `getUrl(command, config)`

### Standard webapp URL

```js
let url = Webapp.getUrl("dashboard", {
  options: { theme: "dark" },
  params: { ref: "home", lang: "en" }
})
// → https://{domain}/webapp/{bot_id}/dashboard?options=...&ref=home&lang=en
```

| Parameter | Type | Description |
| --- | --- | --- |
| `command` | string | Command name or alias (required) |
| `options` | object | JSON config passed to the command |
| `params` | object | Visible query parameters |
| `public` | boolean | If `true`, generate a [public web](public-web.md) URL |
| `publi` | boolean | Typo-tolerant alias for `public` |

### Object form

```js
Webapp.getUrl({
  command: "dashboard",
  options: { theme: "dark" },
  params: { ref: "home" },
  public: false
})
```

---

## `options` vs `params`

| | `options` | `params` |
| --- | --- | --- |
| **Encoding** | Single `options={urlEncodedJson}` query key | Standard `key=value` pairs |
| **Visibility** | One JSON blob in URL | Individual readable parameters |
| **Use for** | App config, structured settings | Shareable filters, `ref`, `lang` |
| **In command** | Available on global [`options`](../globals/options.md) | Available on global [`params`](../globals/params.md) |

```js
// URL: .../dashboard?options=%7B%22theme%22%3A%22dark%22%7D&ref=home&lang=en

let theme = options.theme   // "dark"
let ref = params.ref        // "home"
```

---

## Public web URLs

Set `public: true` to generate a **public web** URL instead of a sandbox webapp URL:

```js
let landing = Webapp.getUrl("index.html", { public: true })
// → https://{domain}/public/{bot_id}/index.html

let landing2 = Webapp.getUrl({
  command: "landing",
  public: true,
  params: { utm: "telegram" }
})
// → https://{domain}/public/{bot_id}/landing?utm=telegram
```

Public URLs:

- Do **not** run the TBL sandbox
- Require the command to have **`is_web = 1`**
- Serve command source directly (with EJS + HTML injection for HTML)
- Do **not** provide `res`, `Api`, or `db`

See [Public Web](public-web.md) for the full guide.

---

## Command validation

When `commandHandlers` are available at URL generation time, `getUrl` validates that the command name or alias exists. Unknown commands throw:

```
Error: Unknown command: {name}
```

---

## Array params

`params` supports arrays — each value becomes a repeated query key:

```js
Webapp.getUrl("search", {
  params: { tag: ["js", "api"] }
})
// → ...?tag=js&tag=api
```

---

## Examples

### Send dashboard link in Telegram

```js
let dashboardUrl = Webapp.getUrl("dashboard", {
  params: { ref: "bot", lang: "en" }
})

await Api.sendMessage({
  chat_id: chat.id,
  text: "Open dashboard: " + dashboardUrl
})
```

### Public landing page link

```js
let home = Webapp.getUrl("index.html", { public: true })
```

### API endpoint URL

```js
let apiUrl = Webapp.getUrl("api/status", {
  params: { format: "json" }
})
```

---

## URL design tips

- Use short, predictable command names (`dashboard`, `api/users`)
- Put marketing/tracking params in `params` (`ref`, `utm_source`)
- Put structured config in `options`
- Never put secrets in URLs — use [webhooks](../webhook-instance/index.md) for signed flows
- Use `public: true` only for static `is_web` commands

---

## See also

- [Public Web](public-web.md)
- [Examples](examples.md)
- [Webapps overview](index.md)
