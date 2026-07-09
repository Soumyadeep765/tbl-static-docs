# Api

Your bot's direct line to Telegram — every `sendMessage`, `editMessageText`, and `answerCallbackQuery` the Bot API offers, without building HTTP requests yourself.

Type `Api.` and you're talking to Telegram. Chat IDs, tokens, and routing? Already handled.

---

## What is Api?

**Api** is how your bot talks to Telegram. Every method maps to something in the [Telegram Bot API](https://core.telegram.org/bots/api) — `sendMessage`, `editMessageText`, `answerCallbackQuery`, and hundreds of others.

| You get | You skip |
| --- | --- |
| Full Bot API coverage | Raw HTTP requests |
| Auto-filled `chat_id` | Hunting for IDs on every line |
| Method chaining on responses | Manual follow-up calls |

`Api` is already there inside every command. No import, no setup.

---

## How to use it

Drop this in any command's **Logic** field:

```js
Api.sendMessage({ text: "Hey." })
```

That sends to whoever triggered the command — the platform fills in the chat automatically.

Pass a single object with the parameters Telegram expects:

```js
Api.sendPhoto({
  photo: "https://example.com/photo.jpg",
  caption: "Here's the file you asked for.",
  parse_mode: "Markdown"
})
```

Most methods target the **current chat** — the conversation where the command fired. Pass `chat_id` only when you intentionally need a different destination, and only if your bot actually has access there.

!!! tip "New to TBL?"
    `user`, `chat`, and `message` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md). For bot-level flow and simple sends, see [`Bot`](../bot-instance/index.md).

!!! info "Bot API compatibility"
    `Api` is updated for **[Telegram Bot API 10.1](https://core.telegram.org/bots/api-changelog#june-11-2026)** (June 2026).  
    New methods such as `sendRichMessage`, `sendRichMessageDraft`, `answerChatJoinRequestQuery`, `sendChatJoinRequestWebApp`, `verifyUser`, `verifyChat`, and managed-bot token methods are available as built-in wrappers.  
    See [Bot API 10.1 support](#bot-api-101-support) below for highlights.

---

## Api or Bot?

Rough rule: if you're shaping what the user *sees in Telegram*, you're probably in Api territory. If you're deciding *what your bot does next*, look at [Bot](../bot-instance/index.md) first.

| `Bot` is for… | `Api` is for… |
| --- | --- |
| Running another command | Inline buttons and callbacks |
| Simple text replies | Message edits and reactions |
| Bot-wide storage via `db` | Stickers, polls, admin methods |
| Keeping flows tidy | Anything the Bot API exposes |

Once you've seen both, the [Bot vs Api guide](../guides/bot-vs-api.md) goes deeper with side-by-side examples.

Command context (`user`, `chat`, `message`, …) comes from [Global Variables](../globals/index.md) — available in every command alongside `Bot` and `Api`.

---

## Try it — copy-paste examples

Start simple. Each example only introduces what it needs.

### Send a message

```js
Api.sendMessage({ text: "Processing your request..." })
```

### Edit the message you just sent

Some calls return a response you can chain:

```js
let sent = await Api.sendMessage({ text: "Processing..." })
await sent.editText("Done.")
```

### Answer a callback button

When a user taps an inline button:

```js
Api.answerCallbackQuery({ text: "Got it!" })
```

### Call any Telegram method

If a method exists in Telegram's docs but not yet as `Api.methodName`, use the generic caller:

```js
Api.call("methodName", { /* params */ })
```

### Validate another bot's token

Store tokens in dashboard **ENV** settings, then read via `process.env`:

```js
let me = await Api.getMe({ bot_token: process.env.OTHER_BOT_TOKEN })

if (me.ok) {
  Bot.inspect(`Other bot: @${me.result.username}`)
}
```

ENV setup: [`process.env`](../globals/process.md) · Full list: [Bot Admin Methods](bot-admin-methods.md)

---

## Optional `bot_token` parameter

A set of **bot-admin methods** accept an optional `bot_token` field. When omitted, the call uses the **current bot's token**. When provided, the call runs against that token instead — useful for multi-bot setups, token validation, or managing another bot you own.

!!! warning "Keep tokens secret"
    Never hard-code bot tokens in commands. Store them in dashboard [environment variables](../globals/process.md) and pass via `process.env`.  
    The `bot_token` field is removed before the request reaches Telegram — your token never leaves the platform in the outbound call.

See [Bot Admin Methods](bot-admin-methods.md) for the full list of methods that support `bot_token`.

---

## Callbacks with `on_run`

Some calls support **`on_run`**, which hands off to another command when Telegram responds. Handy when you want to keep the current command short.

---

## Bot API 10.1 support

The platform tracks Telegram's latest API. Highlights from **Bot API 10.1**:

| Feature | Methods |
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

Parameter shapes match the [official Bot API reference](https://core.telegram.org/bots/api). They're passed through to Telegram as-is.

---

## Error behavior worth knowing

Call a method that doesn't exist — `Api.hitMe()` — and the platform throws. Your `!` error handler catches it.

Send a message to a blocked user or pass a bad parameter, and Telegram returns an error. That usually **doesn't** crash the command; it shows up in your bot's error logs. Use `await` and check `res.ok` when failure would change what you do next. See [Tips and Limitations](tips-and-limitations.md).

---

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
