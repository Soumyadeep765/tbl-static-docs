# Running Commands

Your bot doesn't have to be a one-command wonder. **`Bot.runCommand`** and **`Bot.run`** let you jump to another command mid-flow — like a choose-your-own-adventure, but with less dragons and more `/menu` buttons.

Multi-step wizards, reusable logic, "go to checkout" navigation — all without copy-pasting the same code into five commands.

---

## What is command execution?

When a user triggers `/start`, one command runs. Sometimes you want that command to **hand off** to another — programmatically, from inside your Logic field.

| You get | You skip |
| --- | --- |
| Multi-step flows without duplication | Giant if/else trees in one command |
| Shared logic across commands | Pasting the same block everywhere |
| Optional routing (`ignoreMissingCommand`) | Hard-coded command existence checks |

The target command receives any data you pass via the [`options`](../globals/options.md) global. Think of it as a note slipped to the next command: "here's where we left off."

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md).

---

## How to use it

### Quick start — `Bot.runCommand`

The friendly shorthand. Runs a command in the **current chat** for the **current user**:

```js
// Jump to another command
Bot.runCommand("/menu")

// Pass data along for the ride
Bot.runCommand("/checkout", { step: 2, item: "Widget" })
```

Inside `/checkout`, read `options.step` and `options.item`. Simple.

Returns a **Promise** — add `await` when the next line depends on the target command finishing:

```js
await Bot.runCommand("/validate")
Bot.sendMessage("Validation passed. Moving on!")
```

### Full control — `Bot.run`

When you need to override chat/user, embed params in the command string, or skip missing commands gracefully:

```js
// Basic handoff
Bot.run({ command: "/contact" })

// With options
Bot.run({
  command: "/next",
  options: { step: 2 }
})

// Different user or chat (admin notifications, cross-user flows)
Bot.run({
  command: "/notify",
  options: { alert: "New order" },
  user_id: 123456789,
  chat_id: 987654321
})

// Params baked into the command string
Bot.run({ command: "/greet Alice" })

// Command might not exist — don't crash if it doesn't
Bot.run({
  command: "/optional_hook",
  ignoreMissingCommand: true
})
```

---

## Try it — copy-paste examples

### Simple menu navigation

User tapped "Settings" in your flow? Send them to the settings command:

```js
Bot.runCommand("/settings")
```

### Wizard with state

Step 1 collects a name, step 2 asks for email:

```js
// In /wizard_step1 — user just typed their name
Bot.runCommand("/wizard_step2", { name: params })
```

```js
// In /wizard_step2 — options.name is waiting for you
Bot.sendMessage("Nice to meet you, " + options.name + "! What's your email?")
```

### Safe optional routing

Try a premium hook; fall back gracefully if it's not configured:

```js
let result = await Bot.run({
  command: "/premium_hook",
  ignoreMissingCommand: true
})

if (result.skipped) {
  Bot.sendMessage("Premium hook not set up yet — using default flow.")
  Bot.runCommand("/default_flow")
}
```

---

## Return values

| Result | Meaning |
| --- | --- |
| `{ success: true }` | Command ran successfully |
| `{ success: true, waitingForReply: true }` | Target command is waiting for user reply (`need_reply`) |
| `{ success: true, skipped: true }` | Command not found, skipped (`ignoreMissingCommand: true`) |

---

## Command chain limit

Each `Bot.run` / `Bot.runCommand` call increments an internal chain counter. **Maximum 6 chained commands** per execution — go deeper and you'll get an error.

```js
// Fine — a few levels deep
Bot.runCommand("/step2")  // step2 runs step3, step3 runs step4
```

For complex flows, pass state through [`options`](../globals/options.md) instead of chaining command after command. Your future self will thank you.

---

## Error handling

If the target command **doesn't exist** and `ignoreMissingCommand` is `false`:

- A runtime error is thrown
- Your `!` error handler runs if you've defined one
- Execution stops unless you catch it

Define a `!` command — users see a message instead of silence when something breaks.

---

## `runCommand` vs `run`

| | `runCommand` | `run` |
| --- | --- | --- |
| Syntax | `Bot.runCommand("/cmd", opts)` | `Bot.run({ command: "/cmd", options: opts })` |
| Override chat/user | No | Yes |
| Skip missing commands | No | Yes (`ignoreMissingCommand`) |
| Params in command string | No | Yes (`command: "/greet Bob"`) |

**Rule of thumb:** `runCommand` for simple navigation. `run` when you need overrides or optional routing.

---

## Method reference

### `Bot.runCommand(command, options?)`

| Parameter | Type | Description |
| --- | --- | --- |
| `command` | `string` | Command name (e.g. `"/start"`, `"/help"`) |
| `options` | `object` | Optional data passed to the target as [`options`](../globals/options.md) |

### `Bot.run(params)`

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `command` | `string` | — | **Required.** Command to execute. Can include params: `"/greet Alice"` |
| `options` | `object` | — | Data passed to the target as `options` |
| `user_id` | `number` | `user.id` | Override the user context |
| `chat_id` | `number` | `chat.id` | Override the chat context |
| `user_telegramid` | `number` | — | Override `user.telegramid` in the cloned update |
| `ignoreMissingCommand` | `boolean` | `false` | Skip silently if the command doesn't exist |
