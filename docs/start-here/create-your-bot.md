# Create Your Bot

Every TeleBotHost bot starts as a normal Telegram bot. Create it in Telegram first, then connect it in the TeleBotHost console.

## Create it with BotFather

Open Telegram and search for `@BotFather`. Send `/newbot`, choose a display name, then choose a username that ends in `bot`.

BotFather will send you a token. Copy the full token and keep it private. Anyone with that token can control the bot.

## Connect it to TeleBotHost

Open the TeleBotHost console, choose **Add Bot**, paste the token, and save.

After the bot appears in your dashboard, open it and check the status. Launch it if it is offline. A saved command will not reply while the bot is stopped.

## If it does not work

If the token is rejected, copy it again from BotFather and check for extra spaces.

If the bot does not reply, confirm that it is launched in TeleBotHost.

If you cannot find the bot in Telegram, search for its exact username with the `@` prefix.

Next: [Write Your First Command](write-your-first-command.md).

