# How TBL Runs Commands

TBL runs for one update at a time.

A user sends a message. TeleBotHost receives the update from Telegram. TBL finds the best matching command. The command sends its Answer if it has one, runs its Logic if it has any, then stops.

That is the whole model.

```text
message in -> command match -> answer -> logic -> finish
```

## What a command can contain

The **Command** field is the trigger, such as `/start`, `Help`, or `*`.

The **Answer** field is fixed text sent before logic runs.

The **Keyboard** field adds reply buttons.

The **Logic** field is JavaScript for dynamic work.

The **Aliases** field lets more than one trigger run the same command.

## Built-in data

TBL gives your logic useful values before it runs:

```js
Bot.sendMessage("Hi " + user.first_name);
Bot.sendMessage("Chat ID: " + chat.id);
```

Use `await` only when the next line needs the result of the current one:

```js
let sent = await Api.sendMessage({ text: "Checking..." });
await sent.editText("Done.");
```

Build one small command, test it, then add the next behavior.

Next: [Where To Go Next](where-to-go-next.md).

