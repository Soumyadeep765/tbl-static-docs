# Bot Properties (Deprecated)

!!! warning "Deprecated API"
    `Bot.set`, `Bot.get`, `Bot.del`, and all other `Bot.*` property methods are **deprecated**.  
    Use [`db.bot`](../db-instance/bot.md) for all new bot-wide storage.

The legacy **Bot properties** API stores key-value data shared across all users of the same bot. It still works for existing commands, but has important limits and is not recommended for new development.

## Use `db.bot` instead

| | `Bot.set` / `Bot.get` (deprecated) | `db.bot` (recommended) |
| --- | --- | --- |
| Status | Legacy, maintained for compatibility | Current standard |
| Read | Sync (in-memory cache) | Async (`await`) |
| Write | Cache + background sync | Async with atomic operations |
| Size limit | **1 MB per bot** (hard cap) | Plan-based (up to 100 MB on Elite) |
| Increment | No | `await db.bot.incr(key, n)` |
| TTL | 4th argument to `set` | `{ ttl: seconds }` option |
| Analytics | No | `db.getStorageStats()` |
| Webhook / webapp | **Not available** | Available |
| Reliability | Fire-and-forget writes | Confirmed persistence |

### Quick migration

```js
// Deprecated
Bot.set("maintenance", true)
if (Bot.get("maintenance")) { ... }

// Recommended
await db.bot.set("maintenance", true)
if (await db.bot.get("maintenance", false)) { ... }
```

```js
// Deprecated counter
Bot.set("visits", (Bot.get("visits") || 0) + 1)

// Recommended
await db.bot.incr("visits", 1)
```

See [Bot-Level Storage (`db.bot`)](../db-instance/bot.md) for full examples, TTL, and advanced operations.

## 1 MB storage limit

Bot properties use the legacy sync storage backend, which enforces a **1 MB total cap per bot** (combined bot + user sync data). If a write would exceed this limit, it fails with a storage limit error.

This limit applies to the **serialized size** of all stored properties — not the number of keys. Large objects, cached API responses, or user lists will hit the cap quickly.

!!! danger "Do not use for large data"
    Never store big payloads, user lists, or API caches with `Bot.set`. Use [`db.bot`](../db-instance/bot.md) which supports much larger limits based on your [plan](../globals/plan.md).

## Recommendations

**Do use `db.bot` for:**

- Feature flags and maintenance modes
- Counters and analytics (`db.bot.incr`)
- Cached API responses with TTL
- Any data you need to rely on in webhooks or webapps
- Anything that may grow over time

**Only keep `Bot.set` / `Bot.get` if:**

- You have existing commands that already use them
- You need a quick sync read during a one-off migration

**Never use bot properties for:**

- Secrets or API keys — use dashboard [ENV variables](../globals/process.md)
- Per-user data — use [`db.user`](../db-instance/user.md) (not deprecated `User`)
- Account-wide data across multiple bots — use [`db.global`](../db-instance/global.md)
- Large or unbounded data — you will hit the 1 MB cap

**Migration path:** Replace `Bot.set`/`get`/`del` calls with `await db.bot.set`/`get`/`del` one command at a time. Both can coexist during migration.

---

## Legacy reference

The following methods still work but are deprecated. All have aliases (`setProp`, `getProp`, `delProp`, etc.).

| Method | Description |
| --- | --- |
| `Bot.set(key, value, type?, ttl?)` | Set a property |
| `Bot.get(key)` | Get a property (sync, from cache) |
| `Bot.del(key)` | Delete a property |
| `Bot.getAll()` | Get all properties |
| `Bot.delAll()` | Delete all properties |
| `Bot.has(key)` | Check if key exists |
| `Bot.count()` | Number of stored keys |
| `Bot.getNames()` | List all keys |

### Aliases

| Primary | Aliases |
| --- | --- |
| `Bot.set` | `setProp`, `setProperty` |
| `Bot.get` | `getProp`, `getProperty` |
| `Bot.del` | `delProp`, `delProperty` |
| `Bot.getAll` | `getAllProp`, `getAllProperty` |
| `Bot.delAll` | `delAllProp`, `delAllProperty` |
| `Bot.has` | `hasProp` |
| `Bot.count` | `countProps` |
| `Bot.getNames` | `getPropNames` |

### Legacy example

```js
Bot.set("flag", true)
let flag = Bot.get("flag")   // true
Bot.del("flag")
```

Writes return `{ success, key, bot_id, cached: true }` immediately — persistence to the database happens asynchronously and may fail silently if the 1 MB limit is exceeded.

## Availability

Bot property methods are **not available** in webhook or webapp commands. Use [`db.bot`](../db-instance/bot.md) in those contexts.
