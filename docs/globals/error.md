# The `error` Variable

In TBL, `error` contains **information about an error** that was caught by the `!` command.

It is only available when an error occurs during command execution.

## How `error` Works

- When a runtime error happens, the `!` command is triggered
- Inside the `!` command, `error` becomes available
- `error` describes what went wrong

This allows you to handle failures safely.

## What `error` Contains

The `error` variable is an **object** that may include:

- Error message
- Error type
- Stack information
- Execution details

## Important Notes

- `error` is available only inside the `!` command and HTTP call fallback command on error 
- It is read-only
- It exists only during error handling

The `error` variable helps you debug issues and show user-friendly error messages.
