# Learning TBL

TBL looks like JavaScript because it mostly is — same syntax for variables, `if`, loops, objects. What's different is what's *already there*: `Bot`, `Api`, `user`, `chat`, no `npm install`, no Express server to bootstrap.

You write logic inside commands. Telegram sends an update, TBL picks a command, your code runs, execution ends. That's the whole lifecycle. No event loop babysitting required.

---

## The command lifecycle

Every interaction follows the same path:

```
Update  →  match command  →  send Answer  →  run Logic  →  done
```

Special wrappers `@` (before) and `@@` (after) run automatically around other commands. Details: [Execution Flow](getting-started-with-tbl/execution-flow.md).

Think of it like a vending machine: user picks a snack (sends a command), machine dispenses (Answer + Logic), transaction complete. No machine sitting there idle between customers.

---

## Sync by default

Lines run in order. Most `Bot` and `Api` calls work that way out of the box — call it, move on.

When you need a response before continuing — grab a message id, check whether send succeeded, verify channel membership — add `await`:

```js
let sent = await Api.sendMessage({ text: "One moment..." })
await sent.editText("Ready.")
```

Don't sprinkle `await` on calls where you ignore the result. Async isn't a seasoning — use it when you're actually waiting for something.

Common async cases:

| What | Example |
| --- | --- |
| Edit a message you just sent | `await Api.sendMessage(...)` |
| Check channel membership | `await Libs.mcl.quick(user.id, ["@Channel"])` |
| Parse CSV / hash password | `await modules.ParseCSV.parse(...)` |

---

## Your first line of code

Drop this in a command's **Logic** field:

```js
Bot.sendMessage(chat.id, "Hello from TBL!")
```

Trigger the command on Telegram — you get a reply. For simple text responses, you often only need the **Answer** field — no Logic required. Logic is where things get interesting.

!!! tip "Globals"
    `chat.id` is where the message goes. `user` is who sent the command. Full list: [Global Variables](globals/index.md).

---

## What's already there

You never write `import` or `require`. These globals are ready on day one:

| Global | What it is |
| --- | --- |
| `Bot` | High-level bot helpers — send messages, run commands, storage |
| `Api` | Raw Telegram API — keyboards, edits, file uploads |
| `user` | Who triggered this command |
| `chat` | Where the message came from |
| `params` | Text after the command (e.g. `/start promo` → `"promo"`) |
| `modules` | npm-style utilities — JWT, bcrypt, CSV, etc. |
| `Libs` | Bot helpers — referrals, random, channel checks |

When to use `Bot` vs `Api`? [Bot vs Api](guides/bot-vs-api.md) — short answer: `Bot` for everyday replies, `Api` when you need full control.

---

## Beyond basic replies

| Feature | Start here |
| --- | --- |
| Formatted answers | [Markdown & Formatting](getting-started-with-tbl/markdown-and-formatting.md) |
| Reply keyboard menus | [Adding a Keyboard](getting-started-with-tbl/adding-keyboard.md) |
| Inline button taps | [Handling Callbacks](getting-started-with-tbl/handling-callbacks.md) |
| Wait for user text | [Handling User Input](getting-started-with-tbl/handle-need-reply.md) |
| Static web page | [Public Web Commands](getting-started-with-tbl/public-web-commands.md) |
| HTTP API from command | [Webapps](webapp-instance/index.md) |

---

## Where to go

- [Command Flow](getting-started-with-tbl/index.md) — structured multi-page guide  
- [Tutorials](tutorials/index.md) — hands-on lessons in order  
- [Command Fields](getting-started-with-tbl/command-fields.md) — Answer, Logic, keyboard, `is_web`  
- [Global Variables](globals/index.md) — `user`, `chat`, `update`  
- [Bot](bot-instance/index.md) and [Api](api-instance/index.md) — main instances  
- [Modules](modules/index.md) and [Libs](libs/index.md) — built-in toolboxes
