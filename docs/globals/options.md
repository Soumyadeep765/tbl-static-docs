# options

A backpack for passing data between commands — or carrying API results home.

## What is it?

**`options`** carries **context passed between commands** or **results returned from API calls**. It's how you hand off a `{ step: 2, name: "Alice" }` object from `/start` to `/onboard`, or read the JSON response after an [Api](../api-instance/index.md) call finishes.

Think of it as a note you slip to the next command: "Here's what you need to know."

## When would you use it?

| Scenario | What `options` holds |
| --- | --- |
| Chaining commands with `Bot.run` | The object you passed as the second argument |
| API method callback | Full Telegram API JSON response (`{ ok, result, ... }`) |
| Webhook command | Merged webhook options and HTTP request metadata |

For **your own custom data** through HTTP or API callbacks specifically, see [`tbl_options`](tbl_options.md) — it's the dedicated lane for that.

---

## Try it — chaining commands

```js
// In /start — pass data forward
Bot.run("/onboard", { step: 1, name: user.first_name })

// In /onboard — read what /start sent
let step = options.step    // 1
let name = options.name    // user's first name
Bot.sendMessage("Step " + step + " for " + name)
```

More on chaining: [Running Commands](../bot-instance/running-commands.md).

---

## Try it — API callbacks

When a command runs as the callback of an [Api](../api-instance/index.md) call, `options` contains the Telegram API response:

```js
if (options.ok) {
  let messageId = options.result.message_id
  Bot.sendMessage("Message sent! ID: " + messageId)
} else {
  Bot.sendMessage("API call failed.")
}
```

Example response shape:

```json
{
  "ok": true,
  "result": {
    "message_id": 42,
    "chat": { "id": 123 },
    "text": "Hello!"
  }
}
```

---

## `options` vs `tbl_options`

| Variable | Purpose |
| --- | --- |
| `options` | General context — `Bot.run` payloads, API results, webhook merge |
| [`tbl_options`](tbl_options.md) | Your custom data passed via `tbl_options` in HTTP/API callback options |

Rule of thumb: API gave you a result? That's `options`. You packed your own lunch? That's `tbl_options`.

---

## Good to know

- `options` is `null` when nothing was passed — check before reading properties
- Exists only during command execution
- For **long-lived state** (user scores, settings), use [`db.user`](../db-instance/user.md) or [`db.bot`](../db-instance/bot.md) — `options` doesn't survive between unrelated commands
