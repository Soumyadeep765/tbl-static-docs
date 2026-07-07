# Command Flow

Every Telegram bot on TeleBotHost is a collection of **commands**. TBL receives an update, picks one command, runs it, and finishes. No background process, no event loop.

This section explains how commands are built, matched, and executed — from basic `/start` replies to callbacks, markdown, and public web pages.

---

## How an update becomes a response

```
Telegram update arrives
        │
        ▼
Run `@` initialization (if defined)
        │
        ▼
Match one command (priority order)
        │
        ▼
Send Answer + Keyboard (if configured)
        │
        ▼
Run Logic code (if any)
        │
        ▼
On error → run `!` handler
        │
        ▼
Run `@@` post-processor (if defined)
        │
        ▼
Done
```

See [Execution Flow](execution-flow.md) for the full lifecycle.

---

## Pages in this section

### Core concepts

| Page | What you'll learn |
| --- | --- |
| [Command Fields](command-fields.md) | Answer, Logic, Keyboard, aliases, `need_reply`, `is_web`, `parse_mode` |
| [Matching & Priority](matching-order.md) | How TBL picks which command runs |
| [Execution Flow](execution-flow.md) | `@`, `!`, `@@`, answer-before-logic, sessions |
| [Special Commands](special-commands.md) | `/start`, `@`, `!`, `@@`, `*` |
| [Dynamic Handlers](dynamic-commands.md) | `/handle_{update_type}`, inline query, channel |

### Formatting & web

| Page | What you'll learn |
| --- | --- |
| [Markdown & Formatting](markdown-and-formatting.md) | Answer markdown, `parse_mode`, `modules.md2html` |
| [Public Web Commands](public-web-commands.md) | `is_web` flag, static pages per bot |

### Interactions

| Page | What you'll learn |
| --- | --- |
| [Handling Callbacks](handling-callbacks.md) | Inline buttons, `callback_query`, editing messages |
| [Handling User Input](handle-need-reply.md) | `need_reply` sessions |
| [Using Aliases](adding-aliases.md) | Multiple triggers for one command |
| [Wildcard (*)](using-wildcard.md) | Catch-all for unknown input |

### Hands-on tutorials

| Page | What you'll build |
| --- | --- |
| [Your First Bot](first-hello-bot.md) | `/start` with an answer |
| [Adding a Keyboard](adding-keyboard.md) | Reply keyboard menu |
| [Command Structure](command-structure.md) | Short overview + links |

---

## Command surfaces at a glance

| Surface | Trigger | Answer field | Logic + `res` |
| --- | --- | --- | --- |
| Telegram message | User sends text/command | Yes | Yes |
| Callback query | Inline button tap | Yes (then logic) | Yes |
| Webhook | Signed HTTP URL | No | Yes + `res` |
| Webapp | `/webapp/{bot_id}/{cmd}` | No | Yes + `res` |
| Public web | `/public/{bot_id}/{path}` | N/A — serves command source | **No sandbox** |

---

## Read first

New to TeleBotHost? Start with [Getting Started](../getting-started.md), then [Your First Bot](first-hello-bot.md).

Want the big picture? [What is TBL?](../about-tbl.md) explains the command-driven model.
