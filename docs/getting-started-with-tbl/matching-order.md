# Command Matching & Priority

TBL uses a strict, deterministic order to pick **one** command per update.

---

## Matching priority

When input text is available (message text, `callback_data`, inline query, etc.):

| Priority | Rule | Example |
| --- | --- | --- |
| 1 | **Exact command name** (longest match first) | `/set name` before `/set` |
| 2 | **Alias match** | Button `Help` → command with alias `Help` |
| 3 | **Dynamic handler** | `/handle_{update_type}` e.g. `/handle_callback_query` |
| 4 | **Fallback** | `*` command |

If no input text (some channel/update types), TBL skips straight to update-type routing — see [Dynamic Handlers](dynamic-commands.md).

---

## Input sources

| Update type | Input used for matching |
| --- | --- |
| `message` | `message.text` |
| `callback_query` | `callback_query.data` |
| `inline_query` | `inline_query.query` |
| `channel_post` | `channel_post.text` |
| Webhook / webapp | `command` param or path (not this page) |

---

## Multi-word commands

TBL tries the longest command name first:

| User sends | Commands defined | Matches |
| --- | --- | --- |
| `/set name Alice` | `/set name`, `/set` | `/set name` |
| `/set color red` | `/set` only | `/set` (params: `color red`) |

Parameters after the command name are available as [`params`](../globals/params.md).

---

## Bot username suffix

`/start@YourBotName` is treated as `/start` — the `@bot` suffix is stripped for matching.

---

## Callback matching

For inline buttons, `callback_data` is parsed like message text:

```
callback_data: "confirm"
  → matches command `confirm`

callback_data: "set dark"
  → matches command `set`, params: `dark`
```

See [Handling Callbacks](handling-callbacks.md).

---

## Need Reply override

If a user is in a **need reply** session and sends text that is **not** a recognized command, the **original command's Logic** runs again with the new message as input.

If they send a valid command (e.g. `/start`), the session is cancelled and that command runs instead.

---

## When nothing matches

| Situation | Command run |
| --- | --- |
| Text doesn't match any command | `*` (if defined) |
| `*` not defined | Platform default behavior |
| Update type has `/handle_{type}` | That handler |
| Channel update, no handler | `/channel_update` or `*` |

---

## What does *not* affect priority

- Command order in the editor
- When the command was created
- Whether the command has Logic or only an Answer

Only the rules above matter.

---

## See also

- [Execution Flow](execution-flow.md) — what happens after a match
- [Special Commands](special-commands.md) — `@` runs before, `@@` after
- [Using Aliases](adding-aliases.md)
