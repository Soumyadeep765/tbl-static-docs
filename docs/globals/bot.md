# The `bot` Variable

In TBL, `bot` contains **information about the current bot** running the command. It provides the bot's identity, owner email, and platform status.

## Properties

| Field | Type | Description |
| --- | --- | --- |
| `id` | `number` | Internal bot ID on the platform |
| `bot_id` | `number` | Numeric Telegram bot ID |
| `first_name` | `string` | Bot display name |
| `username` | `string` | Telegram @username |
| `name` | `string` | Alias for `username` |
| `owner` | `string` | Owner email address |
| `status` | `string` | `"working"` when the bot is active, `"stopped"` otherwise |
| `created_at` | `string` | Bot creation timestamp |
| `updated_at` | `string` | Last update timestamp |

## Example

```json
{
  "id": 42,
  "bot_id": 987654321,
  "first_name": "DemoBot",
  "username": "demobot",
  "name": "demobot",
  "owner": "owner@example.com",
  "status": "working",
  "created_at": "2025-01-01T00:00:00.000Z",
  "updated_at": "2025-01-10T00:00:00.000Z"
}
```

## Usage Examples

```javascript
// Greet with the bot's display name
Bot.sendMessage(user.id, `Welcome! I'm ${bot.first_name}.`)

// Check if the bot is running
if (bot.status !== 'working') {
  Bot.sendMessage(user.id, 'Bot is currently offline.')
}

// Log bot identity for admin commands
Bot.inspect(`Bot @${bot.username} (ID ${bot.id})`)
```

## Important Notes

- `bot` is read-only and exists only during command execution
- It represents platform-level bot metadata, not Telegram update data
- The Telegram bot token is **not** exposed as a global variable — use the [Api instance](../api-instance/index.md) to call the Telegram API
