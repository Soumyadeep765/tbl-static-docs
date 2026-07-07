# Learning TBL

TBL looks like JavaScript because it mostly is — same syntax for variables, `if`, loops, objects. What's different is what's *already there*: `Bot`, `Api`, `user`, `chat`, no `npm install`, no Express server.

You write logic inside commands. Telegram sends an update, TBL picks a command, your code runs, execution ends. That's the whole lifecycle.

## The command lifecycle

```
Update  →  match command  →  send Answer  →  run Logic  →  done
```

Special wrappers `@` (before) and `@@` (after) run automatically. Details: [Execution Flow](getting-started-with-tbl/execution-flow.md).

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
Bot.sendMessage("Hello from TBL.")
```

Drop that in a command's **Logic** field, trigger the command on Telegram, you get a reply. For simple replies you often only need the **Answer** field — no Logic required.

## Beyond basic replies

| Feature | Start here |
| --- | --- |
| Formatted answers | [Markdown & Formatting](getting-started-with-tbl/markdown-and-formatting.md) |
| Reply keyboard menus | [Adding a Keyboard](getting-started-with-tbl/adding-keyboard.md) |
| Inline button taps | [Handling Callbacks](getting-started-with-tbl/handling-callbacks.md) |
| Wait for user text | [Handling User Input](getting-started-with-tbl/handle-need-reply.md) |
| Static web page | [Public Web Commands](getting-started-with-tbl/public-web-commands.md) |
| HTTP API from command | [Webapps](webapp-instance/index.md) |

## Where to go

- [Command Flow](getting-started-with-tbl/index.md) — structured multi-page guide  
- [Tutorials](tutorials/index.md) — hands-on lessons in order  
- [Command Fields](getting-started-with-tbl/command-fields.md) — Answer, Logic, keyboard, `is_web`  
- [Global Variables](globals/index.md) — `user`, `chat`, `update`  
- [Bot](bot-instance/index.md) and [Api](api-instance/index.md) — main instances  
- [Bot vs Api](guides/bot-vs-api.md) — when to use which
