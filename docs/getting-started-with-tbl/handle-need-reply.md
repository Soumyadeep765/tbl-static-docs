# Handling User Input with Need Reply

Commands that fire and forget are great until you need to *ask* something — a name, a number, a yes/no. **Need Reply** pauses the command, waits for the user's next message, then runs Logic with that input.

It's a mini conversation in two steps. No wizard framework required.

---

## What is Need Reply?

**Need Reply** tells the bot: send the Answer, then **wait** for the user's next message before running Logic.

| Step | What happens |
| --- | --- |
| 1 | User triggers the command |
| 2 | Bot sends Answer (and keyboard if set) |
| 3 | Bot **waits** — Logic does **not** run yet |
| 4 | User sends their next message |
| 5 | Logic runs with that message as input |

Useful for names, values, choices — any single piece of user text.

Full pipeline: [Execution Flow](execution-flow.md#need-reply-flow).

---

## Simple example — ask for a name

**Command:** `/input`

**Answer:** `Tell me your name 🙂`

**Need Reply:** enabled

**Logic:**

```js
Bot.sendMessage(chat.id, "Your name is " + message)
```

[`Bot`](../bot-instance/index.md) sends the reply. [`message`](../globals/message.md) holds the text the user just sent — plain string, not the full Telegram object.

---

## How this works (step by step)

1. User sends `/input`
2. Bot replies: "Tell me your name"
3. Need Reply is on → bot **waits**
4. User sends `Alice`
5. Logic runs: "Your name is Alice"

**Important:** that next message is treated as **input**, not a new command — unless it matches another valid command name.

---

## What `message` means here

For this beginner flow:

- [`message`](../globals/message.md) is the **text** the user sent
- Photos, stickers, voice → `message` is `null` (handle that in advanced bots)
- Keeps things simple while you're learning

Text after the command name lives in [`params`](../globals/params.md) — different variable, different job.

---

## How to cancel Need Reply

Users change their mind. Let them escape by sending **any valid existing command**:

- `/start`
- `Help`
- `About`

The waiting state clears. Need Reply cancels. Normal matching resumes.

!!! info
    You don't need special "cancel" Logic — valid commands cancel automatically. Consider mentioning `/start` in your Answer so users know the escape hatch.

---

## Why the cancel matters

Without it:

- Users feel **stuck** in input mode
- Other commands **stop working** until they reply or cancel
- The bot feels **broken**

One line in your Answer — *"Send /start anytime to cancel"* — saves support headaches.

---

## Good practices

- **Explain** what input you expect in the Answer
- Keep flows **short** — one question at a time
- Mention **/start** or menu buttons as cancel options
- **Reply immediately** after receiving input
- Avoid chaining many Need Reply steps in a row (use Logic + `db.user` for wizards)

!!! warning
    Leaving users in a reply-waiting state without clear instructions blocks normal bot usage. Always tell them what to send — and how to bail out.

More detail: [handle-need-reply matching](matching-order.md#need-reply-override).

---

## Test cancel behavior

1. Send `/input`
2. Instead of a name, send `/start`
3. Bot should cancel input mode and run `/start` normally

Works? Your Need Reply setup is solid.

---

## What's next

- Store answers in `db.user` for multi-step flows
- Combine with [keyboards](adding-keyboard.md) for guided choices
- [Handling Callbacks](handling-callbacks.md) when buttons live inside messages

Foundation for wizards, forms, and anything that asks before it acts.
