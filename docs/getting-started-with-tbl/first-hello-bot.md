# Your First Bot

Let's get something working on Telegram in the next few minutes. No Logic, no databases, no "what's a callback query?" — just a bot that says hello when someone sends `/start`.

If you can fill in two fields and click Save, you can build a bot. Spoiler: that's literally all we're doing.

---

## What you're building

A single command: user sends `/start`, bot replies with a welcome message. That's it. Everything else in this section builds on top of this.

---

## Open the command editor

Dashboard → your bot → **Commands** → **Add Command**.

Everything your bot does lives here. One command = one row in this list.

---

## Fill in two fields

**Command:** `/start`

**Answer:**

```
Hello 👋
Welcome to my first TBL bot!
```

Save it. Launch the bot from the dashboard if you haven't already. Congratulations — you're a bot developer now. (Technically.)

---

## What happens when someone types `/start`

Telegram delivers the update. TBL matches `/start`, sends the **Answer**, and stops. The answer goes out *before* any Logic runs — so for simple replies you often don't need a Logic field at all.

Pipeline details when you're curious: [Execution Flow](execution-flow.md).

---

## Formatting the answer

The Answer field accepts [Telegram Markdown](markdown-and-formatting.md) by default. Bold, italic, line breaks — nice for welcome text.

```
*Welcome!*
Choose an option below.
```

Start plain. Add formatting once the message sends reliably. Broken asterisks are harder to debug than plain text.

---

## Test it

Open your bot in Telegram, send `/start`. You should see the hello message right away.

**Nothing comes back?**

- Check the bot is **launched** in the dashboard
- Confirm you're messaging the correct `@username`
- Wait a few seconds and try again — sometimes Telegram is slow, not you

---

## What's next

[Adding a Keyboard](adding-keyboard.md) — give users buttons so they don't have to type commands.

Or read [Command Flow](index.md) for the full structured guide when you're ready to go deeper.
