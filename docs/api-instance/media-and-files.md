# Media and Files

Text gets you far. Eventually you'll send photos, PDFs, voice notes, or stickers. Api mirrors Telegram's media methods — same object style as `sendMessage`.

## Photos

```js
Api.sendPhoto({
  photo: "https://example.com/screenshot.png",
  caption: "Here's what your dashboard looks like."
})
```

`photo` accepts a URL, a `file_id` from a previous upload, or a file reference your bot already has on Telegram's servers. URLs are the quickest way to test; `file_id` is what you want in production so Telegram doesn't re-fetch the same image every time.

## Documents

For PDFs, archives, anything that isn't treated as an inline photo:

```js
Api.sendDocument({
  document: "https://example.com/report.pdf",
  caption: "Monthly report"
})
```

Users get a download-style attachment.

## Audio and voice

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

## Video

```js
Api.sendVideo({
  video: "https://example.com/demo.mp4",
  caption: "Product walkthrough",
  supports_streaming: true
})
```

## Stickers and animations

Stickers use `sendSticker`. GIF-style clips use `sendAnimation`. Both take a `file_id` or upload source the same way as photos.

Check the [Telegram Bot API media methods](https://core.telegram.org/bots/api#available-methods) for the full parameter list — dimensions, thumbnails, spoiler flags, and so on all pass through unchanged.

## Captions and formatting

Most media methods accept `caption` and `parse_mode` just like messages. Same Markdown rules apply — don't get clever with nested formatting on day one.

## Sending media as a reply

Add `reply_to_message_id` if the file should thread under a specific message:

```js
Api.sendDocument({
  document: fileUrl,
  reply_to_message_id: message.message_id
})
```

## Bot.sendPhoto vs Api.sendPhoto

`Bot.sendPhoto("url", "caption")` works for quick sends inside bot flows. When you need keyboard markup, spoiler mode, or precise Telegram options, use Api.

## Chaining after send

```js
let photo = await Api.sendPhoto({ photo: url, caption: "Draft" })
await photo.editCaption("Final version")
```

See [Method Chaining](method-chaining.md) for edit and delete helpers on the returned object.
