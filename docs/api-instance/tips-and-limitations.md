# Tips and Limitations

A few things about **`Api`** that aren't obvious until they bite you. Consider this the "read before you ship" page — short, practical, and slightly paranoid in a healthy way.

---

## Two different kinds of errors

Not all failures look the same. Knowing which is which saves debugging hours.

### You typo'd the method name

```js
Api.hitMe()
```

The platform doesn't recognize `hitMe`. That's a **runtime error** in your command — execution stops, and your `!` handler can catch it if you've defined one.

### Telegram rejected a valid call

Wrong chat, user blocked the bot, bad parameter — the method existed, the request reached Telegram, Telegram said no. That usually **doesn't throw**. The command keeps going. The failure is logged in your platform error panel.

If the failure matters to your logic, use `await` and inspect `ok`:

```js
let res = await Api.sendMessage({ text: "Reminder." })

if (!res.ok) {
  // handle it — maybe the user blocked you
}
```

!!! tip "New to TBL?"
    Define a `!` error handler command. Something goes wrong in production, users see a message instead of silence.

---

## Prefer built-in methods

If `Api.sendMessage` exists, use it. Reach for `Api.call("sendMessage", {...})` only when a wrapper doesn't exist yet. Built-in methods are easier to read and less typo-prone.

| Do | Don't |
| --- | --- |
| `Api.sendMessage({ text: "Hi" })` | `Api.call("sendMessage", { text: "Hi" })` |
| `Api.getMe()` | `Api.call("getMe", {})` |

See [Dynamic Methods](dynamic-methods.md) for when `Api.call` is the right tool.

---

## Case sensitivity

`Api.sendMessage` works. `Api.sendmessage` doesn't. Same for every method name. The universe is cruel but consistent.

---

## Chat context

Most calls assume the **current chat**. Explicit `chat_id` overrides that — and introduces a new way to get it wrong. Double-check the bot is actually allowed to message that chat before you wonder why nothing arrived.

---

## bot_token on admin methods

A subset of bot-admin methods (`getMe`, `setWebhook`, `getMyCommands`, etc.) accept an optional `bot_token` to act on behalf of another bot.

Store alternate tokens in dashboard [ENV variables](../globals/process.md) — never hard-code them. See [Bot Admin Methods](bot-admin-methods.md).

---

## Always have a `!` command

Not `Api`-specific, but worth repeating: define the `!` error handler command. Runtime typos, unexpected failures, edge cases — users get a friendly message instead of the void.

---

## Reference

When in doubt, cross-check parameters against the [Telegram Bot API docs](https://core.telegram.org/bots/api). Parameters pass through faithfully. The platform targets **[Bot API 10.1](https://core.telegram.org/bots/api-changelog#june-11-2026)** compatibility — see the [Api overview](index.md#bot-api-101-support) for newly supported methods.

For methods Telegram has but the platform hasn't wrapped yet, see [Dynamic Methods](dynamic-methods.md).

---

## Quick checklist

| Before you ship | Check |
| --- | --- |
| Delivery failures handled? | `await` + `res.ok` where it matters |
| Method name spelled right? | Case-sensitive |
| Sending to another chat? | Bot has access |
| Alternate bot token? | In ENV, not in code |
| Error handler defined? | `!` command exists |
