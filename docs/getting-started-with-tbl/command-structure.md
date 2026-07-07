# Command Structure in TBL

Commands are the foundation of every TeleBotHost bot. Each incoming update triggers **exactly one** matched command (plus the automatic `@` and `@@` wrappers).

---

## The command-driven model

```
User action  →  Telegram update  →  TBL matches command  →  Answer + Logic  →  Done
```

No listeners. No long-running process. One update, one path through your code.

---

## What a command contains

| Part | Role |
| --- | --- |
| **Name** | What triggers it (`/start`, `Help`, `*`) |
| **Answer** | Optional auto-reply before logic |
| **Logic** | TBL code for dynamic behavior |
| **Options** | Keyboard, aliases, need reply, public web, parse mode |

Full field reference: [Command Fields](command-fields.md).

---

## Learn part by part

### Flow & matching

1. [Command Flow overview](index.md) — hub for this section
2. [Matching & Priority](matching-order.md) — which command wins
3. [Execution Flow](execution-flow.md) — `@`, Answer, Logic, `!`, `@@`
4. [Special Commands](special-commands.md) — `/start`, `@`, `!`, `@@`, `*`
5. [Dynamic Handlers](dynamic-commands.md) — `/handle_{update_type}`

### Formatting & surfaces

6. [Markdown & Formatting](markdown-and-formatting.md) — answers and `md2html`
7. [Public Web Commands](public-web-commands.md) — `is_web` static pages

### User interactions

8. [Handling Callbacks](handling-callbacks.md) — inline buttons
9. [Handling User Input](handle-need-reply.md) — need reply sessions
10. [Using Aliases](adding-aliases.md) — multiple triggers
11. [Wildcard (*)](using-wildcard.md) — catch-all

### Hands-on

12. [Your First Bot](first-hello-bot.md) — start here
