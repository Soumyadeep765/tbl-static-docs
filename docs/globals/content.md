# The `content` Variable

In TBL, `content` contains the **response body** from a completed HTTP request. It is only available inside **HTTP callback commands** — commands that run after an [HTTP](../http-instance/index.md) request finishes.

## How `content` Works

`content` is a shortcut for `http_response.response.content`. Depending on the response type, it may be:

| Response type | `content` value |
| --- | --- |
| JSON API | Parsed object or JSON string |
| Plain text | String body |
| Binary | `Buffer` |
| Stream | Stream object (see [http_response](http_response.md)) |

```javascript
// Inside an HTTP success callback command (/fetchData)
let body = content

// If JSON was auto-parsed, use response.data instead
let data = response.data
```

## Example

After fetching an API that returns JSON:

```json
{
  "status": true,
  "message": "Hello from API"
}
```

`content` may contain the parsed object or the raw string depending on the response. Use `response.data` when `response.isJson` is `true` for the parsed result.

## Related Globals

In HTTP callback commands, these are also available:

| Global | Same as |
| --- | --- |
| `http_response` | Full request + response wrapper |
| `response` | `http_response.response` |
| `headers` | `response.headers` |
| `cookies` | `response.cookies` |

## Important Notes

- `content` is only set in HTTP callback commands — not in webhook body responses or normal Telegram commands
- It exists only during the callback command execution
- Prefer `response.data` for parsed JSON and `response.content` for the raw body
