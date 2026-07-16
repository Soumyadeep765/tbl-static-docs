# owner

The human behind the bot — account info and subscription details.

## What is it?

**`owner`** is an object describing the account that created and manages this bot on the platform: email, account ID, and raw subscription data.

Think of it as the bot's boss. Your users talk to the bot; the owner pays the bills and sets the ENV variables.

## When would you use it?

**Admin and owner-only features** — not everyday user-facing logic:

- Owner-only commands (check `user.id` against owner, or gate by email)
- Subscription tier checks via `owner.plan.tier`
- Billing reminders or upgrade nudges
- Error notifications to the owner (pair with [`error`](error.md))

For script-friendly plan limits (timeouts, buffer sizes, rate limits), use [`plan`](plan.md) instead — it's the resolved, ready-to-use version.

!!! tip "Secrets live elsewhere"
    API keys and credentials are **not** in `owner`. Store them in dashboard ENV settings and read them via [`process.env`](process.md).

---

## Try it

```js
// Nudge free-tier owners
if (owner.plan.tier === "FREE") {
  Bot.sendMessage("Upgrade your plan for more features!")
}

// Use resolved limits for feature gating
if (plan.premium) {
  Bot.sendMessage("Premium features are enabled on this bot.")
}

// Alert the owner on errors (in your ! handler)
Bot.sendMessage(owner.mail, "Something broke: " + error.message)
```

---

## Fields

| Field | Type | Description |
| --- | --- | --- |
| `mail` | `string` | Owner email address |
| `id` | `string` | Owner account ID |
| `plan` | `Object` | Raw subscription record (`tier`, `purchase_at`, `expiry_at`) |

### Example object

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

---

## `owner.plan` vs `plan`

| | `owner.plan` | [`plan`](plan.md) |
| --- | --- | --- |
| What | Raw subscription record from the database | Resolved limits and features |
| Best for | Tier name, expiry dates | Timeouts, buffer sizes, rate limits |
| Example | `owner.plan.tier === "ELITE"` | `plan.timeout`, `plan.buffer_size` |

---

## Good to know

- `owner` is read-only and exists only during command execution
- Don't use `owner` for normal user-facing bot behavior — your users aren't the owner
- Full plan comparison table: [`plan`](plan.md)
