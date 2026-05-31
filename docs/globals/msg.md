# The `msg` Variable

In TBL, `msg` is a **simplified version of `update`** that is available **only for message updates**.

It is designed to make working with normal messages easier.

!!! note "Not the same as the msg instance"
    This page documents the **global `msg` variable** (read-only message context).  
    For message-sending methods like `msg.replyText()`, see the [msg instance](../msg-instance/index.md).

## How `msg` Works

- When the update type is a **message**, `msg` is available
- `msg` contains the **same object as `update.message`**
- If the update is **not a message**, `msg` is not available

This means you don’t need to access the full `update` object for common message-based bots.

## Important Notes

- `msg` is available only for message updates
- It is read-only
- It exists only during command execution

For simple bots that mainly handle messages, `msg` is often more convenient than using `update.message` directly.
