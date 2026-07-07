# Api

`Api` is how your bot talks to Telegram.

Every method maps to something in the [Telegram Bot API](https://core.telegram.org/bots/api) — `sendMessage`, `editMessageText`, `answerCallbackQuery`, and hundreds of others. TBL wraps those calls so you don't build HTTP requests or hunt for chat IDs on every line.

`Api` is already there inside every command. No import, no setup.

```js
Api.sendMessage({ text: "Hey." })
```

That sends to whoever triggered the command. TBL fills in the chat automatically.

!!! info "Bot API compatibility"
    TBL's `Api` instance is updated for **[Telegram Bot API 10.1](https://core.telegram.org/bots/api-changelog#june-11-2026)** (June 2026).  
    New methods such as `sendRichMessage`, `sendRichMessageDraft`, `answerChatJoinRequestQuery`, `sendChatJoinRequestWebApp`, `verifyUser`, `verifyChat`, and managed-bot token methods are available as built-in wrappers.  
    See [Bot API 10.1 support](#bot-api-101-support) below for highlights.

## When you'd use Api over Bot

`Bot` is for moving around inside your bot — running another command, storing bot-level data, keeping flows tidy. `Api` is for when you need Telegram itself: inline buttons, message edits, callback answers, stickers, polls, anything the Bot API exposes.

Rough rule: if you're shaping what the user *sees in Telegram*, you're probably in Api territory. If you're deciding *what your bot does next*, look at [Bot](../bot-instance/index.md) first. Once you've seen both, the [Bot vs Api guide](../guides/bot-vs-api.md) goes deeper with side-by-side examples.

Command context (`user`, `chat`, `message`, …) comes from [Global Variables](../globals/index.md) — available in every command alongside `Bot` and `Api`.

## How calls work

Pass a single object with the parameters Telegram expects:

```js
Api.sendPhoto({
  photo: "https://example.com/photo.jpg",
  caption: "Here's the file you asked for.",
  parse_mode: "Markdown"
})
```

Most methods target the **current chat** — the conversation where the command fired. Pass `chat_id` only when you intentionally need a different destination, and only if your bot actually has access there.

Some calls return a response you can use right away:

```js
let sent = await Api.sendMessage({ text: "Processing..." })
await sent.editText("Done.")
```

Others support **`on_run`**, which hands off to another command when Telegram responds. Handy when you want to keep the current command short.

If a method exists in Telegram's docs but not yet as `Api.methodName`, use **`Api.call("methodName", { ... })`**. That keeps you from waiting on platform updates.

## Optional `bot_token` parameter

A set of **bot-admin methods** accept an optional `bot_token` field. When omitted, the call uses the **current bot's token**. When provided, the call runs against that token instead — useful for multi-bot setups, token validation, or managing another bot you own.

```js
// Validate a token stored in dashboard ENV
let me = await Api.getMe({ bot_token: process.env.OTHER_BOT_TOKEN })

if (me.ok) {
  Bot.inspect(`Other bot: @${me.result.username}`)
}
```

!!! warning "Keep tokens secret"
    Never hard-code bot tokens in commands. Store them in dashboard [environment variables](../globals/process.md) and pass via `process.env`.  
    The `bot_token` field is stripped before the request reaches Telegram — it is handled internally by TBL.

See [Bot Admin Methods](bot-admin-methods.md) for the full list of methods that support `bot_token`.

## Bot API 10.1 support

TBL tracks Telegram's latest API. Highlights from **Bot API 10.1**:

| Feature | TBL methods |
| --- | --- |
| Rich Messages (tables, headings, lists, formulas) | `Api.sendRichMessage`, `Api.sendRichMessageDraft` |
| Rich message editing | `Api.editMessageText` with `rich_message` parameter |
| Streaming drafts | `Api.sendMessageDraft`, `Api.sendRichMessageDraft` |
| Join request queries | `Api.answerChatJoinRequestQuery`, `Api.sendChatJoinRequestWebApp` |
| User verification badges | `Api.verifyUser`, `Api.verifyChat`, `Api.removeUserVerification`, `Api.removeChatVerification` |
| Managed bot tokens | `Api.getManagedBotToken`, `Api.replaceManagedBotToken`, `Api.getManagedBotAccessSettings`, `Api.setManagedBotAccessSettings` |
| Profile photos | `Api.setMyProfilePhoto`, `Api.removeMyProfilePhoto` |
| Suggested posts | `Api.approveSuggestedPost`, `Api.declineSuggestedPost` |
| Checklists (business) | `Api.sendChecklist`, `Api.editMessageChecklist` |
| User profile audios | `Api.getUserProfileAudios` |
| Emoji status | `Api.setUserEmojiStatus` |

Parameter shapes match the [official Bot API reference](https://core.telegram.org/bots/api). TBL passes them through to Telegram.

## Error behavior worth knowing

Call a method that doesn't exist — `Api.hitMe()` — and TBL throws. Your `!` error handler catches it.

Send a message to a blocked user or pass a bad parameter, and Telegram returns an error. That usually **doesn't** crash the command; it shows up in your bot's error logs. Use `await` and check `res.ok` when failure would change what you do next. See [Tips and Limitations](tips-and-limitations.md).

## What's in this section

| Page | What it covers |
| --- | --- |
| [Sending Messages](sending-messages.md) | Text, formatting, rich messages, drafts |
| [Inline Keyboards](inline-keyboards.md) | Buttons under messages, callback data |
| [Media and Files](media-and-files.md) | Photos, documents, audio, video |
| [Editing Messages](editing-messages.md) | Change text, captions, keyboards after send |
| [Async Requests](async-requests.md) | `await` and working with responses inline |
| [Callbacks](callbacks.md) | `on_run` and continuing in another command |
| [Method Chaining](method-chaining.md) | Edit, pin, delete the message you just sent |
| [Bot Admin Methods](bot-admin-methods.md) | Methods with optional `bot_token` |
| [Dynamic Methods](dynamic-methods.md) | `Api.call()` for anything Telegram adds |
| [Tips and Limitations](tips-and-limitations.md) | Errors, gotchas, things people miss |

Start with [Sending Messages](sending-messages.md) if you've never called Api before.
