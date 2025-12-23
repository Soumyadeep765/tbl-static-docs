# Using the Wildcard (*) Command

Now let’s build a bot that **always replies**, no matter what the user sends.

This is done using the **wildcard command (`*`)**.

## What is the * Command?

The `*` command is a **catch-all command**.

It runs when:

- No other command matches
- The input is unknown
- The user sends random text or commands

In simple words:

If nothing else matches, `*` runs.

## What We Are Building

We will create a bot that:

- Replies to any message
- Does not require specific commands
- Always sends the same answer

This is useful for simple auto-reply bots or fallback responses.

## Step 1 — Create the Command

Open your bot’s **Commands** section and add a new command.

Command : `*`  
Answer : `Hello 👋 I reply to everything you send!`

That’s it.  
No logic is required.

## How the * Command Works

When a user sends any message:

- TBL checks all defined commands
- If no command matches
- The `*` command is selected
- The answer is sent

This happens for:

- Normal text
- Unknown commands
- Random input
- All telegram update types

!!! tip
    `*` Command able to capture all types of telegram update 

## Example Behavior

With only the `*` command defined:

- User sends `Hi` → bot replies
- User sends `/test` → bot replies
- User sends anything → bot replies

The same answer is sent every time.

!!! info
    The `*` command only runs when no other command matches.

## * With Other Commands

If your bot also has a `/start` command:

- `/start` → `/start` command runs
- Anything else → `*` command runs

This makes `*` perfect as a fallback.

## Good Use Cases

Use the `*` command for:

- Default replies
- Unknown input handling
- Help prompts
- Maintenance messages

!!! warning
    Do not place important bot logic inside `*`.  
    Use it as a fallback, not a primary command.

## Test the Bot

- Open your bot in Telegram
- Send any message
- The bot should always reply

If it does, your wildcard command is working 🎉

## What You Learned

You now understand how:

- The `*` command works
- To build an always-replying bot
- To handle unknown input safely
- To use `*` as a fallback command
