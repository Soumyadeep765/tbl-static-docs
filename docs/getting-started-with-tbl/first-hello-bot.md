# Your First TBL Bot — Hello Bot

Let’s build your very first Telegram bot using TBL.

This bot will do one simple thing:  
when a user sends `/start`, the bot replies with a friendly **Hello message**.

No code logic yet — just a command and an answer.

## What We Are Building

We will create:

- One command
- One automatic reply
- A working Telegram bot response

This is the easiest way to understand how TBL works.

## Step 1 — Open Your Bot Panel

- Go to your bot dashboard on TeleBotHost
- Open the **Commands** section for the bot you added earlier
- Click **Add Command**

This is where all bot behavior starts.

## Step 2 — Create the Command

Fill the command fields like this:

In command field:  
`/start`

Answer:  
`Hello 👋  
Welcome to my first TBL bot!`

That’s it.

No logic is required for this step.

## How This Works

When a user sends `/start`:

- Telegram sends the update
- TBL matches the `/start` command
- The answer is sent instantly
- Execution ends

This happens automatically.

!!! info
    The answer is sent before any code logic. If no logic exists, the answer alone is enough.

## Answer Supports Markdown

The **Answer field supports Telegram Markdown**, which means you can format text to make messages more readable and attractive.

You can use Markdown to:

- Make text **bold** or _italic_
- Show `monospace` text
- Create line breaks
- Add simple emphasis

This is useful for welcome messages, help text, and menus.

!!! tip
    Keep formatting simple to avoid Markdown parsing issues.

### Learn Telegram Markdown

To understand what formatting is supported, see the official Telegram documentation:

https://core.telegram.org/bots/api#formatting-options

## Test Your Bot

- Open your bot in Telegram
- Send `/start`
- You should see your Hello message instantly

If you see the message, your bot is working 🎉

## What You Learned

With this simple bot, you learned that:

- Bots in TBL are command-based
- A command can work without any code
- The Answer field supports Telegram Markdown
- Formatting can improve message clarity
- `/start` is the entry point for most bots

