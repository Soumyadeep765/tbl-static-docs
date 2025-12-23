# The `update` Variable

In TBL, `update` is a **JSON object** that contains the Telegram update which triggered the command.

It is the raw data sent by Telegram for every interaction.

## What It Contains

The `update` JSON may include:

- Message data
- User information
- Chat details
- Update type information

The exact fields depend on what kind of update was received.

## Important Notes

- `update` is read-only
- It exists only during the current command execution
- It represents the original Telegram payload

## Learn More

To understand the full structure of Telegram update JSON, see the official Telegram documentation:

https://core.telegram.org/bots/api#update
