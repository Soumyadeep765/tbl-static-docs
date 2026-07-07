# The `user` Variable

In TBL, `user` contains **information about the Telegram user** who triggered the current update.

## Properties

### Telegram fields

All standard [Telegram User](https://core.telegram.org/bots/api#user) fields are included when present:

| Field | Type | Description |
| --- | --- | --- |
| `id` | `number` | Telegram user ID |
| `is_bot` | `boolean` | Whether this user is a bot |
| `first_name` | `string` | User's first name |
| `last_name` | `string` | User's last name (may be empty) |
| `username` | `string` | Telegram @username (may be empty) |
| `language_code` | `string` | User's language code |
| `is_premium` | `boolean` | Whether the user has Telegram Premium |

### TBL-added fields

| Field | Type | Description |
| --- | --- | --- |
| `telegramid` | `number` | Alias for `id` |
| `premium` | `boolean` | Alias for `is_premium` |
| `full_name` | `string` | `first_name` + `last_name` combined |
| `just_created` | `boolean` | `true` if this is the user's first interaction (private chats) |
| `created_at` | `string \| null` | When the user first interacted (private chats) |
| `last_interaction` | `string \| null` | Last interaction timestamp (private chats) |

## Example

```json
{
  "id": 5723455420,
  "is_bot": false,
  "first_name": "Alice",
  "last_name": "Smith",
  "username": "alice_smith",
  "language_code": "en",
  "is_premium": true,
  "telegramid": 5723455420,
  "premium": true,
  "full_name": "Alice Smith",
  "just_created": false,
  "created_at": "2025-06-01T10:00:00.000Z",
  "last_interaction": "2025-07-07T08:30:00.000Z"
}
```

## When `user` Is Available

| Context | Value |
| --- | --- |
| User sent a message, callback, or inline query | Object with user fields |
| Global webhook with no user context | `null` |
| Channel post without a user | `null` |

## Usage Examples

```javascript
// Greet by name
Bot.sendMessage(chat.id, `Hello, ${user.first_name}!`)

// Welcome new users
if (user.just_created) {
  Bot.sendMessage(chat.id, 'Welcome! This is your first time here.')
}

// Check premium status
if (user.premium) {
  Bot.sendMessage(chat.id, 'Thanks for being a Telegram Premium user!')
}
```

## Important Notes

- `user` is either an **object** or **`null`** — always check before accessing fields
- It is read-only and exists only during the current command execution
- For per-user persistent data, use [`db.user`](../db-instance/user.md) (recommended) or the deprecated [User instance](../user-instance/index.md)
