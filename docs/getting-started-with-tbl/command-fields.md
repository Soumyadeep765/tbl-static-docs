# Command Fields

Each command in the TeleBotHost editor is made of fields. Together they define **what triggers the command**, **what the user sees**, and **what code runs**.

---

## Field overview

| Field | Required | Purpose |
| --- | --- | --- |
| **Command** | Yes | Trigger name (e.g. `/start`, `Help`, `*`) |
| **Answer** | No* | Text sent before logic runs |
| **Logic** | No | TBL code executed after the answer |
| **Keyboard** | No | Reply keyboard buttons below the input |
| **Aliases** | No | Alternative trigger names |
| **Need Reply** | No | Wait for the user's next message |
| **Parse mode** | No | How the Answer is formatted (default: Markdown) |
| **Public web** (`is_web`) | No | Expose command at `/public/{bot_id}/...` |
| **Group only** | No | Restrict command to group/supergroup chats |

\* Answer is required when using a **Keyboard** — buttons cannot be sent without a message.

---

## Command name

The primary trigger. Examples:

| Name | Matches |
| --- | --- |
| `/start` | `/start`, `/start@YourBot` |
| `Help` | Exact text `Help` (case-sensitive) |
| `*` | Fallback when nothing else matches |
| `@` | Runs before every command |
| `/handle_callback_query` | Callback button updates (see [Dynamic Handlers](dynamic-commands.md)) |

Multi-word commands are supported — TBL matches the longest name first (`/set name` before `/set`).

---

## Answer

Plain text or [Telegram-formatted](markdown-and-formatting.md) message sent **before** logic executes.

```
*Welcome!*
Choose an option below.
```

If the command has an Answer, it is sent automatically. You do not need `Bot.sendMessage()` for the same text unless logic should send *additional* messages.

**Not used for:** public web commands (source is served as a file, not sent as a chat message).

---

## Logic

TBL JavaScript that runs after the Answer (if any). Use for:

- Conditional replies
- Database reads/writes
- Inline keyboards
- HTTP calls
- `res.json()` in webhook/webapp commands

```js
let count = await db.bot.get("visits") || 0
await db.bot.set("visits", count + 1)
Bot.sendMessage("Visit #" + (count + 1))
```

Leave Logic empty for answer-only commands.

---

## Keyboard

Reply keyboard — buttons shown **below** the chat input. Tapping a button sends its label as a normal text message.

```
Help, About
Settings
```

| Layout | Keyboard value |
| --- | --- |
| One row, two buttons | `Help, About` |
| Two rows | `Help\nAbout` |
| Mixed | `Yes, No\nCancel` |

Pair keyboard labels with [aliases](adding-aliases.md) so taps match reliably.

For buttons **inside** the message bubble, use inline keyboards in Logic — see [Handling Callbacks](handling-callbacks.md).

---

## Aliases

Comma-separated alternative triggers for the same command.

```
help, HELP, /h
```

Aliases are **case-sensitive**. If your keyboard button says `Help`, add `Help` as an alias.

---

## Need Reply

When enabled, the command:

1. Sends the Answer (and keyboard if set)
2. **Pauses** and waits for the user's next message
3. Runs Logic with that message as input

See [Handling User Input](handle-need-reply.md).

Sending any other valid command cancels the wait.

---

## Parse mode

Controls formatting of the **Answer** field. Default is **Markdown**.

| Value | Effect |
| --- | --- |
| `Markdown` | `*bold*`, `_italic_`, `` `code` `` |
| `HTML` | `<b>bold</b>`, `<i>italic</i>` |
| `MarkdownV2` | Telegram MarkdownV2 rules |

Set in the command editor. Logic messages use `parse_mode` on each `Bot.sendMessage()` / `Api.sendMessage()` call separately.

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

When enabled, the command runs only in **groups and supergroups**. Private chats are ignored (no Answer, no Logic).

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
