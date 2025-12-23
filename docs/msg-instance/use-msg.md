## Using the msg Instance

The **msg instance** is used to interact with the **current Telegram message**.

It allows replying, sending new messages, editing, deleting, reacting, forwarding, and performing chat actions.

All msg methods return **Promises**.  
Using `await` is optional and only needed if you want the response object.

## Available Methods

- Core Messaging  
  `msg.reply()`  
  `msg.send()`

- Media Messages  
  `msg.replyPhoto()`  
  `msg.replyVideo()`  
  `msg.replyDocument()`

- Message Management  
  `msg.editText()`  
  `msg.delete()`  
  `msg.react()`  
  `msg.pin()`  
  `msg.unpin()`

- Forwarding & Copying  
  `msg.forward()`  
  `msg.copy()`

- Special Messages  
  `msg.replySticker()`  
  `msg.replyDice()`

- Chat Actions  
  `msg.sendChatAction()`

## Core Messaging

Reply to the current message:

```js
msg.reply("Hello!")
let result = await msg.reply("Hello!")
```

Send a new message:

```js
msg.send("This is a new message")
await msg.send("This is a new message", { parse_mode: "Markdown" })
```

## Media Messages

Reply with a photo:

```js
msg.replyPhoto("https://example.com/cat.jpg", { caption: "Cute cat 🐱" })
await msg.replyPhoto("https://example.com/cat.jpg", { caption: "Cute cat 🐱" })
```

Reply with a video:

```js
msg.replyVideo("https://example.com/video.mp4")
await msg.replyVideo("https://example.com/video.mp4", { caption: "Watch this!" })
```

Reply with a document:

```js
msg.replyDocument("file.pdf")
await msg.replyDocument("file.pdf")
```

## Message Management

Edit message text:

```js
msg.editText("Updated text")
await msg.editText("Updated text", { parse_mode: "Markdown" })
```

Delete a message:

```js
msg.delete(msg.message_id)
await msg.delete(msg.message_id)
```

React to a message:

```js
msg.react("👍")
msg.react("🔥", true)
```

Pin and unpin messages:

```js
msg.pin()
msg.unpin(msg.message_id)
```

## Forwarding & Copying

Forward a message:

```js
msg.forward(123456789)
await msg.forward(123456789)
```

Copy a message:

```js
msg.copy(123456789, { caption: "Copied message" })
await msg.copy(123456789, { caption: "Copied message" })
```

## Special Messages

Reply with a sticker:

```js
msg.replySticker("CAACAgUAAxkBAAECX-9g1...")
await msg.replySticker("CAACAgUAAxkBAAECX-9g1...")
```

Reply with a dice:

```js
msg.replyDice("🎲")
await msg.replyDice("🎲")
```

## Chat Actions

Show typing indicator:

```js
msg.sendChatAction("typing")
await msg.sendChatAction("typing")
```

Other supported actions include:

- `upload_photo`
- `record_video`
- `record_audio`
- `upload_document`

## Chained Methods

When you use `await`, msg methods support **chained actions**.

```js
let data = await msg.reply("Hello!")
data.pin()
```

More details about [chained] methods: **[Api chained]**

[chained]: ../api-instance/api-chain.md
[Api chained]: ../api-instance/api-chain.md