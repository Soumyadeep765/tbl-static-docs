# Learning TBL

TBL (Tele Bot Lang) is basically **JavaScript**, with built-in features made for Telegram bots.

You write normal JavaScript logic, and TeleBotHost already gives you everything needed to talk to Telegram.

## How TBL Works

- TBL uses JavaScript syntax
- Telegram-related features are built in
- No imports or setup needed

## Sync and Async Behavior

TBL is mostly **synchronous**, so code runs line by line.

Some operations are **asynchronous**, and for those cases `await` and `Promise` are supported.

Only required async behavior is allowed, keeping bots safe and predictable.

## Simple TBL Example

A very simple example that sends a message:

```js
Bot.sendMessage("Hello from my first TBL bot!");
```

That’s all you need to start.

## What’s Next

After this, you can learn about variables, user input, and async requests to build real bot logic.
