# Command Execution

The `Bot` instance lets you **run another command programmatically** — useful for multi-step flows, reusing logic, and navigation without duplicating code.

## Quick start

```js
// Run another command
Bot.runCommand("/menu")

// Pass data to the target command
Bot.runCommand("/checkout", { step: 2, item: "Widget" })
```

Inside the target command, passed data is available as the [`options`](../globals/options.md) global.

## `Bot.runCommand(command, options?)`

Shorthand for running a command in the **current chat** for the **current user**.

| Parameter | Type | Description |
| --- | --- | --- |
| `command` | `string` | Command name (e.g. `"/start"`, `"/help"`) |
| `options` | `object` | Optional data passed to the target command as `options` |

```js
Bot.runCommand("/survey", { question: 1 })
```

Returns a **Promise** resolving to `{ success: true }` on completion.

## `Bot.run(params)`

Full control over command execution. Accepts a single params object:

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `command` | `string` | — | **Required.** Command to execute. Can include params: `"/greet Alice"` |
| `options` | `object` | — | Data passed to the target command as `options` |
| `user_id` | `number` | `user.id` | Override the user context |
| `chat_id` | `number` | `chat.id` | Override the chat context |
| `user_telegramid` | `number` | — | Override `user.telegramid` in the cloned update |
| `ignoreMissingCommand` | `boolean` | `false` | Skip silently if the command doesn't exist |

### Examples

```js
// Basic
Bot.run({ command: "/contact" })

// With options
Bot.run({
  command: "/next",
  options: { step: 2 }
})

// Run for a different user/chat
Bot.run({
  command: "/notify",
  options: { alert: "New order" },
  user_id: 123456789,
  chat_id: 987654321
})

// Optional command — no error if missing
Bot.run({
  command: "/optional_hook",
  ignoreMissingCommand: true
})
```

### Return values

| Result | Meaning |
| --- | --- |
| `{ success: true }` | Command executed successfully |
| `{ success: true, waitingForReply: true }` | Command is waiting for user reply (`need_reply`) |
| `{ success: true, skipped: true }` | Command not found, skipped (`ignoreMissingCommand: true`) |

Use `await` when you need to wait for the target command to finish before continuing:

```js
await Bot.runCommand("/validate")
Bot.sendMessage("Validation passed.")
```

## Command chain limit

Each `Bot.run` / `Bot.runCommand` call increments an internal chain counter. **Maximum 6 chained commands** per execution — exceeding this throws an error.

```js
// This is fine — 3 levels
Bot.runCommand("/step2")  // step2 runs step3, step3 runs step4
```

Avoid deep recursive chains. For complex flows, use [`options`](../globals/options.md) to pass state instead of chaining many commands.

## Error handling

If the target command **does not exist** and `ignoreMissingCommand` is `false`:

- A runtime error is thrown
- The `!` error handler runs if defined
- Execution stops unless caught

```js
// Safe optional routing
let result = await Bot.run({
  command: "/fallback",
  ignoreMissingCommand: true
})

if (result.skipped) {
  Bot.sendMessage("Fallback command not configured.")
}
```

## `Bot.runCommand` vs `Bot.run`

| | `runCommand` | `run` |
| --- | --- | --- |
| Syntax | `Bot.runCommand("/cmd", opts)` | `Bot.run({ command: "/cmd", options: opts })` |
| Override chat/user | No | Yes |
| Skip missing commands | No | Yes (`ignoreMissingCommand`) |
| Include params in command string | No | Yes (`command: "/greet Bob"`) |

Use `runCommand` for simple navigation. Use `run` when you need chat/user overrides or optional commands.
