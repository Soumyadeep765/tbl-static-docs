# Making Requests

Your bot lives inside Telegram. The rest of the internet lives... elsewhere. `HTTP` is the bridge — call any REST API, payment gateway, or weather service directly from your command's **Logic** field.

Every HTTP method is a function: `HTTP.get(url)`, `HTTP.post(url, options)`, and so on. No fetch wrapper, no axios install, no "works on my machine."

---

## What methods are available?

| Method | Typical use |
| --- | --- |
| `HTTP.get` | Fetch data, read resources |
| `HTTP.post` | Create resources, submit forms, send JSON |
| `HTTP.put` | Replace a resource |
| `HTTP.patch` | Partial update |
| `HTTP.delete` | Remove a resource |
| `HTTP.head` | Headers only (no body) |
| `HTTP.options` | CORS preflight / capability check |

Method names are **case-insensitive** on the proxy (`HTTP.GET` and `HTTP.get` both work). Pick your casing. The server won't judge.

---

## How to make a request

Two call styles — same result:

```js
// URL string + options object
let res = await HTTP.get("https://api.example.com/ping", { timeout: 5000 })

// Single options object (url inside)
let res = await HTTP.get({
  url: "https://api.example.com/ping",
  timeout: 5000
})
```

Three things worth knowing upfront:

1. **Always `await`** — every method returns a Promise.
2. **HTTP errors don't throw** — check `res.ok` instead. A 404 is a polite response object, not an exception.
3. **URLs need a protocol** — `https://` or `http://`. `api.example.com` alone will not fly.

---

## Try it — copy-paste examples

### Simple GET

```js
// Fire and forget
HTTP.get("https://api.example.com/ping")

// Await the response
let res = await HTTP.get("https://api.example.com/ping")

if (res.ok) {
  Bot.sendMessage(chat.id, res.data.status)
}
```

### POST with JSON body

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

### PUT, PATCH, DELETE

```js
await HTTP.put("https://api.example.com/users/42", {
  body: { name: "Bob" }
})

await HTTP.patch("https://api.example.com/users/42", {
  body: { email: "bob@example.com" }
})

let res = await HTTP.delete("https://api.example.com/users/42")
```

### Query parameters

Append query string params without manual URL building:

```js
await HTTP.get("https://api.example.com/search", {
  query: { q: "telegram", page: 1, limit: 20 }
})
// → https://api.example.com/search?q=telegram&page=1&limit=20
```

`params` is an alias for `query`.

### Custom headers

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

### Checking results inline

```js
let res = await HTTP.get("https://api.example.com/price/BTC")

if (!res.ok) {
  Bot.sendMessage(chat.id, "Price unavailable (" + res.status + ")")
  return
}

Bot.sendMessage(chat.id, "BTC: $" + res.data.price)
```

### With fallback commands

Fire the request and move on — callback commands handle the result:

```js
HTTP.post({
  url: "https://api.example.com/order",
  body: { item: params, user_id: user.id },
  success: "/orderConfirmed",
  error: "/orderFailed",
  tbl_options: { orderRef: params }
})
```

The current command continues immediately. See [Fallback Commands](fallback-commands.md).

---

## Where to go next

| Topic | Page |
| --- | --- |
| Full option reference | [Request Options](request-options.md) |
| Response fields and error codes | [Responses](responses.md) |
| Chunk-by-chunk reading | [Streaming](streaming.md) |
| HTTP/SOCKS proxies | [HTTP Proxies](proxies.md) |
| Cloudflare Worker routing | [Cloudflare Worker Proxy](cf-proxy.md) |
| Timeouts and size caps | [Limits](limits.md) |

---

## Important notes

- URLs must include the protocol: `https://` or `http://`
- External failures do **not** crash your command — always check `res.ok`
- Default timeout follows your [plan](../globals/plan.md) — see [Limits](limits.md)
- Store API tokens in ENV vars — see [`process.env`](../globals/process.md)
