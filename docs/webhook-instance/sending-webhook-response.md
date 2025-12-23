## Sending Custom HTTP Responses

In webhook commands, you can also **send a custom HTTP response** back to the server using the built-in **[res]** instance.

This is useful when:

- Building APIs with TBL
- Returning JSON to external services
- Acknowledging webhook calls manually
- Creating custom webhook responses

## Using the res Instance

You can send a JSON response like this:

```js
res.json({ ok: true })

```

This immediately sends a response to the caller and ends execution.

You can return any valid JSON object depending on your use case.

!!! tip
    Use `res.json()` when your webhook is acting like an API endpoint
    and the caller expects a structured response.

## Notes

- The **[res]** instance is available **only in webhook commands**
- Once a response is sent, no further output is processed
- If no custom response is sent, a default **2xx** response is returned

For full details and advanced usage, see the official documentation:

[res]: ../res-instance.md
