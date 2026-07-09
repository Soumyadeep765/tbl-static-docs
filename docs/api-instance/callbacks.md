# Callbacks with on_run

Some `Api` calls finish later. Instead of blocking the whole command with `await`, you can tell the platform to **run another command when Telegram responds**.

That's **`on_run`**:

```js
Api.getMe({ on_run: "afterGetMe" })
```

When `getMe` completes, the `afterGetMe` command runs automatically. The response lands in [`options`](../globals/options.md). No nested if-blocks stretching down the page like a bad novel.

---

## What is on_run?

A way to split work across commands. The first command starts the `Api` call. The second handles whatever came back.

```
Command A  →  Api.getMe({ on_run: "B" })  →  Telegram responds  →  Command B runs with options
```

Command A ends after firing the request. Command B picks up the thread.

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Full picture of passed data: [`options`](../globals/options.md).

---

## How to use it

### Basic pattern

```js
// In command A
Api.getChat({ chat_id: chat.id, on_run: "afterGetChat" })
```

```js
// In afterGetChat — options holds Telegram's response
if (options.ok) {
  Api.sendMessage({ text: "Chat type: " + options.result.type })
} else {
  Api.sendMessage({ text: "Couldn't fetch chat info." })
}
```

`options.ok` tells you whether Telegram accepted the call. `options.result` holds the payload — shape depends on which `Api` method you used. Passed automatically. You don't serialize it yourself.

---

## Try it — copy-paste examples

### Fetch bot username in a separate command

```js
// In /check_bot
Api.getMe({ on_run: "show_bot_info" })
```

```js
// In show_bot_info
if (options.ok) {
  Api.sendMessage({
    text: "Running as @" + options.result.username
  })
} else {
  Api.sendMessage({ text: "Couldn't fetch bot info." })
}
```

### Reuse the same handler from multiple places

```js
// From /admin_panel
Api.getWebhookInfo({ on_run: "display_webhook_status" })

// From /debug_tools — same handler
Api.getWebhookInfo({ on_run: "display_webhook_status" })
```

One handler command, many entry points. DRY without the tears.

---

## When to use on_run vs await

**`await`** when the next few lines in the *same* command need the result. Fetch chat info, then immediately send a message based on it — keep it together.

**`on_run`** when the follow-up is logically a separate step, or when you want to reuse the same handler command from multiple places.

Both are valid. It's mostly about organization.

---

## Requirements

- `on_run` must name a **real command** in your bot
- The callback command runs like any other — same globals, same instances
- Errors in the original call still surface through `options`; runtime typos still hit your `!` handler

---

## See also

- [Async Requests](async-requests.md) — `await` in one command
- [`options` variable](../globals/options.md) — full picture of what gets passed
- [Inline Keyboards](inline-keyboards.md) — answering callback queries from button taps
