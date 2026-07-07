# Request Options

All options can be passed as the second argument or inside a single options object with `url`.

## Options reference

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `url` | `string` | required | Full URL with `http://` or `https://` |
| `headers` | `object` | `{}` | Custom request headers |
| `body` / `data` | `any` | `null` | Request body (objects → JSON) |
| `query` / `params` | `object` | — | URL query parameters |
| `timeout` | `number` | plan default | Timeout in milliseconds |
| `responseType` | `string` | `"auto"` | How to decode the response body |
| `redirect` | `boolean` | `true` | Follow HTTP redirects |
| `maxRedirect` | `number` | `3` | Max redirects to follow (0–10) |
| `proxy` | `string` | — | HTTP/SOCKS proxy URL — see [HTTP Proxies](proxies.md) |
| `cfProxy` | `string` | — | Cloudflare Worker URL — see [Cloudflare Worker Proxy](cf-proxy.md) |
| `success` | `string` | — | Command to run on 2xx response |
| `error` | `string` | — | Command to run on non-2xx response |
| `tbl_options` | `any` | — | Data passed to callback as `tbl_options` |

---

## Body and data

For POST, PUT, and PATCH, pass the payload as `body` or `data`:

```js
await HTTP.post("https://api.example.com/events", {
  body: {
    type: "signup",
    user_id: user.id
  }
})
```

Strings and buffers are sent as-is. Objects are JSON-stringified.

---

## Timeout

```js
await HTTP.get("https://slow-api.example.com/data", {
  timeout: 5000  // 5 seconds
})
```

| Constraint | Value |
| --- | --- |
| Minimum | 100 ms |
| Maximum | Your plan's script timeout (see [Limits](limits.md)) |
| Default | Plan timeout if omitted |

If the request exceeds the timeout, `res.ok` is `false` and `res.error.code` is `"TIMEOUT"`.

---

## Redirects

Redirects (301, 302, 303, 307, 308) are followed automatically.

```js
// Disable redirects
await HTTP.get("https://example.com/redirect", { redirect: false })

// Allow up to 5 redirects (max 10)
await HTTP.get("https://example.com/redirect", { maxRedirect: 5 })

// No redirects at all
await HTTP.get("https://example.com", { maxRedirect: 0 })
```

Response fields `redirected` and `redirectCount` show how many redirects were followed. See [Limits](limits.md) for the redirect cap.

---

## Response type

Control body decoding with `responseType`:

| Value | Behavior |
| --- | --- |
| `"auto"` | JSON if Content-Type is JSON, text for `text/*`, Buffer otherwise |
| `"json"` | Force JSON parse |
| `"text"` | UTF-8 string |
| `"buffer"` | Raw Buffer |
| `"arrayBuffer"` | ArrayBuffer for binary processing |
| `"stream"` | Streaming interface for large/SSE responses |

```js
await HTTP.get("https://api.example.com/data", { responseType: "json" })
await HTTP.get("https://example.com/image.png", { responseType: "buffer" })
```

See [Responses](responses.md) for the full response object. For streaming, see [Streaming](streaming.md).

---

## Callback options

### `success` and `error`

Command names (with or without `/`) to run after the request:

```js
HTTP.get({
  url: "https://api.example.com/item/1",
  success: "/onItemLoaded",
  error: "/onItemError"
})
```

- `success` runs when status is **2xx**
- `error` runs when status is **not 2xx**
- If `error` is omitted and the request fails, **no callback runs** — handle inline with `await` instead

### `tbl_options`

Pass custom data to the callback command:

```js
HTTP.get({
  url: "https://api.example.com/data",
  success: "/onData",
  tbl_options: { page: 2, source: "menu" }
})

// Inside /onData:
let page = tbl_options.page
```

Available as the [`tbl_options`](../globals/tbl_options.md) global in callback commands only.

---

## Validation errors

Invalid options (missing URL, bad proxy format, `maxRedirect` out of range) throw before the request is sent. These are caught by the `!` error handler if defined.

```js
// Throws: URL required
HTTP.get({ timeout: 5000 })
```

---

## Important notes

- Store auth tokens in `process.env` — pass via `headers.Authorization`
- `query` and `params` are equivalent aliases
- Proxy details: [HTTP Proxies](proxies.md) and [Cloudflare Worker Proxy](cf-proxy.md)
- See [Limits & Timeouts](limits.md) for all numeric caps
- See [Fallback Commands](fallback-commands.md) for the callback workflow
