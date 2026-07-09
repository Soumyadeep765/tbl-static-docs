# Command Fields

Open any command in the TeleBotHost editor and you'll see a handful of fields. Together they answer three questions: **what triggers this?**, **what does the user see?**, and **what code runs?**

No magic — just a form. Fill it in, save, test in Telegram.

---

## Field overview

| Field | Required | Purpose |
| --- | --- | --- |
| **Command** | Yes | Trigger name (e.g. `/start`, `Help`, `*`) |
| **Answer** | No* | Text sent before logic runs |
| **Logic** | No | Real JavaScript (+ built-in bot extras) that runs after the answer |
| **Keyboard** | No | Reply keyboard buttons below the input |
| **Aliases** | No | Alternative trigger names |
| **Need Reply** | No | Wait for the user's next message |
| **Parse mode** | No | How the Answer is formatted (default: Markdown) |
| **Public web** (`is_web`) | No | Expose command at `/public/{bot_id}/...` |
| **Group only** | No | Restrict command to group/supergroup chats |

\* Answer is required when using a **Keyboard** — buttons cannot be sent without a message. Telegram's rules, not ours.

---

## Command name

The primary trigger — the word or phrase that wakes this command up.

| Name | Matches |
| --- | --- |
| `/start` | `/start`, `/start@YourBot` |
| `Help` | Exact text `Help` (case-sensitive) |
| `*` | Fallback when nothing else matches |
| `@` | Runs before every command |
| `/handle_callback_query` | Callback button updates (see [Dynamic Handlers](dynamic-commands.md)) |

Multi-word commands work fine. TBL always tries the **longest** name first — `/set name` wins over `/set` when both exist.

Matching rules in depth: [Matching & Priority](matching-order.md).

---

## Answer

Plain text (or [Telegram-formatted](markdown-and-formatting.md) text) sent **automatically before** Logic executes.

```
*Welcome!*
Choose an option below.
```

If you fill in Answer, TBL sends it for you. You don't need [`Bot.sendMessage()`](../bot-instance/index.md) for the same text unless Logic should send *additional* messages on top.

**Not used for:** public web commands — those serve source as a file, not a chat message. See [Public Web Commands](public-web-commands.md).

---

## Logic

**Real JavaScript** that runs **after** the Answer (if any). Same language you'd write anywhere else — `if`, `await`, loops, objects — plus bot-building extras already in scope (`Bot`, `Api`, `user`, `chat`, `db`, `modules`, `Libs`). No imports needed.

This is where the interesting stuff happens:

- Conditional replies
- Database reads/writes
- Inline keyboards (via [`Api`](../api-instance/index.md))
- HTTP calls
- `res.json()` in webhook/webapp commands

```js
let count = await db.bot.get("visits") || 0
await db.bot.set("visits", count + 1)
Bot.sendMessage(chat.id, "Visit #" + (count + 1))
```

[`Bot`](../bot-instance/index.md) is a global — no import needed. [`chat`](../globals/chat.md) and [`user`](../globals/user.md) tell you who's talking. Leave Logic empty for answer-only commands — totally valid.

When does Answer run vs Logic? [Execution Flow](execution-flow.md).

---

## Keyboard

A **reply keyboard** — buttons shown **below** the chat input. Tap a button and Telegram sends its label as a normal text message.

```
Help, About
Settings
```

| Layout | Keyboard value |
| --- | --- |
| One row, two buttons | `Help, About` |
| Two rows | `Help\nAbout` |
| Mixed | `Yes, No\nCancel` |

Pair button labels with [aliases](adding-aliases.md) so taps match reliably — aliases are case-sensitive.

For buttons **inside** the message bubble (inline keyboards), skip this field and build them in Logic instead — [Handling Callbacks](handling-callbacks.md).

Walkthrough: [Adding a Keyboard](adding-keyboard.md).

---

## Aliases

Comma-separated alternative triggers for the **same** command.

```
help, HELP, /h
```

Aliases are **case-sensitive**. Keyboard says `Help`? Add `Help` as an alias, not `help` — unless you want both.

Full guide: [Using Aliases](adding-aliases.md).

---

## Need Reply

When enabled, the command doesn't finish in one shot:

1. Sends the Answer (and keyboard if set)
2. **Pauses** and waits for the user's next message
3. Runs Logic with that message as input

See [Handling User Input](handle-need-reply.md). Sending any other valid command (like `/start`) cancels the wait — users aren't trapped.

---

## Parse mode

Controls formatting of the **Answer** field only. Default is **Markdown**.

| Value | Effect |
| --- | --- |
| `Markdown` | `*bold*`, `_italic_`, `` `code` `` |
| `HTML` | `<b>bold</b>`, `<i>italic</i>` |
| `MarkdownV2` | Telegram MarkdownV2 rules |

Logic messages need their own `parse_mode` on each [`Bot.sendMessage()`](../bot-instance/index.md) or [`Api.sendMessage()`](../api-instance/index.md) call — the command setting doesn't carry over.

Details: [Markdown & Formatting](markdown-and-formatting.md).

---

## Public web (`is_web`)

Marks a command as a **static web resource** served at:

```
/public/{bot_id}/{command_name}
```

- HTML, CSS, JS, JSON, `.md` files
- No Logic execution — source is served directly
- EJS templates (`<%`) supported in HTML/text

See [Public Web Commands](public-web-commands.md).

---

## Group only

When enabled, the command runs only in **groups and supergroups**. Private chats are ignored — no Answer, no Logic, no awkward silence in DMs.

---

## Typical combinations

| Goal | Fields to use |
| --- | --- |
| Simple welcome | Command + Answer |
| Formatted welcome | Command + Answer + Parse mode |
| Menu bot | Command + Answer + Keyboard + Aliases |
| Ask a question | Command + Answer + Need Reply + Logic |
| Inline buttons | Logic only (or Answer + Logic) — [Callbacks](handling-callbacks.md) |
| Landing page | Command named `index.html` + `is_web` |
| API endpoint | Logic + webhook/webapp — [Webapps](../webapp-instance/index.md) |

---

## See also

- [Execution Flow](execution-flow.md) — when Answer and Logic run
- [Matching & Priority](matching-order.md) — how triggers resolve
- [Your First Bot](first-hello-bot.md) — put two fields together in five minutes
