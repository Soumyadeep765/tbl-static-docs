# User-Level Storage (`db.user`)

`db.user` stores data **unique to each user** interacting with the bot — profiles, balances, game progress, language preferences, and flow state.

| Property | Value |
| --- | --- |
| Scope | One user on one bot |
| Isolation | Each user-bot pair has separate data |
| Default context | Current bot + current `user.id` from the update |

## Methods

All [unified CRUD methods](unified-methods.md) and [advanced operations](advanced-operations.md) (`incr`, `decr`, `push`, `pull`, `mget`).

## Examples

### User balance

```js
let balance = await db.user.incr("credits", 10)
Bot.sendMessage(`New balance: ${balance} credits`)
```

### Save preference

```js
await db.user.set("language", "es")
let lang = await db.user.get("language", "en")
```

### Multi-step flow state

```js
await db.user.set("onboard_step", 2)
let step = await db.user.get("onboard_step", 0)

if (step === 2) {
  Bot.runCommand("/onboard_step3")
}
```

### Temporary data with TTL

```js
await db.user.set("otp_code", "482910", { ttl: 300, type: "string" })
```

### Admin: access another user's data

```js
let balance = await db.user.get("credits", 0, { user_id: 123456789 })

await db.user.set("credits", 0, { user_id: 123456789 })
await db.user.del("warned", { user_id: 123456789 })
```

### Object syntax

```js
let level = await db.user.get({
  key: "level",
  fallback: 1,
  user_id: 123456789
})

await db.user.set({
  key: "referrals",
  value: 12,
  ttl: 604800,
  type: "integer"
})
```

### History log with push/pull

```js
await db.user.push("visited_pages", "settings")
await db.user.pull("tags", "inactive")
let pages = await db.user.get("visited_pages", [])
```

### Batch read

```js
let profile = await db.user.mget(["language", "credits", "level"])
```

### List all keys for current user

```js
let all = await db.user.getAll({ limit: 30 })
```

### Delete one user's data

```js
await db.user.delAll({ user_id: 123456789 })
```

## Scoping rules

| Operation | Default scope | Override |
| --- | --- | --- |
| `get`, `has`, `mget` | Current user | `{ user_id }` in options |
| `set`, `del` | Current user | `{ user_id }` required for other users |
| `getAll` | Current user | `{ user_id }` in options |
| `delAll({ user_id })` | One user | Deletes all keys for that user |
| `delAll()` (no user_id) | Entire bot | Deletes **all user keys for every user** |

!!! warning "delAll without user_id"
    `db.user.delAll()` with no `user_id` wipes **all user data for the entire bot**. Use only in admin/reset commands.

## Common use cases

- Virtual currency and referral counts (`incr` / `decr`)
- Onboarding and wizard step tracking
- User preferences and settings
- Game state and inventory (`push` / `pull` for lists)
- Per-user cooldowns with TTL

## Important notes

- Replaces deprecated `User.set` / `User.get` — migrate to `db.user`
- `user_id` is auto-filled from the current update — no need to pass it for the active user
- `del` only accepts positional syntax: `db.user.del("key", { user_id })` — not `db.user.del({ key })`
- For bot-wide data, use [`db.bot`](bot.md)
- For cross-bot user bans, use [`db.global`](global.md) with keys like `banned:{user_id}`
