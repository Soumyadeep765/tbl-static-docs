# The `http_response` Variable

In TBL, `http_response` contains **full information about an HTTP request result**.

It is **only available inside HTTP callback commands** (commands triggered after an HTTP request completes).

## When `http_response` Is Available

- Only for HTTP callback commands
- Not available in normal message-based commands
- Automatically provided after an HTTP request finishes

## What `http_response` Contains

The `http_response` variable is an **object** that includes:

- Request options
- HTTP response data
- Metadata like timestamps

## Demo `http_response` Object

Example structure of `http_response`:

```json
{
  "options": {
    "url": "https://webapi.telebothost.com/",
    "success": "/link"
  },
  "response": {
    "ok": true,
    "status": 200,
    "statusText": "",
    "content": "{\"status\":\"ok\",\"message\":\"API Service Running\"}",
    "data": {
      "status": "ok",
      "message": "API Service Running"
    },
    "isJson": true,
    "headers": {
      "server": "nginx/1.24.0 (Ubuntu)",
      "content-type": "application/json; charset=utf-8"
    },
    "cookies": [],
    "url": "https://webapi.telebothost.com/",
    "redirected": false,
    "redirectCount": 0
  },
  "timestamp": 1766335656394
}
```

## The `response` Variable

For convenience, TBL also exposes:

- `response` → same as `http_response.response`

This lets you access response details directly without referencing the full object.

## Commonly Used Response Fields

Inside `response`, you will often use:

- `response.ok` → request success status
- `response.status` → HTTP status code
- `response.content` → raw response body (string)
- `response.data` → parsed JSON data (if available)
- `response.isJson` → whether the response was JSON

## Headers and Cookies

Headers and cookies are also exposed directly.

- `headers` → same as `response.headers`
- `cookies` → same as `response.cookies`

This makes it easier to work with HTTP metadata.

## Important Notes

- `http_response` is read-only
- It exists only during the callback command execution
- Structure depends on the HTTP request and response
- `content` is always a string, even for JSON responses

The `http_response` variable is mainly used for **API integrations**, **external services**, and **data fetching workflows**.
