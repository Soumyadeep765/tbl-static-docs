# Learning TBL

First things first: **TBL is just JavaScript**. It’s not a dialect, it's not a secret language, and it doesn't have custom syntax you need to memorize. If you drop standard JavaScript into the **Logic** field of a command, it will just work. 

What makes it fast is that all the annoying setup is already done for you. No importing libraries, no setting up servers, and no setting up database connections. 

---

## The Command Lifecycle

Every time a user interacts with your bot, they trigger a quick, single run of your code:

```
User Action ➔ Matches Command ➔ Sends Answer (Optional) ➔ Runs Logic ➔ Finished!
```

Think of it like a vending machine: a user presses a button (sends a command), the machine drops a snack (sends an answer and runs logic), and the machine goes back to resting. It does not sit there running and consuming power in between customers.

---

## Doing Things Step-by-Step (Sync vs. Async)

By default, your code runs line-by-line, in order:

```js
Bot.sendMessage(chat.id, "Line one");
Bot.sendMessage(chat.id, "Line two");
```

However, some actions take time to finish—like fetching data from another website or checking if a user is a member of a channel. When you need to wait for a line to finish before moving to the next one, use `await`:

```js
// We wait for the message to send, and store the reference to it
let sentMessage = await Api.sendMessage({ text: "Checking databases..." });

// Once it's sent, we edit the message text
await sentMessage.editText("All systems green!");
```

Only use `await` when you actually need the result of that line before moving forward. 

---

## Writing Your First Lines of Logic

To test this out, go to a command in your dashboard (like `/test`), scroll down to the **Logic** field, and paste this line:

```js
Bot.sendMessage(chat.id, "Hello from the Logic field!");
```

Save it, open your bot on Telegram, and send `/test`. The bot will respond with your message!

!!! tip "Where did chat.id come from?"
    `chat.id` is a built-in variable that automatically contains the ID of the chat where the message was sent. You don't have to define it—it's just there!

---

## What's in Your Toolbox?

Here are the built-in variables and helper objects that are always available in your commands:

| Variable | What it is | How to use it |
| --- | --- | --- |
| `Bot` | High-level bot helper | Great for everyday tasks like sending messages (`Bot.sendMessage()`) |
| `Api` | The full Telegram API | Use this when you want advanced features like keyboards or editing messages |
| `user` | The user who triggered the command | `user.username` gets their Telegram username; `user.first_name` gets their name |
| `chat` | The chat room where it happened | `chat.id` is where you send replies |
| `params` | Extra text sent after the command | If a user sends `/start promo123`, `params` will be `"promo123"` |
| `db` | Built-in database | Save and load data easily without setting up external servers |
| `modules` | Standard utilities | A box of popular tools (like Lodash, BCrypt, dayjs, Cheerio, and Zod) |
| `Libs` | Custom Telegram helpers | Ready-made tools for things like referral links or channel gates |

---

## What to Read Next

Ready to go deeper? Check these out:

*   **[Command Flow](getting-started-with-tbl/index.md)** — A detailed guide on how matching, execution, and keyboards work.
*   **[Your First Bot](getting-started-with-tbl/first-hello-bot.md)** — A complete, step-by-step tutorial for building a bot command.
*   **[Global Variables Reference](globals/index.md)** — The full list of everything you can use in your code.
