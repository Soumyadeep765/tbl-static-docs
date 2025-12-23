# res.render() In-Depth

The `res.render()` method is used to **render another command or template as an HTTP response**.

It automatically detects the response content type, renders templates when needed, and exposes useful context data to the rendered command.

This makes it ideal for building **web pages, APIs, dashboards, and webapps** using TBL.

## Automatic Content Type Detection

`res.render()` automatically sets the correct `Content-Type` based on the file extension.

Examples:

```js
res.render("page.html")        // Content-Type: text/html
res.render("data.json")        // Content-Type: application/json
res.render("script.js")        // Content-Type: application/javascript
res.render("style.css")        // Content-Type: text/css
res.render("api.xml")          // Content-Type: application/xml
res.render("plain-text")       // Content-Type: text/plain
```

No manual headers are required.

## Data Passing and Template Context

You can pass data to `res.render()` using the second argument.

Example webapp URL:

/webapp/showProfile?section=settings&view=compact

Example render call:

```js
res.render("profile-template.html", {
  data: {
    user: user,
    profile: userProfile,
    preferences: userPrefs
  }
})
```

### Available Data Inside the Rendered Template

Inside `profile-template.html`, you can access:

- `user` – current user object (user-based webhook only)
- `profile` – custom data passed via `data`
- `preferences` – custom data passed via `data`
- `params` – URL query parameters  
  `{ section: "settings", view: "compact" }`
- All global TBL variables (`Api`, `Bot`, `msg`, `request`, etc.)

Example usage inside template:

```html
<h1>Welcome <%= user.first_name %></h1>
<p>Profile: <%= profile %></p>
```

## Practical Examples

### Example 1: JSON API Endpoint

This example returns structured JSON data.

```js
let userData = {
  id: user.id,
  name: user.first_name,
  premium: user.premium || false,
  join_date: user.join_date
}

res.status(200)
   .set("Access-Control-Allow-Origin", "*")
   .json({
     status: "success",
     data: userData,
     timestamp: Date.now()
   })
```

!!! note
    The `user` object is available **only in user-based webhooks**.

### Example 2: Render an HTML Page

```js
res.render("dashboard.html", {
  data: {
    stats: statsData,
    user: user
  }
})
```

This renders an HTML page with EJS support.

### Example 3: Render JSON via Template

```js
res.render("api-response.json", {
  data: {
    ok: true,
    result: resultData
  }
})
```

Content type is automatically set to `application/json`.

## Important Notes

- `res.render()` ends execution immediately
- Content type is detected automatically
- EJS rendering works for HTML and text
- `params` always contains query parameters
- User data is available only in user-based webhooks

!!! tip
    Use `res.render()` to keep API logic and presentation cleanly separated.
