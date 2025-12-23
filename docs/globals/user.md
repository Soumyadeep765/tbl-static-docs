# The `user` Variable

In TBL, `user` contains **information about the user** interacting with the bot.

It represents the Telegram user related to the current update.

## What `user` Contains

The `user` variable is a **JSON object** with details about the user.

## Demo User Object

Example structure of the `user` object:

```json
{
  "id": 5723455420,
  "is_bot": false,
  "first_name": "Soumyadeep ∞",
  "username": "soumyadeepdas765",
  "language_code": "en",
  "is_premium": true,
  "last_name": "",
  "telegramid": 5723455420,
  "premium": true,
  "blocked": false,
  "block_reason": null,
  "blocked_at": null,
  "just_created": false
}
```

## When `user` Is Available

- If the update comes from a **user interaction**, `user` is an object
- If the update does **not involve a user**, `user` can be `null`

## Important Notes

- `user` is either an **object or null**
- It is read-only
- It exists only during the current command execution
