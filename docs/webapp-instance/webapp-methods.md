# Webapp Methods

## `getUrl(command, { options, params })`

Generates a global webapp URL for the specified command.

- Use `options` for internal configuration.
- Use `params` for visible query parameters.

```javascript
let dashboardUrl = Webapp.getUrl("dashboard", {
  options: { theme: "dark", userId: 123 },
  params: { ref: "home", lang: "en" }
})

Api.sendMessage({
  text: `Open the web dashboard: ${dashboardUrl}`
})
```

## URL Design Tips

- Keep command names clear and predictable.
- Put internal app config in `options`.
- Put readable query values in `params`.
- Avoid passing sensitive data in URL params.
