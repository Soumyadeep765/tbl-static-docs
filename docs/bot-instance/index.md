# Bot

Your bot's personal assistant — sends replies, runs other commands, stores settings, and fires off broadcasts. No imports, no setup, just `Bot.` and go.

Where [`Api`](../api-instance/index.md) speaks Telegram's language method-for-method, `Bot` speaks *bot author* language: sensible defaults, less boilerplate, and the current chat filled in for you.

---

## What is Bot?

**Bot** is TeleBotHost's high-level toolkit for running your bot day to day — replying to users, chaining commands, managing bot-wide settings, listing users, and launching broadcasts.

| You get | You skip |
| --- | --- |
| Auto-targeted sends (`Bot.sendMessage`) | Passing `chat_id` every time |
| Command chaining (`Bot.runCommand`) | Manual routing logic |
| Bot-wide storage (via [`db.bot`](../db-instance/bot.md)) | Rolling your own persistence |

`Bot` is available in every command alongside `Api` — no import or setup required.

---

## How to use it

Drop this in any command's **Logic** field:

```js
Bot.sendMessage("Welcome!")
Bot.runCommand("/menu")
```

Three things worth knowing upfront:

1. **`Bot` is already there** — you never import or initialize it.
2. **Most send methods target the current chat** — the conversation where the command fired.
3. **`Bot.run` / `Bot.runCommand` return a Promise** — use `await` when you need to wait for completion.

!!! tip "New to TBL?"
    `chat`, `user`, and `params` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md). For Telegram read operations (`getChat`, `getMe`, etc.), use [`Api`](../api-instance/index.md).

---

## Bot or Api?

Both live in every command. Pick the right tool before you reach for the keyboard:

| Task | Use |
| --- | --- |
| Send a quick text reply | `Bot.sendMessage` |
| Run another command with data | `Bot.runCommand` / `Bot.run` |
| Store bot-wide settings | [`db.bot`](../db-instance/bot.md) |
| List users who interacted | `Bot.getUsers` |
| Mass-message all users | `Bot.broadcast` |
| Inline buttons, edit messages, reactions | [`Api`](../api-instance/index.md) |
| Raw Telegram API access | [`Api`](../api-instance/index.md) |

See the [Bot vs Api guide](../guides/bot-vs-api.md) for side-by-side examples.

---

## Try it — copy-paste examples

Start simple. Each example only introduces what it needs.

### Send a welcome message

No setup — just text:

```js
Bot.sendMessage("Hey " + user.first_name + "! Type /menu to get started.")
```

### Run another command

Hand off to `/menu` with optional data:

```js
Bot.runCommand("/menu", { params: "from_start" })
```

### Store a bot-wide setting

Use [`db.bot`](../db-instance/bot.md) — the modern async storage API:

```js
await db.bot.set("maintenance", false)
let mode = await db.bot.get("maintenance", false)
```

### Debug output

Format and send debug info to the current chat:

```js
Bot.inspect(user, chat, params)
```

---

## Method categories

### Command flow

| Method | Description |
| --- | --- |
| `Bot.runCommand(cmd, options?)` | Run a command by name |
| `Bot.run(params)` | Run a command with full control (chat, user, options) |
| `Bot.read(cmd)` | Get a command's source code as a string |
| `Bot.readCommand(cmd)` | Get full command definition (code, keyboard, aliases, etc.) |

### Sending output

| Method | Description |
| --- | --- |
| `Bot.sendMessage(text, options?)` | Send text to the current chat |
| `Bot.sendKeyboard(text, keyboard, options?)` | Send text with a reply keyboard |
| `Bot.sendPhoto` / `sendDocument` / `sendAudio` / `sendVideo` / `sendVoice` | Send media to the current chat |
| `Bot.inspect(...values)` | Format and send debug output to the current chat |

### Bot-wide properties (deprecated)

| Method | Aliases | Description |
| --- | --- | --- |
| `Bot.set(key, value, type?, ttl?)` | `setProp`, `setProperty` | Set a bot property — **deprecated**, 1 MB limit |
| `Bot.get(key)` | `getProp`, `getProperty` | Get a bot property — **deprecated** |
| `Bot.del(key)` | `delProp`, `delProperty` | Delete a bot property — **deprecated** |
| `Bot.getAll()` | `getAllProp`, `getAllProperty` | Get all properties — **deprecated** |
| `Bot.delAll()` | `delAllProp`, `delAllProperty` | Delete all properties — **deprecated** |
| `Bot.has(key)` | `hasProp` | Check if a key exists — **deprecated** |
| `Bot.count()` | `countProps` | Number of stored keys — **deprecated** |
| `Bot.getNames()` | `getPropNames` | List of all keys — **deprecated** |

!!! warning "Use `db.bot` instead"
    `Bot.set` / `Bot.get` are deprecated with a **1 MB per-bot limit**. Use [`db.bot`](../db-instance/bot.md) for all new storage — see [Bot Properties](bot-properties.md).

### User management

| Method | Description |
| --- | --- |
| `Bot.getUsers(filters?)` | Query user/chat IDs with filters (async) |

### Broadcasting

| Method | Description |
| --- | --- |
| `Bot.broadcast(params)` | Start a distributed broadcast job |
| `Bot.stopBroadcast(broadcastId)` | Stop a running broadcast |
| `Bot.getBroadcastStats(broadcastId)` | Get job statistics |
| `Bot.listBroadcasts(status?)` | List broadcast jobs for this bot |

---

## Important notes

- Method names are **case-sensitive** — `Bot.runCommand` works, `Bot.runcommand` does not
- Most send methods target the **current chat** automatically
- `Bot.run` / `Bot.runCommand` return a Promise with `{ success: true }` — use `await` when you need to wait for completion
- Command chains are limited to **6** nested `Bot.run` calls per execution
- `Bot` property methods are **not available** in webhook/webapp context
- For Telegram read operations (`getChat`, `getMe`, etc.), use [`Api`](../api-instance/index.md)

---

## Pages in this section

| Page | Covers |
| --- | --- |
| [Running Commands](running-commands.md) | `runCommand`, `Bot.run`, options, chain limits |
| [Reading Commands](reading-commands.md) | `read`, `readCommand` |
| [Sending Messages](sending-messages.md) | Text, keyboards, media, `inspect` |
| [Bot Properties (Deprecated)](bot-properties.md) | Legacy `Bot.set` / `Bot.get` — use `db.bot` instead |
| [Listing Users](listing-users.md) | `getUsers` filters and pagination |
| [Broadcasting](broadcasting.md) | Distributed mass messaging |
