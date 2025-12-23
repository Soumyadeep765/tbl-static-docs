# Using Callback Commands with on_run

Sometimes you want to **continue execution in another command** after an Api call finishes.

TBL provides `on_run` for this purpose.

`on_run` lets you tell TBL **which command to run next** when an Api call completes.

## What is on_run?

`on_run` is an option you can pass to **any Api call**.

When the Api request finishes:

- The specified command is executed
- The response data is passed using [options]

This is useful for splitting logic into clean, separate commands.

## Why Use on_run?

Using `on_run` helps you:

- Keep commands small and readable
- Separate API calls from response handling
- Avoid long and complex command logic
- Reuse response-handling commands

Think of it as **“do this, then continue there”**.

## Basic Example

Calling an Api method and continuing in another command:

```js
// Get bot info and continue in another command
Api.getMe({
  on_run: "afterGetMe"
})
```

Here:

- `Api.getMe` calls Telegram
- When it finishes, the command `afterGetMe` is triggered automatically

## Handling the Callback Command

Inside the `afterGetMe` command, the Api response is available in `options`.

```js
// Inside "afterGetMe" command
if (options.ok) {
  Api.sendMessage({
    text: "Bot username: @" + options.result.username
  })
}
```

### What `options` Contains

In callback commands:

- `options.ok` → whether the Api call succeeded
- `options.result` → data returned by Telegram
- `options` structure depends on the Api method used

You don’t need to manually pass data — TBL does it automatically.

## How the Flow Works

Step by step:

- A command calls `Api.method({ on_run })`
- Telegram processes the request
- TBL receives the response
- The callback command is executed
- Response data is available via `options`

No polling, no waiting, no manual wiring.

## When to Use Callback Commands

Use `on_run` when:

- You need the result of an Api call
- You want to keep logic organized
- You want to continue execution cleanly
- One command depends on the result of another action

## Important Notes

- `on_run` must be a valid command name
- The callback command receives [options] automatically
- Callback commands run like normal commands
- Errors can still be handled using the `!` command

## Summary

- `on_run` lets you continue execution in another command
- It works with any Api call
- Response data is available via [options]
- Helps keep bot logic clean and modular

[options]: ../globals/options.md