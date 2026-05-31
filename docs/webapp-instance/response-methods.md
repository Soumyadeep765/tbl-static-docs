# Response Methods (`res`)

This page is a quick reference for **`res`** methods in webhook and Webapp commands.

For full explanations, examples, and notes, see the canonical [Response (res) overview](../res-instance.md).

## Method Summary

| Method | Purpose |
| --- | --- |
| `set(key, value)` | Set HTTP response headers |
| `status(code)` | Set HTTP status code |
| `send(body)` | Send any content type (auto-detected) |
| `json(obj)` | Send JSON with `application/json` |
| `html(content)` | Send HTML (EJS auto-rendered if detected) |
| `xml(content)` | Send XML with `application/xml` |
| `text(content)` | Send plain text (EJS auto-rendered if detected) |
| `redirect(url)` | Redirect to a URL or command |
| `render(path, options)` | Render another command as the response |

## Quick Examples

```js
// JSON API response
res.status(200).json({ status: "success", data: result })

// HTML page
res.html("<h1>Welcome</h1>")

// Redirect
res.redirect("https://example.com/done")

// Render a template command
res.render("dashboard.html", { data: { stats: statsData } })
```

## Related Pages

- [Response (res) overview](../res-instance.md) — full method documentation
- [res.render() Guide](../res-instance-advanced.md) — content types, template context, and examples
- [Template Rendering](render-details.md) — short guide to template data and query params
