# Callbacks with on_run

Some Api calls finish later. Instead of blocking the whole command with `await`, you can tell TBL to run another command when Telegram responds.

That's `on_run`:

```js
Api.getMe({ on_run: "afterGetMe" })
```

When `getMe` completes, the `afterGetMe` command runs automatically. The response lands in [`options`](../globals/options.md).

## Why bother?

Splitting work across commands keeps each one readable. The first command starts the Api call. The second handles whatever came back. No nested if-blocks stretching down the page.

You'll see this pattern in bots that call several Telegram methods in sequence but don't want one giant command file.

## Reading the response

Inside `afterGetMe`:

```js
if (options.ok) {
  Api.sendMessage({
    text: "Running as @" + options.result.username
  })
} else {
  Api.sendMessage({ text: "Couldn't fetch bot info." })
}
```

`options.ok` tells you whether Telegram accepted the call. `options.result` holds the payload — shape depends on which Api method you used.

TBL passes this automatically. You don't serialize it yourself.

## Flow

```
Command A  →  Api.getMe({ on_run: "B" })  →  Telegram responds  →  Command B runs with options
```

Command A ends after firing the request. Command B picks up the thread.

## When to use on_run vs await

**`await`** when the next few lines in the *same* command need the result. Fetch chat info, then immediately send a message based on it — keep it together.

**`on_run`** when the follow-up is logically a separate step, or when you want to reuse the same handler command from multiple places.

Both are valid. It's mostly about how you like to organize commands.

## Requirements

- `on_run` must name a real command in your bot
- The callback command runs like any other — same globals, same instances
- Errors in the original call still surface through `options`; runtime typos still hit your `!` handler

## See also

- [Async Requests](async-requests.md) — `await` in one command  
- [options variable](../globals/options.md) — full picture of what gets passed
