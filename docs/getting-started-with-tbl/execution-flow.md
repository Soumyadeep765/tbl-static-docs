# Execution Flow

Once TBL matches a command, execution follows a fixed pipeline. Understanding this order helps you avoid duplicate messages and know where special commands fit.

---

## Full pipeline

```
┌─────────────────────────────────────┐
│  1. Update received                 │
└─────────────────┬───────────────────┘
                  ▼
┌─────────────────────────────────────┐
│  2. `@` initialization (always)     │
│     Skips answer/keyboard side      │
│     effects — logic only            │
└─────────────────┬───────────────────┘
                  ▼
┌─────────────────────────────────────┐
│  3. Matched command                 │
│     a. Group-only check             │
│     b. Need Reply? → send Answer,   │
│        start session, STOP          │
│     c. Send Answer + Keyboard       │
│     d. Run Logic                    │
└─────────────────┬───────────────────┘
                  ▼
         ┌────────┴────────┐
         │ Runtime error?  │
         └────────┬────────┘
              yes  │  no
                  ▼
┌─────────────────────────────────────┐
│  4. `!` error handler (on error)    │
│     Sends its Answer, runs Logic    │
└─────────────────┬───────────────────┘
                  ▼
┌─────────────────────────────────────┐
│  5. `@@` post-processor (always)    │
│     Skips answer side effects       │
└─────────────────┬───────────────────┘
                  ▼
              Complete
```

---

## Answer before Logic

For normal commands, the **Answer** (and **Keyboard**) is sent **first**, then **Logic** runs.

```js
// Answer field: "Loading..."
// Logic:
await HTTP.get("https://api.example.com/data")
Bot.sendMessage("Done!")
```

The user sees "Loading..." immediately, then "Done!" when logic finishes.

!!! tip
    Put static text in **Answer**. Put dynamic work in **Logic**.

---

## Special command behavior

| Command | When | Answer sent? | Logic runs? |
| --- | --- | --- | --- |
| `@` | Before every command | No | Yes |
| Matched command | Per update | Yes (unless Need Reply blocks logic) | Yes |
| `!` | On runtime error | Yes | Yes |
| `@@` | After every command | No | Yes |
| `*` | No other match | Yes | Yes |

`@` and `@@` skip the automatic Answer/keyboard send — they are for setup and cleanup logic only.

---

## Need Reply flow

When **Need Reply** is enabled:

1. Answer (+ keyboard) is sent
2. A session is stored for this user
3. **Logic does not run yet**
4. User's next message triggers the **same command's Logic**
5. That message is available as `message` / `params`

If the user sends a different valid command (e.g. `/start`), the session is cancelled and the new command runs normally.

See [Handling User Input](handle-need-reply.md).

---

## Callback query flow

Inline button taps send a **callback query**. TBL treats `callback_query.data` as the command input (like message text).

1. Match command from `callback_data` (command name + optional params)
2. Send Answer if configured
3. Run Logic

Always call `Api.answerCallbackQuery()` in Logic to dismiss the loading spinner.

See [Handling Callbacks](handling-callbacks.md).

---

## Webhook & webapp flow

HTTP-triggered commands **skip** the Answer field. Only **Logic** runs, using [`res`](../res-instance/index.md) for output.

Public web commands **skip the sandbox entirely** — command source is served as static content.

| Surface | Answer | Logic | `res` |
| --- | --- | --- | --- |
| Telegram / callback | Yes | Yes | No |
| Webhook / webapp | No | Yes | Yes |
| Public web | No | No | No |

---

## Error handling

If Logic throws an error:

1. Platform may send a default error message to the user
2. `!` command runs (if defined) — its Answer and Logic execute
3. `@@` still runs afterward

Use `!` to log errors or send a friendly fallback:

```js
// ! command Logic
Bot.sendMessage("Something went wrong. Try /start again.")
```

---

## Chained commands

`Bot.run("otherCommand")` triggers another command inside the same execution. Chain depth is limited (max **6** for Telegram commands).

Webhooks have a separate depth limit. See [Running Commands](../bot-instance/running-commands.md).

---

## See also

- [Matching & Priority](matching-order.md)
- [Special Commands](special-commands.md)
- [Command Fields](command-fields.md)
