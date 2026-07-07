# Using the Wildcard (*) Command

Most bots have named commands — `/start`, `Help`, settings, whatever. But users don't read manuals. They send `hi`, `??`, or `/randomthing`. The **wildcard command (`*`)** catches everything else.

One command. Every unmatched message. Your bot's polite "I didn't get that."

---

## What is the `*` command?

The **`*`** command is a **catch-all**. It runs when:

- No command name matches
- No alias matches
- Nothing more specific wins

In plain terms: **if nothing else fits, `*` runs.**

It's priority #4 in matching — [Matching & Priority](matching-order.md). Named commands always beat it.

---

## What we're building

A bot that always replies to unknown input — same friendly fallback every time. No Logic required for the simplest version.

---

## Step 1 — Create the command

Dashboard → **Commands** → **Add Command**

**Command:** `*`

**Answer:** `Hello 👋 I reply to everything you send!`

Save. Done. (For this demo, make it your only command — or pair it with `/start` below.)

Special command details: [Special Commands](special-commands.md).

---

## How the `*` command works

When a user sends a message:

1. TBL checks all defined command names and aliases
2. If nothing matches → `*` is selected
3. Answer is sent (Logic runs too, if you add it)

Works for normal text, unknown slash commands, random keyboard mash — anything that didn't match something specific.

---

## Example behavior

**Only `*` defined:**

| User sends | Result |
| --- | --- |
| `Hi` | `*` runs |
| `/test` | `*` runs |
| `🎉` | `*` runs (if no other match) |

Same answer every time.

**`*` plus `/start`:**

| User sends | Result |
| --- | --- |
| `/start` | `/start` runs |
| Anything else | `*` runs |

That's the usual pattern: real commands for real actions, `*` for the rest.

---

## Good use cases

- Default "I didn't understand" reply
- Point users to `/start` or your menu
- Maintenance mode message
- Channel/update fallback when no dynamic handler exists

!!! warning
    Don't put your **main** bot logic in `*`. It's a safety net, not the star of the show. Important flows deserve named commands.

---

## Test it

- Open your bot in Telegram
- Send random text
- Bot should reply with your fallback

If `/start` still works separately, even better — you've got proper routing.

Wildcard working 🎉

---

## What's next

- Combine with [aliases](adding-aliases.md) so common phrases hit named commands first
- Add Logic to `*` for smarter fallbacks (keyword hints, fuzzy help)
- [Dynamic Handlers](dynamic-commands.md) for update types text matching can't catch

You now have a bot that never leaves users talking into the void.
