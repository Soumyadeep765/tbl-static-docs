# Redirects

Send an HTTP redirect with `res.redirect(url)`. Browsers follow it; API clients get a `302` (or similar) and the `Location` header.

---

## `redirect(url)`

Redirects the client to another URL. **Only HTTPS URLs are allowed.**

```js
res.redirect("https://example.com/success")
```

### Invalid URLs

Non-HTTPS or malformed URLs return **400 JSON**:

```json
{
  "error": "Invalid redirect",
  "message": "Only HTTPS redirect URLs are allowed"
}
```

Relative paths like `/another-page` are **not** accepted — use a full `https://` URL.

---

## Webhook `redirect` query parameter

When generating webhook URLs, you can pass a `redirect` option to **prefetch external content** into the global [`content`](../globals/content.md) variable — this is separate from `res.redirect()`.

Think of it as "fetch this URL before my command runs" vs "send the browser somewhere after."

| Method | `redirect` support |
| --- | --- |
| `Webhook.getUrl()` | **No** |
| `Webhook.getUrlFor()` | Yes |
| `Webhook.getGlobalUrl()` | Yes |

Example:

```js
let url = Webhook.getGlobalUrl("processFeed", {
  redirect: "https://api.example.com/data.json",
  options: { source: "cron" }
})
```

When the webhook runs, the platform fetches the redirect URL (HTTPS only, size/time limited) and exposes the result as `content` inside your command. Your command can then process it and optionally call `res.redirect()` to send the browser elsewhere.

---

## Try it — copy-paste examples

### Redirect after processing

```js
await db.bot.set("last_sync", Date.now())
res.redirect("https://myapp.com/dashboard?synced=1")
```

### JSON response instead of redirect

```js
// Caller expects JSON — don't redirect
res.json({ ok: true, synced: true })
```

---

## See also

- [User-Based Webhooks](../webhook-instance/user-webhook.md) — `getUrlFor` with `redirect`
- [Global Webhooks](../webhook-instance/global-webhook.md) — `getGlobalUrl` with `redirect`
- [`content`](../globals/content.md) — prefetched redirect body
