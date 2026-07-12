# Handling User Input with Need Reply

Fire-and-forget commands are great, but eventually you will want to ask your user for information—like a username, email, phone number, or age. 

With the **Need Reply** setting, you can pause your command, wait for the user to type their response, and then run JavaScript logic on the input they sent.

---

## How Need Reply Works

Instead of running your code immediately, a Need Reply command works like a two-step conversation:

1. **Step 1:** User triggers the command. The bot sends the **Answer** text (e.g., "What is your name?") and **pauses**.
2. **Step 2:** The user types their answer (e.g., "Alice") and sends it.
3. **Step 3:** The command wakes up and runs your JavaScript **Logic** field. The text they typed is automatically saved in the global variable `message`.

---

## Step 1: Create the Command

Let's build a name-prompting command:
1. Open your dashboard and click **Add Command**.
2. **Command:** Type `/askname`.
3. **Answer:** Type the question:
   ```text
   Please type your name below! (Or send /start to cancel)
   ```
4. **Need Reply:** Toggle this setting **ON** (enabled).
5. **Logic:** Paste this standard JavaScript code:
   ```js
   Bot.sendMessage(chat.id, "Nice to meet you, " + message + "!");
   ```
6. Click **Save Command**.

---

## Step 2: Test It!

1. Open Telegram and send `/askname` to your bot.
2. The bot will send "Please type your name below!" and wait.
3. Type your name (e.g. `Sam`) and hit send.
4. The bot will run your logic and reply: "Nice to meet you, Sam!"

---

## The Escape Hatch: Canceling Input Mode

What if a user changes their mind and doesn't want to enter their name? They shouldn't get stuck forever.

If a user is in a "Need Reply" waiting state and they send **any valid existing command** (like `/start` or `Help`), TBL will automatically cancel the input mode and run that command instead.

!!! safety "Beginner Tip"
    Always tell your users how to cancel in your Answer field! Add a quick line like: *(send /start to cancel)*. It prevents users from feeling stuck or thinking your bot is broken.

---

## What's Next?

Now that you can capture user text, let's look at **Inline Keyboards**—buttons that sit directly inside message bubbles and execute actions behind the scenes without sending chat spam!

➔ **[Handling Callbacks](handling-callbacks.md)**
