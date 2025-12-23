# Commands in TBL

Commands are the foundation of how bots work in **TBL (Tele Bot Lang)**.  
Every action, response, or behavior in a TeleBotHost bot is driven by a command.

TBL does not rely on event listeners or long-running background processes.  
Instead, it follows a **command-driven execution model**, where each incoming update triggers exactly one command.

## What is a Command?

A command is a rule that defines what the bot should do when a specific trigger is matched.

For every incoming update:

- Telegram sends an update to the bot
- TBL inspects the update
- A matching command is selected
- That command is executed
- Execution ends cleanly

Only one command runs per update.

!!! info
    TBL never executes multiple commands automatically for a single update.

## Types of Command Triggers

### Slash Commands

Slash commands start with `/`, such as `/start`.

They are commonly used for:

- Entry points
- User onboarding
- Explicit user actions

### Text-Based Commands

Commands can also be triggered by plain text messages.

They are useful for:

- Menu-driven bots
- Keyword-based replies
- Conversational flows

Text-based commands behave exactly the same as slash commands.

### Button and Interaction Triggers

Commands may also be triggered by user interactions, such as:

- Reply keyboards
- Inline buttons
- Menu selections

These triggers help guide users and reduce manual typing.

### Inline Query Commands

Inline query commands handle Telegram inline mode, when users type  
`@yourbot query` inside any chat.

These commands are useful for:

- Search-style bots
- Inline tools
- Quick content insertion

Inline queries are handled by a dedicated command.

## Command Matching Order

TBL uses a strict and predictable matching order.

When an update arrives, commands are checked in this order:

- Exact command name
- Aliases
- Dynamic update handlers
- Fallback command

This ensures that specific logic always runs before generic logic.

!!! tip
    A strict matching order makes command behavior predictable and easier to debug.

## Command Parts

Each command can include multiple optional parts.  
These parts define how the command behaves.

### Command Name

The command name defines the trigger.

It can be:

- A slash command
- A keyword
- A system identifier

### Answer

An answer is a static message sent immediately when the command is triggered.

It is useful for:

- Quick responses
- Simple instructions
- Instant feedback

The answer is always sent before any command logic runs.

### Logic (Bot Main Codes)

The logic defines what the bot actually does after the command is triggered.

Typical responsibilities include:

- Sending messages
- Processing user input
- Calling external APIs
- Saving or reading data
- Triggering other commands

### Aliases

Aliases allow a command to be triggered using multiple names.

They are useful for:

- Handling typos
- Supporting multiple languages
- Creating shortcuts

All aliases behave exactly the same as the main command.

### Keyboard

Commands can optionally display keyboards.

Keyboards help:

- Reduce typing
- Guide user actions
- Improve user experience

They are shown only when explicitly defined.

### Need Reply

Some commands expect a follow-up message from the user.

When enabled:

- The bot waits for the next user message
- That message becomes the input
- The command flow continues

!!! warning
    Overusing reply-based commands can confuse users and make flows harder to manage.

## Built-in Special Commands

### /start — Entry Command

The `/start` command is the primary entry point for users.

It is typically used for:

- Welcoming users
- Explaining bot features
- Resetting user flow

While not mandatory, it is strongly recommended.

### @ — Initialization Command

The `@` command runs before any other command.

It is used for:

- Preparing global data
- Defining helper logic
- Setting shared configuration

!!! info
    The `@` command runs on every update and executes before command matching.

!!! tip
    This command has advanced use cases that will be covered later.

### ! — Error Handler Command

The `!` command runs when a runtime error occurs during command execution.

It is used for:

- Handling failures gracefully
- Sending error messages
- Preventing silent crashes

!!! alert
    Always define a `!` command to handle unexpected errors safely.

### @@ — Post-Processing Command

The `@@` command runs after every command execution, whether it succeeds or fails.

It is commonly used for:

- Cleanup tasks
- Logging
- Analytics
- Post-execution actions

### * — Fallback (Wildcard) Command

The `*` command runs when no other command matches.

It acts as:

- A default handler
- A safety net
- A universal fallback

!!! warning
    Not defining a fallback command may cause some updates to be ignored.

## Update-Specific Commands

### /inline_query — Inline Mode Handler

The `/inline_query` command handles inline queries triggered by users typing  
`@yourbot query` inside chats.

It is responsible for:

- Reading inline query input
- Returning inline results
- Powering search-style interactions

If `/inline_query` is not defined, inline updates fall back to the `*` command.

### /channel_update — Channel Post Handler

The `/channel_update` command handles channel-related updates automatically.

It is used for:

- Channel posts
- Channel edits
- Channel-related events

If this command is not defined, channel updates fall back to the `*` command.

## Dynamic Commands

TBL supports dynamic commands that handle specific Telegram update types automatically.

Dynamic commands follow a fixed naming pattern:

- `/handle_{update_type}`

Examples include:

- `/handle_channel_post`
- `/handle_chat_member`
- `/handle_poll_answer`
- `/handle_message_reaction`

These commands are triggered automatically when the corresponding Telegram update is received.

If a dynamic command is not defined:

- Channel-related updates fall back to `/channel_update`
- All other updates fall back to `*`

!!! info
    Dynamic commands remove the need for manual update parsing or event listeners.

## Final Command Execution Flow

Every update in TBL follows the same execution order:

- The update is received
- The `@` initialization command runs
- A matching command runs
- The `!` command runs only if an error occurs
- The `@@` command runs after execution
- Execution ends

Flow summary:

Update → @ → matched command → ! (on error) → @@ → end

## Good Practices

- Use clear and meaningful command names
- Keep one responsibility per command
- Always define `!` and `*`
- Use aliases thoughtfully
- Prefer dynamic commands for system updates
- Keep reply-based flows short and clear

## What to Avoid

Avoid:

- Overloading a single command with too much logic
- Creating deep or confusing reply chains
- Relying on fallback commands for core features
- Ignoring error handling
- Creating ambiguous or overlapping triggers

## Why This Model Works

TBL’s command system is intentionally focused and restricted.

This design:

- Improves security
- Prevents unexpected behavior
- Makes bots easier to understand
- Scales reliably under high traffic

Instead of managing events and listeners, developers define clear reactions to specific triggers, resulting in predictable and maintainable bots.