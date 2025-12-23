# The `bot` Variable

In TBL, `bot` contains **information about the current bot** running the command.

It provides details about the bot’s identity, owner, and platform status.

## What `bot` Contains

The `bot` variable is a **JSON object** with platform-level information about the bot.

It may include:

- Internal bot ID on TeleBotHost
- Telegram bot ID
- Bot name
- Owner information
- Bot status
- Creation and update timestamps

## Demo Bot Object

Example structure of the `bot` object:

```json
{
  "id": 42,
  "token": "123456:ABC...",
  "name": "DemoBot",
  "bot_id": 987654321,
  "owner": "somemail@telebothost.com",
  "status": "working",
  "created_at": "2025-01-01",
  "updated_at": "2025-01-10"
}
```

## Important Notes

- `bot` is read-only
- It exists only during command execution
- It represents platform-level information, not Telegram updates

The `bot` variable is useful for admin tools, logging, and bot management logic.
