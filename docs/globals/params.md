# params

Whatever the user typed after your command — the arguments, the query, the extra words.

## What is it?

**`params`** is a **string** containing the text that comes after a command name. If someone sends `/start hello world`, the command is `/start` and `params` is `"hello world"`.

No parsing magic, no JSON, no key-value pairs. Just a string you can read, split, or validate. Simple on purpose.

## When would you use it?

- Commands that take user input: `/search cats`, `/greet Alice`, `/calc 2+2`
- Quick argument checks before doing work
- Webhook endpoints where query or body values map to `params`

For structured data (objects with multiple fields), consider [`options`](options.md) via `Bot.run` instead. For the full message text (not just post-command args), see [`message`](message.md).

---

## Try it

```js
// /greet Alice
if (params) {
  Bot.sendMessage(chat.id, "Hello, " + params + "!")
} else {
  Bot.sendMessage(chat.id, "Usage: /greet <name>")
}
```

```js
// /search something
if (!params) {
  return Bot.sendMessage(chat.id, "Usage: /search <query>")
}
Bot.sendMessage(chat.id, "Searching for: " + params)
```

---

## Where `params` comes from

### Telegram commands

| User sends | Command | `params` |
| --- | --- | --- |
| `/start` | `/start` | `""` (empty string) |
| `/start hello world` | `/start` | `"hello world"` |
| `/greet Alice` | `/greet` | `"Alice"` |

The command name itself is **not** included in `params`.

### Webhooks and webapps

In [Webhook](../webhook-instance/index.md) and [Webapp](../webapp-instance/index.md) mode, `params` may come from URL query parameters or the request body:

```js
// Webhook URL: /myHook?params=search+term
let query = params  // "search term"
```

See also [`request`](request.md) for full HTTP request access.

---

## Parsing multiple arguments

`params` is one string. Split it yourself if you need separate values:

```js
let args = params.split(" ")
let action = args[0]
let value = args[1]

if (!action) {
  return Bot.sendMessage(chat.id, "Usage: /do <action> <value>")
}
```

For anything more complex than space-separated words, pass an object through [`options`](options.md) instead.

---

## Good to know

- `params` is always a **string** — may be empty, never `null`
- Exists only during command execution
- Validate with [validator](../modules/validator.md) or [zod](../modules/zod.md) when input needs rules
