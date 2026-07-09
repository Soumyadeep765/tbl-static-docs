# The TBL Language

TeleBotHost bots run on **TBL** — short for Tele Bot Language. **It's JavaScript** with extra built-in tools for Telegram bot development. If you know JS, you're already halfway there. If you don't, start with [Your First Bot](getting-started-with-tbl/first-hello-bot.md) and add Logic when you're ready.

---

## What is TBL?

**TBL is JavaScript plus bot-building extras.** You write the same language you'd use in a browser or Node app — variables, objects, `if`, functions, `await` — inside TeleBotHost commands.

On top of standard JavaScript, you get globals and instances purpose-built for bots:

| Built-in extra | What it saves you |
| --- | --- |
| `Bot`, `Api` | Telegram send/edit/API calls without HTTP boilerplate |
| `user`, `chat`, `params` | Parsing who sent what and where |
| `db` | Async storage without setting up a database |
| `modules`, `Libs` | Curated utilities without `npm install` |
| `HTTP`, `Webhook`, `Webapp` | Outbound requests and HTTP endpoints |

You don't bootstrap a server, install a Telegram library, or configure webhooks manually. Write commands in the dashboard, launch the bot, TeleBotHost runs your JavaScript.

That's the deal: real JS, sandboxed runtime, built around **commands** instead of long-running processes.

---

## JavaScript — not a full Node server

You can't paste an Express app or a python-telegram-bot script into TeleBotHost and expect it to run unchanged. TBL runs **JavaScript in a bot-focused sandbox** — intentionally limited so bots stay stable and debuggable.

| You can't | You can |
| --- | --- |
| `npm install` arbitrary packages | Use curated [modules](modules/index.md) |
| Keep background processes alive | Chain commands and react to new updates |
| Open raw sockets | Call HTTP via built-in fetch patterns |

The sandbox limits what code can do — which keeps bots stable and makes it harder to accidentally ship something dangerous. Less freedom, fewer 3 AM "why is my bot eating RAM" incidents.

---

## Command surfaces

One bot project can serve multiple surfaces from the same command list:

| Surface | How | Logic runs? |
| --- | --- | --- |
| Telegram chat | User sends command text | Yes |
| Callback button | Inline keyboard tap | Yes |
| Public web | `/public/{bot_id}/page.html` | No — serves source |
| Webapp | `/webapp/{bot_id}/api` | Yes |
| Webhook | Signed HTTP URL | Yes |

Same bot, different doors. Most beginners start with Telegram chat commands — the rest is there when you need it.

---

## Built-in toolboxes

No package manager required. TBL ships with two drawers:

| Toolbox | Examples | Docs |
| --- | --- | --- |
| `modules` | lodash, JWT, md2html, bcrypt, ethers | [Modules](modules/index.md) |
| `Libs` | tgutil, date helpers, referrals, MCL | [Libs](libs/index.md) |

Rule of thumb: general utility you'd npm install → `modules`. Telegram-bot-specific glue → `Libs`.

---

## A line of TBL

```js
Bot.sendMessage(chat.id, "Hi!")
```

That's real JavaScript calling a built-in extra. One line, no imports, no Telegram library setup. Or skip Logic entirely and put `"Hi!"` in the **Answer** field for the same result. Your call — Logic is where the fun starts.

---

## Formatting and web

- **Markdown answers** — default parse mode on commands; see [Markdown & Formatting](getting-started-with-tbl/markdown-and-formatting.md)
- **Public web** — HTML/CSS/JS commands with `is_web`; see [Public Web Commands](getting-started-with-tbl/public-web-commands.md)
- **md2html** — convert Markdown to HTML in Logic via `modules.md2html`

---

## Read next

- [Getting Started](getting-started.md) — create and launch your first bot  
- [What is TBL?](about-tbl.md) — execution model and philosophy  
- [Learning TBL](learning-tbl.md) — sync, async, first steps  
- [Command Flow](getting-started-with-tbl/index.md) — full structured guide  
- [Your First Bot](getting-started-with-tbl/first-hello-bot.md) — five-minute tutorial  

If you already write JavaScript, you're writing TBL — the extras just save you boilerplate. If you're new to JS, the tutorials walk you through one step at a time — no assumptions about what you already know.
