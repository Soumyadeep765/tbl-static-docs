# Handling Callbacks

Reply keyboards send button text as messages. **Inline buttons** are different — they live *inside* the message bubble and fire a **callback query** when tapped. No new message in the chat. Just a tap, a spinner, and your Logic.

This guide covers the full flow: sending inline keyboards, matching callback commands, answering callbacks, and editing messages.

---

## Reply keyboard vs inline keyboard

Same word "keyboard," two different animals:

| | Reply keyboard | Inline keyboard |
| --- | --- | --- |
| Location | Below chat input | Inside the message |
| Sends | Button label as text | `callback_query` update |
| Match via | Command name / alias | `callback_data` → command |
| Docs | [Adding a Keyboard](adding-keyboard.md) | This page |

Pick reply keyboards for menus users type through. Pick inline for "Yes / No" on a specific message.

---

## Step 1 — Send inline buttons (Logic)

Inline keyboards are built in **Logic** via [`Api.sendMessage()`](../api-instance/index.md):

```js
await Api.sendMessage({
  chat_id: chat.id,
  text: "Choose an option:",
  reply_markup: {
    inline_keyboard: [
      [
        { text: "✅ Yes", callback_data: "confirm" },
        { text: "❌ No", callback_data: "cancel" }
      ],
      [{ text: "Help", callback_data: "help" }]
    ]
  }
})
```

- `url` buttons open a link — no callback, no command
- `callback_data` buttons trigger a callback query (max **64 bytes**)

[`chat`](../globals/chat.md) gives you `chat.id` for the send call.

---

## Step 2 — Create matching commands

Each `callback_data` value should match a **command name** or **alias**.

| `callback_data` | Command to create |
| --- | --- |
| `confirm` | Command `confirm` |
| `help` | Command `help` (or alias on a shared handler) |
| `set dark` | Command `set` with param `dark` |

TBL reads `callback_query.data` the same way as message text — command name first, optional [`params`](../globals/params.md) after a space.

Matching rules: [Matching & Priority](matching-order.md).

### Example `confirm` command

**Answer:** `Confirmed!`

**Logic:**

```js
await Api.answerCallbackQuery({
  callback_query_id: update.callback_query.id,
  text: "Saved"
})

await Api.editMessageText({
  chat_id: chat.id,
  message_id: update.callback_query.message.message_id,
  text: "✅ You confirmed this action."
})
```

---

## Step 3 — Always answer the callback

Telegram shows a loading spinner until you respond. **Always** call [`Api.answerCallbackQuery()`](../api-instance/index.md) — even if you only acknowledge:

```js
await Api.answerCallbackQuery({
  callback_query_id: update.callback_query.id
})
```

Optional toast notification:

```js
await Api.answerCallbackQuery({
  callback_query_id: update.callback_query.id,
  text: "Done!",
  show_alert: false
})
```

In callback commands, [`request`](../globals/request.md) equals `update.callback_query` when `update_type === 'callback_query'`.

---

## What globals are available

Callbacks aren't normal messages — some globals behave differently:

| Global | In callback commands |
| --- | --- |
| `update.callback_query` | Full callback object |
| `update.callback_query.data` | The `callback_data` string |
| `update.callback_query.message` | Message the button is on |
| [`user`](../globals/user.md), [`chat`](../globals/chat.md) | Available |
| [`msg`](../globals/msg.md) | **`null`** — use `Api` with explicit IDs |
| [`message`](../globals/message.md) | **`null`** — use `update.callback_query.message` |

```js
let data = update.callback_query.data
let msgId = update.callback_query.message.message_id
let userId = user.id
```

Full object shape: [`update`](../globals/update.md).

---

## Edit the message instead of sending new

Cleaner UX — update the same bubble:

```js
await Api.editMessageText({
  chat_id: chat.id,
  message_id: update.callback_query.message.message_id,
  text: "You picked: " + update.callback_query.data,
  reply_markup: {
    inline_keyboard: [
      [{ text: "Back", callback_data: "menu" }]
    ]
  }
})
```

Swap only the keyboard with `Api.editMessageReplyMarkup()`. See [Editing Messages](../api-instance/editing-messages.md).

---

## Shared handler pattern

One command, many buttons — branch in Logic:

**Command:** `action`

**Logic:**

```js
let action = update.callback_query.data.split(" ")[0]

await Api.answerCallbackQuery({
  callback_query_id: update.callback_query.id
})

if (action === "yes") {
  await Api.editMessageText({
    chat_id: chat.id,
    message_id: update.callback_query.message.message_id,
    text: "You said yes!"
  })
} else if (action === "no") {
  await Api.editMessageText({
    chat_id: chat.id,
    message_id: update.callback_query.message.message_id,
    text: "You said no."
  })
}
```

Set buttons' `callback_data` to `action yes`, `action no`, etc. — or use separate commands per button for simpler bots.

---

## Dynamic handler (advanced)

Route **all** callbacks through one command when nothing more specific matches:

**Command:** `/handle_callback_query`

**Logic:** inspect `update.callback_query.data` and branch.

See [Dynamic Handlers](dynamic-commands.md).

---

## `callback_data` limits

- Maximum **64 bytes** — store short tokens, not JSON
- Look up details in `db.user` or `db.bot` by ID
- Use aliases for readable names that map to one command

---

## Common mistakes

| Mistake | Fix |
| --- | --- |
| Spinner never stops | Call `Api.answerCallbackQuery()` |
| Command not found | `callback_data` must match command name or alias |
| `msg.reply()` fails | `msg` is null — use `Api` + `chat.id` |
| Data too long | Keep `callback_data` under 64 bytes |

---

## Full example — settings menu

**`/menu` Logic** — send inline keyboard:

```js
await Api.sendMessage({
  chat_id: chat.id,
  text: "Settings:",
  reply_markup: {
    inline_keyboard: [
      [{ text: "🔔 Notifications", callback_data: "toggle_notify" }],
      [{ text: "🌙 Dark mode", callback_data: "toggle_theme" }]
    ]
  }
})
```

**`toggle_notify` Logic:**

```js
let on = await db.user.get("notify") !== false
await db.user.set("notify", !on)

await Api.answerCallbackQuery({
  callback_query_id: update.callback_query.id,
  text: on ? "Notifications off" : "Notifications on"
})
```

---

## See also

- [Inline Keyboards](../api-instance/inline-keyboards.md) — Api reference
- [Execution Flow](execution-flow.md) — callback in the pipeline
- [Adding a Keyboard](adding-keyboard.md) — reply keyboards (different feature)
