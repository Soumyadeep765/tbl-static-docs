## Handling Webhooks

Handling webhooks in TBL is **very easy**.

When a command is triggered via a webhook, you automatically get access to the **request** object.

This object contains all details about the incoming HTTP request.

## Accessing the request Object

Inside a webhook-triggered command, you can read `request`.

Example structure:

```json
{
  "url": "/ownlang/webhook/5484560?command=data&options=%7B%22level%22%3A10%7D&sig=...",
  "method": "GET",
  "headers": {
    "host": "prod-api.telebothost.com",
    "user-agent": "Reqable/2.33.12",
    "x-real-ip": "157.34.201.36"
  },
  "ip": "157.34.201.36",
  "query": {
    "command": "data",
    "options": "{\"level\":10}",
    "sig": "SECURE_SIGNATURE",
    "user": "5723455420",
    "ref": "profile",
    "lang": "en"
  },
  "body": null
}
```

This gives you full control over query parameters, headers, IP address, and request method.

## Difference from Telegram Updates

- For Telegram updates, data is available under `update.{type}`
- For webhook execution, data comes from the **request** object

This makes webhook handling closer to normal HTTP request handling.

## Message Sending in Webhooks

All other TBL features work the same inside webhook commands.

However, there is one important difference:

!!! warning
    In **global webhooks**, there is no user or chat context.

Because of this:

- Bot message helpers may not work automatically
- When using `Api.xxx`, you **must pass `chat_id` explicitly**

User-based webhooks do not have this limitation.

## Security & Restrictions

Some features may be **restricted or limited** in webhook commands.

This is intentional and helps:

- Prevent abuse
- Protect system resources
- Keep webhook execution safe

!!! note
    Webhooks are signed and verified automatically.
    Invalid or modified requests will not execute.

## Summary

- Webhook commands receive a `request` object
- Query parameters and headers are fully accessible
- Telegram updates use `update`, webhooks use `request`
- Global webhooks require explicit `chat_id` for sending messages
- Some features may be disabled for safety
