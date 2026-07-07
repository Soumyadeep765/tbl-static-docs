# tbl_options

Your custom note attached to a callback — "when this HTTP request finishes, here's the context."

## What is it?

**`tbl_options`** holds **custom data you pass to a callback command** when chaining [HTTP](../http-instance/index.md) requests or [Api](../api-instance/index.md) calls. It's your personal payload that rides along with the request and shows up when the callback command runs.

Normal commands don't get `tbl_options`. Callback commands do. It's a VIP pass for the second leg of a round trip.

## When would you use it?

Whenever a callback command needs to know **why** it was called:

- Which page of results to fetch next
- Which user started the flow
- A step number in a multi-step wizard
- Any context the callback can't infer from the HTTP response alone

If you just need the API response itself, that's [`options`](options.md). If you need *your* data alongside it, that's `tbl_options`.

---

## Try it — pass data in

```js
// HTTP: pass data to the success callback
HTTP.get("https://api.example.com/data", {
  success: "/onData",
  tbl_options: { page: 2, userId: user.id }
})

// API: pass data to a callback command
Api.sendMessage(chat.id, "Done!", {
  tbl_options: { step: 3 }
})
```

---

## Try it — read data in the callback

```js
// Inside /onData (HTTP success callback)
let page = tbl_options.page       // 2
let userId = tbl_options.userId   // who started this

Bot.sendMessage(userId, "Page " + page + " loaded!")
```

---

## `tbl_options` vs `options`

| Variable | Source |
| --- | --- |
| `tbl_options` | Explicitly passed via `tbl_options` in HTTP/API options |
| [`options`](options.md) | `Bot.run` data, full API JSON response, or webhook merge |

Both can be available in the same callback. `options` has the API result; `tbl_options` has what you packed.

---

## Good to know

- `tbl_options` exists only in **callback commands** — not normal Telegram commands
- If nothing is passed, it's **`null`** — not `undefined`
- Can be any type — object, string, number, array, etc.
- Read-only during callback execution
- Pair with [`content`](content.md) and [`http_response`](http_response.md) for the actual HTTP response data
