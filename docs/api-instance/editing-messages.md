# Editing Messages

Messages don't have to be permanent. Telegram lets bots edit text, captions, and keyboards on messages they sent — and Api exposes all of it.

You'll edit messages constantly in menu-driven bots: swap button labels, replace a status line, remove buttons after the user picks an option.

## Edit text

```js
Api.editMessageText({
  chat_id: chat.id,
  message_id: message.message_id,
  text: "Updated content.",
  parse_mode: "Markdown"
})
```

You need the `message_id` of the message you're changing. In a callback handler that's usually `update.callback_query.message.message_id`. If you just sent the message yourself, `await Api.sendMessage(...)` and chain `.editText()` instead — see [Method Chaining](method-chaining.md).

## Edit caption on media

Photos and documents use captions, not message text:

```js
Api.editMessageCaption({
  chat_id: chat.id,
  message_id: message.message_id,
  caption: "Revised caption."
})
```

## Swap the inline keyboard

Remove buttons after a choice, or replace the whole menu:

```js
Api.editMessageReplyMarkup({
  chat_id: chat.id,
  message_id: message.message_id,
  reply_markup: {
    inline_keyboard: [[{ text: "Done", callback_data: "done" }]]
  }
})
```

Pass an empty `inline_keyboard: []` to strip buttons entirely.

## Delete instead of edit

Sometimes deletion is cleaner:

```js
Api.deleteMessage({
  chat_id: chat.id,
  message_id: message.message_id
})
```

Or, if you have the chained response object:

```js
let msg = await Api.sendMessage({ text: "Temporary notice." })
await msg.delete()
```

## What you can't edit

Bots can't edit messages they didn't send (with the usual Telegram exceptions around admins and channels). They also can't turn a text message into a photo — edit the text or send new media.

Telegram returns an error if the message is too old or the content is identical to what's already there. Check `res.ok` when using `await`.

## Typical callback flow

1. User taps inline button
2. `Api.answerCallbackQuery(...)` — dismiss the spinner
3. `Api.editMessageText(...)` — update the same message
4. Optionally `Bot.runCommand(...)` — start a new flow

That pattern keeps chats tidy. One message morphs instead of five new ones stacking up.

## Reference

Full parameter lists live in the Telegram docs:

- [editMessageText](https://core.telegram.org/bots/api#editmessagetext)
- [editMessageCaption](https://core.telegram.org/bots/api#editmessagecaption)
- [editMessageReplyMarkup](https://core.telegram.org/bots/api#editmessagereplymarkup)
- [deleteMessage](https://core.telegram.org/bots/api#deletemessage)
