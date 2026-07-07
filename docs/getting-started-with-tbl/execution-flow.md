# Execution Flow

TBL matched a command. Now what? Execution follows a **fixed pipeline** every time — same order, same rules. Understanding it saves you from duplicate messages, mystery double-replies, and "why didn't my logic run?" moments.

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

Special commands (`@`, `!`, `@@`) are covered in [Special Commands](special-commands.md). Matching happens *before* step 3 — see [Matching & Priority](matching-order.md).

---

## Answer before Logic

For normal Telegram commands, the **Answer** (and **Keyboard**) goes out **first**, then **Logic** runs.

```js
// Answer field: "Loading..."
// Logic:
await HTTP.get("https://api.example.com/data")
Bot.sendMessage(chat.id, "Done!")
```

The user sees "Loading..." immediately, then "Done!" when logic finishes. No waiting for your API call to show *something*.

!!! tip
    Put static text in **Answer**. Put dynamic work in **Logic**. [`Bot`](../bot-instance/index.md) is for messages Logic sends on its own.

---

## Special command behavior

These run automatically — you don't trigger them manually:

| Command | When | Answer sent? | Logic runs? |
| --- | --- | --- | --- |
| `@` | Before every command | No | Yes |
| Matched command | Per update | Yes (unless Need Reply blocks logic) | Yes |
| `!` | On runtime error | Yes | Yes |
| `@@` | After every command | No | Yes |
| `*` | No other match | Yes | Yes |

`@` and `@@` skip the automatic Answer/keyboard send — setup and cleanup logic only. No accidental double messages.

---

## Need Reply flow

**Need Reply** breaks the normal "Answer then Logic" rhythm on the first visit:

1. Answer (+ keyboard) is sent
2. A session is stored for this user
3. **Logic does not run yet**
4. User's next message triggers the **same command's Logic**
5. That message is available as [`message`](../globals/message.md) / [`params`](../globals/params.md)

Send a different valid command (e.g. `/start`) and the session cancels — the new command runs normally.

See [Handling User Input](handle-need-reply.md).

---

## Callback query flow

Inline button taps send a **callback query**. TBL treats `callback_query.data` as command input — same matching rules as message text.

1. Match command from `callback_data` (command name + optional params)
2. Send Answer if configured
3. Run Logic

Always call [`Api.answerCallbackQuery()`](../api-instance/index.md) in Logic to dismiss Telegram's loading spinner. Users hate spinners that never stop.

See [Handling Callbacks](handling-callbacks.md). Callback globals: [`update`](../globals/update.md), [`request`](../globals/request.md).

---

## Webhook & webapp flow

HTTP-triggered commands **skip** the Answer field. Only **Logic** runs, using [`res`](../res-instance/index.md) for output.

Public web commands **skip the sandbox entirely** — command source is served as static content. No Logic, no [`Bot`](../bot-instance/index.md), no database.

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
Bot.sendMessage(chat.id, "Something went wrong. Try /start again.")
```

---

## Chained commands

[`Bot.run("otherCommand")`](../bot-instance/running-commands.md) triggers another command inside the same execution. Chain depth is limited (max **6** for Telegram commands).

Webhooks have a separate depth limit. Don't go infinite — Telegram users have patience limits too.

---

## See also

- [Matching & Priority](matching-order.md) — how we get to step 3
- [Special Commands](special-commands.md) — `@`, `!`, `@@`, `*`
- [Command Fields](command-fields.md) — what Answer and Logic actually are
