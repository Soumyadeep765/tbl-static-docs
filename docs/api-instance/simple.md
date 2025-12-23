# Using the Api Instance

This page shows simple examples of using the **Api instance**.

All examples assume the command is already running and the Api instance is already available.

## Api.sendMessage

Used to send text messages to a chat.

### Simple Message

```js
Api.sendMessage({
  text: "Hello user!"
})
```

This sends a message to the **current chat** (the chat where the command was triggered).

!!! tip
    You usually don’t need to pass `chat_id`.  
    Api automatically knows which chat to reply to.

### Message with Formatting

```js
Api.sendMessage({
  text: "*Hello!* Welcome to my bot 😊",
  parse_mode: "Markdown"
})
```

Telegram Markdown can be used to format text such as **bold**, _italic_, and inline code.

!!! tip
    Keep formatting simple to avoid Telegram Markdown parsing issues.

### Message with Inline Buttons

```js
Api.sendMessage({
  text: "Choose an option below:",
  reply_markup: {
    inline_keyboard: [
      [{ text: "Visit Website", url: "https://telebothost.com" }],
      [{ text: "Help", callback_data: "help" }]
    ]
  }
})
```

Inline buttons let users interact with your bot without typing messages.

## Api.sendPhoto

Used to send images to a chat.

### Send a Photo with Caption

```js
Api.sendPhoto({
  photo: "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg",
  caption: "Cute dog 🐕"
})
```

This photo is sent to the **current chat** by default.

!!! tip
    You can use URLs or file IDs for the `photo` field.

## Using chat_id Explicitly

By default, Api methods send messages to the **current chat**.

If you want to send a message to a **different chat**, you can pass `chat_id` manually.

```js
Api.sendMessage({
  chat_id: 123456789,
  text: "This message goes to another chat"
})
```

!!! warning
    Only use explicit `chat_id` when you are sure the bot has access to that chat.

## Telegram API Reference

The Api instance supports **all methods available in the Telegram Bot API**.

To see all possible methods and options, refer to the official Telegram documentation:

https://core.telegram.org/bots/api

Any method listed there can be used in TBL as:

Api.methodName({ ... })

## Summary

- Api methods accept an object as input
- Messages are sent to the current chat by default
- `chat_id` can be passed explicitly if needed
- Formatting and buttons are supported
- Api directly maps to Telegram Bot API methods