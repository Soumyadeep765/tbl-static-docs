# Tips and Limitations

A few things about `Api` that aren't obvious until they bite you.

## Two different kinds of errors

**You typo'd the method name.**

```js
Api.hitMe()
```

TBL doesn't recognize `hitMe`. That's a runtime error in your command — execution stops, and your `!` handler can catch it if you've defined one.

**Telegram rejected a valid call.**

Wrong chat, user blocked the bot, bad parameter — the method existed, the request reached Telegram, Telegram said no. That usually **doesn't** throw. The command keeps going. The failure is logged in TeleBotHost's error panel.

If the failure matters to your logic, use `await` and inspect `ok`:

```js
let res = await Api.sendMessage({ text: "Reminder." })

if (!res.ok) {
  // handle it — maybe the user blocked you
}
```

## Prefer built-in methods

If `Api.sendMessage` exists, use it. Reach for `Api.call("sendMessage", {...})` only when TBL hasn't added a wrapper yet. Built-in methods are easier to read and less typo-prone.

## Case sensitivity

`Api.sendMessage` works. `Api.sendmessage` doesn't. Same for every method name.

## Chat context

Most calls assume the current chat. Explicit `chat_id` overrides that — and introduces a new way to get it wrong. Double-check the bot is actually allowed to message that chat.

## Always have a `!` command

Not Api-specific, but worth repeating: define the `!` error handler command. Something goes wrong in production, users see a message instead of silence.

## Reference

When in doubt, cross-check parameters against the [Telegram Bot API docs](https://core.telegram.org/bots/api). TBL passes them through faithfully.

For methods Telegram has but TBL hasn't wrapped yet, see [Dynamic Methods](dynamic-methods.md).
