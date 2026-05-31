# Sending Custom HTTP Responses

In webhook and Webapp commands, you can send a **custom HTTP response** back to the caller using the built-in **`res`** instance.

This is useful when:

- Building APIs with TBL
- Returning JSON to external services
- Acknowledging webhook calls manually
- Serving HTML or redirect responses

## Using the res Instance

Send a JSON response like this:

```js
res.json({ ok: true })
```

This immediately sends a response to the caller and ends execution.

You can return any valid JSON object depending on your use case.

!!! tip
    Use `res.json()` when your endpoint acts like an API and the caller expects structured data.

## Notes

- The **`res`** instance is available in **webhook commands** and **Webapp commands**
- Once a response is sent, no further output is processed
- If no custom response is sent, a default **2xx** response is returned

## Full Reference

For all response methods (`json`, `html`, `render`, `redirect`, and more), see the [Response (res) overview](../res-instance.md).

For advanced template rendering, see the [res.render() Guide](../res-instance-advanced.md).
