# Special Commands

Most commands wait for a user to type something. A few **reserved names** run on their own — before, after, or instead of normal matching. Think of them as hooks wired into every update.

You still create them like any other command in the editor. The difference is *when* they fire.

---

## `/start` — the front door

The first thing most users do: tap **Start** or send `/start`.

| | |
| --- | --- |
| **Trigger** | User clicks Start or sends `/start` |
| **Typical use** | Welcome message, main menu, first-run setup |

It's not magic — just a normal command name that Telegram and users expect. Your welcome text goes in **Answer**; menus and logic go in **Keyboard** and **Logic**.

Tutorial: [Your First Bot](first-hello-bot.md).

---

## `@` — runs before everything

The **`@`** command runs automatically **before** any other matched command on **every** update.

| | |
| --- | --- |
| **Answer sent?** | No |
| **Logic runs?** | Yes |
| **Typical use** | Auth checks, rate limits, loading shared config |

It skips Answer and keyboard side effects — pure setup logic. If `@` throws, the matched command may not run. Use it for lightweight checks, not heavy API calls that slow every message.

---

## `!` — the error catcher

When **any** command's Logic throws a runtime error, the **`!`** command runs.

| | |
| --- | --- |
| **Answer sent?** | Yes (if configured) |
| **Logic runs?** | Yes |
| **Typical use** | Friendly fallback message, error logging, alerting you |

Without `!`, users might see a generic platform error. With it, you control the apology:

```js
// ! command Logic
Bot.sendMessage("Oops — something broke. Try /start to reset.")
```

---

## `@@` — runs after everything

The **`@@`** command runs **after** every command finishes — success or failure.

| | |
| --- | --- |
| **Answer sent?** | No |
| **Logic runs?** | Yes |
| **Typical use** | Analytics, metrics, cleanup |

Like `@`, it skips automatic Answer sends. Good for "increment message counter" or "log command name" without spamming the user.

---

## `*` — the catch-all

When **no other command** matches the incoming text, **`*`** runs.

| | |
| --- | --- |
| **Answer sent?** | Yes (if configured) |
| **Logic runs?** | Yes |
| **Typical use** | "I didn't understand that", help hints, default reply |

It's a safety net, not a primary feature. Put real logic in named commands; use `*` for graceful "huh?" responses.

Guide: [Using the Wildcard](using-wildcard.md).

---

## How they fit together

One update, one matched command — but the wrappers always run:

```
@  →  matched command (or *)  →  ! (on error)  →  @@
```

Full pipeline diagram: [Execution Flow](execution-flow.md).

---

## See also

- [Matching & Priority](matching-order.md) — when `*` wins
- [Dynamic Handlers](dynamic-commands.md) — `/handle_{update_type}` is a different kind of special
