# The TBL Language

TeleBotHost bots run on **TBL** — short for Tele Bot Language.

If you've written any JavaScript, the syntax will look familiar: variables, objects, `if`, functions, `await`. What's different is the environment. `Bot`, `Api`, `user`, and `chat` are already there. You don't bootstrap a server or wire up a Telegram library.

## Not Node, not Python

You can't paste a Express app or a python-telegram-bot script into TeleBotHost and expect it to run. TBL is its own runtime — smaller, sandboxed, built around commands.

That's intentional. The sandbox limits what code can do, which keeps bots stable and makes it harder to accidentally ship something dangerous.

## What you gain

No VPS. No webhook nginx config. No keeping a process alive on a $5 droplet. You write commands in the dashboard, launch the bot, TeleBotHost runs it.

Telegram integration isn't a dependency you install — it's the platform.

## A line of TBL

```js
Bot.sendMessage("Hi");
```

That's a complete interaction pattern in one call. Everything else in the docs builds on moments like that.

## Read next

- [What is TBL?](about-tbl.md) — how commands execute  
- [Learning TBL](learning-tbl.md) — sync, async, first steps  
- [Tutorials](tutorials/index.md) — build a bot hands-on

If you come from JavaScript, you'll be productive quickly. If you don't, the tutorials still work — start with [Your First Bot](getting-started-with-tbl/first-hello-bot.md) and ignore the code until you're ready.
