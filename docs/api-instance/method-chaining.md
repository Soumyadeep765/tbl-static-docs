## Chained Methods on Api.xxx Responses

Every response object returned from methods like  
`Api.sendMessage()`, `Api.sendPhoto()` etc.  
supports **chained methods**.

This means once a message is sent, you can **immediately act on that same message**.

You can edit it, reply to it, pin it, react to it, forward it, or delete it — all using the returned response object.

## Why Chained Methods Exist

Chained methods make message handling:

- Faster
- Cleaner
- More readable
- More powerful

Instead of searching for message IDs or writing extra logic, you directly operate on the message you just sent.

## Basic Example

Send a message and then perform actions on it:

```js
// Send a message and chain methods
let data = await Api.sendMessage({ text: "Hello user!" })

await data.pin()                        // Pin the message
await data.react("👍")                 // Add a reaction
await data.editText("Updated text")    // Edit message text
await data.reply("Replied Message")    // Reply to the message
```

Here:

- `data` represents the sent message
- All actions apply to that exact message
- No manual IDs are required

## How It Works

- `Api.sendMessage()` sends a message
- Telegram returns message data
- TBL wraps that response
- Chained methods become available on it

Each chained method internally calls the correct Telegram API method.

## Supported Chained Methods

### Editing and Updating

- `editText(text, {...options})`
- `editCaption(caption, {...options})`
- `editMedia(media, {...options})`
- `editReplyMarkup(rm, {...options})`

### Message Control

- `delete()`
- `pin(dn = false)`  
  `dn` → disable notification
- `unpin()`

### Reactions

- `react(emoji, big = false)`  
  `big` → large reaction

### Forwarding and Copying

- `forward(to, {...options})`
- `copy(to, {...options})`

### Reply Methods

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

### Message Info and Utilities

- `get()`  
  Returns message ID and metadata
- `downloadFile()`  
  Download url of attached media if available

### Live Location and Poll Control

- `editLiveLocation(lat, lon, {...options})`
- `stopLiveLocation({...options})`
- `stopPoll({...options})`

## Example: Edit Then Delete

```js
let msg = await Api.sendMessage({ text: "Temporary message" })

await msg.editText("This will be deleted soon")
await msg.delete()
```

## When to Use Chained Methods

Use chained methods when:

- You want to act on the message you just sent
- You need clean and readable logic
- You want to avoid handling message IDs manually
- You’re building interactive or dynamic bots


???+ Note
    Chained methods are available only on message responses. All Api calls return chainable responses (But will not work for all only work for message sending methods)
