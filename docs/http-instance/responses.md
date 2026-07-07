# Responses

Every `HTTP` call resolves to a **response object**. Failed HTTP status codes do not throw — inspect `res.ok` and `res.status` instead.

## Response object

```js
let res = await HTTP.get("https://api.example.com/data")
```

| Field | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | `true` for HTTP 2xx |
| `status` | `number` | HTTP status code |
| `statusText` | `string` | HTTP status text |
| `headers` | `object` | Response headers (lowercase keys) |
| `url` | `string` | Final URL after redirects |
| `redirected` | `boolean` | Whether any redirect was followed |
| `redirectCount` | `number` | Number of redirects followed |
| `content` | `string` / `Buffer` | Raw parsed body — **not set** when `isStream: true` |
| `data` | `any` | Parsed data — **not set** when `isStream: true` |
| `isJson` | `boolean` | Whether `data` was JSON-parsed — **not set** on streams |
| `cookies` | `object` | Extracted cookies `{ name: value }` |
| `isStream` | `boolean` | `true` only for `responseType: "stream"` |
| `contentType` | `string` | Content-Type header (stream responses only) |
| `stream` | `object` | Stream reader when `isStream: true` — see [Streaming](streaming.md) |
| `responseType` | `string` | Decode mode used |
| `error` | `object` | Present on failure: `{ code, message }` |
| `usedWorkerProxy` | `boolean` | `true` when `cfProxy` was used |

### Example response

```json
{
  "ok": true,
  "status": 200,
  "statusText": "OK",
  "content": "{\"status\":\"ok\"}",
  "data": { "status": "ok" },
  "isJson": true,
  "headers": {
    "content-type": "application/json; charset=utf-8",
    "content-length": "15"
  },
  "cookies": {},
  "url": "https://api.example.com/status",
  "redirected": false,
  "redirectCount": 0,
  "isStream": false,
  "responseType": "auto"
}
```

## Reading the body

| Field | When to use |
| --- | --- |
| `res.data` | Parsed JSON or decoded body — most common |
| `res.content` | Raw string or Buffer |
| `res.isJson` | Check before assuming `data` is an object |

```js
let res = await HTTP.get("https://api.example.com/user/1")

if (res.ok && res.isJson) {
  Bot.sendMessage(chat.id, "Name: " + res.data.name)
} else if (res.ok) {
  Bot.sendMessage(chat.id, res.content)
}
```

## Response types

Set `responseType` in request options:

```js
// Auto-detect (default)
await HTTP.get(url)

// Force JSON
await HTTP.get(url, { responseType: "json" })

// Plain text
await HTTP.get(url, { responseType: "text" })

// Binary (images, files)
await HTTP.get(url, { responseType: "buffer" })

// ArrayBuffer
await HTTP.get(url, { responseType: "arrayBuffer" })
```

If `responseType: "json"` is set but the body is not valid JSON, `res.ok` is `false` and `res.error.code` is `"INVALID_JSON"`.

For large or live responses, use `responseType: "stream"` — see [Streaming](streaming.md).

## Cookies

`Set-Cookie` headers are parsed into a flat object:

```js
let login = await HTTP.post("https://api.example.com/login", {
  body: { username: "bot", password: process.env.API_PASSWORD }
})

let session = login.cookies.sessionId

let profile = await HTTP.get("https://api.example.com/profile", {
  headers: { Cookie: "sessionId=" + session }
})
```

In callback commands, cookies are also available as the `cookies` global alias. See [`http_response`](../globals/http_response.md).

## Error inspection

Failures return a structured object — no thrown exceptions for HTTP errors:

```js
let res = await HTTP.get("https://api.example.com/missing")

if (!res.ok) {
  Bot.sendMessage(chat.id, "Error " + res.status + ": " + res.error.message)
}
```

### Common error codes

| `error.code` | Typical `status` | Cause |
| --- | --- | --- |
| `TIMEOUT` | 408 | Request exceeded timeout |
| `REDIRECT_LIMIT_EXCEEDED` | 310 | Too many redirects |
| `RESPONSE_SIZE_EXCEEDED` | 413 | Response body too large |
| `RESPONSE_TOO_LARGE` | 413 | Content-Length exceeds limit |
| `INVALID_JSON` | 500 | `responseType: "json"` but body is not JSON |
| `RESPONSE_READ_ERROR` | 500 | Failed to read response body |
| `WORKER_PROXY_ERROR` | 502 | Cloudflare Worker proxy error |
| `HTTP_REQUEST_ERROR` | 500 | Unexpected request failure |

## In callback commands

When using `success` / `error` fallback commands, the same response shape is available through globals:

| Global | Source |
| --- | --- |
| `http_response` | Full wrapper (`options` + `response` + `timestamp` + `url`) |
| `response` | The response object above |
| `content` | `response.content` |
| `headers` | `response.headers` |
| `cookies` | `response.cookies` |
| `error` | Full response object (in `error` callback only) |

See [Fallback Commands](fallback-commands.md) and [`http_response`](../globals/http_response.md).

## Important notes

- Always check `res.ok` before using `res.data`
- Default max response size is **2 MB** — see [Limits](limits.md)
- For streaming responses, see [Streaming](streaming.md)
- Validation errors (bad URL, invalid options) throw before any request is made
