# The `plan` Variable

In TBL, `plan` contains the **resolved subscription limits and features** for the bot owner. TBL uses these values internally to enforce timeouts, buffer sizes, and rate limits — you can also read them to gate features in your bot logic.

## Properties

| Field | Type | Description |
| --- | --- | --- |
| `name` | `string` | Plan name: `"Free"`, `"Freemium"`, `"Premium"`, or `"Elite"` |
| `premium` | `boolean` | Whether the plan is a premium tier |
| `ads` | `boolean` | Whether ads are shown |
| `prop_limit.per_account` | `number` | Max storage properties per account |
| `timeout` | `number` | Max script runtime in **milliseconds** |
| `buffer_size` | `number` | Max Buffer allocation in **bytes** |
| `parallel_process` | `number` | Max concurrent Promise executions |
| `support_contact` | `boolean` | Support access enabled |
| `sleep` | `number` | Max total `sleep()` duration in **seconds** |
| `rate_limit.perMinute` | `number` | Web/webapp requests per minute |
| `rate_limit.perDay` | `number` | Web/webapp requests per day |

## Tier Comparison

| Tier | Premium | Timeout | Buffer | Parallel | Max Sleep | Rate (min / day) |
| --- | --- | --- | --- | --- | --- | --- |
| **Free** | No | 15s | 512 KB | 10 | 10s | 15 / 5,000 |
| **Freemium** | No | 15s | 512 KB | 10 | 10s | 30 / 5,000 |
| **Premium** | Yes | 30s | 5 MB | 20 | 20s | 60 / 10,000 |
| **Elite** | Yes | 60s | 10 MB | 40 | 50s | 120 / 20,000 |

## Example Object

```json
{
  "name": "Elite",
  "premium": true,
  "ads": false,
  "prop_limit": { "per_account": 100 },
  "timeout": 60000,
  "buffer_size": 10485760,
  "parallel_process": 40,
  "support_contact": true,
  "sleep": 50,
  "rate_limit": { "perMinute": 120, "perDay": 20000 }
}
```

## Usage

```javascript
// Gate a premium feature
if (!plan.premium) {
  return Bot.sendMessage(user.id, 'This feature requires a Premium plan.')
}

// Show plan info to the owner
if (user.id === owner.id) {
  Bot.sendMessage(user.id, `Your plan: ${plan.name} (${plan.timeout / 1000}s timeout)`)
}
```

## Important Notes

- `plan` is read-only and frozen during command execution
- `timeout` and `buffer_size` are in milliseconds and bytes respectively; `sleep` is in seconds
- Raw subscription dates are on [owner.plan](owner.md); resolved limits are on `plan`
