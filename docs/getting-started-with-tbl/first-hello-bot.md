# Your First Bot

Let's get something working on Telegram in the next few minutes. No JavaScript logic, no databases, no complex structures—just a bot that says hello when someone sends `/start`.

Spoiler: If you can fill in two fields in a dashboard and click "Save", you can build a bot. That is literally all we are doing here!

---

## Step 1: Open the Command Editor

First, navigate to your bot project in the dashboard:

1. Open the [TeleBotHost Console](https://console.telebothost.com/).
2. Click on your bot from the dashboard list.
3. Open the **Commands** tab.
4. Click **Add Command**.

---

## Step 2: Fill in the Fields

You will see a form with several fields. For now, we only care about two:

1. **Command:** Type `/start` (This is the message users send when they first interact with your bot).
2. **Answer:** Type your greeting message, for example:
   ```text
   Hello there! 👋 Welcome to my first bot.
   ```

Click **Save Command** at the bottom of the form.

---

## Step 3: Turn It On!

Before testing, make sure your bot is online:

1. Look at the top right of your bot's management panel.
2. If it says **Offline**, click the **Launch Bot** button.
3. Wait a second until the status indicator turns green (**Online**).

---

## Step 4: Test Your Bot!

Let's see it in action:

1. Open Telegram on your phone or computer.
2. Search for your bot's username (the one you set up with `@BotFather`).
3. Open the chat and click the **Start** button at the bottom (or type `/start` manually and send it).
4. Boom! Your bot will reply instantly with your greeting.

🎉 **You are officially a bot creator!** 

---

## How does this work under the hood?

When someone sends `/start` to your bot:

1. Telegram sends the message data (called an **update**) to TeleBotHost.
2. TeleBotHost searches your command list, finds the `/start` command, and immediately sends the text in your **Answer** field back to the chat.
3. The flow ends. Simple and fast!

---

## What's Next?

Tapping buttons is way cooler than typing commands. In the next step, we'll add reply buttons below the chat input!

➔ **[Adding a Keyboard](adding-keyboard.md)**
