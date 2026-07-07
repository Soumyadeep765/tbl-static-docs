# Editing Messages

Messages don't have to be permanent. Telegram lets bots edit text, captions, and keyboards on messages they sent — and **`Api`** exposes all of it.

You'll edit messages constantly in menu-driven bots: swap button labels, replace a status line, remove buttons after the user picks an option. One message morphs instead of five new ones stacking up like dirty dishes.

---

## What can you edit?

| Action | Method |
| --- | --- |
| Change message text | `Api.editMessageText` |
| Change media caption | `Api.editMessageCaption` |
| Swap inline keyboard | `Api.editMessageReplyMarkup` |
| Remove the message | `Api.deleteMessage` |

You need the `message_id` of the message you're changing. In a callback handler that's usually `update.callback_query.message.message_id`. If you just sent it yourself, `await Api.sendMessage(...)` and chain `.editText()` instead — see [Method Chaining](method-chaining.md).

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md).

---

## How to use it

### Edit text

```js
Api.editMessageText({
  chat_id: chat.id,
  message_id: request.message.message_id,
  text: "Updated content.",
  parse_mode: "Markdown"
})
```

Rich messages (Bot API 10.1) — pass `rich_message` instead of `text`:

```js
Api.editMessageText({
  chat_id: chat.id,
  message_id: request.message.message_id,
  rich_message: {
    markdown: "**Status:** Complete"
  }
})
```

### Edit caption on media

Photos and documents use captions, not message text:

```js
Api.editMessageCaption({
  chat_id: chat.id,
  message_id: request.message.message_id,
  caption: "Revised caption."
})
```

### Swap the inline keyboard

Remove buttons after a choice, or replace the whole menu:

```js
Api.editMessageReplyMarkup({
  chat_id: chat.id,
  message_id: request.message.message_id,
  reply_markup: {
    inline_keyboard: [[{ text: "Done", callback_data: "done" }]]
  }
})
```

Pass an empty `inline_keyboard: []` to strip buttons entirely.

---

## Try it — copy-paste examples

### Typical callback flow

The pattern that keeps chats tidy:

```js
// 1. Dismiss the spinner
Api.answerCallbackQuery({
  callback_query_id: update.callback_query.id
})

// 2. Update the same message
Api.editMessageText({
  chat_id: chat.id,
  message_id: update.callback_query.message.message_id,
  text: "You chose Option A. Processing..."
})

// 3. Optionally hand off to another command
Bot.runCommand("/option_a_flow")
```

### Temporary notice — send, wait, delete

```js
let sent = await Api.sendMessage({ text: "Temporary notice." })
await sent.delete()
```

Or standalone:

```js
Api.deleteMessage({
  chat_id: chat.id,
  message_id: request.message.message_id
})
```

---

## What you can't edit

Bots can't edit messages they didn't send (with the usual Telegram exceptions around admins and channels). They also can't turn a text message into a photo — edit the text or send new media.

Telegram returns an error if the message is too old or the content is identical to what's already there. Check `res.ok` when using `await`.

---

## Reference

Full parameter lists in the Telegram docs:

- [editMessageText](https://core.telegram.org/bots/api#editmessagetext)
- [editMessageCaption](https://core.telegram.org/bots/api#editmessagecaption)
- [editMessageReplyMarkup](https://core.telegram.org/bots/api#editmessagereplymarkup)
- [deleteMessage](https://core.telegram.org/bots/api#deletemessage)

Also see [Method Chaining](method-chaining.md) for shorthand after `await Api.sendMessage`.
