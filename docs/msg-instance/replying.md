# Replying

All `reply*` methods send a **new message** as a reply to the current one. `chat_id` and `reply_to_message_id` are set automatically.

```js
await msg.reply("Hello!")
await msg.replyPhoto("https://example.com/cat.jpg", { caption: "Cute cat" })
```

There is no `msg.send()` — use `msg.reply()` to respond in the same chat, or `Bot.sendMessage()` / `Api.sendMessage()` to send without replying.

---

## Text

### `reply(text, options?)` — alias: `r`

```js
await msg.reply("Hello!")
await msg.r("Short alias works too")

await msg.reply("**Bold** text", { parse_mode: "Markdown" })
await msg.reply({ text: "Full control", parse_mode: "HTML", disable_web_page_preview: true })
```

| Arg | Type | Description |
| --- | --- | --- |
| `text` | `string` or `object` | Message text, or full `sendMessage` params |
| `options` | `object` | Extra Telegram options (merged with defaults) |

Default: `parse_mode: "Markdown"`. Throws if text is empty.

---

## Photos and videos

### `replyPhoto(photo, options?)` — alias: `photo`

```js
await msg.replyPhoto("https://example.com/image.jpg")
await msg.replyPhoto(fileId, { caption: "From Telegram file_id" })
await msg.photo({ photo: url, caption: "Object syntax", parse_mode: "HTML" })
```

### `replyVideo(video, options?)` — alias: `video`

```js
await msg.replyVideo("https://example.com/clip.mp4", { caption: "Watch this" })
```

### `replyAnimation(animation, options?)` — alias: `gif`, `animation`

```js
await msg.replyAnimation("https://example.com/funny.gif", { caption: "GIF" })
```

---

## Audio and documents

### `replyAudio(audio, options?)` — alias: `audio`

```js
await msg.replyAudio(fileId, { title: "Song", performer: "Artist" })
```

### `replyVoice(voice, options?)` — alias: `voice`

```js
await msg.replyVoice(fileId, { caption: "Voice note" })
```

### `replyDocument(document, options?)` — alias: `doc`, `document`

```js
await msg.replyDocument("https://example.com/file.pdf", { caption: "Report" })
await msg.doc(fileId)
```

---

## Stickers and dice

### `replySticker(sticker, options?)` — alias: `sticker`

```js
await msg.replySticker("CAACAgUAAxkBAAECX-9g1...")
```

Sticker shorthand does not set a default `parse_mode`.

### `replyDice(emoji?, options?)` — alias: `dice`

```js
await msg.replyDice()           // default 🎲
await msg.replyDice("🎯")
await msg.replyDice("🏀")
await msg.replyDice("🎰")
```

Supported dice emojis: `🎲`, `🎯`, `🏀`, `⚽`, `🎳`, `🎰`.

---

## Location and contact

### `replyLocation(lat, lng, options?)` — alias: `location`

```js
// Coordinates
await msg.replyLocation(40.7128, -74.0060)

// Object syntax
await msg.replyLocation({
  latitude: 40.7128,
  longitude: -74.0060,
  title: "New York"
})
```

### `replyContact(phone, firstName, options?)` — alias: `contact`

```js
await msg.replyContact("+1234567890", "John")

await msg.replyContact({
  phone_number: "+1234567890",
  first_name: "John",
  last_name: "Doe"
})
```

---

## Polls

### `replyPoll(question, options?, pollOptions?)` — alias: `poll`

```js
await msg.replyPoll("Favorite color?", ["Red", "Blue", "Green"])

await msg.replyPoll({
  question: "Best language?",
  options: ["JavaScript", "Python", "TBL"],
  is_anonymous: false,
  allows_multiple_answers: true
})
```

---

## Method reference

| Method | Alias | Telegram API |
| --- | --- | --- |
| `reply(text, opts?)` | `r` | `sendMessage` |
| `replyPhoto(photo, opts?)` | `photo` | `sendPhoto` |
| `replyVideo(video, opts?)` | `video` | `sendVideo` |
| `replyAudio(audio, opts?)` | `audio` | `sendAudio` |
| `replyVoice(voice, opts?)` | `voice` | `sendVoice` |
| `replyDocument(doc, opts?)` | `doc` | `sendDocument` |
| `replySticker(sticker, opts?)` | `sticker` | `sendSticker` |
| `replyAnimation(anim, opts?)` | `gif` | `sendAnimation` |
| `replyLocation(lat, lng, opts?)` | `location` | `sendLocation` |
| `replyContact(phone, name, opts?)` | `contact` | `sendContact` |
| `replyPoll(question, opts, opts?)` | `poll` | `sendPoll` |
| `replyDice(emoji?, opts?)` | `dice` | `sendDice` |

---

## Examples

### Reply with inline keyboard

```js
await msg.reply({
  text: "Choose an option:",
  reply_markup: {
    inline_keyboard: [
      [{ text: "Yes", callback_data: "/yes" }, { text: "No", callback_data: "/no" }]
    ]
  }
})
```

### Reply with photo and HTML caption

```js
await msg.replyPhoto(process.env.WELCOME_IMAGE, {
  caption: "<b>Welcome</b> to the bot!",
  parse_mode: "HTML"
})
```

### Show typing then reply

```js
await msg.sendChatAction("typing")
await sleep(1)
await msg.reply("Here's your answer: " + params)
```

---

## Notes

- All reply methods return a **Promise** — use `await` when you need the result
- Returned message objects support [Api method chaining](../api-instance/method-chaining.md) (`sent.pin()`, `sent.editText()`, etc.)
- Business messages automatically include `business_connection_id` when needed
- Media shorthand defaults to `parse_mode: "Markdown"` for captions
