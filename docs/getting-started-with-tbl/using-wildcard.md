# Using the Wildcard (*) Command

No matter how many keyboards, buttons, and help menus you build, users will still send unexpected messages like `hello`, `who are you?`, or typos like `/sttart`. 

By default, sending an unknown command results in the bot ignoring it or showing a raw system message. The **wildcard command (`*`)** acts as a safety net to catch any messages that don't match your existing commands.

---

## How the Wildcard Works

The `*` command is a catch-all trigger. 

1. A user sends a message.
2. TBL searches all your defined commands and aliases.
3. If no command or alias matches, TBL runs your `*` command.

---

## Step 1: Create the Wildcard Command

Let's build a polite "I didn't get that" responder:
1. Open your bot dashboard and click **Add Command**.
2. **Command:** Type `*` (just a single asterisk).
3. **Answer:** Type your fallback response:
   ```text
   Hmm, I didn't quite catch that. 🤔 
   Type /start or use the buttons below to navigate!
   ```
4. **Keyboard:** (Optional) Add your main menu buttons (e.g. `Help, About`) to help them get back on track.
5. Click **Save Command**.

---

## Step 2: Test It!

1. Open Telegram and message your bot.
2. Send a valid command, like `/start`. Your `/start` greeting should run normally.
3. Now send something completely random, like `hello bot!`.
4. Your bot will execute the `*` command and reply: "Hmm, I didn't quite catch that..." along with your menu buttons.

---

## Best Practices for Wildcards

*   **Don't put core features in `*`**: The wildcard is meant as a friendly safety net or a router. Don't write your main bot logic here. Keep that in specific, named commands.
*   **Give clear navigation**: When the wildcard triggers, always tell the user how to get back to the main menu (like suggesting `/start` or showing reply keyboard buttons).
*   **Case Sensitivity Safety**: If you want to catch simple words like `help` without aliases, `*` will catch them. You can use JavaScript `if` conditions in the `*` command's Logic to inspect the input text (using the global `message` variable) and route it accordingly.

---

## Congratulations!

You have completed the TBL Hands-on Tutorial Series. You now know how to:
1. Create commands and static responses.
2. Build reply menus.
3. Map multiple buttons to single commands using Aliases.
4. Capture user text input step-by-step.
5. Build inline buttons and callback handlers.
6. Catch unknown messages with a wildcard handler.

To understand how these pieces execute in sequence, check out the Concept Guides:

➔ **[Execution Flow](execution-flow.md)**
