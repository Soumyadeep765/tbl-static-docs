# Fallback Commands

Chain HTTP requests to other commands using `success` and `error`. The HTTP call returns immediately; callback commands run when the response arrives.

## Basic setup

```js
HTTP.get({
  url: "https://api.example.com/todos/1",
  success: "/onSuccess",
  error: "/onError",
  tbl_options: { source: "menu" }
})
```

| Option | When it runs |
| --- | --- |
| `success` | HTTP status is **2xx** (`res.ok === true`) |
| `error` | HTTP status is **not 2xx** (`res.ok === false`) |

If the request fails and `error` is **not defined**, no callback command runs. Use `await` inline when you need to handle failures in the same command.

## Passing data with `tbl_options`

```js
HTTP.post({
  url: "https://api.example.com/order",
  body: { item: params },
  success: "/onOrderDone",
  tbl_options: { item: params, userId: user.id }
})
```

Inside `/onOrderDone`, read `tbl_options.item` and `tbl_options.userId`. See [`tbl_options`](../globals/tbl_options.md).

## Success callback (`/onSuccess`)

When the request succeeds, these globals are available:

| Global | Description |
| --- | --- |
| `http_response` | Full result wrapper |
| `response` | Parsed HTTP response object |
| `content` | Raw body (`response.content`) |
| `headers` | Response headers |
| `cookies` | Parsed cookies |
| `tbl_options` | What you passed in the request |

```js
// Command: /onSuccess
if (response.ok && response.isJson) {
  Bot.sendMessage(chat.id, "Title: " + response.data.title)
} else {
  Bot.sendMessage(chat.id, "Response: " + content)
}
```

## Error callback (`/onError`)

When the request fails (non-2xx), the `error` global contains the **full HTTP response object**:

| Field | Example |
| --- | --- |
| `error.status` | `404`, `500` |
| `error.ok` | `false` |
| `error.content` | Error body string |
| `error.data` | Parsed error JSON (if applicable) |
| `error.error.code` | Machine-readable code (e.g. `"TIMEOUT"`) |
| `error.error.message` | Human-readable message |

```js
// Command: /onError
if (error.status === 404) {
  Bot.sendMessage(chat.id, "Resource not found.")
} else if (error.status === 408 || error.error?.code === "TIMEOUT") {
  Bot.sendMessage(chat.id, "Request timed out.")
} else {
  Bot.sendMessage(chat.id, "Request failed: " + error.status)
}
```

`http_response`, `response`, `content`, `headers`, and `cookies` are also set the same way as in success callbacks.

## Inline vs callback

| Approach | Best for |
| --- | --- |
| `await HTTP.get(...)` | Same command needs the result immediately |
| `success` / `error` | Fire-and-forget, keep commands short, multi-step pipelines |

```js
// Inline — handle in same command
let res = await HTTP.get("https://api.example.com/price")
if (res.ok) Bot.sendMessage(chat.id, "$" + res.data.price)

// Callback — delegate to another command
HTTP.get({
  url: "https://api.example.com/price",
  success: "/showPrice",
  error: "/priceUnavailable"
})
```

## Command chain limit

Each `success` or `error` callback counts toward the **6-command chain limit** per execution (same as `Bot.run`). Deep HTTP → command → HTTP chains should be kept shallow.

## What fallback commands do not catch

| Not caught by `error` callback | Handle with |
| --- | --- |
| TBL script errors in the same command | `!` error handler |
| Invalid HTTP options (bad URL, etc.) | `!` error handler (throws before request) |
| Network-level throws in validation | `!` error handler |

## Full pipeline example

```js
// /fetchWeather command
HTTP.get({
  url: "https://api.weather.com/current",
  query: { city: params },
  headers: { "X-Key": process.env.WEATHER_API_KEY },
  success: "/showWeather",
  error: "/weatherError",
  tbl_options: { city: params }
})

Bot.sendMessage(chat.id, "Fetching weather for " + params + "...")
```

```js
// /showWeather command
let temp = response.data.temperature
Bot.sendMessage(chat.id, tbl_options.city + ": " + temp + "°")
```

```js
// /weatherError command
Bot.sendMessage(chat.id, "Could not fetch weather (" + error.status + ")")
```

## Important notes

- Callback commands have full access to `Bot`, `Api`, `db`, and globals
- `HTTP` is **not available** inside broadcast commands
- Response globals exist only during callback command execution
- See [Responses](responses.md) for the full response object reference
