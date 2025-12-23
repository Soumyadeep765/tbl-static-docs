# The `options` Variable

In TBL, `options` contains **custom data passed between commands** or **data returned from API callbacks**.

It helps share context without using global state.

## How `options` Is Used

The `options` variable is commonly used in two cases:

- When chaining or triggering another command
- When receiving the result of a Telegram API call

## Custom Data Example

When passing custom data between commands, `options` may look like this:

```json
{
  "name": "Alice",
  "step": 2
}
```

This is useful for multi-step flows and internal state tracking.

## API Callback Example

When `options` comes from a Telegram API response, it may contain result data:

```json
{
  "ok": true,
  "result": { }
}
```

The `options` variable is mainly used for **advanced flows and integrations**.
