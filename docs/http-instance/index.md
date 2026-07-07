# HTTP

The `HTTP` instance lets your bot make **outbound requests** to external APIs, websites, and services — GET, POST, PUT, and more — directly from command scripts.

```js
let res = await HTTP.get("https://api.example.com/status")

if (res.ok) {
  Bot.sendMessage(chat.id, "API says: " + res.data.message)
}
```

Use `HTTP` when you need data or actions **outside Telegram**. For Telegram API calls, use [`Api`](../api-instance/index.md).

## When to use HTTP

| Use HTTP for | Use Api for |
| --- | --- |
| Your backend API | Sending Telegram messages |
| Payment / auth services | Inline keyboards and callbacks |
| Weather, news, external data | Editing Telegram messages |
| Webhooks to your server | Bot admin methods (`getMe`, etc.) |

## How it works

`HTTP` is a **dynamic method proxy** — any HTTP verb works as a method name:

```js
HTTP.get(url, options?)
HTTP.post(url, options?)
HTTP.put(url, options?)
HTTP.patch(url, options?)
HTTP.delete(url, options?)
HTTP.head(url, options?)
HTTP.options(url, options?)
```

Two call styles:

```js
// URL string + options object
await HTTP.get("https://api.example.com/users", { query: { page: 1 } })

// Single options object (url inside)
await HTTP.post({
  url: "https://api.example.com/users",
  body: { name: "Alice" },
  success: "/onCreated"
})
```

All methods return a **Promise** with a response object. Requests do not throw on HTTP errors — check `res.ok` instead.

## Callback workflow

Attach `success` and `error` command names to run another command when the request finishes:

```js
HTTP.get({
  url: "https://api.example.com/data",
  success: "/onSuccess",
  error: "/onError",
  tbl_options: { requestId: "abc" }
})
```

Inside callback commands, response data is available via [`http_response`](../globals/http_response.md), `response`, `content`, `headers`, and `cookies`. See [Fallback Commands](fallback-commands.md).

## Routing through proxies

| Option | Page |
| --- | --- |
| `proxy` — HTTP/SOCKS proxy server | [HTTP Proxies](proxies.md) |
| `cfProxy` — your Cloudflare Worker | [Cloudflare Worker Proxy](cf-proxy.md) |

Deploy [cf-http-router](https://github.com/Soumyadeep765/cf-http-router) to get a free `*.workers.dev` cfProxy endpoint.

## Availability

| Context | `HTTP` |
| --- | --- |
| Normal Telegram commands | ✓ |
| Webhook / webapp | ✓ |
| Broadcast commands | ✗ (`null`) |

## Pages in this section

| Page | Covers |
| --- | --- |
| [Making Requests](making-requests.md) | Methods, syntax, GET/POST examples |
| [Request Options](request-options.md) | Headers, body, query, timeout, redirects |
| [HTTP Proxies](proxies.md) | HTTP, HTTPS, SOCKS4/5 — protocols, auth, examples |
| [Cloudflare Worker Proxy](cf-proxy.md) | `cfProxy`, deploy [cf-http-router](https://github.com/Soumyadeep765/cf-http-router), why use it |
| [Responses](responses.md) | Response object, `responseType`, cookies, error codes |
| [Streaming](streaming.md) | `responseType: "stream"`, SSE, chunk reading, limits |
| [Fallback Commands](fallback-commands.md) | `success` / `error` chaining, `tbl_options` |
| [Limits & Timeouts](limits.md) | Plan timeouts, response size, redirects, stream caps |

## Quick example

```js
let res = await HTTP.post("https://api.example.com/notify", {
  body: { user_id: user.id, event: "signup" },
  headers: { Authorization: "Bearer " + process.env.API_TOKEN },
  timeout: 10000,
  responseType: "json"
})

if (!res.ok) {
  Bot.sendMessage(chat.id, "Could not reach server (" + res.status + ")")
  return
}

Bot.sendMessage(chat.id, "Registered! ID: " + res.data.id)
```

Store API tokens in dashboard [ENV variables](../globals/process.md) — never hard-code secrets.
