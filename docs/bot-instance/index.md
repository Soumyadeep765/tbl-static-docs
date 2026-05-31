# Bot

`Bot` is TeleBotHost's shortcut for running your bot — not for wrestling with Telegram's API surface.

Where `Api` mirrors Telegram method-for-method, `Bot` wraps the things bot authors do every day: send a quick reply, jump to another command, store a setting, pull a list of users. Less boilerplate, fewer parameters you can get wrong.

It's there in every command, same as `Api`. Just call it.

## What people actually use it for

**Moving between commands.** A survey bot finishes step three and needs step four:

```js
Bot.runCommand("/step4")
```

Pass data along with the second argument — it shows up as [`options`](../globals/options.md) in the target command.

**Simple sends.** When you don't need inline keyboards or edit-in-place:

```js
Bot.sendMessage("Your code is 48291. It expires in 10 minutes.")
```

**Bot-wide storage.** Settings that apply to the whole bot, not one user — feature flags, API keys you've stored, cached totals. See [Storing Data](storing-data.md).

**User lists.** Who's used the bot, filtered by chat type or premium status. [Listing Users](listing-users.md).

## Case sensitivity

Methods are case-sensitive. `Bot.runCommand` yes, `Bot.runcommand` no.

## Bot and Api together

Common pattern: Api handles the Telegram UI (edit the menu message, answer the callback), Bot handles what happens next (run the command that processes the order).

The [Bot vs Api guide](../guides/bot-vs-api.md) has a full walkthrough.

## Pages in this section

| Page | Covers |
| --- | --- |
| [Running Commands](running-commands.md) | `runCommand`, passing options |
| [Reading Commands](reading-commands.md) | Inspect another command's code or config |
| [Sending Messages](sending-messages.md) | Text, keyboards, media via Bot |
| [Storing Data](storing-data.md) | Key-value storage at bot level |
| [Listing Users](listing-users.md) | Query users who've interacted |

If you're sending inline buttons or editing messages after send, you'll still need [Api](../api-instance/index.md) for that part.
