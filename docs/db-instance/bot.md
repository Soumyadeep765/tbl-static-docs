# Bot-Level Storage (`db.bot`)

Imagine a whiteboard every user in your bot can read — maintenance mode, cached API responses, feature flags, that sort of thing. That's `db.bot`. One key, one value, shared across your entire bot.

No per-user isolation here. If you store `"maintenance": true`, everyone sees maintenance mode. If that's not what you want, head over to [`db.user`](user.md).

---

## What is `db.bot`?

**`db.bot`** stores data **shared across all users** of the current bot — feature flags, cached API responses, bot-wide counters, and configuration.

| Property | Value |
| --- | --- |
| Scope | One bot (all users) |
| Isolation | Private to the bot — other bots can't read it unless you pass `bot_id` for a bot you own |
| Default context | Current bot (`bot.id`) |

---

## How to use it

Start with the basics — get, set, and check:

```js
await db.bot.set("maintenance", true)
let maintenance = await db.bot.get("maintenance", false)

if (maintenance) {
  return Bot.sendMessage(chat.id, "Bot is under maintenance. Back soon!")
}
```

Three things worth knowing upfront:

1. **Always `await`** — every `db` method is async.
2. **Check `{ ok }` on writes** — storage can fill up. The bot won't throw a tantrum; it'll return `{ ok: false, message }`.
3. **Secrets go in ENV vars** — not here. See [`process.env`](../globals/process.md).

---

## Methods

Inherits all [unified CRUD methods](unified-methods.md), plus one extra:

| Method | Description |
| --- | --- |
| `clearAllData(options?)` | Delete all bot + user async data for this bot |

Also supports [advanced operations](advanced-operations.md): `incr`, `decr`, `push`, `pull`, `mget`.

---

## Try it — copy-paste examples

### Maintenance mode

```js
let maintenance = await db.bot.get("maintenance_mode", false)

if (maintenance) {
  return Bot.sendMessage(chat.id, "Bot is under maintenance. Try again later.")
}
```

### Bot-wide counter

```js
let totalRuns = await db.bot.incr("total_commands_run", 1)
Bot.sendMessage(chat.id, "Commands run: " + totalRuns)
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

Own multiple bots? Target another with `bot_id`:

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
Bot.inspect("Deleted " + res.total_deleted + " records")
```

`clearAllData` is the nuclear option. Use it like you mean it.

---

## Common use cases

- Maintenance and feature flags
- Bot-wide analytics counters (`incr`)
- API response caching with TTL
- Shared configuration across all users
- Admin toggles and bot settings

---

## Where to store what

| Need | Use |
| --- | --- |
| Bot-wide settings, caches, flags | `db.bot` (this page) |
| Per-user scores, preferences, flow state | [`db.user`](user.md) |
| Data shared across multiple bots | [`db.global`](global.md) |
| API keys, tokens, secrets | Dashboard [ENV variables](../globals/process.md) |

---

## Important notes

- Replaces deprecated `Bot.set` / `Bot.get` (1 MB sync limit) — migrate to `db.bot`
- Always `await` and check `{ ok }` on writes
- For per-user data, use [`db.user`](user.md)
- For data shared across multiple bots, use [`db.global`](global.md)
