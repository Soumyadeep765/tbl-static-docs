
Both **Bot** and **Api** are built-in objects available inside TBL commands.  
They are used for different purposes.

## Bot — Use Cases

Use **Bot** when you want to:

- Control command flow
- Move the user to another command
- Send simple messages or media
- Manage bot-level data
- Build step-by-step bot logic

Bot is focused on **how the bot behaves internally**.

## Api — Use Cases

Use **Api** when you want to:

- Communicate directly with Telegram
- Use advanced Telegram features
- Work with inline buttons, callbacks, or edits
- Call Telegram methods not provided by Bot
- Use newly released Telegram API features

Api is focused on **talking directly to Telegram**.

## Case Sensitivity

Both **Bot** and **Api** are **case-sensitive**.

This means method names must be written exactly as defined.  
Using incorrect casing will cause runtime errors.

Always use the correct capitalization when calling methods.

## Simple Rule

- Use **Bot** for bot logic and flow
- Use **Api** for Telegram-level operations
