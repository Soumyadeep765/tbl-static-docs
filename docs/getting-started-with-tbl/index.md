# Command Flow

Every bot on TeleBotHost is just a collection of **commands**. TBL doesn't keep a server running forever or manage an event loop. Instead, a user sends a message, TBL finds the matching command, runs it, sends the reply, and goes back to sleep.

This section covers all the concepts you need to understand how commands match, run, and interact with the Telegram API.

---

## 1. The Basics: Command Structure

Before writing code, you should understand what a command actually is and how the special `@` command lets you share configurations and variables across all your bot commands.

➔ **[Command Structure](command-structure.md)** — The building block of your bot and sharing variables with `@`.

➔ **[Command Fields](command-fields.md)** — A breakdown of the dashboard editor fields (Answer, Logic, Keyboard, Aliases).

---

## 2. Core Mechanics: Execution & Matching

Once you know how to build a command, learn how TBL runs and matches them:

➔ **[Execution Flow](execution-flow.md)** — The step-by-step pipeline of code execution, and how to stop execution early using `return` in `@`.

➔ **[Matching & Priority](matching-order.md)** — How TBL decides which command to run when a user sends a message.

---

## 3. Special Commands & Advanced Routing

Learn how to handle unexpected inputs and non-text events:

➔ **[Special Commands](special-commands.md)** — Pre-defined triggers like `/start`, `@`, `!`, `@@`, and `*`.

➔ **[Wildcard Command (*)](using-wildcard.md)** — Creating a friendly safety net for unmatched user messages.

➔ **[Dynamic Handlers](dynamic-commands.md)** — Routing background updates, channel events, and inline queries.

---

## 4. Presentation & Web Pages

Make your bot look professional and host public web pages:

➔ **[Markdown & Formatting](markdown-and-formatting.md)** — Styling your replies with bold, italic, and pre-formatted text.

➔ **[Public Web Commands](public-web-commands.md)** — Serving static HTML, CSS, and client-side JavaScript pages directly from your bot.
