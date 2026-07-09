# Inline Keyboards

Buttons *inside* the message bubble — not the chunky reply keyboard at the bottom of the screen. Users tap them; Telegram sends a callback query; you respond with `Api`.

Reply keyboards (`"Help, About"`) send plain text when tapped. Inline buttons send structured callback data. Different beasts. Don't mix them up at parties.

---

## What are inline keyboards?

An `inline_keyboard` is a grid of buttons attached to a message. Two main button types:

| Button type | User sees | Your bot receives |
| --- | --- | --- |
| `url` | Opens browser / in-app view | Nothing |
| `callback_data` | Stays in chat | Callback query update |

Mix them freely in the same keyboard.

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Callback handling tutorial: [Handling Callbacks](../getting-started-with-tbl/handling-callbacks.md).

---

## How to use it

### A minimal keyboard

```js
Api.sendMessage({
  text: "Choose:",
  reply_markup: {
    inline_keyboard: [
      [{ text: "Website", url: "https://telebothost.com" }],
      [{ text: "Help", callback_data: "help" }]
    ]
  }
})
```

URL buttons open a link. `callback_data` buttons fire a callback query — handle that in a command triggered by the callback.

### Layout

Each inner array is a **row**. Buttons in the same row sit side by side:

```js
reply_markup: {
  inline_keyboard: [
    [{ text: "Yes", callback_data: "yes" }, { text: "No", callback_data: "no" }],
    [{ text: "Cancel", callback_data: "cancel" }]
  ]
}
```

Two buttons on the first row, one full-width button below. Tetris for UX designers.

---

## Try it — copy-paste examples

### Yes / No prompt

```js
Api.sendMessage({
  text: "Delete your account?",
  reply_markup: {
    inline_keyboard: [
      [{ text: "Yes, delete", callback_data: "confirm_delete" }, { text: "Cancel", callback_data: "cancel" }]
    ]
  }
})
```

### Answer the callback (dismiss the spinner)

When someone taps a callback button, Telegram expects a response — even if it's just "ok, I got it." Without `answerCallbackQuery`, the client shows a loading spinner forever. Rude.

```js
Api.answerCallbackQuery({
  callback_query_id: update.callback_query.id,
  text: "Saved."
})
```

The optional `text` pops a small toast at the top of the chat. Keep it short.

### Update the message they tapped

Often you want to change the message instead of sending a new one:

```js
Api.editMessageText({
  chat_id: chat.id,
  message_id: update.callback_query.message.message_id,
  text: "You picked Help. Here's what that means..."
})
```

Or swap the keyboard while leaving text alone — `editMessageReplyMarkup`. [Editing Messages](editing-messages.md) walks through both.

---

## callback_data limits

Telegram caps `callback_data` at **64 bytes**. Don't stash JSON in there. Store an ID or short token, look up the rest in [`db.user`](../db-instance/user.md).

```js
// Good — short token
callback_data: "help"

// Bad — won't fit
callback_data: JSON.stringify({ userId: 123, action: "delete", reason: "..." })
```

---

## Where to go next

- [Handling Callbacks](../getting-started-with-tbl/handling-callbacks.md) — full callback flow tutorial
- [Editing Messages](editing-messages.md) — change text and keyboards after send
- [Callbacks](callbacks.md) — route callback handling through `on_run`
- [Method Chaining](method-chaining.md) — if you sent the message with `await Api.sendMessage`
