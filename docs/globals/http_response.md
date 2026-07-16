# http_response

The full receipt from an HTTP request — status, headers, body, and all.

## What is it?

**`http_response`** contains the **complete result** of a finished [HTTP](../http-instance/index.md) request. It's only available inside **HTTP callback commands** — the commands that run after a request succeeds or fails.

Think of it as the delivery confirmation: what you asked for, what came back, and whether the server was happy about it.

## When would you use it?

- Read status codes and response bodies from external APIs
- Check response headers (rate limits, content type)
- Access cookies from authenticated requests
- Inspect the original request options (URL, callback routes, [`tbl_options`](tbl_options.md))

For just the body, [`content`](content.md) is a shorter path. For failures, the error callback gets the response as [`error`](error.md).

---

## Try it

```js
// Inside HTTP success callback (/onSuccess)
if (response.ok && response.isJson) {
  Bot.sendMessage("API says: " + response.data.message)
}

// Read a rate-limit header
let remaining = headers["x-ratelimit-remaining"]
if (remaining && Number(remaining) < 5) {
  Bot.sendMessage("Running low on API quota!")
}

// Check what you originally requested
Bot.inspect("Fetched: " + http_response.url)
```

---

## When is it available?

| Context | `http_response` |
| --- | --- |
| HTTP success callback command | Full result object |
| HTTP error callback command | Full result object (check `response.ok`) |
| Normal Telegram command | `null` |
| Webhook command (no HTTP chain) | `null` |

---

## Structure

| Field | Type | Description |
| --- | --- | --- |
| `options` | `Object` | Original HTTP request options (`url`, `success`, `error`, `tbl_options`, etc.) |
| `response` | `Object` | Parsed HTTP response (see below) |
| `timestamp` | `number` | `Date.now()` when the response was received |
| `url` | `string` | Request URL |

### `response` sub-object

| Field | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | `true` for HTTP 2xx responses |
| `status` | `number` | HTTP status code |
| `statusText` | `string` | HTTP status text |
| `headers` | `Object` | Response headers |
| `url` | `string` | Final URL after redirects |
| `redirected` | `boolean` | Whether a redirect occurred |
| `redirectCount` | `number` | Number of redirects followed |
| `content` | `string/Buffer/object` | Raw body — **not set** when `isStream: true` |
| `data` | `any` | Parsed JSON or body — **not set** when `isStream: true` |
| `isJson` | `boolean` | Whether body was JSON-parsed — **not set** on streams |
| `cookies` | `object` | Parsed cookies |
| `isStream` | `boolean` | `true` when `responseType: "stream"` |
| `responseType` | `string` | `"auto"`, `"json"`, `"text"`, `"buffer"`, `"arrayBuffer"`, or `"stream"` |
| `contentType` | `string` | Content-Type header (stream responses) |
| `stream` | `object` | `read()`, `collect()`, `cancel()`, async iterator — see [Streaming](../http-instance/streaming.md) |

### Example object

```json
{
  "options": {
    "url": "https://api.example.com/status",
    "success": "/onSuccess"
  },
  "response": {
    "ok": true,
    "status": 200,
    "statusText": "OK",
    "content": "{\"status\":\"ok\"}",
    "data": { "status": "ok" },
    "isJson": true,
    "headers": { "content-type": "application/json" },
    "cookies": [],
    "url": "https://api.example.com/status",
    "redirected": false,
    "redirectCount": 0
  },
  "timestamp": 1766335656394,
  "url": "https://api.example.com/status"
}
```

---

## Convenience aliases

Shorthand globals available in HTTP callback commands:

| Global | Same as |
| --- | --- |
| `response` | `http_response.response` |
| `headers` | `http_response.response.headers` |
| `cookies` | `http_response.response.cookies` |
| [`content`](content.md) | `http_response.response.content` |

---

## Good to know

- `http_response` is read-only and exists only during callback execution
- Use `response.data` for parsed JSON on non-stream responses
- For `responseType: "stream"`, read the body via `response.stream` — see [Streaming](../http-instance/streaming.md)
- Failed requests? See [`error`](error.md) in HTTP error callbacks
