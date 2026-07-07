# Dynamic Methods

Telegram adds API methods regularly. The platform adds wrappers for the common ones, but you shouldn't have to wait for an update to use something new in Telegram's docs.

**`Api.call()`** forwards any official method by name:

```js
Api.call("getChat", { chat_id: chat.id })
```

First argument: exact Telegram method name. Second: parameter object, same as the API reference. Same contract as built-in methods — `await`, `ok`/`result`, `on_run`, all of it.

---

## What is Api.call?

A escape hatch for Telegram methods that don't have a dedicated `Api.something` wrapper yet. When the wrapper exists, use the wrapper. When it doesn't, call it directly.

Recent additions already wrapped as built-in methods include `sendRichMessage`, `verifyUser`, `answerChatJoinRequestQuery`, and `getManagedBotToken`. Check the [Api overview](index.md#bot-api-101-support) before reaching for `Api.call`.

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md).

---

## How to use it

### When to use built-in vs dynamic

| Situation | Use |
| --- | --- |
| Wrapper exists (`Api.sendMessage`) | Built-in — reads better |
| New Telegram feature, niche method | `Api.call("methodName", {...})` |
| Not sure if wrapped | Check [Api overview](index.md) first |

```js
// Prefer this when it exists
Api.sendMessage({ text: "Hello." })

// Not this
Api.call("sendMessage", { text: "Hello." })
```

### Await and check ok

```js
let res = await Api.call("getChatMember", {
  chat_id: chat.id,
  user_id: user.id
})

if (res.ok) {
  Api.sendMessage({ text: "Member status: " + res.result.status })
}
```

### on_run works too

```js
Api.call("getChat", { chat_id: chat.id, on_run: "afterGetChat" })
```

Same as built-in methods — response lands in [`options`](../globals/options.md).

---

## Try it — copy-paste examples

### Get chat member info

```js
let res = await Api.call("getChatMember", {
  chat_id: chat.id,
  user_id: user.id
})

if (res.ok && res.result.status === "administrator") {
  Api.sendMessage({ text: "You're an admin here." })
}
```

### Hypothetical — if getChat weren't built in

```js
Api.call("getChat", { chat_id: 4444443444 })
```

In practice, prefer `Api.getChat` when you see it in the docs. Keep `Api.call` for the gaps.

---

## Parameters are on you

The platform doesn't validate dynamic calls against Telegram's schema. Wrong parameter name? Telegram errors. Check the [official API docs](https://core.telegram.org/bots/api) — parameter names must match **exactly**.

---

## bot_token and Api.call

`Api.call()` does **not** accept `bot_token`. It always uses the current bot's token. To call Telegram with a different token, use a built-in [Bot Admin Method](bot-admin-methods.md) such as:

```js
await Api.getMe({ bot_token: process.env.OTHER_TOKEN })
```

---

## Important notes

- Prefer built-in wrappers when they exist — less typo-prone, easier to read
- Case-sensitive method names — must match Telegram's docs exactly
- Same error behavior as built-in methods — check `res.ok` when failures matter
