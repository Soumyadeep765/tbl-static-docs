# The `owner` Variable

In TBL, `owner` contains **information about the bot owner** — the account that created and manages the bot on the platform.

## Properties

| Field | Type | Description |
| --- | --- | --- |
| `mail` | `string` | Owner email address |
| `id` | `string` | Owner account ID |
| `plan` | `Object` | Raw subscription record from the database (includes `tier`, `purchase_at`, `expiry_at`) |

The resolved, script-friendly limits are available separately on the [plan](plan.md) global.

## Example

```json
{
  "mail": "owner@example.com",
  "id": "507f1f77bcf86cd799439011",
  "plan": {
    "tier": "ELITE",
    "purchase_at": "2025-11-21T14:06:37.815Z",
    "expiry_at": "2026-08-18T12:01:06.657Z"
  }
}
```

## Usage Examples

```javascript
// Check subscription tier from raw plan data
if (owner.plan.tier === 'FREE') {
  Bot.sendMessage(user.id, 'Upgrade your plan for more features!')
}

// Use resolved limits from the plan global
if (plan.premium) {
  Bot.sendMessage(user.id, 'Premium features are enabled.')
}
```

## Important Notes

- `owner` is read-only and exists only during command execution
- API keys and platform credentials are **not** available in command scripts — manage secrets through dashboard [environment variables](process.md) instead
- Use `owner` for admin logic, billing checks, and owner-only features — not for normal user-facing bot behavior
