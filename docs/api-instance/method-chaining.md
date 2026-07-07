# Method Chaining

Send a message with Api, get back an object you can act on immediately — edit it, reply to it, pin it, delete it — without hunting for `message_id`.

```js
let sent = await Api.sendMessage({ text: "Hello." })

await sent.pin()
await sent.react("👍")
await sent.editText("Updated.")
await sent.reply("Follow-up.")
await sent.delete()
```

Each method maps to the Telegram API call you'd otherwise write by hand with ids and chat references.

## What supports chaining

Chaining comes from **message-sending** Api methods — `sendMessage`, `sendPhoto`, and similar. Not every Api call returns a chainable object. `getMe` gives you data; `sendMessage` gives you something you can keep working with.

If you're unsure, `await` the send and try — if chaining methods exist on the result, you're good.

## Available chained methods

### Editing and updating

- `editText(text, {...options})`
- `editCaption(caption, {...options})`
- `editMedia(media, {...options})`
- `editReplyMarkup(rm, {...options})`

### Message control

- `delete()`
- `pin(dn = false)` — pass `dn: true` to pin silently
- `unpin()`

### Reactions

- `react(emoji, big = false)`

### Forwarding and copying

- `forward(to, {...options})`
- `copy(to, {...options})`

### Reply methods

- `reply(text, {...options})`
- `replyPhoto(photo, {...options})`
- `replyVideo(video, {...options})`
- `replyAudio(audio, {...options})`
- `replyVoice(voice, {...options})`
- `replyDocument(doc, {...options})`
- `replySticker(sticker, {...options})`
- `replyAnimation(anim, {...options})`
- `replyLocation(lat, lon, {...options})`
- `replyContact(phone, fn, {...options})`
- `replyPoll(q, options, {...options})`
- `replyDice(emoji = "", {...options})`

### Info and utilities

- `get()` — message id and metadata
- `downloadFile()` — download URL for attached media, if any

### Live location and polls

- `editLiveLocation(lat, lon, {...options})`
- `stopLiveLocation({...options})`
- `stopPoll({...options})`

## Tiny example

```js
let sent = await Api.sendMessage({ text: "Temporary." })
await sent.editText("This will disappear.")
await sent.delete()
```

## See also

- [Editing Messages](editing-messages.md) — same edits via standalone Api calls  
- [Async Requests](async-requests.md) — why `await` matters here

!!! note
    Chaining only applies to message-sending Api responses. Other methods return plain response objects.
