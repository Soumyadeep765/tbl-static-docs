# The `update_type` Variable

In TBL, `update_type` is a **string** that tells you **what kind of Telegram update** triggered the command.

It helps you understand the context of the incoming update.

## Example Values

Some common values of `update_type` include:

- `message`
- `chat_member`
- `channel_post`
- `poll`
- `message_reaction` 
 And more...

The value depends on the type of update received from Telegram.

## Important Notes

- `update_type` is read-only
- It exists only during command execution
- It matches Telegram update type names

## Learn More

For a full list of Telegram update types, see the official documentation:

https://core.telegram.org/bots/api#update
