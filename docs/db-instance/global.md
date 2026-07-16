# Account-Level Storage (`db.global`)

Run three bots? Ban someone on one, block them everywhere. Share a maintenance flag across your whole network. That's `db.global` — storage at the **account** level, not the bot level.

Think of it as the owner's filing cabinet. Every bot under your account can reach in. Other people's bots cannot.

---

## What is `db.global`?

**`db.global`** stores data **shared across all bots** under the same owner account — cross-bot bans, shared balances, and account-wide configuration.

| Property | Value |
| --- | --- |
| Scope | Entire owner account |
| Isolation | Any bot on the account can read and write |
| Default context | Current owner's account |

---

## How to use it

Network-wide ban in three lines:

```js
let isBanned = await db.global.get("banned:" + user.id, false)

if (isBanned) {
  return Bot.sendMessage("Access denied across this network of bots.")
}
```

One syntax quirk — `set` is **positional only**:

```js
// Works
await db.global.set("lock", true, { ttl: 3600 })

// Does NOT work
await db.global.set({ key: "lock", value: true })
```

`get`, `has`, and `del` support object syntax for the key. `set` does not. The universe is cruel but consistent.

---

## Methods

All [unified CRUD methods](unified-methods.md) and [advanced operations](advanced-operations.md). Replaces the removed `Global` instance.

---

## Try it — copy-paste examples

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

---

## Key naming — avoid collisions

Use namespaced keys so your bots don't step on each other:

| Pattern | Example |
| --- | --- |
| `banned:{user_id}` | `banned:123456789` |
| `config:{name}` | `config:api_url` |
| `pool:{resource}` | `pool:referral_credits` |

A key called `"version"` shared by three bots is a recipe for confusion. Prefix it.

---

## Common use cases

- Unified ban lists across companion bots
- Shared virtual currency or referral pools
- Account-wide feature flags and maintenance mode
- Cross-bot analytics counters

---

## Where to store what

| Need | Use |
| --- | --- |
| Cross-bot bans, shared pools | `db.global` (this page) |
| One bot's settings and caches | [`db.bot`](bot.md) |
| Per-user data on one bot | [`db.user`](user.md) |
| API keys, tokens | Dashboard [ENV variables](../globals/process.md) |

---

## Important notes

- Replaces removed `Global.set` / `Global.get` — update old commands to `db.global`
- Use namespaced keys to avoid collisions: `banned:{user_id}`, `config:api_url`
- Store **secrets** in dashboard [ENV variables](../globals/process.md), not in `db.global`
- For data scoped to one bot only, use [`db.bot`](bot.md)
- For per-user data on one bot, use [`db.user`](user.md)
