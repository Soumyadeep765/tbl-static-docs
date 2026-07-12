# Using Aliases in Your Bot

Having one command trigger name is clean, but users don't always do what you expect. If your keyboard button says `Help`, your users might type `/help`, `/h`, or `help` in lowercase.

Instead of copying and pasting the exact same answer and logic into four different commands, you can use **Aliases** to map all of these triggers to a single command.

---

## What is an Alias?

An alias is just an alternative trigger word for an existing command. 

```
/help (Main Command)
  ├── help (Alias)
  ├── HELP (Alias)
  └── /h   (Alias)
```

No matter which one the user types, the exact same command runs.

---

## Step 1: Open Your Command

Let's add aliases to the `Help` command we built in the last step:
1. Open your bot dashboard and click **Commands**.
2. Find your `Help` command and click **Edit** (pencil icon).

---

## Step 2: Add Aliases

1. Locate the **Aliases** field in the form.
2. Type the aliases you want to support, separated by commas:
   ```text
   help, HELP, /h
   ```
3. Click **Save Command**.

---

## Why are Aliases Awesome?

*   **Keyboard matching:** If your menu button text says `ℹ️ About Us`, you can name your command `about_us` internally, and simply add `ℹ️ About Us` as an alias.
*   **Catching Typos & Shorthands:** You can map shorthand forms (like `/h` for help, or `/q` for quit) to make life easier for power users.
*   **Case Sensitivity:** TBL commands are case-sensitive. If your command name is `Help`, typing `help` in lowercase won't work unless you add it as an alias.

---

## Test It!

1. Open Telegram and search for your bot.
2. Send the shorthand command `/h`.
3. Send the lowercase word `help`.
4. Send the capital word `HELP`.

If the bot responds with the same help message for all of them, your aliases are working perfectly!

---

## What's Next?

So far, our commands are "one-way"—the bot sends an answer and immediately stops. What if you need to ask the user a question (like "What is your name?") and wait for their answer before running code?

In the next step, we will use **Need Reply** to handle user input step-by-step.

➔ **[Handling User Input](handle-need-reply.md)**
