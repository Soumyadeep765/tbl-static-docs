# The `content` Variable

In TBL, `content` contains the **response body returned from an HTTP request**.

It represents the main data received from the server.

## How `content` Works

When you make an HTTP request:

- The response body is converted to text
- That text is stored in `content`
- The value is usually **stringified data**

For example, if an API returns JSON, `content` will contain it as a string.

## Demo Example

Example value of `content`:

```json
"{\"status\":true,\"message\":\"Hello from API\"}"
```

You can then parse or process this value in your logic if needed.

## Important Notes

- `content` contains text data
- It exists only during command execution
- Its value depends on the HTTP response

The `content` variable is mainly used when working with external APIs.
