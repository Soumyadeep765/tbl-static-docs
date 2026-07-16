# Start Here

Start with a working bot, not a reference manual.

This section explains the few concepts you need before writing commands: what Telegram owns, what TeleBotHost owns, and where your TBL code runs.

## What you are building

You are building a Telegram bot hosted by TeleBotHost. Telegram provides the chat. TeleBotHost receives updates from Telegram, chooses the command to run, and executes your JavaScript.

You write small command blocks instead of a server app.

## Terms that matter

A Telegram bot is the account users message in Telegram.

A bot token is the private token from `@BotFather`. TeleBotHost uses it to connect to that bot.

A TeleBotHost bot is the project in your dashboard.

A TBL command is one unit of behavior. It has a trigger, an optional answer, optional buttons, and optional JavaScript logic.

## The build path

Create the bot in Telegram, add the token to TeleBotHost, create `/start`, test it, then add logic. Keep each step small. When something breaks, you will know which step caused it.

Next: [Create Your Bot](create-your-bot.md).

