# Command Execution

The Bot instance allows you to **execute another command programmatically**.

This is useful when you want to:

- Move a user to a new flow
- Reuse existing commands
- Control navigation inside your bot

These methods **do not return any value** — they only execute the target command.

## Running Another Command

You can run another command directly using `Bot.runCommand`.

### Basic Example

```js
// Run another command
Bot.runCommand("/start")
```

This immediately executes the `/start` command.

## Running a Command with Options

You can pass custom data to the target command.

```js
// Run with options

/* 
Bot.runCommnad("command", options)
*/

Bot.runCommand("/ok", { key: 111 })
```

Inside the `/ok` command, this data is available as [options]

## Options Availability

- The passed object is available as **[options]** in the target command
- You can pass any JSON-serializable data
- Useful for sharing state between commands

## Invalid Command Handling

If the target command **does not exist**:

- A runtime error is thrown
- The error can be caught using the `!` command
- Execution stops unless handled

!!! warning
    Running a non-existent command will throw an error  
    unless explicitly told not to.

## Advanced Command Execution

For more control, you can use `Bot.run()`.

This allows you to define execution behavior using an options object.

### Basic Usage

```js
Bot.run({
  command: "/contact"
})
```

## Available Parameters for Bot.run()

### command (required)

- The command to execute  
- Example: `/start`
- You can include parameters in the command string

### options

- A JSON object passed to the target command
- Available as `options` inside that command

### user_id

- User ID to execute the command for
- Default: current `user.id`

### chat_id

- Chat ID to execute the command in
- Default: current `chat.id`

### ignoreMissingCommand

- If `true`, no error is thrown when the command is not found
- Default: `false`

## Example with Full Options

```js
Bot.run({
  command: "/next",
  options: { step: 2 },
  user_id: 123456789,
  chat_id: 987654321,
  ignoreMissingCommand: true
})
```

## When to Use ignoreMissingCommand

This option is useful when:

- Running optional commands
- Building fallback logic
- Working with system commands like `@` or `*`

!!! tip
    Use `ignoreMissingCommand` carefully.  
    Silently skipping commands can make debugging harder.

## Summary

- `Bot.runCommand()` runs a command directly
- `Bot.run()` provides advanced control
- Options are passed through `options`
- Missing commands throw errors by default
- Errors can be handled using the `!` command

[options]: ../globals/options.md/#custom-data-example