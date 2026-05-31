# Bot vs Api

You'll see both `Bot` and `Api` in almost every TBL project. They overlap just enough to be confusing — both can send a message — but they're built for different jobs.

## The short version

**Bot** runs your bot. **Api** talks to Telegram.

When a user taps a button and you want to jump them into a checkout flow, that's `Bot.runCommand()`. When you need to edit the message they tapped, swap the inline keyboard, or answer a callback within Telegram's UI rules, that's `Api`.

## A concrete example

Imagine a `/menu` command that shows three options as inline buttons.

You could send the menu with either:

```js
Bot.sendMessage("Pick one:", { reply_markup: "..." })
```

or

```js
Api.sendMessage({
  text: "Pick one:",
  reply_markup: { inline_keyboard: [[{ text: "Help", callback_data: "help" }]] }
})
```

Both work for the initial send. The difference shows up next.

When the user taps **Help**, you get a callback update. To acknowledge it properly you call `Api.answerCallbackQuery()`. To replace the menu text in place, `Api.editMessageText()`. Bot doesn't wrap those — they're Telegram API territory.

If the tap should start a whole new conversation branch, you might do:

```js
Api.answerCallbackQuery({ callback_query_id: update.callback_query.id })
Bot.runCommand("/help")
```

Bot for navigation. Api for the Telegram interaction around it.

## When Bot is the right call

Reach for **Bot** when you're orchestrating:

- Running another command (`Bot.runCommand`)
- Sending straightforward messages without touching Telegram's deeper options
- Reading or writing [bot-level storage](../bot-instance/storing-data.md)
- Listing users who've talked to your bot

Bot methods are shorter because TeleBotHost already knows the context. Less typing, fewer ways to pass a wrong `chat_id`.

## When Api is the right call

Reach for **Api** when Telegram's API is the product:

- Inline keyboards and callback queries
- Editing or deleting messages after they're sent
- Reactions, pins, polls, stickers
- Anything from the [official method list](https://core.telegram.org/bots/api) that Bot doesn't wrap yet

Api gives you the full parameter set. That power comes with responsibility — you're closer to raw Telegram behavior, including its error codes.

## Case sensitivity

Both objects are case-sensitive. `Bot.runCommand` works. `Bot.runcommand` does not.

The [msg instance](../msg-instance/index.md) has its own naming rules — check that page if you're mixing `msg` methods with Bot and Api in the same command.

## Still not sure?

Ask yourself: *Am I changing what Telegram displays, or what my bot does internally?*

Display → Api. Internal flow → Bot.

Many real commands use both in the same file. That's normal.
