# Sending Messages

`Bot` provides shorthand methods for sending text, keyboards, and media to the **current chat**. All methods auto-fill `chat_id` from the command context.

## Text messages

### Simple string

```js
Bot.sendMessage("Hello!")
```

Defaults to `parse_mode: "Markdown"`. Keep formatting simple — unclosed markers cause send failures.

### Object format

```js
Bot.sendMessage({ text: "Hello!" })
```

### Custom parse mode

```js
await Bot.sendMessage("Hello friend", { parse_mode: "HTML" })
```

### Disable formatting

```js
Bot.sendMessage("Price: $5 * 2", { parse_mode: undefined })
```

## Reply keyboards

Send a message with a reply keyboard using comma-separated button labels:

```js
// String format
Bot.sendKeyboard("Choose an option:", "Yes,No,Maybe")

// Object format
Bot.sendKeyboard({
  text: "Choose an option:",
  keyboard: "Yes,No,Maybe"
})
```

For **inline buttons** (callback buttons under a message), use [`Api.sendMessage`](../api-instance/inline-keyboards.md) with `reply_markup` instead.

## Media

All media methods accept a **string** (file URL or path) or an **object** with the media field and options.

| Method | String example | Object example |
| --- | --- | --- |
| `Bot.sendPhoto` | `Bot.sendPhoto("photo.jpg")` | `Bot.sendPhoto({ photo: "photo.jpg", caption: "Nice!" })` |
| `Bot.sendDocument` | `Bot.sendDocument("file.pdf")` | `Bot.sendDocument({ document: "file.pdf", caption: "Your file" })` |
| `Bot.sendAudio` | `Bot.sendAudio("music.mp3")` | `Bot.sendAudio({ audio: "music.mp3", caption: "Listen" })` |
| `Bot.sendVideo` | `Bot.sendVideo("video.mp4")` | `Bot.sendVideo({ video: "video.mp4", caption: "Watch" })` |
| `Bot.sendVoice` | `Bot.sendVoice("voice.ogg")` | `Bot.sendVoice({ voice: "voice.ogg", caption: "Voice note" })` |

Captions default to Markdown when provided.

## Awaiting responses

`await` is optional. When used, you get the Telegram API response — and message-sending methods return a **chainable object**:

```js
let sent = await Bot.sendMessage("Pinned message")
await sent.pin()
await sent.editText("Updated.")
await sent.delete()
```

See [Api Method Chaining](../api-instance/method-chaining.md) for all chained methods. Not every `Bot` send method returns a chainable object — `sendMessage` and media sends do when awaited.

## Debugging with `Bot.inspect`

Formats values and sends them to the current chat. Useful during development.

```js
// Single value
Bot.inspect(user)

// Multiple values
Bot.inspect("User data:", user, { step: 2 })

// String + object
Bot.inspect("Result:", someArray)
```

| Behavior | Detail |
| --- | --- |
| Input | One or more values (strings sent as-is, objects formatted) |
| Output | Sent as a plain-text message (no Markdown) |
| `console.log` | Routes to `Bot.inspect` in TBL commands |

!!! warning "Development only"
    Avoid sending `Bot.inspect` output to end users in production — it may expose internal data.

## What's not in Bot

Telegram **read/query** methods are not available on `Bot`:

- `getChat`, `getMe`, `getUserProfilePhotos`, etc.

Use the [`Api` instance](../api-instance/index.md) for those. `Bot` is for **sending output** and **controlling bot flow**.

## Method reference

| Method | Parameters | Description |
| --- | --- | --- |
| `sendMessage(text, options?)` | Text string or `{ text, ...options }` | Send formatted text |
| `sendKeyboard(text, keyboard?, options?)` | Text + comma-separated buttons | Send with reply keyboard |
| `sendPhoto(photo, options?)` | URL/path or `{ photo, caption?, ... }` | Send photo |
| `sendDocument(doc, options?)` | URL/path or `{ document, caption?, ... }` | Send document |
| `sendAudio(audio, options?)` | URL/path or `{ audio, caption?, ... }` | Send audio |
| `sendVideo(video, options?)` | URL/path or `{ video, caption?, ... }` | Send video |
| `sendVoice(voice, options?)` | URL/path or `{ voice, caption?, ... }` | Send voice message |
| `inspect(...values)` | One or more values | Debug output to chat |

## Important notes

- All send methods target the **current chat** — no `chat_id` needed
- Method names are case-sensitive
- Errors from Telegram are logged; use `await` and check `res.ok` when failures matter
- For advanced Telegram features (inline keyboards, message edits, rich messages), use [`Api`](../api-instance/index.md)
