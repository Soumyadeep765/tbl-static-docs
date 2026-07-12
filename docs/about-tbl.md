# What is TBL?

Let's clear one thing up first: **TBL (Tele Bot Language) is not a brand new, scary programming language** you have to learn from scratch. It is just standard **JavaScript** dressed up in a superhero costume, pre-loaded with built-in tools specifically made for Telegram bots.

If you know basic JavaScript (variables, `if` statements, functions), you already know TBL. If you don't know JavaScript yet, don't sweat it—we'll walk you through the basics step-by-step.

---

## The Old Way vs. The TBL Way

Usually, building a Telegram bot looks like this:

1. Rent a server (VPS).
2. Install Node.js, configure Nginx, and deal with SSL certificates.
3. Write tons of boilerplate code to connect to the Telegram API.
4. Pray that the server doesn't crash at 3 AM.

**With TeleBotHost and TBL, you skip all the boring infrastructure stuff.** 

```
User texts your bot ➔ TeleBotHost wakes up ➔ Runs your code ➔ Sends reply ➔ Goes back to sleep
```

No background processes, no memory leaks, no DevOps guilt. Just a simple request-response loop.

---

## How it works (Step-by-Step)

Here is exactly what happens when someone interacts with your bot:

1. **The Trigger:** A user sends a message to your bot on Telegram (for example, `/start`).
2. **The Match:** TeleBotHost checks your dashboard, finds the command matching `/start`, and grabs your code.
3. **The Execution:** The platform runs your JavaScript logic instantly in a secure, isolated sandbox.
4. **The Response:** Your code sends a message back to the user (like "Hello there!").
5. **The Clean Up:** The command finishes executing and stops. Nothing stays running in the background waiting for the next message.

---

## What's in your toolbox?

When you write code on TeleBotHost, you don't need to run `npm install` or import libraries. Everything you need is already global and ready to use:

*   **`Bot`**: Your go-to helper. Want to send a simple message? Just use `Bot.sendMessage(chat.id, "Hi!")`.
*   **`Api`**: The raw Telegram Bot API power. Use this when you want to send inline keyboards, edit existing messages, or upload files.
*   **`user` & `chat`**: Objects that tell you exactly *who* sent the message and *where* they sent it from.
*   **`db`**: A built-in database that works out of the box. No setup required. You can save user high scores, settings, or bot states instantly.
*   **`modules` & `Libs`**: Pre-loaded toolboxes containing useful packages (like Lodash, BCrypt, dayjs, and referral system helpers).

---

## Why are there limits?

Since TBL runs in a shared serverless environment, you can't run infinite background loops or install arbitrary npm packages. 

This might feel limiting if you want to build a general-purpose web server—but for Telegram bots, it's a superpower. It keeps your bot super stable, lightning-fast, and protects it from bugs that would otherwise freeze a raw Node.js server.

---

## What to explore next

Ready to start building? Here are the best steps to follow:

1. **[Getting Started](getting-started.md)** — Create your bot with `@BotFather` and link it to TeleBotHost.
2. **[Learning TBL](learning-tbl.md)** — Learn how to write your first lines of logic.
3. **[Your First Bot](getting-started-with-tbl/first-hello-bot.md)** — Build a step-by-step `/start` responder in 5 minutes.
4. **[Command Flow](getting-started-with-tbl/index.md)** — Learn how matching and execution work under the hood.
