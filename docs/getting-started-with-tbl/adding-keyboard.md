# Adding a Keyboard to Your Bot

Now let’s improve our first bot by adding a **keyboard**.

Keyboards allow users to tap buttons instead of typing commands.  
This makes bots easier to use and more user-friendly.

## What We Are Building

We will update the `/start` command to:

- Send a welcome message
- Show buttons on the screen
- Let users choose what to do next

## What is a Keyboard?

A keyboard is a set of buttons shown below the message input field.

When a user taps a button, the button text is sent back to the bot as a normal message.

This means:

- No typing required
- Fewer mistakes
- Better user experience

## Step 1 — Open the Command

- Go to your bot panel on TeleBotHost
- Open the **Commands** section
- Find the existing `/start` command
- Click the pencil (edit) icon to update it

## Step 2 — Add the Keyboard

Update the command fields like this:

Command: `/start`

Answer:
`Hello 👋  
Choose one of the options below to continue.`

Keyboard : `Help, About`

This creates **two buttons in a single row**.

## Keyboard Layout Basics

Keyboards are simple to define using text.

- Buttons in the same row are separated by commas
- New rows are created using a new line
!!! warning
    A keyboard always requires an Answer.  
    Buttons cannot be sent without a message, so make sure the Answer field is filled whenever you use a keyboard.
Examples:

- `Yes,No` → one row with two buttons  
- `Yes\nNo` → two rows with one button each  
- `Yes,No\nBoth` → two rows, First row: Yes, No  , Second row: Both  

!!! tip
    You can mix rows and button counts freely to design your menu.

## How Keyboard Buttons Work

When a user taps a keyboard button:

- Telegram sends the button text as a message
- TBL treats it like normal text input
- A matching command can respond to it

For example, tapping `Help` sends the message `Help`.

## Creating the Help Command

Now let’s make the `Help` button actually do something.

Add a new command with these details:

Command : `Help`

Answer : 
`Here’s what I can help you with:  
- Use the buttons to navigate  
- Tap About to learn more about me  
- Send /start anytime to restart`

No logic is needed yet.

## Creating the About Command

Next, create the `About` command.

Add another command with:

Command : `About`

Answer :
`I’m a simple Telegram bot built using TBL on TeleBotHost.  
I use commands and keyboards to guide users easily.`

This gives users basic information about your bot.

## Why Keyboards Are Useful

Keyboards are great for:

- Menus
- Navigation
- Guided user flows
- Reducing confusion for new users

!!! tip
    Use keyboards for common actions instead of forcing users to remember commands.

## Test the Keyboard and Commands

- Open your bot in Telegram
- Send `/start`
- You should see the buttons
- Tap **Help** and **About**
- Each button should show its response

If everything works, your bot menu is complete 🎉

## What You Learned

With this update, you learned:

- How to add a keyboard to a command
- How keyboard buttons send text messages
- How to handle buttons using normal commands
- How to build a simple menu-based bot

## What’s Next

Next, you can:

- Add a **Back** button
- Create multi-level menus
- Combine keyboards with reply-based input
- Add logic to commands

Your bot is now interactive and user-friendly.