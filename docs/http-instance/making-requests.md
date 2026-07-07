# Making Requests

Every HTTP method is available as `HTTP.<method>(url, options?)` or `HTTP.<method>({ url, ...options })`.

## Supported methods

| Method | Typical use |
| --- | --- |
| `HTTP.get` | Fetch data, read resources |
| `HTTP.post` | Create resources, submit forms, send JSON |
| `HTTP.put` | Replace a resource |
| `HTTP.patch` | Partial update |
| `HTTP.delete` | Remove a resource |
| `HTTP.head` | Headers only (no body) |
| `HTTP.options` | CORS preflight / capability check |

Method names are **case-insensitive** on the proxy (`HTTP.GET` and `HTTP.get` both work).

## Simple GET

```js
// Fire and forget
HTTP.get("https://api.example.com/ping")

// Await the response
let res = await HTTP.get("https://api.example.com/ping")

if (res.ok) {
  Bot.sendMessage(chat.id, res.data.status)
}
```

## POST with JSON body

Objects are automatically serialized to JSON. `Content-Type: application/json` is set for you.

```js
let res = await HTTP.post("https://api.example.com/users", {
  body: {
    name: user.first_name,
    telegram_id: user.id
  }
})
```

`data` is an alias for `body`:

```js
await HTTP.post("https://api.example.com/users", {
  data: { name: "Alice" }
})
```

## PUT, PATCH, DELETE

```js
await HTTP.put("https://api.example.com/users/42", {
  body: { name: "Bob" }
})

await HTTP.patch("https://api.example.com/users/42", {
  body: { email: "bob@example.com" }
})

let res = await HTTP.delete("https://api.example.com/users/42")
```

## Query parameters

Append query string params without manual URL building:

```js
await HTTP.get("https://api.example.com/search", {
  query: { q: "telegram", page: 1, limit: 20 }
})
// → https://api.example.com/search?q=telegram&page=1&limit=20
```

`params` is an alias for `query`.

## Object syntax

Pass everything in one object — useful for callbacks and long option lists:

```js
await HTTP.get({
  url: "https://api.example.com/data",
  headers: { Authorization: "Bearer " + process.env.API_TOKEN },
  query: { format: "json" },
  timeout: 8000,
  success: "/onData",
  error: "/onDataError"
})
```

## Custom headers

Default headers are added automatically (User-Agent, Accept, Connection). Override or extend with `headers`:

```js
await HTTP.get("https://api.example.com/private", {
  headers: {
    Authorization: "Bearer " + process.env.API_TOKEN,
    Accept: "application/xml",
    "X-Request-Id": "req-001"
  }
})
```

Default User-Agent format: `TBL/1.0.0 (Telegram Bot Lang; AppID:TBLAPP; +TBL-BOT-<botId>)`.

## With fallback commands

```js
HTTP.post({
  url: "https://api.example.com/order",
  body: { item: params, user_id: user.id },
  success: "/orderConfirmed",
  error: "/orderFailed",
  tbl_options: { orderRef: params }
})
```

The current command continues immediately — callback commands run when the request completes. See [Fallback Commands](fallback-commands.md).

## Checking results inline

```js
let res = await HTTP.get("https://api.example.com/price/BTC")

if (!res.ok) {
  Bot.sendMessage(chat.id, "Price unavailable (" + res.status + ")")
  return
}

Bot.sendMessage(chat.id, "BTC: $" + res.data.price)
```

## Important notes

- URLs must include the protocol: `https://` or `http://`
- External failures do **not** crash your command — always check `res.ok`
- Default timeout follows your [plan](../globals/plan.md) — see [Limits](limits.md)
- For full option reference, see [Request Options](request-options.md)
- For response fields, see [Responses](responses.md)
- For streaming, see [Streaming](streaming.md)
- For proxies, see [HTTP Proxies](proxies.md) and [Cloudflare Worker Proxy](cf-proxy.md)
