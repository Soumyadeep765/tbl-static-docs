# The `params` Variable

In TBL, `params` contains the **text arguments** sent after a command name. It is a simple way to pass input without reply-based flows.

## Telegram Commands

If a user sends:

```
/start hello world
```

Then:

- Command → `/start`
- `params` → `"hello world"`

If no extra text is provided, `params` is an empty string `""`.

```javascript
// /greet Alice
if (params) {
  Bot.sendMessage(chat.id, `Hello, ${params}!`)
} else {
  Bot.sendMessage(chat.id, 'Hello! Usage: /greet <name>')
}
```

## Webhook and Webapp Commands

In [Webhook](../webhook-instance/index.md) and [Webapp](../webapp-instance/index.md) mode, `params` may come from URL query parameters or the request body, depending on how the endpoint is called.

```javascript
// Webhook URL: /myHook?params=search+term
let query = params  // "search term"
```

## Parsing Multiple Arguments

`params` is a single string. Split it yourself if you need separate values:

```javascript
let args = params.split(' ')
let action = args[0]
let value = args[1]
```

For structured data, consider passing JSON via `Bot.run` [options](options.md) instead.

## Important Notes

- `params` is always a **string** (may be empty)
- It exists only during command execution
- It does not include the command name itself
