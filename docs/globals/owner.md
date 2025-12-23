# The `owner` Variable

In TBL, `owner` contains **information about the bot owner**.

It provides details such as the owner’s email, subscription plan, and API keys used for platform-level integrations.

## What `owner` Contains

The `owner` variable is a **JSON object** that may include:

- Owner email address
- API keys (public and private)
- Subscription plan details
- Purchase and expiry dates

This information is useful for admin features, billing checks, and integrations.

## Demo Owner Object

Example structure of the `owner` object (values masked):

```json
{
  "mail": "owner@example.com",
  "api_keys": {
    "public": "pub-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "private": "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "generated_at": "2025-11-07T16:33:19.208Z"
  },
  "plan": {
    "tier": "ELITE",
    "purchase_at": "2025-11-21T14:06:37.815Z",
    "expiry_at": "2026-08-18T12:01:06.657Z"
  }
}
```

## Important Notes

- `owner` is read-only
- It exists only during command execution
- API keys should never be shared or exposed to users

The `owner` variable is mainly intended for **platform-level logic**, not normal user-facing bot behavior.
