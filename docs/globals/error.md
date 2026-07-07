# The `error` Variable

In TBL, `error` contains **information about a failure** that triggered an error-handling command. The shape depends on which error handler ran.

## When `error` Is Available

| Trigger | Handler command | `error` shape |
| --- | --- | --- |
| Script exception or runtime error | `!` (error handler) | Error details object |
| HTTP request returned a non-2xx status | HTTP error callback command | Full HTTP response object |

In normal commands, `error` is `null`.

## Shape A: `!` Error Handler

When a command throws an error, TBL runs the `!` command with:

| Field | Type | Description |
| --- | --- | --- |
| `message` | `string` | Human-readable error message |
| `type` | `string` | Error type (e.g. `"Error"`, `"CleanError"`, `"ApiError"`) |
| `stack` | `string` | Sanitized stack trace (file paths redacted) |
| `timestamp` | `string` | ISO 8601 timestamp of when the error occurred |

```javascript
// Inside the ! command
Bot.sendMessage(owner.mail, `Error in ${filename}: ${error.message}`)
Bot.inspect(error.stack)
```

## Shape B: HTTP Error Callback

When an [HTTP](../http-instance/index.md) request fails and routes to an error callback command, `error` is the **full HTTP response object** (same structure as `response` in [http_response](http_response.md)):

| Field | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | `false` for failed requests |
| `status` | `number` | HTTP status code |
| `statusText` | `string` | Status text |
| `content` | `string` | Raw response body |
| `data` | `any` | Parsed JSON body (if applicable) |
| `error` | `Object` | Error details (`code`, `message`) when the request was blocked |
| `headers` | `Object` | Response headers |

```javascript
// Inside an HTTP error callback command
if (error.status === 404) {
  Bot.sendMessage(user.id, 'Resource not found.')
} else {
  Bot.sendMessage(user.id, `API error: ${error.status}`)
}
```

## Important Notes

- `error` is read-only and exists only during error-handling command execution
- The `!` handler is the right place for logging and user-friendly fallback messages
- Stack traces in the `!` handler are sanitized — internal paths are redacted
