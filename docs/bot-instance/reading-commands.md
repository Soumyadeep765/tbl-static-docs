# Reading Commands

Ever wish you could peek at another command's source code without leaving the dashboard? **`Bot.read`** and **`Bot.readCommand`** let your bot inspect its own commands at runtime — perfect for admin panels, documentation bots, and "what does `/secret` actually do?" debugging sessions.

Read-only, safe, and slightly meta. Your bot reading itself. Very introspective.

---

## What is reading commands?

Two methods, two levels of detail:

| Method | Returns | Best for |
| --- | --- | --- |
| `Bot.read("/start")` | Raw source code (string) | Code previews, AI analysis, debugging logic |
| `Bot.readCommand("/start")` | Full definition (object) | Admin panels, config audits, command editors |

Neither method **executes** anything — you're just looking. Like reading a recipe without turning on the oven.

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md).

---

## How to use it

### Read source code only — `Bot.read`

Returns the command's **Logic field** as a plain string. No keyboard, aliases, or `need_reply` settings:

```js
let code = Bot.read("/start")
// Returns something like: "Bot.sendMessage('Welcome!')"

Bot.sendMessage("That command is " + code.length + " characters long.")
```

| Parameter | Type | Description |
| --- | --- | --- |
| `commandName` | `string` | Command name (e.g. `"/start"`) |

**Returns:** `string` — the command's source code.

### Read full definition — `Bot.readCommand`

Returns **everything** — code plus dashboard settings:

```js
let cmd = Bot.readCommand("/start")

Bot.sendMessage("Keyboard: " + (cmd.keyboard || "none"))
Bot.sendMessage("Aliases: " + cmd.aliases.join(", ") || "none")
```

**Returns:** `object` with fields such as:

| Field | Type | Description |
| --- | --- | --- |
| `code` | `string` | Source code from the Logic field |
| `answer` | `string \| null` | Auto-reply text |
| `keyboard` | `string \| null` | Reply keyboard config |
| `aliases` | `array` | Command aliases |
| `allow_only_group` | `boolean` | Restrict to groups |
| `need_reply` | `boolean` | Wait for user reply before running |

Example response:

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

---

## Try it — copy-paste examples

### Code length checker (admin tool)

```js
let code = Bot.read("/help")
Bot.sendMessage("/help logic: " + code.length + " chars")
```

### List commands that use reply keyboards

```js
// Assume you have a list of command names from your admin panel
let cmd = Bot.readCommand("/menu")
if (cmd.keyboard) {
  Bot.sendMessage("/menu has a reply keyboard configured.")
}
```

### Safe read with error handling

Both methods throw if the command name is missing, not a string, or doesn't exist (with suggestions for similar names):

```js
try {
  let code = Bot.read("/nonexistent")
} catch (e) {
  Bot.sendMessage("That command doesn't exist.")
}
```

Errors can also be caught by your `!` error handler.

---

## Important notes

- **Read-only** — returned data never runs. You're inspecting, not executing.
- The target command must exist in your bot's command list.
- Great for in-bot documentation, moderation tools, or "show me the code" admin features.
- Restrict these commands to admins — exposing source code to everyone is rarely a good idea.
