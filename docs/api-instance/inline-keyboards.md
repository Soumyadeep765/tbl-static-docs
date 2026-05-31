# Inline Keyboards

Inline buttons sit *inside* the message bubble — not in the keyboard area at the bottom of the screen. Users tap them; Telegram sends a callback query to your bot; you respond with Api.

Reply keyboards (the `Help, About` style from the tutorials) are different. Those send plain text. Inline buttons send structured callback data.

## A minimal keyboard

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

URL buttons open a link. `callback_data` buttons fire a callback query — you'll handle that in a command triggered by the callback.

## Layout

Each inner array is a row. Buttons in the same row sit side by side:

```js
reply_markup: {
  inline_keyboard: [
    [{ text: "Yes", callback_data: "yes" }, { text: "No", callback_data: "no" }],
    [{ text: "Cancel", callback_data: "cancel" }]
  ]
}
```

Two buttons on the first row, one full-width button below.

## Answering callbacks

When someone taps a callback button, Telegram expects a response — even if it's just "ok, I got it." Without `answerCallbackQuery`, the client shows a loading spinner on the button.

```js
Api.answerCallbackQuery({
  callback_query_id: update.callback_query.id, // or, request.id 
  text: "Saved."
})
```

The optional `text` pops a small toast at the top of the chat. Keep it short.

## Updating the message they tapped

Often you want to change the message instead of sending a new one:

```js
Api.editMessageText({
  chat_id: chat.id,
  message_id: update.callback_query.message.message_id,
  text: "You picked Help. Here's what that means..."
})
```

Or swap the keyboard while leaving the text alone — `editMessageReplyMarkup`. [Editing Messages](editing-messages.md) walks through both.

## callback_data limits

Telegram caps `callback_data` at 64 bytes. Don't stash JSON in there. Store an ID or short token, look up the rest in [User storage](../user-instance/basics.md) or [Bot storage](../bot-instance/storing-data.md).

## URL vs callback

| Button type | User sees | Your bot receives |
| --- | --- | --- |
| `url` | Opens browser / in-app view | Nothing |
| `callback_data` | Stays in chat | Callback query update |

Mix them freely in the same keyboard.

## Where to go next

- [Editing Messages](editing-messages.md) — change text and keyboards after send
- [Callbacks](callbacks.md) — route callback handling through `on_run`
- [Method Chaining](method-chaining.md) — if you sent the message with `await Api.sendMessage`
