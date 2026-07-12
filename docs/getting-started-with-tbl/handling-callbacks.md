# Handling Callbacks (Inline Buttons)

Reply keyboards sit below the text entry field. **Inline buttons**, on the other hand, sit directly inside the message bubble. Tapping an inline button doesn't send a normal chat message; instead, it triggers a **callback query** that runs code silently in the background.

This is perfect for "Yes / No" confirmations, pagination ("Next Page"), or toggle settings without cluttering the chat.

---

## Step 1: Send Inline Buttons in Logic

Unlike reply keyboards, inline keyboards must be generated programmatically inside the **Logic** field using `Api.sendMessage`.

Create a command named `/buttons` and paste this into its **Logic** field:

```js
await Api.sendMessage({
  chat_id: chat.id,
  text: "Choose your favorite fruit:",
  reply_markup: {
    inline_keyboard: [
      [
        { text: "🍎 Apple", callback_data: "pick_apple" },
        { text: "🍌 Banana", callback_data: "pick_banana" }
      ]
    ]
  }
});
```

*   `text` is what the user sees on the button.
*   `callback_data` is the hidden payload sent to your bot when clicked (maximum 64 bytes).

---

## Step 2: Create matching handler commands

When a user taps the "Apple" button, Telegram fires `pick_apple`. TBL treats this payload exactly like a command name!

Let's create two new commands to handle these button taps:

### Create the `pick_apple` command:
1. Click **Add Command**.
2. **Command:** Type `pick_apple` (matches `callback_data`).
3. **Logic:** Paste this code:
   ```js
   // 1. Tell Telegram to stop showing the button's loading spinner
   await Api.answerCallbackQuery({
     callback_query_id: update.callback_query.id,
     text: "You picked Apple!"
   });

   // 2. Edit the message to clean up the screen
   await Api.editMessageText({
     chat_id: chat.id,
     message_id: update.callback_query.message.message_id,
     text: "🍎 You selected Apple. Delicious!"
   });
   ```
4. Save the command.

### Create the `pick_banana` command:
1. Click **Add Command**.
2. **Command:** Type `pick_banana`.
3. **Logic:** Paste this code:
   ```js
   await Api.answerCallbackQuery({
     callback_query_id: update.callback_query.id,
     text: "You picked Banana!"
   });

   await Api.editMessageText({
     chat_id: chat.id,
     message_id: update.callback_query.message.message_id,
     text: "🍌 You selected Banana. Sweet choice!"
   });
   ```
4. Save the command.

---

## Two Golden Rules of Inline Buttons

### Rule 1: Always answer the callback!
When a user clicks an inline button, Telegram shows a loading spinner on that button. If you don't call `Api.answerCallbackQuery()`, the spinner will spin for up to 10 seconds. Always call it!

### Rule 2: Message variables change in callbacks
Because callbacks aren't standard text messages, the global variable `message` is `null`. Instead, use `update.callback_query` to fetch context:
*   `update.callback_query.id` ➔ Required to answer the callback query.
*   `update.callback_query.data` ➔ The button's `callback_data` payload.
*   `update.callback_query.message.message_id` ➔ The ID of the message bubble the buttons are attached to (required to edit the message).

---

## Test It!

1. Open Telegram and send `/buttons` to your bot.
2. Tap the **🍎 Apple** button.
3. The loading spinner will disappear, a quick popup (toast notification) saying "You picked Apple!" will show up, and the message text will edit itself to: "🍎 You selected Apple. Delicious!".

---

## What's Next?

We've covered structured commands and menus. But what happens if a user types something completely random like "skdfjldsf"? In the final step, we'll build a catch-all command!

➔ **[Wildcard Command (*)](using-wildcard.md)**
