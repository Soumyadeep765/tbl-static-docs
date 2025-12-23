## Response Object (res)

The **res instance** is used to send **custom HTTP responses** from webhook and Webapp commands.

It allows your bot to behave like an HTTP API or web endpoint.

Using `res`, you can return:

- JSON
- HTML
- XML
- Plain text
- Redirects
- Rendered templates (EJS)

Once a response is sent using `res`, execution ends.

## Response Methods

### set(key, value)

Sets HTTP headers on the response.

```js
res.set("Content-Type", "application/json")
   .set("X-Custom-Header", "my-value")
```

Headers can be chained.

### status(code)

Sets the HTTP response status code.

```js
res.status(200)
res.status(404)
res.status(500)
```

You can chain this with other methods.

### send(body)

Sends a response with **any content type**.

```js
res.send("Hello World")
res.send({ message: "Success", data: { id: 1 } })
res.status(201).send("Resource created")
```

The content type is auto-detected.

### json(obj)

Sends a JSON response with `application/json` content type.

```js
res.json({
  status: "success",
  user: user.name,
  data: processedData
})
```

This is the most common method for API-style responses.

### html(content)

Sends an HTML response.

If EJS tags are detected, the content is **automatically rendered**.

```js
res.html("<h1>Welcome</h1><p>Hello World</p>")
```

With EJS rendering:

```js
res.html(`
  <h1>Welcome <%= user.first_name %></h1>
  <p>Your ID: <%= user.id %></p>
  <% if (user.premium) { %>
    <div class='premium'>Premium User</div>
  <% } %>
`)
```

### xml(content)

Sends an XML response with `application/xml` content type.

```js
res.xml('<?xml version="1.0"?><response><status>success</status></response>')
```

### text(content)

Sends a plain text response.

EJS templates are auto-rendered if detected.

```js
res.text("This is plain text")

const textTemplate = "Hello <%= name %>, welcome!"
res.text(textTemplate)
```

### redirect(url)

Redirects the request to another URL or command.

```js
res.redirect("https://example.com/success")
res.redirect("/another-command")
```

Redirect responses are sent immediately.

### render(commandPath, options)

Renders another command’s output as the response.

Content type is detected automatically based on the target.

```js
res.render("user-profile")
```

With options:

```js
res.render("api-data.json", {
  data: { user: { name: "John", age: 30 } }
})
```

Rendering an HTML command:

```js
res.render("dashboard.html", {
  data: {
    user: user,
    stats: userStats,
    params: params
  }
})
```

## Notes

- The `res` instance is available **only in webhook and Webapp commands**
- Sending a response ends execution
- Headers, status, and body can be chained
- EJS rendering works automatically for HTML and text
- If no response is sent, a default **2xx** response is returned
