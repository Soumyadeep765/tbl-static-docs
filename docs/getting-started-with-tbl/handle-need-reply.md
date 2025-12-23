# Handling User Input with Need Reply

Now that your bot can respond to commands and keyboards, the next step is handling **user input**.

This is done using **Need Reply**, which allows a command to wait for the user’s next message before continuing.

## What is Need Reply?

`Need Reply` tells the bot to **pause and wait for the user’s next message**.

Instead of finishing immediately, the command stays active until the user replies.

This is useful when you need input like:

- A name
- A value
- A choice
- Any simple user response

## Simple Input Example

We will create a command that asks for the user’s name and replies using that input.

Command : `/input`

Answer : `Tell me your name 🙂`

Need Reply : true

Logic (TBL Code)
```js 
Bot.sendMessge("Your name is " + message)
```

## How This Works

Step by step:

- User sends `/input`
- The bot replies: “Tell me your name”
- Because `Need Reply` is enabled, the bot waits
- User sends their next message
- That message is captured
- The logic runs and replies using the input

The important rule is this:

**The next message is treated as input, not as a new command.**

## What `message` Means Here

For this beginner example:

- `message` refers only to the **text** sent by the user
- It does not handle media or other message types
- This keeps the bot simple and easy to understand

!!! note
    Advanced bots can handle all update types, but for learning purposes, `message` is treated as plain text here.

## How to Cancel Need Reply

Sometimes a user may change their mind or want to stop the input process.

To cancel `Need Reply`, the user can simply send **any valid existing command**.

For example:

- `/start`
- `Help`
- `About`

When a valid command is received:

- The waiting state is cleared
- `Need Reply` is cancelled
- Normal command matching resumes

!!! info
    Sending a valid command automatically cancels the active Need Reply state.

This makes it easy for users to escape input mode without getting stuck.

## Why This Is Important

Without a cancel option:

- Users can feel trapped
- Other commands stop working temporarily
- The bot feels broken

Allowing users to send a valid command keeps the bot safe and user-friendly.

## Good Practices for Need Reply

Follow these rules:

- Always explain what input you expect
- Keep reply flows short
- Allow users to cancel using `/start` or menu buttons
- Respond immediately after receiving input
- Avoid chaining many reply-based steps

!!! warning
    Leaving users in a reply-waiting state without clear instructions can block normal bot usage.

## Test the Cancel Behavior

To test cancellation:

- Send `/input`
- Instead of replying with text, send `/start`
- The bot should cancel the input flow and restart normally

If this works, your Need Reply handling is correct.

## What You Learned

With `Need Reply`, you now understand how to:

- Pause a command and wait for input
- Read simple text input using `message`
- Cancel input mode safely
- Build basic interactive flows

This is the foundation for setup wizards, forms, and guided user interactions.