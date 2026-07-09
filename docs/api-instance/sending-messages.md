# Sending Messages

The most common thing a bot does is say hello. With **`Api.sendMessage`**, that's one line — no `chat_id` unless you're deliberately sending somewhere else. The platform fills in the chat from wherever the command was triggered.

`Bot.sendMessage` is great for quick replies. `Api.sendMessage` is the full Telegram toolkit — formatting, silent sends, different chats, rich messages, the works.

---

## What can you send?

Plain text, Markdown, HTML, rich structured content — all through `Api.sendMessage` or related methods. Pick your format with `parse_mode`:

```js
Api.sendMessage({ text: "Hello." })
```

Most calls assume the **current chat**. Override with `chat_id` when you need to notify an admin channel or message someone from a background command.

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md).

---

## How to use it

### Formatted text

Telegram supports Markdown and HTML. Keep formatting simple — unclosed bold markers are the usual reason a message fails:

```js
Api.sendMessage({
  text: "*Order confirmed.*\nTracking: `ABC-123`",
  parse_mode: "Markdown"
})
```

If a formatted message keeps erroring, strip the markup and add it back piece by piece. Telegram's parsers are picky.

### Sending to a different chat

```js
Api.sendMessage({
  chat_id: 123456789,
  text: "New signup from the website."
})
```

Only do this when the bot can actually post there — it's a group member, hasn't been blocked by the user, etc. Telegram rejects invalid targets, and by default that rejection lands in your error logs rather than crashing the command.

### Silent sends

No buzz on the user's phone:

```js
Api.sendMessage({
  text: "Background sync finished.",
  disable_notification: true
})
```

Handy for admin alerts in busy groups.

---

## Try it — copy-paste examples

### Simple reply

```js
Api.sendMessage({ text: "Got your message!" })
```

### Edit what you just sent

`await` the call when the next line needs to change the message:

```js
let sent = await Api.sendMessage({ text: "Working..." })
await sent.editText("Finished.")
```

See [Method Chaining](method-chaining.md) for everything you can do with that returned object.

### Hand off to another command

When the response matters but you don't want the rest of the logic here:

```js
Api.getChat({ chat_id: chat.id, on_run: "afterGetChat" })
```

The `afterGetChat` command receives Telegram's response in [`options`](../globals/options.md). [Callbacks](callbacks.md) covers that pattern.

### Rich messages (Bot API 10.1)

Structured content — tables, headings, nested lists, formulas, collapsible blocks:

```js
Api.sendRichMessage({
  rich_message: {
    markdown: "# Order Summary\n\n| Item | Qty |\n| --- | --- |\n| Widget | 2 |"
  }
})
```

Pass content via `markdown` or `html` inside `rich_message`. For streaming partial rich content (AI replies), use `Api.sendRichMessageDraft` with a `draft_id`. Plain-text streaming: `Api.sendMessageDraft`.

---

## Everything else Telegram supports

`Api.sendMessage` accepts any parameter the [Telegram Bot API documents](https://core.telegram.org/bots/api#sendmessage) — reply markup, link previews, protected content, message threading in groups, the lot.

| Need | Read |
| --- | --- |
| Buttons under the message | [Inline Keyboards](inline-keyboards.md) |
| Photos, PDFs, voice notes | [Media and Files](media-and-files.md) |
| Edit or delete after send | [Editing Messages](editing-messages.md) |

---

## Important notes

- Use `await` and check `res.ok` when delivery failure would change your logic
- Case-sensitive: `Api.sendMessage` works, `Api.sendmessage` does not
- Cross-check parameters against the [Telegram Bot API docs](https://core.telegram.org/bots/api#sendmessage) when in doubt
