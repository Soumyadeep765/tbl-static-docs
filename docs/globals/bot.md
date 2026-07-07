# bot

Your bot's identity card — name, username, and whether it's actually awake.

## What is it?

**`bot`** is an object with metadata about the bot running your command right now: its display name, Telegram username, platform ID, owner email, and current status.

It's the mirror your bot looks into. "Who am I? Am I online? Who built me?" All answered here.

## When would you use it?

- Show the bot's name in welcome messages
- Build admin panels that display bot info
- Check if the bot is running (`status === "working"`)
- Log identity in debug commands

This is **platform metadata**, not Telegram update data. For sending messages, you still use [Bot](../bot-instance/index.md) or [Api](../api-instance/index.md). The bot token is never exposed here — that's by design, not an oversight.

---

## Try it

```js
// Introduce yourself
Bot.sendMessage(user.id, "Welcome! I'm " + bot.first_name + ".")

// Health check
if (bot.status !== "working") {
  Bot.sendMessage(user.id, "Bot is currently offline. Try again later.")
}

// Admin debug
Bot.inspect("Running as @" + bot.username + " (ID " + bot.id + ")")
```

---

## Fields

| Field | Type | Description |
| --- | --- | --- |
| `id` | `number` | Internal bot ID on the platform |
| `bot_id` | `number` | Numeric Telegram bot ID |
| `first_name` | `string` | Bot display name |
| `username` | `string` | Telegram @username |
| `name` | `string` | Alias for `username` |
| `owner` | `string` | Owner email address |
| `status` | `string` | `"working"` when active, `"stopped"` otherwise |
| `created_at` | `string` | Bot creation timestamp |
| `updated_at` | `string` | Last update timestamp |

### Example object

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

---

## Good to know

- `bot` is read-only and exists only during command execution
- For owner account details (subscription, billing), see [`owner`](owner.md)
- For plan limits that affect your scripts, see [`plan`](plan.md)
