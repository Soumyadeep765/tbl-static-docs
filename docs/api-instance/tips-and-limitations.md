## Notes About Api.xxx

The `Api` instance is designed for **direct communication with Telegram**.

Every call you make using `Api.xxx()` is sent straight to the Telegram Bot API.

## Invalid Api Method Calls

If you call a method that **does not exist**, for example:

```js
Api.hitMe()
```

This is a **TBL-side error**, not a Telegram error.

What happens:

- TBL throws a runtime error
- The error can be handled using the `!` command
- Execution stops for that command

!!! warning
    Calling a non-existent Api method will always trigger an error.
    Make sure the method exists or use `Api.call()` for dynamic methods.

## Telegram API Errors

Errors returned **by Telegram itself** behave differently.

For example:

- Invalid parameters
- Permission issues
- Chat not found
- Bot blocked by user

In these cases:

- The Api call does **not crash execution**
- The error is **logged in the platform’s bot error logs**
- The command continues running unless you explicitly check the response

Telegram API errors are considered **silent by default**.

## Handling Telegram Errors with await

If you use `await`, you can manually inspect the Telegram response.

```js
let res = await Api.sendMessage({ text: "Hello!" })

if (!res.ok) {
  Api.sendMessage({ text: "Failed to send message" })
}
```

This allows you to:

- Detect Telegram-side failures
- Handle them gracefully
- Avoid relying only on platform logs

!!! tip
    Use `await` when you need confirmation that a Telegram action succeeded.

## Error Handling Summary

- Invalid `Api.xxx` method → TBL error → handled by `!`
- Telegram API error → silent → logged on platform
- `await` lets you manually detect Telegram failures

## Best Practices

- Use valid Api method names
- Prefer built-in Api methods when available
- Use `Api.call()` for unsupported Telegram methods
- Use `await` when the result matters
- Always define a `!` command for safety

Understanding this difference helps you debug bots faster and write more reliable logic.
