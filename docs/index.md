# TBL Documentation

Docs for building Telegram bots on **TeleBotHost** with **TBL (Tele Bot Language)**.

TeleBotHost runs your bot in the cloud. TBL is the code you write in the command editor — JavaScript-shaped syntax, built-in Telegram tools, no server to manage.

## New here?

1. [Getting Started](getting-started.md) — account, BotFather token, launch your bot  
2. [Tutorials](tutorials/index.md) — six short lessons from `/start` to wildcard handlers  
3. [What is TBL?](about-tbl.md) — how commands run and why the model looks the way it does  

## Reference sections

**[Global Variables](globals/index.md)** — `user`, `chat`, `update`, `message`, and the rest of the context available in every command. Read this before diving into instances.

**Instances** — the objects you call in command logic:

- [Bot](bot-instance/index.md) — flow, storage, simple sends  
- [Api](api-instance/index.md) — full Telegram Bot API access  
- [Bot vs Api](guides/bot-vs-api.md) — when to use which (read after the Bot and Api overviews)  
- [HTTP](http-instance/index.md) — outbound requests to external services  
- [User](user-instance/index.md) / [Global](global-instance/index.md) — per-user and bot-wide data  
- [msg](msg-instance/index.md) — reply, edit, delete on the current message  
- [Webhooks](webhook-instance/index.md) / [Webapps](webapp-instance/index.md) — HTTP endpoints tied to commands  
- [res](res-instance.md) — JSON, HTML, redirects from webhook/Webapp commands  

**[Modules](modules/index.md)** and **[Libraries](libs/index.md)** — lodash, jwt, date helpers, Telegram utilities, and other preloaded tools.

## Outside these docs

- [TeleBotHost Console](https://console.telebothost.com/)  
- [First bot tutorial (with screenshots)](https://telebothost.com/tutorials/adding-first-bot)  
- [Telegram Bot API](https://core.telegram.org/bots/api)
