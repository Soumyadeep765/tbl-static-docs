# Global Variables

The context your command already has — who's talking, where, what they sent, and what plan you're on. No imports, no setup, just read and go.

Read this section before [Bot](../bot-instance/index.md) and [Api](../api-instance/index.md): instances are what you *call*; globals are what you *read* from the current run.

---

## What are global variables?

TeleBotHost provides built-in **global variables** in every command. They give you access to the current update, user, chat, and runtime context without any setup or imports.

| You get | You skip |
| --- | --- |
| `user`, `chat`, `params` ready to use | Parsing raw Telegram JSON |
| `process.env` for secrets | Hard-coding API keys |
| `plan` limits at a glance | Guessing your quotas |

Variables are **read-only** during command execution unless noted otherwise.

!!! tip "New to TBL?"
    Globals are the foundation of every command. Quick intro: [Learning TBL](../learning-tbl.md). After both instance sections, use [Bot vs Api](../guides/bot-vs-api.md) to choose between them.

---

## How to use them

Drop this in any command's **Logic** field:

```js
Bot.sendMessage("Hey " + user.first_name + "! You said: " + params)
```

Three things worth knowing upfront:

1. **Globals exist only while a command is running** — they're not persistent storage (use [`db`](../db-instance/index.md) for that).
2. **`user` and `chat` may be `null`** on global webhooks or system updates with no user context.
3. **Use `process.env` (or `env`) for secrets** — never hard-code API keys. See [`process.env`](process.md).

---

## Available variables

Each variable below is documented on its own page with examples and field descriptions.

| Variable | Description |
| --- | --- |
| [update](update.md) | Full Telegram update object that triggered the command |
| [update_type](update_type.md) | String name of the update type (e.g. `message`, `callback_query`) |
| [request](request.md) | Active update payload, or HTTP request data in webhook mode |
| [message](message.md) | Plain text from `update.message` (text messages only) |
| [user](user.md) | The user who triggered the update |
| [chat](chat.md) | The chat where the update occurred |
| [bot](bot.md) | Metadata about the current bot |
| [owner](owner.md) | The bot owner's account information |
| [plan](plan.md) | The bot owner's subscription plan limits and features |
| [params](params.md) | Text arguments after a command, or webhook query/body params |
| [options](options.md) | Custom data passed when running a command programmatically |
| [tbl_options](tbl_options.md) | Data passed to HTTP or API callback commands |
| [content](content.md) | Response body from an HTTP callback command |
| [msg](msg.md) | Current message with built-in reply and edit helpers |
| [error](error.md) | Error details in the `!` handler or HTTP error callbacks |
| [http_response](http_response.md) | Full HTTP result in callback commands (`response`, `headers`, `cookies` aliases) |
| [process](process.md) | Environment variables, bot uptime, and runtime metadata |
| [env](process.md#the-env-alias) | Alias for `process.env` — dashboard environment variables |

---

## Try it — copy-paste examples

Start simple. Each example only introduces what it needs.

### Greet the user

```js
if (user) {
  Bot.sendMessage("Welcome back, " + user.first_name + "!")
}
```

### Read command arguments

`params` is whatever the user typed after your command:

```js
if (!params) {
  return Bot.sendMessage("Usage: /search <query>")
}
Bot.sendMessage("Searching for: " + params)
```

### Check your plan limits

```js
Bot.inspect("Storage limit: " + plan.prop_limit.per_account + " MB")
```

### Use a secret from ENV

Store API keys in dashboard **ENV** settings:

```js
let apiKey = process.env.MY_API_KEY
if (!apiKey) {
  return Bot.sendMessage("API key not configured.")
}
```

ENV setup: [`process.env`](process.md)

---

## Availability by command type

Not every global is available in every execution context.

| Variable | Telegram commands | Webhook / Webapp | Broadcast |
| --- | --- | --- | --- |
| `update`, `user`, `chat`, `bot`, `owner`, `plan`, `params`, `process`, `env` | ✓ | ✓ | ✓ |
| `msg` | ✓ (message updates) | `null` | `null` |
| `request` | Update sub-object | HTTP request object | Update sub-object |
| `message` | Text from `update.message` only | Usually `null` | Usually `null` |
| `options` | `Bot.run`, API callbacks, webhooks | Webhook merge | `Bot.run` |
| `http_response`, `response`, `content`, `headers`, `cookies` | HTTP callbacks only | HTTP callbacks only | HTTP callbacks only |
| `tbl_options` | Callback commands only | Callback commands only | Callback commands only |
| `error` | `!` handler or HTTP error callback | Same | Same |

---

## Important notes

- The global `msg` variable includes helper methods — see [msg](msg.md) and the [msg instance](../msg-instance/index.md) for the full method list
- Use `process.env` (or `env`) for secrets and configuration — never hard-code API keys in command scripts
