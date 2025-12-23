## Global Webhooks

Global webhooks execute commands **without any user context**.

They are designed for system-level or public actions where no specific user or chat is involved.

In global webhooks:

- `user` is `null`
- `chat` is `null`
- The command runs at the **account level**

These are ideal for dashboards, public pages, cron jobs, or backend services.

## Generate a Global Webhook URL

### getGlobalUrl(command, { options, params, redirect })

Creates a **globally accessible webhook URL**.

This URL does not require user authentication and can be triggered by any external source.

- `command` → command to execute
- `options` → custom data passed to the command
- `params` → extra query parameters
- `redirect` → optional URL to redirect after execution

Example:

```js
let statsUrl = Webhook.getGlobalUrl("getStats", {
  options: { days: 30 },
  redirect: "https://telebothost.com",
  params: { ref: "home" }
})

Api.sendMessage({
  text: `View global statistics: ${statsUrl}`
})
```

## How Global Webhooks Behave

- Commands run **without user or chat data**
- Useful for account-wide logic
- Suitable for read-only or system actions
- Safe for public or automated triggers

!!! warning
    Since global webhooks have no user context,
    avoid using them for actions that modify user data.

## Execution & Response

- Global webhook execution returns a **2xx HTTP response** by default
- Redirects are handled automatically if `redirect` is provided
- You can manually control responses using the **[res]** instance

## Notes

- Global webhooks are secure and signed
- Parameters and options are protected
- Best used for dashboards, analytics, and automation

[res]: ../res-instance.md