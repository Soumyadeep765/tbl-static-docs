## User-Based Webhooks

User-based webhooks execute commands **in the context of a user**.  
This means `user` and `chat` are available inside the command.

They are useful for triggering bot actions from websites, dashboards, or external APIs **on behalf of a user**.

## Generate Webhook for Current User

### getUrl(command, { options, params, redirect })

Generates a **secure webhook URL** for the **current user**.

- `command` → command to execute
- `options` → custom data passed to the command
- `params` → extra query parameters
- `redirect` → optional URL to redirect after execution

Example:

```js
let syncUrl = Webhook.getUrl("syncGameData", {
  options: { level: 10 },
  params: { ref: "profile", lang: "en" }
})

Api.sendMessage({
  text: `Sync your game data: ${syncUrl}`
})
```

## Generate Webhook for a Specific User

### getUrlFor({ user_id, command, options, params, redirect })

Generates a **personalized webhook URL** for a specific user ID.

This is ideal for sending links that should work only for a given user.

Example:

```js
let upgradeUrl = Webhook.getUrlFor({
  user_id: 123,
  command: "syncGameData",
  redirect: "https://telebothost.com",
  options: { plan: "pro" },
  params: { ref: "upgrade" }
})

Api.sendMessage({
  text: `Upgrade your plan here: ${upgradeUrl}`
})
```

## Example Webhook URL

A generated webhook URL may look like this:

```
https://prod-api.telebothost.com/ownlang/webhook/XXXXXXX
?command=syncGameData
&options=%7B%22level%22%3A10%7D
&sig=SECURE_SIGNATURE
&user=USER_ID
&ref=profile
&lang=en
```

Values are signed and protected.  
Changing them will invalidate the request.

## Execution & Response

- By default, webhook execution returns a **2xx HTTP response**
- This indicates successful command execution
- Redirects are handled automatically when `redirect` is provided

!!! note
    You can also use the **[res]** instance to control the HTTP response manually.

[res]: ../res-instance.md

## Notes

- User-based webhooks always include user context
- `user` and `chat` are available in the command
- Options and params are safely signed
- URLs cannot be forged or reused for other users
- Ideal for user-specific actions and flows
