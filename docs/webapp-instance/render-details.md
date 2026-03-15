# `res.render()` In-Depth

## Automatic Content Type Detection

`res.render()` detects the content type from file extension.

```javascript
res.render("page.html")   // text/html
res.render("data.json")   // application/json
res.render("script.js")   // application/javascript
res.render("style.css")   // text/css
res.render("api.xml")     // application/xml
res.render("plain-text")  // text/plain
```

## Data Passing and Template Context

All rendering methods can access multiple data sources.

```javascript
// Webapp URL: /webapp/showProfile?section=settings&view=compact

res.render("profile-template.html", {
  data: {
    user: user,
    profile: userProfile,
    preferences: userPrefs
  }
})

// In profile-template.html you can access:
// - user, profile, preferences
// - params (from URL query string)
// - All TBL variables (msg, Api, State, etc.)
```
