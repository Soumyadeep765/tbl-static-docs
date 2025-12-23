# The `chat` Variable

In TBL, `chat` contains **details about the current chat** where the interaction happened.

This can be a **private chat**, **group**, or **channel**.

## What `chat` Contains

The `chat` variable is a **JSON object** that describes the chat context.

It may include information such as:

- Chat ID
- Chat type (private, group, channel)
- Chat username or title
- Block status
- Whether the chat was just created

## Demo Chat Object

Example structure of the `chat` object:

```json
{
  "id": 5723455420,
  "first_name": "Soumyadeep ∞",
  "username": "soumyadeepdas765",
  "type": "private",
  "chatid": 5723455420,
  "chatId": 5723455420,
  "blocked": false,
  "block_reason": null,
  "blocked_at": null,
  "just_created": true
}
```

## When `chat` Is Available

- For most message-based updates, `chat` is available
- For some system or webhook updates, it may be `null`

## Important Notes

- `chat` is either an **object or null**
- It is read-only
- It exists only during the current command execution

The `chat` variable helps your bot understand **where** the interaction is happening.
