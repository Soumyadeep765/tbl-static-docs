# Media and Files

Text gets you far. Eventually you'll send photos, PDFs, voice notes, or stickers. **`Api`** mirrors Telegram's media methods — same object style as `sendMessage`, same "just works in the current chat" defaults.

URLs for testing. `file_id` for production — so Telegram doesn't re-fetch the same image every time like an overeager intern.

---

## What can you send?

| Method | Best for |
| --- | --- |
| `Api.sendPhoto` | Images (inline preview) |
| `Api.sendDocument` | PDFs, archives, downloads |
| `Api.sendAudio` | Music tracks with metadata |
| `Api.sendVoice` | Round voice-message player |
| `Api.sendVideo` | Video files |
| `Api.sendSticker` | Stickers |
| `Api.sendAnimation` | GIF-style clips |

All accept a URL, a `file_id` from a previous upload, or a file reference already on Telegram's servers.

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md).

---

## How to use it

### Photos

```js
Api.sendPhoto({
  photo: "https://example.com/screenshot.png",
  caption: "Here's what your dashboard looks like."
})
```

### Documents

For PDFs, archives, anything that isn't treated as an inline photo:

```js
Api.sendDocument({
  document: "https://example.com/report.pdf",
  caption: "Monthly report"
})
```

Users get a download-style attachment.

### Audio and voice

```js
Api.sendAudio({
  audio: "https://example.com/track.mp3",
  title: "Intro theme"
})

Api.sendVoice({
  voice: "https://example.com/note.ogg"
})
```

Voice messages show the round player UI. Audio files show as music tracks with metadata.

### Video

```js
Api.sendVideo({
  video: "https://example.com/demo.mp4",
  caption: "Product walkthrough",
  supports_streaming: true
})
```

---

## Try it — copy-paste examples

### Photo with caption

```js
Api.sendPhoto({
  photo: "https://example.com/welcome.png",
  caption: "*Welcome!* Tap /help to get started.",
  parse_mode: "Markdown"
})
```

### Document as a reply

Thread under a specific message:

```js
Api.sendDocument({
  document: fileUrl,
  caption: "Here's your receipt.",
  reply_to_message_id: message.message_id
})
```

### Send, edit caption, delete

```js
let photo = await Api.sendPhoto({ photo: url, caption: "Draft" })
await photo.editCaption("Final version")
await photo.delete()
```

See [Method Chaining](method-chaining.md) for edit and delete helpers on the returned object.

---

## Captions and formatting

Most media methods accept `caption` and `parse_mode` just like messages. Same Markdown rules apply — don't get clever with nested formatting on day one.

Check the [Telegram Bot API media methods](https://core.telegram.org/bots/api#available-methods) for the full parameter list — dimensions, thumbnails, spoiler flags, and so on all pass through unchanged.

---

## Bot.sendPhoto vs Api.sendPhoto

| | `Bot.sendPhoto` | `Api.sendPhoto` |
| --- | --- | --- |
| Syntax | `Bot.sendPhoto("url", "caption")` | `Api.sendPhoto({ photo, caption, ... })` |
| Best for | Quick sends inside bot flows | Keyboards, spoiler mode, precise Telegram options |

When you need keyboard markup, spoiler mode, or full Telegram control, use `Api`.

---

## Important notes

- `photo` / `document` / etc. accept URL, `file_id`, or existing Telegram file reference
- Use `await` when you need to edit or delete what you just sent
- Case-sensitive method names — `Api.sendPhoto`, not `Api.sendphoto`
