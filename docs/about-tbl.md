# What is TBL?

**TBL (Tele Bot Lang)** is the scripting language used by TeleBotHost to build and run Telegram bots.

It is made specifically for bot logic and avoids everything that is not needed for Telegram bots.

## What is TBL Used For?

TBL is used to handle everyday bot tasks like replying to messages, reacting to commands, processing user input, calling external APIs, and storing small pieces of data related to users or the bot itself.

It focuses only on what a Telegram bot needs to do and nothing more.

## How TBL Works

TBL follows a command-based execution model.

Instead of running event listeners or background processes, the bot reacts to incoming updates. When something happens on Telegram, TBL finds the matching command and runs its logic.

This makes bot behavior predictable and easy to understand.

## TBL Behavior

TBL is designed to be safe and controlled.

Each execution is isolated, runs for a short time, and then ends. There is no permanent process running in the background.

Because of this design, bots stay fast and stable even when many users interact at the same time.

## Execution Style

TBL runs only when needed.

A user sends a message, the bot handles it, and the execution finishes. Nothing keeps running after that unless a new update arrives.

This on-demand model keeps resource usage low and performance high.

## Asynchronous Behavior

TBL allows async operations where required, but avoids unnecessary complexity.

There are no long-running timers, uncontrolled loops, or hidden background tasks. Everything happens in a clear and predictable flow.

## Why TBL Feels Different

TBL is not trying to be a full programming language like Node.js or Python.

It is intentionally limited and focused. These limits help prevent common mistakes, improve security, and make bot development simpler.

Because of this, developers spend more time building bot logic and less time managing infrastructure.
