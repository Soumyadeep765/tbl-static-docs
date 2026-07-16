# Write Your First Command

Start with one command: `/start`. Do not add storage, APIs, callbacks, or custom logic yet. First prove that Telegram, TeleBotHost, and command matching are connected.

## Create `/start`

Open your bot in the TeleBotHost dashboard, go to **Commands**, and choose **Add Command**.

Set **Command** to `/start`.

Set **Answer** to something simple:

```text
Hello. Your bot is running on TeleBotHost.
```

Save the command, open your bot in Telegram, and send `/start`.

## Add logic after the static answer works

The **Answer** field sends fixed text. The **Logic** field runs JavaScript.

Try this in the Logic field:

```js
Bot.sendMessage("This message came from the Logic field.");
```

When you send `/start`, the bot can send the static answer and then run your JavaScript.

Use **Answer** for fixed replies. Use **Logic** when the reply depends on the user, stored data, an external API, buttons, or message editing.

Next: [How TBL Runs Commands](how-tbl-runs.md).

