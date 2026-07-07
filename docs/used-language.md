# The TBL Language

TeleBotHost bots run on **TBL** — short for Tele Bot Language.

If you've written any JavaScript, the syntax will look familiar: variables, objects, `if`, functions, `await`. What's different is the environment. `Bot`, `Api`, `user`, and `chat` are already there. You don't bootstrap a server or wire up a Telegram library.

## Not Node, not Python

You can't paste an Express app or a python-telegram-bot script into TeleBotHost and expect it to run. TBL is its own runtime — smaller, sandboxed, built around **commands**.

That's intentional. The sandbox limits what code can do, which keeps bots stable and makes it harder to accidentally ship something dangerous.

## Command surfaces

One bot project can serve multiple surfaces:

| Surface | How | Logic runs? |
| --- | --- | --- |
| Telegram chat | User sends command text | Yes |
| Callback button | Inline keyboard tap | Yes |
| Public web | `/public/{bot_id}/page.html` | No — serves source |
| Webapp | `/webapp/{bot_id}/api` | Yes |
| Webhook | Signed HTTP URL | Yes |

## What you gain

No VPS. No webhook nginx config. No keeping a process alive on a $5 droplet. You write commands in the dashboard, launch the bot, TeleBotHost runs it.

Telegram integration isn't a dependency you install — it's the platform.

Built-in tools include [modules](modules/index.md) (lodash, jwt, md2html, …) and [libraries](libs/index.md) (tgutil, date helpers, …).

## A line of TBL

```js
Bot.sendMessage("Hi")
```

That's a complete interaction pattern in one call. Or skip Logic entirely and use the **Answer** field for the same result.

## Formatting & web

- **Markdown answers** — default parse mode on commands; see [Markdown & Formatting](getting-started-with-tbl/markdown-and-formatting.md)
- **Public web** — HTML/CSS/JS commands with `is_web`; see [Public Web Commands](getting-started-with-tbl/public-web-commands.md)
- **md2html** — convert Markdown to HTML in Logic via `modules.md2html`

## Read next

- [Command Flow](getting-started-with-tbl/index.md) — full structured guide  
- [What is TBL?](about-tbl.md) — execution model  
- [Learning TBL](learning-tbl.md) — sync, async, first steps  
- [Your First Bot](getting-started-with-tbl/first-hello-bot.md) — five-minute tutorial  

If you come from JavaScript, you'll be productive quickly. If you don't, start with [Your First Bot](getting-started-with-tbl/first-hello-bot.md) and add Logic when you're ready.
