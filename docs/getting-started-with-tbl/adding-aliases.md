# Using Aliases in Your Bot

One command, one trigger name — sounds tidy until your keyboard button says `Help`, your users type `help`, and someone tries `/h`. **Aliases** let one command answer to multiple names without duplicating Logic.

Same behavior every time. Less copy-paste. Fewer "why didn't that work?" moments.

---

## What is an alias?

An **alias** is an alternative trigger for a command you already have.

| | |
| --- | --- |
| **One command** | Single Answer + Logic |
| **Many triggers** | Main name + aliases |
| **Same behavior** | Every alias runs the same command |

TBL checks the command name first, then aliases — [Matching & Priority](matching-order.md).

---

## Why aliases are useful

- Match **keyboard button text** exactly
- Support shorthand (`/h` for Help)
- Catch common typos or case variations (if you add each variant)
- Improve UX **without** extra Logic

Aliases are configuration, not code. Free flexibility.

---

## Adding aliases to a command

Open a command in the editor. Fill the **Aliases** field:

```
help, HELP, /h
```

Each value is a separate trigger for the **same** command.

!!! note "Case-sensitive"
    `Help`, `help`, and `HELP` are three different triggers. Add each variation you want to support — the universe is cruel but consistent.

Field details: [Command Fields](command-fields.md).

---

## Aliases and keyboards

This is the most common use case.

Your keyboard button says `Help`. Your command might be named `help_menu` internally. Add alias **`Help`** (exact button text) and taps just work.

!!! tip
    Always add an alias that **exactly** matches each keyboard button label. See [Adding a Keyboard](adding-keyboard.md).

---

## Best practices

- Keep aliases **short and clear**
- Match keyboard labels **character for character**
- Avoid the **same alias on two commands** — only one can win, and it might not be the one you expect
- Fewer well-chosen aliases beat a laundry list of random words

---

## Common mistakes

| Mistake | What happens |
| --- | --- |
| Same alias on two commands | Unpredictable matching — pick one owner |
| Button says `Help`, alias says `help` | Tap does nothing — case mismatch |
| Alias on wrong command | Wrong response — double-check the editor |

---

## Test your aliases

- Open your bot in Telegram
- Type each alias manually
- Tap keyboard buttons
- Confirm they all hit the **same** response

All paths lead to one command? You're set.

---

## What's next

- [Handling User Input](handle-need-reply.md) — pause and wait for replies
- [Using the Wildcard](using-wildcard.md) — catch what aliases don't cover
- [Command Flow](index.md) — full matching rules
