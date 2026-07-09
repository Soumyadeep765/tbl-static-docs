# Command Matching & Priority

User sends `/start`. Or taps `Help`. Or smashes the keyboard with `asdfghjkl`. Something has to run — and TBL picks **exactly one** command per update, using a strict, deterministic order.

No randomness. No "whichever command was listed first in the editor." Just rules.

---

## What gets matched?

First, TBL needs **input text** to compare against your command names. Where that text comes from depends on the update type:

| Update type | Input used for matching |
| --- | --- |
| `message` | `message.text` |
| `callback_query` | `callback_query.data` |
| `inline_query` | `inline_query.query` |
| `channel_post` | `channel_post.text` |
| Webhook / webapp | `command` param or path (different rules — see [Webapps](../webapp-instance/index.md)) |

If there's no input text (some channel/update types), TBL skips straight to update-type routing — [Dynamic Handlers](dynamic-commands.md).

---

## Matching priority

When input text *is* available, TBL checks in this order:

| Priority | Rule | Example |
| --- | --- | --- |
| 1 | **Exact command name** (longest match first) | `/set name` before `/set` |
| 2 | **Alias match** | Button `Help` → command with alias `Help` |
| 3 | **Dynamic handler** | `/handle_{update_type}` e.g. `/handle_callback_query` |
| 4 | **Fallback** | `*` command |

First match wins. Everything else sits this one out.

---

## Multi-word commands

TBL always tries the **longest** command name first:

| User sends | Commands defined | Matches |
| --- | --- | --- |
| `/set name Alice` | `/set name`, `/set` | `/set name` |
| `/set color red` | `/set` only | `/set` (params: `color red`) |

Whatever remains after the command name lands in [`params`](../globals/params.md) — a string you can split, trim, or ignore in Logic.

---

## Bot username suffix

`/start@YourBotName` is treated as `/start`. The `@bot` suffix gets stripped for matching. Telegram adds it in group chats; you don't have to define a separate command for it.

---

## Callback matching

Inline buttons work the same way — `callback_data` is parsed like message text:

```
callback_data: "confirm"
  → matches command `confirm`

callback_data: "set dark"
  → matches command `set`, params: `dark`
```

See [Handling Callbacks](handling-callbacks.md) for the full inline-button flow.

---

## Need Reply override

If a user is in a **need reply** session and sends text that is **not** a recognized command, the **original command's Logic** runs again with the new message as input.

If they send a valid command (e.g. `/start`), the session is cancelled and that command runs instead. Escape hatch built in.

Details: [Handling User Input](handle-need-reply.md).

---

## When nothing matches

| Situation | Command run |
| --- | --- |
| Text doesn't match any command | `*` (if defined) |
| `*` not defined | Platform default behavior |
| Update type has `/handle_{type}` | That handler |
| Channel update, no handler | `/channel_update` or `*` |

The `*` command is your safety net — [Using the Wildcard](using-wildcard.md).

---

## What does *not* affect priority

Worth repeating because people assume otherwise:

- Command order in the editor
- When the command was created
- Whether the command has Logic or only an Answer

Only the rules above matter. The universe is cruel but consistent.

---

## See also

- [Execution Flow](execution-flow.md) — what happens after a match
- [Special Commands](special-commands.md) — `@` runs before, `@@` after
- [Using Aliases](adding-aliases.md) — second place in the priority list
