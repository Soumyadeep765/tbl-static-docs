# Database Storage (`db`)

The `db` instance is TBL's **modern asynchronous storage API**. Use it to persist bot-wide settings, per-user data, and account-level shared state across commands, webhooks, and webapps.

It replaces the removed legacy APIs:

| Legacy (removed / deprecated) | Use instead |
| --- | --- |
| `Global.set` / `Global.get` | `db.global` |
| `Bot.set` / `Bot.get` (1 MB sync cap) | `db.bot` |
| `User.set` / `User.get` | `db.user` |

`db` is available in every command as `TBL.db`. All methods are **async** — use `await`.

```js
await db.bot.set("maintenance", true)
let score = await db.user.get("score", 0)
```

## Collections

| Collection | Scope | Use for |
| --- | --- | --- |
| [`db.bot`](bot.md) | Current bot (all users) | Feature flags, caches, bot-wide counters |
| [`db.user`](user.md) | Current bot + user | Profiles, balances, flow state |
| [`db.global`](global.md) | Owner account (all bots) | Cross-bot bans, shared config |

## Top-level methods

| Method | Description |
| --- | --- |
| `db.getStorageStats()` | Account storage usage report |
| `db.getCollections()` | Returns `["user", "bot", "global"]` |

## Methods on every collection

Each collection (`db.bot`, `db.user`, `db.global`) supports:

| CRUD | Advanced |
| --- | --- |
| `get`, `set`, `has`, `del` | `incr`, `decr` |
| `mget`, `getAll`, `delAll` | `push`, `pull` |

`db.bot` also has `clearAllData()` — wipes all bot + user async data for a bot.

See [Unified Methods](unified-methods.md) for signatures and [Advanced Operations](advanced-operations.md) for counters and lists.

## Syntax styles

Most methods on `db.bot` and `db.user` accept **positional** or **object** syntax. `db.global` is mostly positional.

```js
// Positional
await db.bot.get("score", 0)
await db.user.set("level", 5, { ttl: 86400 })

// Object (bot and user only)
await db.user.get({ key: "level", fallback: 1, user_id: 123456789 })
await db.bot.set({ key: "flag", value: true, ttl: 3600 })

// Global — positional only for set
await db.global.set("lock", true, { ttl: 3600 })
await db.global.get("lock", false)
```

Not every method supports both forms — see [Unified Methods](unified-methods.md) for the full matrix.

## Key behavior

### Async and cached

Reads check **memory → Redis → MongoDB** (fastest first). Writes update memory and Redis immediately, then persist to MongoDB in the background.

### Delete on empty value

Passing `null`, `undefined`, or `""` to `set` **deletes** the key instead of storing it.

### Return shapes

| Operation | Success | Failure |
| --- | --- | --- |
| `get` | Value or `fallback` | Returns `fallback` (no throw) |
| `set`, `del`, `delAll` | `{ ok: true }` | `{ ok: false, message }` |
| `incr`, `decr`, `push`, `pull` | New value | **Throws** `Error` |
| `has` | `boolean` | `false` on error |
| `mget` | `{ key: value, ... }` | Missing keys omitted |

Always check `result.ok` after `set` and `del`:

```js
let res = await db.bot.set("big_payload", data)
if (!res.ok) {
  Bot.sendMessage("Storage full: " + res.message)
}
```

### TTL

Pass `{ ttl: seconds }` in the options argument:

| Constraint | Value |
| --- | --- |
| Minimum | 60 seconds (shorter values clamped up) |
| Maximum | 31,536,000 seconds (1 year) |
| Unit | Seconds |

```js
await db.bot.set("cache", data, { ttl: 3600 })  // expires in 1 hour
```

### Type casting

Types are auto-detected. Override with `{ type: "integer" }` (or `"string"`, `"boolean"`, `"array"`, `"object"`, `"number"`, `"date"`, `"binary"`, `"text"`).

Shorthand aliases: `str`, `int`, `num`, `bool`, `arr`, `obj`, `bin`, `txt`.

### Storage limits

Total async `db` storage per account is capped by your [plan](../globals/plan.md):

| Plan | Limit |
| --- | --- |
| Free / Freemium | 20 MB |
| Premium | 50 MB |
| Elite | 100 MB |

`plan.prop_limit.per_account` is in **megabytes**. Exceeding the limit returns `{ ok: false, message: "Storage limit exceeded" }`.

### Rate limiting

`db` methods are rate-limited to **10 calls per second** per command execution. Bursting above this throws a rate limit error.

### Pagination (`getAll`)

| Setting | Default | Maximum |
| --- | --- | --- |
| `limit` | 10 | 30 |
| `offset` | 0 | — |

```js
let page1 = await db.user.getAll({ offset: 0, limit: 30 })
let page2 = await db.user.getAll({ offset: 30, limit: 30 })
```

## Pages in this section

| Page | Covers |
| --- | --- |
| [Bot Storage (`db.bot`)](bot.md) | Bot-wide data, `clearAllData` |
| [User Storage (`db.user`)](user.md) | Per-user data, scoping |
| [Global Storage (`db.global`)](global.md) | Account-wide shared data |
| [Unified Methods](unified-methods.md) | All CRUD signatures and syntax matrix |
| [Advanced Operations](advanced-operations.md) | `incr`, `decr`, `push`, `pull`, `mget` |
| [Analytics & Stats](analytics.md) | `getStorageStats`, monitoring usage |

## Migration from legacy storage

```js
// Global (removed)
// Global.set("key", val)  →  await db.global.set("key", val)

// Bot properties (deprecated, 1 MB cap)
// Bot.set("key", val)     →  await db.bot.set("key", val)
// Bot.get("key")          →  await db.bot.get("key", null)

// User instance (deprecated)
// User.set("key", val)    →  await db.user.set("key", val)
```

Legacy sync storage and async `db` storage are separate systems. `getStorageStats()` tracks **async `db` only**.
