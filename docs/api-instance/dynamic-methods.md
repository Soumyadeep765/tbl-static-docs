# Dynamic Methods

Telegram adds API methods regularly. TBL adds wrappers for the common ones, but you shouldn't have to wait for a platform update to use something new in Telegram's docs.

`Api.call()` forwards any official method by name:

```js
Api.call("getChat", { chat_id: chat.id })
```

First argument: exact Telegram method name. Second: parameter object, same as the API reference.

## When to use it

**Use built-in methods when they exist.** `Api.sendMessage` reads better than `Api.call("sendMessage", ...)`.

**Use `Api.call` when they don't.** New Telegram feature, niche method, something not wrapped yet — call it directly.

## Responses work the same

You can `await` dynamic calls. You get `ok` and `result`. You can pass `on_run`. Same contract as `Api.getChat` would have if it were built in.

```js
let res = await Api.call("getChatMember", {
  chat_id: chat.id,
  user_id: user.id
})
```

## Parameters are on you

TBL doesn't validate dynamic calls against Telegram's schema. Wrong parameter name? Telegram errors. Check the [official API docs](https://core.telegram.org/bots/api) — parameter names must match exactly.

## Example

If `getChat` weren't available as `Api.getChat`:

```js
Api.call("getChat", { chat_id: 4444443444 })
```

In practice, prefer the built-in wrapper when you see it in the docs. Keep `Api.call` for the gaps.
