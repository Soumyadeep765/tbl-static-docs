# The `tbl_options` Variable

In TBL, `tbl_options` holds **custom data you pass to a callback command** when chaining HTTP requests or API calls. It is not available in normal command execution.

## When `tbl_options` Is Set

| Flow | How to pass |
| --- | --- |
| HTTP request callback | Pass `tbl_options` in the HTTP request options |
| API method callback | Pass `tbl_options` in the API call options |

```javascript
// HTTP: pass data to the success callback
HTTP.get('https://api.example.com/data', {
  success: '/onData',
  tbl_options: { page: 2, userId: user.id }
})

// API: pass data to a callback command
Api.sendMessage(chat.id, 'Done!', {
  tbl_options: { step: 3 }
})
```

## Reading in the Callback Command

```javascript
// Inside /onData (HTTP callback)
let page = tbl_options.page
let userId = tbl_options.userId
```

## Value When Not Set

If nothing is passed, `tbl_options` is **`null`** — not `undefined`.

## `tbl_options` vs `options`

| Variable | Source |
| --- | --- |
| `tbl_options` | Explicitly passed via `tbl_options` in HTTP/API options |
| `options` | `Bot.run` data, full API JSON response, or webhook merge |

Use `tbl_options` when you need to pass your own context through a callback. Use `options` for API results or `Bot.run` payloads.

## Important Notes

- `tbl_options` exists only in callback commands
- It can be any type — object, string, number, array, etc.
- It is read-only during callback execution
