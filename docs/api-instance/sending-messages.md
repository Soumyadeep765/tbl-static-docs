# Sending Messages

The most common thing a bot does is send text. In TBL that's one call:

```js
Api.sendMessage({ text: "Hello." })
```

No `chat_id` unless you're deliberately sending somewhere else. TBL uses the chat where the command was triggered.

## Formatting

Telegram supports Markdown and HTML in messages. Pick one with `parse_mode`:

```js
Api.sendMessage({
  text: "*Order confirmed.*\nTracking: `ABC-123`",
  parse_mode: "Markdown"
})
```

Keep formatting simple. Unclosed bold markers or nested styles are the usual reason a message fails to send. If a formatted message keeps erroring, strip the markup and add it back piece by piece.

## Sending to a different chat

Sometimes you need to notify an admin channel or message a user from a background command:

```js
Api.sendMessage({
  chat_id: 123456789,
  text: "New signup from the website."
})
```

Only do this when you're sure the bot can post in that chat — it's a member of the group, hasn't been blocked by the user, etc. Telegram will reject the call otherwise, and by default that rejection lands in your error logs rather than crashing the command.

## Silent sends

Pass `disable_notification: true` if the message shouldn't buzz the user's phone:

```js
Api.sendMessage({
  text: "Background sync finished.",
  disable_notification: true
})
```

Useful for admin alerts in busy groups.

## Getting a handle on the message

If your next line needs to edit or delete what you just sent, `await` the call:

```js
let msg = await Api.sendMessage({ text: "Working..." })
// later
await msg.editText("Finished.")
```

See [Method Chaining](method-chaining.md) for everything you can do with that returned object.

## Handing off to another command

When the response matters but you don't want the rest of the logic in this command:

```js
Api.getChat({ chat_id: chat.id, on_run: "afterGetChat" })
```

The `afterGetChat` command receives Telegram's response in [`options`](../globals/options.md). [Callbacks](callbacks.md) covers that pattern properly.

## Everything else Telegram supports

`Api.sendMessage` accepts any parameter the [Telegram Bot API documents](https://core.telegram.org/bots/api#sendmessage) — reply markup, link previews, protected content, message threading in groups, the lot.

If you need buttons under the message, read [Inline Keyboards](inline-keyboards.md). For files and media, [Media and Files](media-and-files.md).
