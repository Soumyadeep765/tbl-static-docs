# Editing

Edit the **current message** in place — text, captions, media, keyboards, and live locations. `chat_id` and `message_id` are filled automatically.

```js
await msg.editText("Updated content")
await msg.editCaption("New caption")
```

You can only edit messages the bot sent (or has permission to edit). User messages in private chats can be edited by the bot only if the bot sent them.

---

## Text and captions

### `editText(text, options?)` — alias: `edit`

```js
await msg.editText("New text")
await msg.edit("**Bold** update", { parse_mode: "Markdown" })

await msg.editText({
  text: "Full control",
  parse_mode: "HTML",
  link_preview_options: { is_disabled: true }
})
```

Default: `parse_mode: "Markdown"`. Throws if text is empty.

### `editCaption(caption, options?)` — alias: `editCap`, `editCaptionText`

For photo, video, document, and animation messages:

```js
await msg.editCaption("Updated caption")
await msg.editCap({ caption: "New *caption*", parse_mode: "Markdown" })
```

---

## Media and keyboards

### `editMedia(media, options?)` — alias: `editMessageMedia`

Replace photo/video/animation on the current message:

```js
await msg.editMedia({
  type: "photo",
  media: "https://example.com/new-image.jpg",
  caption: "Replaced photo"
})

// Or pass InputMedia directly in options
await msg.editMedia({ type: "photo", media: fileId }, { parse_mode: "HTML" })
```

### `editReplyMarkup(replyMarkup, options?)` — alias: `editMarkup`, `editKeyboard`

Update inline or reply keyboard:

```js
await msg.editReplyMarkup({
  inline_keyboard: [
    [{ text: "Done", callback_data: "/done" }]
  ]
})

// Or wrap in reply_markup
await msg.editKeyboard({ reply_markup: { inline_keyboard: [] } })
```

Pass an empty keyboard to remove buttons.

---

## Live location

### `editLiveLocation(lat, lng, options?)` — alias: `editLocation`

```js
await msg.editLiveLocation(40.7128, -74.0060)

await msg.editLocation({
  latitude: 40.7128,
  longitude: -74.0060,
  horizontal_accuracy: 10
})
```

### `stopLiveLocation(options?)` — alias: `stopLocation`

Stop sharing live location on the current message:

```js
await msg.stopLiveLocation()
```

---

## Polls

### `stopPoll(options?)` — alias: `endPoll`

Close an active poll on the current message:

```js
await msg.stopPoll()
```

Returns the stopped poll object.

---

## Method reference

| Method | Alias | Telegram API |
| --- | --- | --- |
| `editText(text, opts?)` | `edit` | `editMessageText` |
| `editCaption(caption, opts?)` | `editCap` | `editMessageCaption` |
| `editMedia(media, opts?)` | `editMessageMedia` | `editMessageMedia` |
| `editReplyMarkup(rm, opts?)` | `editMarkup`, `editKeyboard` | `editMessageReplyMarkup` |
| `editLiveLocation(lat, lng, opts?)` | `editLocation` | `editMessageLiveLocation` |
| `stopLiveLocation(opts?)` | `stopLocation` | `stopMessageLiveLocation` |
| `stopPoll(opts?)` | `endPoll` | `stopPoll` |

---

## Examples

### Edit bot's last reply in a loop

```js
let sent = await msg.reply("Loading...")
await sleep(2)
await sent.editText("Done!")
```

### Update progress message

```js
await msg.editText("Step 1/3 complete...")
// ... later in same command
await msg.editText("Step 2/3 complete...")
await msg.editText("All done!")
```

### Swap inline keyboard

```js
await msg.editReplyMarkup({
  inline_keyboard: [
    [{ text: "Page 2", callback_data: "/page2" }],
    [{ text: "Close", callback_data: "/close" }]
  ]
})
```

### Edit media message caption

```js
if (msg.photo) {
  await msg.editCaption("Photo caption updated")
} else if (msg.text) {
  await msg.editText("Text updated")
}
```

---

## Notes

- `editText` works on text messages; `editCaption` on media messages
- Default `parse_mode: "Markdown"` on shorthand calls
- Editing another message in the same chat requires that message's `message_id` via `Api.editMessageText`
- All methods return Promises — failed edits (e.g. message too old) return `ok: false` from Telegram
