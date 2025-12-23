## Sending Messages and Media with Bot

These Bot methods send messages or media to the **current chat**.

- All messages go to the current chat by default
- Using `await` is optional
- If awaited, the Telegram API response is returned
- Only **some methods** support [chained] actions

## Sending Text Messages

### Simple Text

```js
Bot.sendMessage("Hello user!")
```

### Object Format

```js
Bot.sendMessage({ text: "Hello user!" })
```

### With Formatting

```js
let res = await Bot.sendMessage(
  "Hello friend",
  { parse_mode: "HTML" }
)
```

## Sending Keyboards

### String Format

```js
Bot.sendKeyboard("Choose an option:", "Yes,No")
```

### Object Format

```js
Bot.sendKeyboard({
  text: "Choose an option:",
  keyboard: "Yes,No"
})
```

## Sending Media

All media methods support **string** and **object** formats.

### Photo

```js
Bot.sendPhoto("photo.jpg")

Bot.sendPhoto({
  photo: "photo.jpg",
  caption: "Nice view!"
})
```

### Document

```js
Bot.sendDocument("file.pdf", "Here is your pdf")

Bot.sendDocument({
  document: "file.pdf",
  caption: "Here is your file"
})
```

### Audio

```js
Bot.sendAudio("music.mp3")

Bot.sendAudio({
  audio: "music.mp3",
  caption: "Here is your music"
})
```

### Video

```js
Bot.sendVideo("video.mp4")

Bot.sendVideo({
  video: "video.mp4",
  caption: "Watch this"
})
```

### Voice

```js
Bot.sendVoice("voice.ogg")

Bot.sendVoice({
  voice: "voice.ogg",
  caption: "Voice note"
})
```

## Using Chained Methods (Limited Support)

Only **specific Bot methods** return a response that supports **[chained] methods**  
(when used with `await`).

Example:

```js
let data = await Bot.sendMessage("Pinned message")

data.pin()
```

!!! note
    Not all Bot methods support chaining.
    Chaining works only when the method returns a Telegram message object.

## Debugging with Bot.inspect()

`Bot.inspect()` sends **inspect data to the current chat**.

It is mainly used for **debugging** and **checking values quickly**.

### Inspect Any Data

```js
Bot.inspect({ user: "Alice", id: 123 })
```

### Inspect Multiple Values

```js
Bot.inspect(
  "User data:",
  user,
  { id: 123 },
  someArray
)
```

The inspected data is formatted and sent as a message in the chat.

!!! tip
    Use `Bot.inspect()` only during development.
    Avoid using it in production bots for users.

## Available Bot Methods

Only the following Bot methods are available for sending output:

- `Bot.sendMessage`
- `Bot.sendKeyboard`
- `Bot.sendDocument`
- `Bot.sendPhoto`
- `Bot.sendAudio`
- `Bot.sendVideo`
- `Bot.sendVoice`
- `Bot.inspect`

These methods are intentionally limited and focused on output and flow control.

## Not Available in Bot

Methods that **read or query Telegram data**, such as:

- `getChat`
- `getMe`
- `getUserProfilePhotos`
- or similar Telegram API read methods

are **not available** in the Bot instance.

!!! info
    The Bot instance is designed for sending responses and controlling bot behavior,
    not for querying Telegram data.

## Important Notes

- All Bot send methods use the current chat
- `await` is optional
- Only limited methods support chained actions
- `Bot.inspect()` sends output to chat
- Method names are case-sensitive
- Errors can be handled using the `!` command

[chained]: ../api-instance/api-chain.md