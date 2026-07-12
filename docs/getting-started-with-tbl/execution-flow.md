# Execution Flow

Every time a user interacts with your bot, TBL executes your commands in a **fixed, predictable pipeline**. Understanding how this pipeline works will help you avoid bugs, duplicate messages, and state leakage.

---

## The Execution Pipeline

Here is the exact step-by-step path an update takes from start to finish:

```
Update Received 
   │
   ▼
1. Run `@` initialization (Code only — always runs first)
   │
   ▼
2. Run Matched Command (e.g. `/start` or `Help`)
   │  a. Send Answer and Keyboard (if configured)
   │  b. Run Logic code (if any)
   │
   ▼ (if an error occurs in Logic)
3. Run `!` error handler (if defined)
   │  a. Send Answer
   │  b. Run Logic
   │
   ▼
4. Run `@@` post-processor (Code only — always runs last)
   │
   ▼
Done!
```

---

## What is skipped on `@` and `@@`?

`@` and `@@` are special helper hooks. To prevent spamming your users with unwanted messages:
*   **No Auto-Replies:** TBL **always skips** the automatic sending of `Answer` and `Keyboard` fields for `@` and `@@`. 
*   **Pure Logic Hooks:** Only the **Logic** fields of `@` and `@@` are executed. They are designed for background setup (like authorization, database caching) and cleanup (like metrics, logging).

---

## Early Termination: Skipping Code with `return` in `@`

Because TBL packages the `@` (init), your main command, and the `@@` (post-processor) code into a single, top-level asynchronous function block, you can use a top-level `return;` statement inside `@` to exit the entire execution instantly!

If you trigger a `return;` inside `@`:
1. The execution stops immediately.
2. The matched command's Answer is **not** sent, and its Logic is **not** executed.
3. The `@@` post-processor is **not** run.

### Example: Authorization gate in `@`
```js
// Inside the Logic field of your `@` command:
if (user.id !== 123456789) {
  Bot.sendMessage(chat.id, "Access denied. You are not the admin.");
  return; // Exits the entire execution block immediately!
}
```

---

## Next Steps in Command Flow

Want to see how TBL decides which command to run? Let's check out how command matching and priority work:

➔ **[Matching & Priority](matching-order.md)**
