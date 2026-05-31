# Template Rendering with res.render()

This page covers how **`res.render()`** passes data into rendered commands and templates.

For the complete method reference and practical examples, see the [res.render() Guide](../res-instance-advanced.md).

## Automatic Content Type Detection

`res.render()` sets the correct `Content-Type` from the file extension:

```js
res.render("page.html")   // text/html
res.render("data.json")   // application/json
res.render("script.js")   // application/javascript
res.render("style.css")   // text/css
res.render("api.xml")     // application/xml
res.render("plain-text")  // text/plain
```

## Data Passing and Template Context

Pass data using the second argument:

```js
// Webapp URL: /webapp/showProfile?section=settings&view=compact

res.render("profile-template.html", {
  data: {
    user: user,
    profile: userProfile,
    preferences: userPrefs
  }
})
```

Inside the rendered template you can access:

- Custom fields from `data` (e.g. `profile`, `preferences`)
- `params` — URL query parameters (`{ section: "settings", view: "compact" }`)
- Global TBL variables (`Api`, `Bot`, `msg`, `request`, etc.)
- `user` — **only in user-based webhooks**, not in public Webapp URLs

!!! warning
    Webapp URLs are public and unsigned. Do not expose sensitive user data through public Webapp endpoints.

## See Also

- [res.render() Guide](../res-instance-advanced.md) — full documentation with examples
- [Response (res) overview](../res-instance.md) — all `res` methods
