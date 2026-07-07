# Your First Bot

Let's get something working on Telegram in the next few minutes.

The bot will respond to `/start` with a hello message. No logic field required — just a command name and an answer.

## Open the command editor

Dashboard → your bot → **Commands** → **Add Command**.

Everything your bot does lives here.

## Fill in two fields

**Command:** `/start`

**Answer:**

```
Hello 👋
Welcome to my first TBL bot!
```

Save it. That's the whole bot for now.

## What happens when someone types /start

Telegram delivers the update. TBL matches `/start`, sends the answer, done. The answer goes out *before* any logic runs — so for simple replies you often don't need a logic field at all.

## Formatting the answer

The answer field accepts [Telegram Markdown](markdown-and-formatting.md) by default. Bold, italic, line breaks — useful for welcome text.

```
*Welcome!*
Choose an option below.
```

Start plain. Add formatting once the message sends reliably.

## Test it

Open your bot in Telegram, send `/start`. You should see the hello message right away.

If nothing comes back, check the bot is launched in the dashboard and you're messaging the correct bot username.

## What's next

[Adding a Keyboard](adding-keyboard.md) — give users buttons so they don't have to type commands.

Or read [Command Flow](index.md) for the full structured guide.
