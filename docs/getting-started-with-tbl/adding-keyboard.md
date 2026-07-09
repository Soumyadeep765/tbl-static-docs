# Adding a Keyboard to Your Bot

Typing commands is fine for developers. Everyone else? They'd rather tap a button. **Reply keyboards** put buttons below the chat input — tap one, and Telegram sends that label as a normal message.

Let's upgrade your `/start` command from [Your First Bot](first-hello-bot.md) into a tiny menu bot.

---

## What we're building

We'll update `/start` to:

- Send a welcome message
- Show **Help** and **About** buttons
- Respond when users tap those buttons

No Logic required yet — just Answer fields and a keyboard layout string.

---

## What is a keyboard?

A **reply keyboard** is a set of buttons shown **below** the message input field.

When a user taps a button:

- Telegram sends the button text as a message (e.g. `Help`)
- TBL treats it like any other text input
- A matching command responds

No typing. Fewer typos. Happier users.

!!! note "Not inline buttons"
    Buttons *inside* the message bubble are **inline keyboards** — different feature, built in Logic. See [Handling Callbacks](handling-callbacks.md). This page is about reply keyboards only.

---

## Step 1 — Open the command

- Dashboard → your bot → **Commands**
- Find your existing `/start` command
- Click edit (pencil icon)

---

## Step 2 — Add the keyboard

Update the fields:

**Command:** `/start`

**Answer:**

```
Hello 👋
Choose one of the options below to continue.
```

**Keyboard:** `Help, About`

That creates **two buttons in one row**.

!!! warning
    A keyboard always requires an **Answer**. Buttons can't be sent without a message — Telegram's rule, not ours.

Field reference: [Command Fields](command-fields.md).

---

## Keyboard layout basics

Keyboards are plain text with simple rules:

- **Same row:** separate buttons with commas → `Help, About`
- **New row:** line break → `Help\nAbout`
- **Mix freely:** `Yes, No\nCancel`

| Keyboard value | Result |
| --- | --- |
| `Yes,No` | One row, two buttons |
| `Yes\nNo` | Two rows, one button each |
| `Yes,No\nBoth` | Row 1: Yes, No — Row 2: Both |

Design menus like you'd sketch them on a napkin.

---

## Step 3 — Create the Help command

Tapping `Help` sends the text `Help`. TBL needs a command named `Help` to respond.

**Command:** `Help`

**Answer:**

```
Here's what I can help you with:
- Use the buttons to navigate
- Tap About to learn more about me
- Send /start anytime to restart
```

No Logic needed. Case matters — `Help` is not `help`.

---

## Step 4 — Create the About command

**Command:** `About`

**Answer:**

```
I'm a simple Telegram bot built on TeleBotHost.
I use commands and keyboards to guide users easily.
```

---

## Why keyboards are useful

Great for:

- Menus and navigation
- Guided flows ("Yes / No / Maybe")
- Reducing "what do I type?" confusion

!!! tip
    Use keyboards for common actions instead of making users memorize commands. Save `/commands` for power users.

If button text doesn't match your command name exactly, add an [alias](adding-aliases.md).

---

## Test it

- Open your bot in Telegram
- Send `/start` — buttons should appear
- Tap **Help** and **About** — each should reply

If a button does nothing, check the command name matches the button label (including capitalization).

Menu complete 🎉

---

## What's next

- Add a **Back** button (point it at `/start` via alias or command)
- Combine keyboards with [Need Reply](handle-need-reply.md) for forms
- Add **Logic** when static answers aren't enough — [`Bot`](../bot-instance/index.md) sends dynamic replies

Your bot is officially interactive.
