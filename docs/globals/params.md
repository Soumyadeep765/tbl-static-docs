# The `params` Variable

In TBL, `params` contains the **extra text sent after a command**.

It is useful when a command needs simple arguments or input.

## How `params` Works

If a user sends:

`/start hello`

Then:

- Command → `/start`
- Params → `hello`

So the value of `params` will be:

"hello"

## Important Notes

- `params` contains text only
- It may be an empty string if no extra text is provided
- It exists only during command execution

`params` is a simple way to pass arguments to commands without using reply-based input.
