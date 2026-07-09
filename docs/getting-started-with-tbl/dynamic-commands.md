# Dynamic and Update-Specific Commands

Not every Telegram update is a plain text message. Users tap inline buttons, vote in polls, join groups, type `@yourbot` in other chats. You *could* parse all of that manually in one giant Logic block — or you could let TBL route each update type to its own command.

That's what dynamic handlers are for: dedicated commands for dedicated events.

---

## Dynamic handlers (`/handle_{update_type}`)

When an update arrives with a specific event type, TBL looks for a command named `/handle_{update_type}`.

Pattern: **`/handle_` + the update type string**.

### Common examples

| Command | Fires when… |
| --- | --- |
| `/handle_callback_query` | User taps an inline button |
| `/handle_channel_post` | New post in a channel where the bot is admin |
| `/handle_chat_member` | User joins, leaves, or gets banned |
| `/handle_poll_answer` | User votes in a bot poll |
| `/handle_message_reaction` | User adds or changes a reaction |

These run when no **more specific** command matches first. If `callback_data` is `"confirm"` and you have a `confirm` command, that wins over `/handle_callback_query`.

Matching order: [Matching & Priority](matching-order.md).

---

## `/handle_callback_query` — the callback safety net

Routes inline button taps when **no command name** matches `callback_data`.

| | |
| --- | --- |
| **Trigger** | Any `callback_query` update (after specific matches fail) |
| **Typical use** | One handler that branches on `update.callback_query.data` |

For simple bots, one command **per** `callback_data` is easier — see [Handling Callbacks](handling-callbacks.md). Reach for `/handle_callback_query` when you have dozens of buttons or shared routing logic.

[`update.callback_query`](../globals/update.md) and [`Api.answerCallbackQuery()`](../api-instance/index.md) are your friends here.

---

## `/inline_query` — inline mode

When someone types `@yourbot search term` **in any chat** (not just yours), Telegram sends an **inline query**.

| | |
| --- | --- |
| **Trigger** | Incoming inline query updates |
| **Typical use** | Search results, shareable buttons, GIF pickers |

The user's query string is available for matching and in Logic — build results with [`Api.answerInlineQuery()`](../api-instance/index.md).

---

## `/channel_update` — channel fallback

Channel posts and edits that don't match a more specific handler land here.

| | |
| --- | --- |
| **Trigger** | Channel-related updates when `/handle_channel_post` isn't defined |
| **Typical use** | Logging channel activity, cross-posting, moderation hooks |

Prefer `/handle_channel_post` when you only care about new posts — `/channel_update` is the wider net.

---

## When there's no input text

Some update types don't carry matchable text. TBL skips the normal name → alias → `*` flow and routes straight to the appropriate `/handle_{type}` or `/channel_update`.

That's why your `*` command might not catch every update type — dynamic handlers exist for the weird ones.

---

## See also

- [Handling Callbacks](handling-callbacks.md) — inline buttons step by step
- [Special Commands](special-commands.md) — `@`, `!`, `@@`, `*`
- [`update_type`](../globals/update_type.md) — string name of the current update
