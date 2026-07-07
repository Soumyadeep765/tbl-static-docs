# Bot-Level Storage (`db.bot`)

`db.bot` stores data **shared across all users** of the current bot — feature flags, cached API responses, bot-wide counters, and configuration.

| Property | Value |
| --- | --- |
| Scope | One bot (all users) |
| Isolation | Private to the bot — other bots cannot read it unless you pass `bot_id` for a bot you own |
| Default context | Current bot (`bot.id`) |

## Methods

Inherits all [unified CRUD methods](unified-methods.md) plus:

| Method | Description |
| --- | --- |
| `clearAllData(options?)` | Delete all bot + user async data for this bot |

Also supports [advanced operations](advanced-operations.md): `incr`, `decr`, `push`, `pull`, `mget`.

## Examples

### Maintenance mode

```js
let maintenance = await db.bot.get("maintenance_mode", false)

if (maintenance) {
  return Bot.sendMessage("Bot is under maintenance. Try again later.")
}
```

### Bot-wide counter

```js
let totalRuns = await db.bot.incr("total_commands_run", 1)
Bot.sendMessage(`Commands run: ${totalRuns}`)
```

### Cached data with TTL

```js
await db.bot.set("promotions_cache", promoList, { ttl: 3600 })

let cached = await db.bot.get("promotions_cache", [])
```

### Feature flag

```js
await db.bot.set("new_ui_enabled", true)

if (await db.bot.has("new_ui_enabled")) {
  Bot.runCommand("/new_menu")
}
```

### Batch read

```js
let config = await db.bot.mget(["version", "maintenance", "max_items"])
let version = config.version || 1
```

### Paginated listing

```js
let page = await db.bot.getAll({ offset: 0, limit: 30 })
for (let [key, value] of Object.entries(page)) {
  Bot.inspect(key + ": " + value)
}
```

### Cross-bot access

If you own multiple bots, target another with `bot_id`:

```js
let flag = await db.bot.get("shared_flag", false, { bot_id: 99 })
await db.bot.set("synced_at", Date.now(), { bot_id: 99 })
```

Ownership is verified — you can only access bots on your account.

### Reset all bot data

```js
// Delete only bot-level keys
await db.bot.delAll()

// Delete bot-level AND all user-level async data
let res = await db.bot.clearAllData()
Bot.inspect(`Deleted ${res.total_deleted} records`)
```

## Common use cases

- Maintenance and feature flags
- Bot-wide analytics counters (`incr`)
- API response caching with TTL
- Shared configuration across all users
- Admin toggles and bot settings

## Important notes

- Replaces deprecated `Bot.set` / `Bot.get` (1 MB sync limit) — migrate to `db.bot`
- Always `await` and check `{ ok }` on writes
- For per-user data, use [`db.user`](user.md)
- For data shared across multiple bots, use [`db.global`](global.md)
- Secrets belong in dashboard [ENV variables](../globals/process.md), not `db.bot`
