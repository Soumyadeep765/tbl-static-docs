# The `plan` Variable

In TBL, `plan` contains **subscription and feature details** of the bot owner’s plan.

It tells you what limits and features are available for the current bot.

## What `plan` Is Used For

The `plan` variable helps you:

- Check feature availability
- Respect usage limits
- Adjust behavior based on plan level

This is useful when building premium or restricted features.

## Demo Plan Object

Example structure of the `plan` object:

```json
{
  "name": "Elite",
  "premium": true,
  "ads": false,
  "prop_limit": {
    "per_account": 100
  },
  "timeout": 60000,
  "buffer_size": 10485760,
  "parallel_process": 40,
  "support_contact": true,
  "sleep": 50
}
```

## Important Notes

- `plan` is read-only
- It exists only during command execution
- Values depend on the user’s active subscription

The `plan` variable allows bots to scale features safely based on account limits.
