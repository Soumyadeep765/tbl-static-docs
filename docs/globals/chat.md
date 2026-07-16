# chat

Where the conversation is happening — DM, group, or channel.

## What is it?

**`chat`** is an object describing the current chat: private message, group, supergroup, or channel. It tells you *where* to send replies and *what kind* of place you're in.

Private chats feel like a hallway conversation. Groups feel like a party. Channels feel like a stage. `chat.type` tells you which one you're at.

## When would you use it?

You'll use `chat` in almost every command that sends a message:

- `Bot.sendMessage(...)` — the most common line in bot history
- Branch logic by chat type (DM vs group vs channel)
- Welcome new private chats (`just_created`)
- Check if you're in a public group (`username`) or a private one

Pair with [`user`](user.md) for *who* and `chat` for *where*.

---

## Try it

```js
// The line you'll write a thousand times
Bot.sendMessage("Hello from the bot!")

// Different vibes for different chat types
if (chat.chat_type === "private") {
  Bot.sendMessage("Thanks for messaging me directly!")
} else if (chat.chat_type === "supergroup") {
  Bot.sendMessage("Hello, group!")
}

// First time in a private chat?
if (chat.just_created) {
  Bot.sendMessage("Nice to meet you!")
}
```

---

## Fields

### Telegram fields

Standard [Telegram Chat](https://core.telegram.org/bots/api#chat) properties when present:

| Field | Type | Description |
| --- | --- | --- |
| `id` | `number` | Chat ID |
| `type` | `string` | `"private"`, `"group"`, `"supergroup"`, or `"channel"` |
| `title` | `string` | Group or channel title (groups/channels) |
| `username` | `string` | Public username (if set) |
| `first_name` | `string` | First name (private chats) |

### Bonus fields

| Field | Type | Description |
| --- | --- | --- |
| `chatid` | `number` | Alias for `id` |
| `chatId` | `number` | Alias for `id` |
| `chat_type` | `string` | Alias for `type` |
| `just_created` | `boolean` | `true` if first interaction (private chats) |
| `created_at` | `string \| null` | When the chat was first seen (private chats) |
| `last_interaction` | `string \| null` | Last interaction timestamp (private chats) |

### Example object

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

---

## When is `chat` available?

| Context | Value |
| --- | --- |
| Message, callback, or member update | Object with chat fields |
| Global webhook with no chat context | `null` |
| Some system-only updates | `null` |

---

## Good to know

- `chat` is either an **object** or **`null`** — check before accessing fields
- Use `chat.id` when calling [Bot](../bot-instance/index.md) or [Api](../api-instance/index.md)
- In private chats, `chat.id` often equals [`user`](user.md)`.id — but they're different concepts
