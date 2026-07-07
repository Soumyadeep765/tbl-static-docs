# Getting Started

This guide walks you through creating and running your first Telegram bot on **TeleBotHost**.

## 1. Open TeleBotHost

Go to the [TeleBotHost console](https://console.telebothost.com/).

## 2. Log In or Sign Up

- Log in to your existing account, or
- Create a new account if you are new

After logging in, you will see the dashboard.

## 3. Create a Telegram Bot

1. Open Telegram
2. Search for [@BotFather](https://t.me/BotFather)
3. Send `/newbot`
4. Set a bot name and username
5. Copy the bot token provided

## 4. Add the Bot on TeleBotHost

1. Open the TeleBotHost dashboard
2. Click **Add Bot**
3. Paste your bot token
4. Click **Create**

Your bot will appear in the bot list.

## 5. Open the Bot Panel

Click your bot in the dashboard to open its management panel.

From here you can:

- Add and edit commands
- Write TBL code in the Logic field
- Set Answer, Keyboard, aliases, **public web**, and parse mode
- Start or stop the bot

## 6. Start the Bot

Click **Launch Bot** to start your bot.

Your bot is now online and ready to respond on Telegram.

## 7. Add Your First Command

1. Open the **Commands** section
2. Add a command such as `/start`
3. Fill in the **Answer** field (e.g. `Hello! Welcome to my bot.`)
4. Save the command

Test it by sending `/start` to your bot on Telegram.

!!! tip "Formatting"
    The Answer field supports [Markdown](getting-started-with-tbl/markdown-and-formatting.md) by default — try `*bold*` and `_italic_`.

## What's Next

| Step | Page |
| --- | --- |
| Understand command flow | [Command Flow overview](getting-started-with-tbl/index.md) |
| Hands-on tutorial | [Your First Bot](getting-started-with-tbl/first-hello-bot.md) |
| Add buttons | [Adding a Keyboard](getting-started-with-tbl/adding-keyboard.md) |
| Inline button taps | [Handling Callbacks](getting-started-with-tbl/handling-callbacks.md) |
| Static web page | [Public Web Commands](getting-started-with-tbl/public-web-commands.md) |
| How TBL works | [What is TBL?](about-tbl.md) |
| Screenshots walkthrough | [Official tutorial](https://telebothost.com/tutorials/adding-first-bot) |
