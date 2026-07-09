# Getting Started

You want a Telegram bot. You don't want to rent a VPS, configure nginx, or explain to your friends why your "hello world" needs Docker. Good news — that's exactly what **TeleBotHost** is for.

This guide gets you from zero to a live bot in a few minutes. No prior coding required for the first command (though we'll nudge you toward Logic soon enough).

---

## What you're building

A bot on Telegram that responds when users send commands — hosted and run by TeleBotHost. You write behavior in the dashboard; the platform handles the rest.

Ready? Let's go.

---

## 1. Open TeleBotHost

Head to the [TeleBotHost console](https://console.telebothost.com/).

That's home base — where you add bots, write commands, and hit **Launch Bot**.

---

## 2. Log in or sign up

- Log in to your existing account, or
- Create a new account if you're new

After logging in, you'll see the dashboard. This is where the magic (and the Logic fields) live.

---

## 3. Create a Telegram bot

Telegram bots are registered with [@BotFather](https://t.me/BotFather) — Telegram's official bot manager. Yes, the name is on the nose.

1. Open Telegram
2. Search for [@BotFather](https://t.me/BotFather)
3. Send `/newbot`
4. Pick a display name and a username (must end in `bot`, e.g. `MyCoolHelperBot`)
5. Copy the **bot token** BotFather gives you — you'll paste this into TeleBotHost

Keep that token secret. Anyone with it can control your bot. Treat it like a password, not a tweet.

---

## 4. Add the bot on TeleBotHost

1. Open the TeleBotHost dashboard
2. Click **Add Bot**
3. Paste your bot token
4. Click **Create**

Your bot appears in the bot list. It exists — it just isn't running yet.

---

## 5. Open the bot panel

Click your bot in the dashboard to open its management panel.

From here you can:

- Add and edit **commands**
- Write TBL code in the **Logic** field
- Set **Answer**, **Keyboard**, aliases, **public web**, and parse mode
- Start or stop the bot

Think of each command as a mini program that runs when a user triggers it.

---

## 6. Start the bot

Click **Launch Bot**.

Your bot is now online and ready to respond on Telegram. Go say hi — it won't judge you for talking to a bot at 2 AM.

---

## 7. Add your first command

1. Open the **Commands** section
2. Add a command such as `/start`
3. Fill in the **Answer** field (e.g. `Hello! Welcome to my bot.`)
4. Save the command

Test it: open Telegram, find your bot, send `/start`. If you get your welcome message, you're officially a bot developer. Frame the screenshot.

!!! tip "Formatting"
    The Answer field supports [Markdown](getting-started-with-tbl/markdown-and-formatting.md) by default — try `*bold*` and `_italic_`.

---

## What's next?

You've got a live bot. Now make it interesting:

| Step | Page |
| --- | --- |
| Understand command flow | [Command Flow overview](getting-started-with-tbl/index.md) |
| Hands-on tutorial | [Your First Bot](getting-started-with-tbl/first-hello-bot.md) |
| Add buttons | [Adding a Keyboard](getting-started-with-tbl/adding-keyboard.md) |
| Inline button taps | [Handling Callbacks](getting-started-with-tbl/handling-callbacks.md) |
| Static web page | [Public Web Commands](getting-started-with-tbl/public-web-commands.md) |
| How TBL works | [What is TBL?](about-tbl.md) |
| Write your first Logic | [Learning TBL](learning-tbl.md) |
| Screenshots walkthrough | [Official tutorial](https://telebothost.com/tutorials/adding-first-bot) |
