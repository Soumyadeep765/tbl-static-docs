# Command Structure in TBL

Every TeleBotHost bot is a collection of **commands**. Not routes, not controllers, not event listeners — commands. Telegram sends an update, TBL matches **exactly one**, runs it, and finishes.

One update in. One path through your code out. That's the whole model.

---

## The command-driven model

```
User action  →  Telegram update  →  TBL matches command  →  Answer + Logic  →  Done
```

No background process humming away. No `while(true)` loop. Each message is a fresh, self-contained run — plus automatic `@` and `@@` wrappers around it ([Special Commands](special-commands.md)).

---

## What a command contains

Think of a command as a small form with a few parts:

| Part | Role |
| --- | --- |
| **Name** | What triggers it (`/start`, `Help`, `*`) |
| **Answer** | Optional auto-reply before logic |
| **Logic** | JavaScript for dynamic behavior |
| **Options** | Keyboard, aliases, need reply, public web, parse mode |

**Answer** is the fast path — static text TBL sends for you. **Logic** is where [`Bot`](../bot-instance/index.md), [`Api`](../api-instance/index.md), `db`, and [globals](../globals/index.md) like [`user`](../globals/user.md) and [`params`](../globals/params.md) come in.

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

12. [Your First Bot](first-hello-bot.md) — **start here** if you haven't built anything yet

---

## Where to go next

Built `/start` already? Add [a keyboard](adding-keyboard.md). Need buttons inside messages? [Callbacks](handling-callbacks.md). Want a landing page? [Public web](public-web-commands.md).

The docs are modular — read what you need, skip what you don't.
