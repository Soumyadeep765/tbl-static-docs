# Learning TBL

TBL looks like JavaScript because it mostly is — same syntax for variables, `if`, loops, objects. What's different is what's *already there*: `Bot`, `Api`, `user`, `chat`, no `npm install`, no Express server.

You write logic inside commands. Telegram sends an update, TBL picks a command, your code runs, execution ends. That's the whole lifecycle.

## Sync by default

Lines run in order. Most Bot and Api calls work that way out of the box.

When you need a response before continuing — grab a message id, check whether send succeeded — add `await`:

```js
let sent = await Api.sendMessage({ text: "One moment..." })
await sent.editText("Ready.")
```

Don't sprinkle `await` on calls where you ignore the result.

## Your first line of code

```js
Bot.sendMessage("Hello from TBL.");
```

Drop that in a command's logic field, trigger the command on Telegram, you get a reply. Everything else builds from there.

## Where to go

- [Tutorials](tutorials/index.md) if you learn by doing  
- [Command Structure](getting-started-with-tbl/command-structure.md) for triggers and special commands  
- [Global Variables](globals/index.md) for `user`, `chat`, `update`, and the rest of the built-in context  
- [Bot](bot-instance/index.md) and [Api](api-instance/index.md) when you start calling instances in commands  
- [Bot vs Api](guides/bot-vs-api.md) after both overviews — clears up the overlap between the two
