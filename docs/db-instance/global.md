# Account-Level Storage (`db.global`)

`db.global` stores data **shared across all bots** under the same owner account — cross-bot bans, shared balances, and account-wide configuration.

| Property | Value |
| --- | --- |
| Scope | Entire owner account |
| Isolation | Any bot on the account can read and write |
| Default context | Current owner's account |

## Methods

All [unified CRUD methods](unified-methods.md) and [advanced operations](advanced-operations.md). Replaces the removed `Global` instance.

!!! note "Syntax difference"
    `db.global.set` accepts **positional syntax only**: `set(key, value, options)`. Object-form `set({ key, value })` is not supported. `get`, `has`, and `del` support object syntax for the key.

## Examples

### Network-wide ban

```js
let isBanned = await db.global.get("banned:" + user.id, false)

if (isBanned) {
  return Bot.sendMessage("Access denied across this network of bots.")
}

// Ban a user account-wide
await db.global.set("banned:" + user.id, true)
```

### Shared maintenance lock

```js
await db.global.set("global_maintenance", true, { ttl: 3600 })

if (await db.global.get("global_maintenance", false)) {
  Bot.sendMessage("All bots are in maintenance mode.")
}
```

### Cross-bot counter

```js
let total = await db.global.incr("network_visits", 1)
```

### Batch read

```js
let flags = await db.global.mget(["maintenance", "max_daily", "version"])
```

### List global keys

```js
let all = await db.global.getAll({ offset: 0, limit: 30 })
```

### Clear all global data

```js
await db.global.delAll()
```

## Common use cases

- Unified ban lists across companion bots
- Shared virtual currency or referral pools
- Account-wide feature flags and maintenance mode
- Cross-bot analytics counters

## Important notes

- Replaces removed `Global.set` / `Global.get` — update old commands to `db.global`
- Use namespaced keys to avoid collisions: `banned:{user_id}`, `config:api_url`
- Store **secrets** in dashboard [ENV variables](../globals/process.md), not in `db.global`
- For data scoped to one bot only, use [`db.bot`](bot.md)
- For per-user data on one bot, use [`db.user`](user.md)
