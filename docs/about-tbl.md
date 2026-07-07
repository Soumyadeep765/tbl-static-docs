# What is TBL?

**TBL (Tele Bot Language)** is what you write inside TeleBotHost to make a bot do things.

It's not a general-purpose language for building websites or CLI tools. It's for Telegram bots — receiving updates, sending replies, storing user data, calling external APIs when you need to. TeleBotHost handles hosting; TBL handles bot behavior.

New to the platform? [Getting Started](getting-started.md). Want to write code? [Learning TBL](learning-tbl.md).

## Commands, not event loops

Most Node bot frameworks look like this: register listeners, keep a process alive, hope nothing leaks. TBL flips that.

Telegram sends an update. TBL finds the matching **command** and runs it. The command finishes. Nothing stays running in the background waiting for the next message — the next update starts a fresh execution.

That makes behavior easier to reason about. One update, one command, one path through the code.

## What a command can do

| Surface | Example |
| --- | --- |
| **Telegram reply** | Answer field + Logic → chat message |
| **Inline buttons** | Logic sends keyboard → [Handling Callbacks](getting-started-with-tbl/handling-callbacks.md) |
| **Formatted text** | Markdown/HTML answers — [Markdown & Formatting](getting-started-with-tbl/markdown-and-formatting.md) |
| **Public web page** | `is_web` command → `/public/{bot_id}/index.html` |
| **HTTP API** | Webhook or webapp command → `res.json()` |

See [Command Flow](getting-started-with-tbl/index.md) for the full structured guide.

## Short-lived executions

Each run is sandboxed and time-bounded. Your command does its work — send messages, read storage, call HTTP — and exits. Under load, many users can trigger commands at once without one long-running script getting tangled.

You won't find background timers or daemons in TBL by design. If something should happen "later," it's because a new update arrived or you chained work through `on_run` / another command.

## Async when it helps

Some calls take time — Telegram's API, an external HTTP request. TBL supports `await` where you need the result before continuing. It doesn't push async everywhere; only where waiting actually matters.

## Why the limits exist

TBL deliberately isn't Node.js. You can't install arbitrary npm packages or open raw sockets. That frustrates people who want a full server — and protects everyone else from accidental infinite loops, runaway memory, or bots that become impossible to debug.

The tradeoff: less flexibility, faster path to a working bot.

## What to read next

- [Command Flow](getting-started-with-tbl/index.md) — fields, matching, execution, callbacks, public web  
- [Your First Bot](getting-started-with-tbl/first-hello-bot.md) — hands-on `/start`  
- [Global Variables](globals/index.md) — `user`, `chat`, `update`, and runtime context  
- [Bot](bot-instance/index.md) and [Api](api-instance/index.md) — the two main instances  
- [Bot vs Api](guides/bot-vs-api.md) — two objects, two jobs
