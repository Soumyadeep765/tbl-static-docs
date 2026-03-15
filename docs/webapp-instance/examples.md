# Webapp Practical Examples

## JSON API Endpoint Example

```javascript
let userData = {
  id: user.id,
  name: user.first_name,
  premium: user.premium || false,
  join_date: user.join_date
}

// user object is available only on user-based webhook
res.status(200)
   .set("Access-Control-Allow-Origin", "*")
   .json({
     status: "success",
     data: userData,
     timestamp: Date.now()
   })
```

## Simple Public Dashboard Link Example

```javascript
let publicDashboard = Webapp.getUrl("dashboard", {
  params: { ref: "docs", lang: "en" }
})

Api.sendMessage({
  text: `Open dashboard: ${publicDashboard}`
})
```
