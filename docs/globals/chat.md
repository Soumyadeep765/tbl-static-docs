# The `chat` Variable

In TBL, `chat` contains **details about the current chat** where the interaction happened — private, group, supergroup, or channel.

## Properties

### Telegram fields

All standard [Telegram Chat](https://core.telegram.org/bots/api#chat) fields are included when present:

| Field | Type | Description |
| --- | --- | --- |
| `id` | `number` | Chat ID |
| `type` | `string` | `"private"`, `"group"`, `"supergroup"`, or `"channel"` |
| `title` | `string` | Group or channel title (groups/channels) |
| `username` | `string` | Public username (if set) |
| `first_name` | `string` | First name (private chats) |

### TBL-added fields

| Field | Type | Description |
| --- | --- | --- |
| `chatid` | `number` | Alias for `id` |
| `chatId` | `number` | Alias for `id` |
| `chat_type` | `string` | Alias for `type` |
| `just_created` | `boolean` | `true` if this is the chat's first interaction (private chats) |
| `created_at` | `string \| null` | When the chat was first seen (private chats) |
| `last_interaction` | `string \| null` | Last interaction timestamp (private chats) |

## Example

```json
{
  "id": 5723455420,
  "type": "private",
  "first_name": "Alice",
  "username": "alice_smith",
  "chatid": 5723455420,
  "chatId": 5723455420,
  "chat_type": "private",
  "just_created": true,
  "created_at": "2025-07-07T08:30:00.000Z",
  "last_interaction": "2025-07-07T08:30:00.000Z"
}
```

## When `chat` Is Available

| Context | Value |
| --- | --- |
| Message, callback, or member update | Object with chat fields |
| Global webhook with no chat context | `null` |
| Some system-only updates | `null` |

## Usage Examples

```javascript
// Respond differently by chat type
if (chat.chat_type === 'private') {
  Bot.sendMessage(chat.id, 'Thanks for messaging me directly!')
} else if (chat.chat_type === 'supergroup') {
  Bot.sendMessage(chat.id, 'Hello group!')
}

// Welcome new private chats
if (chat.just_created) {
  Bot.sendMessage(chat.id, 'Nice to meet you!')
}
```

## Important Notes

- `chat` is either an **object** or **`null`** — always check before accessing fields
- It is read-only and exists only during the current command execution
- Use `chat.id` (or `chat.chatid`) when sending messages via [Api](../api-instance/index.md) or [Bot](../bot-instance/index.md)
