# Async Requests

Put **`await`** in front of an `Api` call when the next line needs what Telegram sent back. Skip it when you don't care — extra awaits add wait time without benefit.

Simple rule: need the result? `await`. Fire-and-forget? Don't.

---

## What does await give you?

Execution pauses at the `await`, the request completes, and the variable holds Telegram's response. Then the command continues.

```js
let me = await Api.getMe()

if (me.ok) {
  Api.sendMessage({ text: "Bot id: " + me.result.id })
}
```

Responses follow Telegram's shape: typically `ok` (boolean) and `result` (the useful payload). Failed calls set `ok` to false.

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md).

---

## How to use it

### Check for failures

Wrong chat, user blocked the bot, bad parameter — Telegram said no. That usually **doesn't throw**. The command keeps going. The failure is logged in your platform error panel.

If the failure matters to your logic, use `await` and inspect `ok`:

```js
let res = await Api.sendMessage({ text: "Reminder." })

if (!res.ok) {
  // handle it — maybe the user blocked you
}
```

Without that check, the command runs as if nothing went wrong. Optimistic, but not always accurate.

### Message sends return something useful

When you `await Api.sendMessage`, the return value is also a **chainable object** — edit, delete, pin the message you just created:

```js
let sent = await Api.sendMessage({ text: "Loading..." })
await sent.editText("Done.")
```

See [Method Chaining](method-chaining.md) for the full list.

### Don't await everything

If you fire a message and don't care about the response:

```js
Api.sendMessage({ text: "Got it, processing." })
// command continues immediately
```

---

## Try it — copy-paste examples

### Fetch bot info, then reply

```js
let me = await Api.getMe()

if (me.ok) {
  Api.sendMessage({ text: "Running as @" + me.result.username })
} else {
  Api.sendMessage({ text: "Couldn't fetch bot info." })
}
```

### Dynamic calls work the same

```js
let chatInfo = await Api.call("getChat", { chat_id: chat.id })

if (chatInfo.ok) {
  Api.sendMessage({ text: "Chat title: " + chatInfo.result.title })
}
```

Same rules — check `ok`, read `result`.

---

## await vs on_run

| Pattern | When to use |
| --- | --- |
| **`await`** | Next few lines in the *same* command need the result |
| **`on_run`** | Follow-up is logically a separate command, or reused from multiple places |

Both are valid. It's mostly about how you like to organize commands. [Callbacks](callbacks.md) covers `on_run` in detail.

---

## See also

- [Callbacks](callbacks.md) — defer handling to another command with `on_run`
- [Tips and Limitations](tips-and-limitations.md) — platform errors vs Telegram errors
- [Method Chaining](method-chaining.md) — why `await` matters for send methods
