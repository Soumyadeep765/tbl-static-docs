# content

The response body from an HTTP request — what's inside the envelope.

## What is it?

**`content`** is the **response body** from a completed [HTTP](../http-instance/index.md) request. It's a shortcut for `http_response.response.content` — the raw (or parsed) payload the remote server sent back.

Only exists inside **HTTP callback commands** — the commands that run after an HTTP request finishes. Normal Telegram commands don't have one. They weren't invited to the HTTP party.

## When would you use it?

- Read a plain-text API response
- Grab the raw body before deciding how to parse it
- Quick access when you don't need the full [`http_response`](http_response.md) wrapper

For **parsed JSON**, prefer `response.data` when `response.isJson` is `true`. For headers and status codes, use [`http_response`](http_response.md) or the `response` alias.

---

## Try it

```js
// Inside an HTTP success callback (/fetchData)
let body = content

// JSON response? Use response.data for the parsed object
if (response.isJson) {
  Bot.sendMessage("API says: " + response.data.message)
} else {
  Bot.sendMessage("Raw response: " + body)
}
```

---

## What `content` contains

Depends on the response type:

| Response type | `content` value |
| --- | --- |
| JSON API | Parsed object or JSON string |
| Plain text | String body |
| Binary | `Buffer` |
| Stream | Stream object (see [Streaming](../http-instance/streaming.md)) |

Example JSON response:

```json
{
  "status": true,
  "message": "Hello from API"
}
```

`content` may hold the parsed object or the raw string depending on how the response was handled. When in doubt, check `response.isJson` and use `response.data`.

---

## Related globals in HTTP callbacks

These shorthand aliases are also available:

| Global | Same as |
| --- | --- |
| [`http_response`](http_response.md) | Full request + response wrapper |
| `response` | `http_response.response` |
| `headers` | `response.headers` |
| `cookies` | `response.cookies` |

Your custom context from the original request lives in [`tbl_options`](tbl_options.md).

---

## Good to know

- `content` is only set in **HTTP callback commands** — not webhooks or normal Telegram commands
- Exists only during callback execution
- Failed requests route to an error callback — see [`error`](error.md)
