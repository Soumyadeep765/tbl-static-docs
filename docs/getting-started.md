# Getting Started

So, you want to build a Telegram bot. But you probably *don't* want to rent a virtual server, figure out SSL certificates, or explain to your friends why a simple "hello world" bot needs a database and Docker setup. 

Good news: you don't have to. That is exactly why **TeleBotHost** exists.

This guide will take you from absolute zero to a live, working bot in under five minutes. No coding required for your very first command.

---

## 1. Create a Bot on Telegram

Before TeleBotHost can run your bot, we need to register it with Telegram. We do this using Telegram’s official bot manager: **@BotFather**. Yes, the name is a Godfather reference.

1. Open Telegram and search for [@BotFather](https://t.me/BotFather). (Make sure it has the blue verification checkmark!)
2. Click **Start** and send the command `/newbot`.
3. Give your bot a friendly **display name** (e.g., `My Cool Support Assistant`).
4. Choose a unique **username** that ends with the word `bot` (e.g., `super_helper_xyz_bot`).
5. BotFather will send you a message with an **API Token** (a long string of letters and numbers). 
6. **Copy that token** and keep it secret. Treat it like a password!

---

## 2. Connect Your Bot to TeleBotHost

Now, let's give your bot a brain:

1. Open the [TeleBotHost Console](https://console.telebothost.com/).
2. Log in or create a quick free account.
3. On your dashboard, click **Add Bot**.
4. Paste the **API Token** you copied from BotFather.
5. Click **Create**.

Your bot is now registered in your dashboard!

---

## 3. Add Your First Command

Let's teach your bot how to say hello:

1. Click on your new bot in the dashboard to open its panel.
2. Go to the **Commands** section and click **Add Command**.
3. In the **Command** field, type `/start` (this is the button users click when they first open your bot).
4. In the **Answer** field, type what you want the bot to reply with:
   ```text
   Hello! Welcome to my first Telegram bot. Send me /start to see this message again!
   ```
5. Click **Save Command**.

---

## 4. Turn the Bot On!

Your command is saved, but the bot is still sleeping:

1. Look at the top right of your bot's panel in the dashboard.
2. Click **Launch Bot** (or click the start button).
3. The status will change to show your bot is **Online**.

---

## 5. Test It!

Now for the best part:

1. Open Telegram.
2. Search for your bot's username (e.g., `@super_helper_xyz_bot`) and open the chat.
3. Click the **Start** button at the bottom (or send `/start`).
4. Watch your bot respond instantly with the text you set up!

Congratulations, you are officially a bot developer. Take a screenshot, show your friends, or just celebrate.

---

## What's Next?

Now that your bot is alive, let's make it smart:

*   **[Learning TBL](learning-tbl.md)** — Take your first steps into writing simple JavaScript logic to make your bot interactive.
*   **[Your First Bot Tutorial](getting-started-with-tbl/first-hello-bot.md)** — A hands-on walkthrough to build a `/hello` command with some custom logic.
*   **[Adding Keyboards](getting-started-with-tbl/adding-keyboard.md)** — Give your users nice buttons to click instead of typing commands.
