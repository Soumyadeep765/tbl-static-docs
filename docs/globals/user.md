# user

Who's talking to your bot right now.

## What is it?

**`user`** is an object with everything TeleBotHost knows about the Telegram account that triggered the current update — name, username, ID, premium status, and a few handy extras.

It's how you say "Hello, Alice!" instead of "Hello, person with numeric ID 5723455420!" Names are nicer. IDs are more reliable. Lucky you get both.

## When would you use it?

Almost always. Typical uses:

- Greet someone by [`first_name`](#telegram-fields)
- Check if they're new (`just_created`)
- Gate premium features (`premium` / `is_premium`)
- Store or look up per-user data via [`db.user`](../db-instance/user.md)
- Send a DM with `Bot.sendMessage(...)`

!!! warning "It can be null"
    `user` is `null` on global webhooks or system updates with no user context. Always check before accessing fields.

---

## Try it

```js
if (!user) {
  return Bot.sendMessage("Couldn't identify who sent this.")
}

// Greet by name
Bot.sendMessage("Hello, " + user.first_name + "!")

// Welcome first-timers
if (user.just_created) {
  Bot.sendMessage("Welcome! This is your first time here.")
}

// Premium shout-out
if (user.premium) {
  Bot.sendMessage("Thanks for being a Telegram Premium user!")
}
```

---

## Fields

### Telegram fields

Standard [Telegram User](https://core.telegram.org/bots/api#user) properties when present:

| Field | Type | Description |
| --- | --- | --- |
| `id` | `number` | Telegram user ID |
| `is_bot` | `boolean` | Whether this user is a bot |
| `first_name` | `string` | User's first name |
| `last_name` | `string` | User's last name (may be empty) |
| `username` | `string` | Telegram @username (may be empty) |
| `language_code` | `string` | User's language code |
| `is_premium` | `boolean` | Whether the user has Telegram Premium |

### Bonus fields

| Field | Type | Description |
| --- | --- | --- |
| `telegramid` | `number` | Alias for `id` |
| `premium` | `boolean` | Alias for `is_premium` |
| `full_name` | `string` | `first_name` + `last_name` combined |
| `just_created` | `boolean` | `true` if first interaction (private chats) |
| `created_at` | `string \| null` | First interaction timestamp (private chats) |
| `last_interaction` | `string \| null` | Last interaction timestamp (private chats) |

### Example object

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

---

## When is `user` available?

| Context | Value |
| --- | --- |
| Message, callback, or inline query | Object with user fields |
| Global webhook with no user context | `null` |
| Channel post without a user | `null` |

---

## Good to know

- `user` is read-only and exists only during command execution
- For **persistent** per-user data (scores, settings, inventory), use [`db.user`](../db-instance/user.md)
- Sending to a private chat? `user.id` and [`chat`](chat.md)`.id are often the same number
