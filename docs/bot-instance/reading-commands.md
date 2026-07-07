# Reading Commands

Read existing command source code and configuration at runtime — useful for admin panels, documentation bots, debugging, and auditing.

## `Bot.read(commandName)`

Returns the **raw source code** of a command as a plain string. Does not include settings like keyboard, aliases, or `need_reply`.

```js
let code = Bot.read("/start")
// Returns: "Bot.sendMessage('Welcome!')"

Bot.sendMessage("Code length: " + code.length)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `commandName` | `string` | Command name (e.g. `"/start"`) |

**Returns:** `string` — the command's TBL source code.

## `Bot.readCommand(commandName)`

Returns the **full command definition** — code plus all dashboard settings.

```js
let cmd = Bot.readCommand("/start")
```

**Returns:** `object` with fields such as:

| Field | Type | Description |
| --- | --- | --- |
| `code` | `string` | TBL source code |
| `answer` | `string \| null` | Auto-reply text |
| `keyboard` | `string \| null` | Reply keyboard config |
| `aliases` | `array` | Command aliases |
| `allow_only_group` | `boolean` | Restrict to groups |
| `need_reply` | `boolean` | Wait for user reply before running |

### Example response

```json
{
  "code": "Bot.sendMessage('Welcome!')",
  "answer": null,
  "keyboard": null,
  "aliases": [],
  "allow_only_group": false,
  "need_reply": false
}
```

## Error handling

Both methods throw if:

- The command name is missing or not a string
- The command does not exist (with a suggestion for similar command names)

Errors can be caught by the `!` error handler.

```js
try {
  let code = Bot.read("/nonexistent")
} catch (e) {
  Bot.sendMessage("Command not found.")
}
```

## Use cases

| Method | Best for |
| --- | --- |
| `Bot.read` | Code previews, AI analysis, debugging logic |
| `Bot.readCommand` | Admin panels, command editors, full config audit |

## Important notes

- Both methods are **read-only** — returned data never executes
- The target command must exist in your bot's command list
- Useful for building in-bot documentation or moderation tools
