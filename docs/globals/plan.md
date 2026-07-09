# plan

Your bot's subscription limits — timeouts, storage, and rate caps in one object.

## What is it?

**`plan`** is an object with the **resolved limits and features** for your bot's subscription tier. TeleBotHost uses these values internally to enforce timeouts, buffer sizes, and rate limits. You can read them too — handy for gating premium features or showing owners what they're working with.

It's the fine print, but readable. No lawyers required.

## When would you use it?

- Gate features behind premium (`plan.premium`)
- Show owners their current limits in an admin command
- Adjust bot behavior based on timeout or buffer size
- Warn users when they're on a plan with ads (`plan.ads`)

For raw subscription dates and tier strings, check [`owner.plan`](owner.md). For module input size limits that reference `buffer_size`, see [Modules](../modules/index.md#size-limits).

---

## Try it

```js
// Premium-only feature
if (!plan.premium) {
  return Bot.sendMessage(user.id, "This feature requires a Premium plan.")
}

// Show plan info to the owner
Bot.sendMessage(user.id,
  "Your plan: " + plan.name +
  " (" + (plan.timeout / 1000) + "s script timeout)"
)

// Respect buffer limits when parsing big files
Bot.inspect("Max input size: " + (plan.buffer_size / 1024) + " KB")
```

---

## Fields

| Field | Type | Description |
| --- | --- | --- |
| `name` | `string` | `"Free"`, `"Freemium"`, `"Premium"`, or `"Elite"` |
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

### Tier comparison

| Tier | Premium | Timeout | Buffer | Parallel | Max Sleep | Rate (min / day) |
| --- | --- | --- | --- | --- | --- | --- |
| **Free** | No | 15s | 512 KB | 10 | 10s | 15 / 5,000 |
| **Freemium** | No | 15s | 512 KB | 10 | 10s | 30 / 5,000 |
| **Premium** | Yes | 30s | 5 MB | 20 | 20s | 60 / 10,000 |
| **Elite** | Yes | 60s | 10 MB | 40 | 50s | 120 / 20,000 |

### Example object

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

---

## Good to know

- `plan` is read-only and frozen during command execution
- `timeout` and `buffer_size` are in milliseconds and bytes; `sleep` is in seconds
- Raw subscription dates live on [`owner.plan`](owner.md)
