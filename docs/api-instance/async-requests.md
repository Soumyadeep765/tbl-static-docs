# Async Requests

Put `await` in front of an Api call when the next line needs what Telegram sent back.

```js
let me = await Api.getMe()

if (me.ok) {
  Api.sendMessage({ text: "Bot id: " + me.result.id })
}
```

Execution pauses at the `await`, the request completes, and `me` holds the response. Then the command continues.

## What you get back

Responses follow Telegram's shape: typically `ok` (boolean) and `result` (the useful payload). Failed calls set `ok` to false — check it when the failure would change your logic.

```js
let sent = await Api.sendMessage({ text: "Hello again." })

if (!sent.ok) {
  // user blocked the bot, chat gone, etc.
}
```

Without that check, the failure only appears in your platform error logs. The command keeps running as if nothing went wrong.

## Message sends return something useful

When you `await Api.sendMessage`, the return value is also a chainable object — edit, delete, pin the message you just created. See [Method Chaining](method-chaining.md).

```js
let sent = await Api.sendMessage({ text: "Loading..." })
await sent.editText("Done.")
```

## Don't await everything

If you fire a message and don't care about the response, skip `await`:

```js
Api.sendMessage({ text: "Got it, processing." })
// command continues immediately
```

Extra awaits add wait time without benefit.

## Works with dynamic calls too

```js
let chat = await Api.call("getChat", { chat_id: chat.id })
```

Same rules — check `ok`, read `result`.

## See also

- [Callbacks](callbacks.md) — defer handling to another command with `on_run`  
- [Tips and Limitations](tips-and-limitations.md) — TBL errors vs Telegram errors
