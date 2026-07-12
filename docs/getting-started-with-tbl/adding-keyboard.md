# Adding a Keyboard to Your Bot

Typing out commands is fine for developers, but regular users would much rather tap buttons. **Reply keyboards** put buttons right below the message input box. When a user taps a button, Telegram sends that text as a message automatically.

In this tutorial, we will upgrade the `/start` command you built in the last step into a mini navigation menu!

---

## What We Are Building

We will modify `/start` so that:

1. It sends a message asking the user to choose an option.
2. It shows two buttons: **Help** and **About**.
3. We will create two new commands that respond when the user taps those buttons.

---

## Step 1: Add Buttons to `/start`

Let's configure the keyboard layout:

1. Open your bot dashboard and click **Edit** (pencil icon) next to your `/start` command.
2. Find the **Keyboard** field.
3. Type the button labels separated by a comma:
   ```text
   Help, About
   ```
4. Click **Save Command**.

Now, when someone sends `/start`, they will see **Help** and **About** buttons sitting side-by-side in a single row.

---

## Keyboard Layout Rules

Arranging your buttons is super simple. You just type text with these rules:

*   **Buttons on the same row:** Separate them with a comma `,` (e.g., `Yes, No` ➔ Row 1: `Yes` | `No`)
*   **Buttons on a new row:** Separate them with a newline `\n` or a line break (e.g., `Yes\nNo` ➔ Row 1: `Yes`, Row 2: `No`)
*   **Mix it up:** `Yes, No\nCancel` ➔ Row 1: `Yes` | `No`, Row 2: `Cancel`.

---

## Step 2: Make the Buttons Work

Right now, if you tap the **Help** button, Telegram will send the text `Help` to the chat, but nothing will happen because your bot doesn't know what `Help` means yet.

Let's create the handler commands:

### Create the `Help` Command:

1. Click **Add Command**.
2. **Command:** Type `Help` (Note: Capitalization matters! `Help` is not the same as `help`).
3. **Answer:** Type your help message:
   ```text
   Here is what I can do:
   - Tap About to read more about me.
   - Send /start to reload the main menu.
   ```
4. Save the command.

### Create the `About` Command:

1. Click **Add Command**.
2. **Command:** Type `About`.
3. **Answer:** Type your description:
   ```text
   I am a helpful bot running on TeleBotHost. I'm built entirely on JavaScript!
   ```
4. Save the command.

---

## Step 3: Test It!

1. Open your bot in Telegram and send `/start`. The menu buttons should pop up at the bottom of your screen.
2. Tap **Help**. Your bot should reply with your help message.
3. Tap **About**. Your bot should reply with your about description.

If a button doesn't do anything, double-check that the command name in your dashboard matches the button label exactly (character for character!).

---

## What's Next?

If you have multiple buttons that should lead to the same command (like `Help`, `help`, and `/help`), you don't need to duplicate your code. In the next step, we will look at using **Aliases** to map multiple triggers to a single command.

➔ **[Using Aliases](adding-aliases.md)**
