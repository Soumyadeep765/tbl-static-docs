# Response Methods (`res`)

The `res` object allows **Webhook** and **Webapp** commands to send structured HTTP responses.

It supports JSON, HTML, XML, text, redirects, and template rendering.

## `set(key, value)`

Sets HTTP headers on the response object.

```javascript
res.set("Content-Type", "application/json")
   .set("X-Custom-Header", "my-value")
```

## `status(code)`

Sets the HTTP response status code.

```javascript
res.status(200)
res.status(404)
res.status(500)
```

## `send(body)`

Sends a response with any content type.

```javascript
res.send("Hello World")
res.send({ message: "Success", data: { id: 1 } })
res.status(201).send("Resource created")
```

## `json(obj)`

Sends a JSON response with `application/json` content type.

```javascript
res.json({
  status: "success",
  user: user.name,
  data: processedData
})
```

## `html(content)`

Sends an HTML response. Auto-renders EJS templates if tags are detected.

```javascript
res.html("<h1>Welcome</h1><p>Hello World</p>")

res.html(`
  <h1>Welcome <%= user.first_name %></h1>
  <p>Your ID: <%= user.id %></p>
  <% if (user.premium) { %>
    <div class='premium'>Premium User</div>
  <% } %>
`)
```

## `xml(content)`

Sends an XML response with `application/xml` content type.

```javascript
res.xml('<?xml version="1.0"?><response><status>success</status></response>')
```

## `text(content)`

Sends a plain text response. Auto-renders EJS templates if tags are detected.

```javascript
res.text("This is plain text")

const textTemplate = "Hello <%= name %>, welcome!"
res.text(textTemplate)
```

## `redirect(url)`

Redirects the request to a different URL.

```javascript
res.redirect("https://example.com/success")
res.redirect("/another-command")
```

## `render(commandPath, options)`

Renders another command output as response.

```javascript
res.render("user-profile")

res.render("api-data.json", {
  data: { user: { name: "John", age: 30 } }
})

res.render("dashboard.html", {
  data: {
    user: user,
    stats: userStats,
    params: params
  }
})
```
