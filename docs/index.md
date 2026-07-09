# TBL Documentation

Build Telegram bots in the cloud without managing servers — write commands, hit save, and TeleBotHost runs the rest.

**TBL (Tele Bot Language)** is **JavaScript** — real `if`, `await`, objects, the works — plus built-in extras for bot development: `Bot`, `Api`, `user`, `chat`, `modules`, `Libs`, and `db`. No boilerplate, no DevOps guilt.

---

## New here?

Work through these in order — each step takes about five minutes:

1. [Getting Started](getting-started.md) — account, BotFather token, launch your bot  
2. [Command Flow](getting-started-with-tbl/index.md) — how commands match, run, and respond  
3. [Your First Bot](getting-started-with-tbl/first-hello-bot.md) — `/start` in five minutes  
4. [What is TBL?](about-tbl.md) — the command-driven execution model  

!!! tip "New to TBL?"
    TBL is **JavaScript** with built-in bot extras — `Bot`, `Api`, `user`, `chat`, and more. The fastest on-ramp: [Learning TBL](learning-tbl.md) — globals, instances, and your first Logic field in one page.

---

## Command flow (structured guide)

| Topic | Page |
| --- | --- |
| Command fields (Answer, Logic, keyboard, `is_web`) | [Command Fields](getting-started-with-tbl/command-fields.md) |
| Matching & priority | [Matching & Priority](getting-started-with-tbl/matching-order.md) |
| Execution pipeline (`@`, `!`, `@@`) | [Execution Flow](getting-started-with-tbl/execution-flow.md) |
| Markdown & formatting | [Markdown & Formatting](getting-started-with-tbl/markdown-and-formatting.md) |
| Public web pages | [Public Web Commands](getting-started-with-tbl/public-web-commands.md) |
| Inline button callbacks | [Handling Callbacks](getting-started-with-tbl/handling-callbacks.md) |

Full index: [Command Flow overview](getting-started-with-tbl/index.md) · [Tutorials](tutorials/index.md)

---

## Reference sections

**[Global Variables](globals/index.md)** — `user`, `chat`, `update`, `message`, and the rest of the context available in every command.

**Instances** — the objects you call in command logic:

- [Bot](bot-instance/index.md) — flow, storage, simple sends  
- [Api](api-instance/index.md) — full Telegram Bot API access  
- [Bot vs Api](guides/bot-vs-api.md) — when to use which  
- [HTTP](http-instance/index.md) — outbound requests to external services  
- [db](db-instance/index.md) — bot, user, and global storage  
- [msg](msg-instance/index.md) — reply, edit, delete on the current message  
- [Webhooks](webhook-instance/index.md) / [Webapps](webapp-instance/index.md) — HTTP endpoints tied to commands  
- [Public Web](webapp-instance/public-web.md) — static `is_web` pages per bot  
- [res](res-instance/index.md) — JSON, HTML, redirects from webhook/webapp commands  

**[modules](modules/index.md)** and **[Libraries](libs/index.md)** — lodash, jwt, md2html, date helpers, and more.

---

## Outside these docs

- [TeleBotHost Console](https://console.telebothost.com/)  
- [First bot tutorial (with screenshots)](https://telebothost.com/tutorials/adding-first-bot)  
- [Telegram Bot API](https://core.telegram.org/bots/api)
