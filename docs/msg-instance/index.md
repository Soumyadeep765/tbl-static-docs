# msg Instance

The **msg instance** is used to interact with **Telegram messages** through methods like `msg.replyText()`, `msg.editText()`, and `msg.delete()`.

!!! note "Not the same as the global msg variable"
    This page documents the **msg instance** (message methods).  
    For the read-only global `msg` variable, see [msg (global)](../globals/msg.md).

It allows you to perform message-level actions such as:

- Send messages
- Reply to messages
- Edit messages
- Delete messages
- Forward or copy messages
- Add reactions
- Perform chat actions (like typing, upload, etc.)

All `msg` methods return **Promises**.

Using `await` is **optional** — it is required only when you need access to the response object for further actions.

The `msg` instance works only when a **message context exists**, meaning it is available in message-based updates.
