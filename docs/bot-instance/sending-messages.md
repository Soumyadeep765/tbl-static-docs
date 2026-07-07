# Sending Messages

The bread and butter of every bot: **sending stuff to the chat**. `Bot` gives you shorthand methods for text, keyboards, and media — all auto-targeted to the **current chat**. No `chat_id` required. Less typing, more chatting.

For inline buttons, message edits, and other Telegram power moves, see [`Api`](../api-instance/index.md). `Bot` is your fast lane for everyday output.

---

## What can Bot send?

| Method | What it sends |
| --- | --- |
| `Bot.sendMessage` | Formatted text |
| `Bot.sendKeyboard` | Text + reply keyboard (bottom of screen) |
| `Bot.sendPhoto` / `sendDocument` / etc. | Media files |
| `Bot.inspect` | Debug output (dev only) |

All send methods use the **current chat** from command context. Method names are case-sensitive — `Bot.sendMessage` works, `Bot.sendmessage` does not. The universe is cruel but consistent.

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md).

---

## How to use it

### Text messages

Simplest possible send:

```js
Bot.sendMessage("Hello!")
```

Defaults to `parse_mode: "Markdown"`. Keep formatting simple — unclosed `*` or `_` markers are the #1 reason messages fail to send.

Object format works too:

```js
Bot.sendMessage({ text: "Hello!" })
```

Custom parse mode or no formatting at all:

```js
await Bot.sendMessage("Hello friend", { parse_mode: "HTML" })

// Literal asterisks — no Markdown interpretation
Bot.sendMessage("Price: $5 * 2", { parse_mode: undefined })
```

### Reply keyboards

Comma-separated button labels at the bottom of the screen:

```js
// String format
Bot.sendKeyboard("Choose an option:", "Yes,No,Maybe")

// Object format
Bot.sendKeyboard({
  text: "Choose an option:",
  keyboard: "Yes,No,Maybe"
})
```

For **inline buttons** (tappable buttons *inside* the message bubble), use [`Api.sendMessage`](../api-instance/inline-keyboards.md) with `reply_markup` instead.

### Media

String (URL or path) or object with options:

```js
Bot.sendPhoto("photo.jpg")
Bot.sendPhoto({ photo: "photo.jpg", caption: "Nice shot!" })

Bot.sendDocument("file.pdf")
Bot.sendVideo({ video: "video.mp4", caption: "Watch this" })
```

| Method | String example | Object example |
| --- | --- | --- |
| `Bot.sendPhoto` | `Bot.sendPhoto("photo.jpg")` | `Bot.sendPhoto({ photo: "photo.jpg", caption: "Nice!" })` |
| `Bot.sendDocument` | `Bot.sendDocument("file.pdf")` | `Bot.sendDocument({ document: "file.pdf", caption: "Your file" })` |
| `Bot.sendAudio` | `Bot.sendAudio("music.mp3")` | `Bot.sendAudio({ audio: "music.mp3", caption: "Listen" })` |
| `Bot.sendVideo` | `Bot.sendVideo("video.mp4")` | `Bot.sendVideo({ video: "video.mp4", caption: "Watch" })` |
| `Bot.sendVoice` | `Bot.sendVoice("voice.ogg")` | `Bot.sendVoice({ voice: "voice.ogg", caption: "Voice note" })` |

Captions default to Markdown when provided.

---

## Try it — copy-paste examples

### Welcome message

```js
Bot.sendMessage("*Welcome!* Type /help for commands.")
```

### Quick menu with reply keyboard

```js
Bot.sendKeyboard("What would you like?", "Shop,Support,About")
```

### Send then edit (with await)

`await` is optional — but when you use it, send methods return a **chainable object**:

```js
let sent = await Bot.sendMessage("Working on it...")
await sent.editText("Done!")
await sent.delete()
```

See [Method Chaining](../api-instance/method-chaining.md) for all chained methods.

### Debug with `Bot.inspect`

Formats values and sends them to the current chat. `console.log` routes here in command Logic fields:

```js
Bot.inspect(user)
Bot.inspect("Step:", 2, "Result:", someArray)
```

| Behavior | Detail |
| --- | --- |
| Input | One or more values (strings as-is, objects formatted) |
| Output | Plain-text message (no Markdown) |

!!! warning "Development only"
    Don't send `Bot.inspect` output to end users in production — it may expose internal data.

---

## What's not on Bot?

Telegram **read/query** methods aren't on `Bot`:

- `getChat`, `getMe`, `getUserProfilePhotos`, etc.

Use the [`Api` instance](../api-instance/index.md) for those. `Bot` is for **sending output** and **controlling bot flow**.

---

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

---

## Important notes

- All send methods target the **current chat** — no `chat_id` needed
- Errors from Telegram are logged; use `await` and check `res.ok` when failures matter
- For inline keyboards, message edits, and rich messages, use [`Api`](../api-instance/index.md)
