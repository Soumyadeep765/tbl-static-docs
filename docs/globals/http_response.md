# The `http_response` Variable

In TBL, `http_response` contains the **full result** of a completed HTTP request. It is only available inside **HTTP callback commands** — commands triggered after an [HTTP](../http-instance/index.md) request finishes.

## When Available

| Context | `http_response` |
| --- | --- |
| HTTP success callback command | Full result object |
| HTTP error callback command | Full result object (check `response.ok`) |
| Normal Telegram command | `null` |
| Webhook command (no HTTP chain) | `null` |

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

## Convenience Aliases

TBL exposes shorthand globals in HTTP callback commands:

| Global | Same as |
| --- | --- |
| `response` | `http_response.response` |
| `headers` | `http_response.response.headers` |
| `cookies` | `http_response.response.cookies` |
| `content` | `http_response.response.content` |

## Example

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

## Usage

```javascript
// Inside HTTP success callback (/onSuccess)
if (response.ok && response.isJson) {
  Bot.sendMessage(user.id, `API says: ${response.data.message}`)
}

// Read a specific header
let rateLimit = headers['x-ratelimit-remaining']
```

## Important Notes

- `http_response` is read-only and exists only during callback execution
- Use `response.data` for parsed JSON on non-stream responses
- For `responseType: "stream"`, read body via `response.stream` — see [Streaming](../http-instance/streaming.md)
- For error handling on failed requests, see the [error](error.md) global in HTTP error callbacks
