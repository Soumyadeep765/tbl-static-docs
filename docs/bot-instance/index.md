# Bot Instance

The **Bot instance** is used to control your bot directly.

It provides simple methods that help manage how your bot works inside commands.

## What Bot Is Used For

The Bot instance is commonly used to:

- Run other commands
- Send messages easily
- Control command flow
- Manage bot-level properties

It is designed to make command-based logic easier and cleaner.

## Availability

The Bot instance is always available inside every command.

You don’t need to create it or import it.

You can use it directly.

## Important Alert

!!! warning
    All **Bot instance methods are case-sensitive**.

    For example:
    - `Bot.runCommand()` ✅
    - `Bot.runcommand()` ❌

    Always use the correct method name and casing.

## How It Fits in TBL

TBL is command-driven.

The Bot instance helps you move between commands and organize bot behavior in a clear way.

It focuses on **bot logic**, not low-level details.
