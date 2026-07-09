# error

Something went wrong — here's what happened.

## What is it?

**`error`** contains **information about a failure** that triggered an error-handling command. It's your bot's "incident report" — what broke, when, and (sometimes) why.

In normal commands, `error` is `null`. Everything is fine. Nothing to see here.

It only shows up in two special places: the **`!` error handler** (when a script throws) and **HTTP error callback commands** (when a request returns a non-2xx status).

## When would you use it?

- Log failures to the owner in your `!` handler
- Send user-friendly fallback messages after a crash
- Handle API errors gracefully in HTTP error callbacks (404, 500, rate limits)
- Inspect stack traces for debugging (sanitized — internal paths are redacted)

Pair with [`owner`](owner.md) for alerting and [`http_response`](http_response.md) for successful HTTP flows.

---

## Try it — script errors (`!` handler)

When any command throws, the `!` command runs with:

```js
// Inside the ! command
Bot.sendMessage(owner.mail, "Error: " + error.message)
Bot.inspect(error.stack)
```

| Field | Type | Description |
| --- | --- | --- |
| `message` | `string` | Human-readable error message |
| `type` | `string` | Error type (e.g. `"Error"`, `"CleanError"`, `"ApiError"`) |
| `stack` | `string` | Sanitized stack trace (file paths redacted) |
| `timestamp` | `string` | ISO 8601 timestamp of when the error occurred |

---

## Try it — HTTP error callbacks

When an [HTTP](../http-instance/index.md) request fails and routes to an error callback, `error` is the **full HTTP response object** (same structure as `response` in [`http_response`](http_response.md)):

```js
// Inside an HTTP error callback command
if (error.status === 404) {
  Bot.sendMessage(user.id, "Resource not found.")
} else if (error.status === 429) {
  Bot.sendMessage(user.id, "Too many requests. Slow down!")
} else {
  Bot.sendMessage(user.id, "API error: " + error.status)
}
```

| Field | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | `false` for failed requests |
| `status` | `number` | HTTP status code |
| `statusText` | `string` | Status text |
| `content` | `string` | Raw response body |
| `data` | `any` | Parsed JSON body (if applicable) |
| `error` | `Object` | Error details (`code`, `message`) when the request was blocked |
| `headers` | `Object` | Response headers |

---

## Which handler ran?

| Trigger | Handler command | `error` shape |
| --- | --- | --- |
| Script exception or runtime error | `!` (error handler) | Error details object |
| HTTP request returned non-2xx | HTTP error callback command | Full HTTP response object |
| Normal command | — | `null` |

---

## Good to know

- `error` is read-only and exists only during error-handling command execution
- The `!` handler is the right place for logging and graceful fallbacks — don't let users see raw stack traces
- Stack traces in the `!` handler are sanitized for safety
