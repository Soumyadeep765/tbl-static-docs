# Webapp Practical Examples

## JSON API Endpoint (User-Based Webhook)

This example returns structured JSON for a **user-based webhook** where the `user` object is available:

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
    The `user` object is available in **user-based webhooks only**. Public Webapp URLs do not include authenticated user context — use static or query-parameter data instead.

## Simple Public Dashboard Link

Generate a public Webapp URL and send it in a Telegram message:

```js
let publicDashboard = Webapp.getUrl("dashboard", {
  params: { ref: "docs", lang: "en" }
})

Api.sendMessage({
  text: `Open dashboard: ${publicDashboard}`
})
```

## Related Pages

- [Webapp overview](index.md)
- [Webapp Methods](webapp-methods.md)
- [Response (res) overview](../res-instance.md)
