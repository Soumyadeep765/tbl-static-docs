# Bot Properties (Deprecated)

Once upon a time, `Bot.set` and `Bot.get` were how you stored bot-wide data. They still work — but they're the flip phone of storage APIs. **`db.bot`** is the smartphone: bigger limits, confirmed writes, works in webhooks.

If you're starting fresh, skip this page and go straight to [Bot-Level Storage (`db.bot`)](../db-instance/bot.md). If you're maintaining legacy commands, read on — then migrate when you can.

---

## What's deprecated?

`Bot.set`, `Bot.get`, `Bot.del`, and all other `Bot.*` property methods are **deprecated**. They store key-value data shared across all users of the same bot.

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

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md).

---

## How to migrate

Three lines changed, one world of difference:

```js
// Deprecated
Bot.set("maintenance", true)
if (Bot.get("maintenance")) { ... }

// Recommended
await db.bot.set("maintenance", true)
if (await db.bot.get("maintenance", false)) { ... }
```

Counters got easier too:

```js
// Deprecated — race conditions waiting to happen
Bot.set("visits", (Bot.get("visits") || 0) + 1)

// Recommended — atomic increment
await db.bot.incr("visits", 1)
```

Full examples, TTL, and advanced ops: [Bot-Level Storage (`db.bot`)](../db-instance/bot.md).

---

## The 1 MB trap

Bot properties use a legacy sync backend with a **1 MB total cap per bot** (combined bot + user sync data). Hit the limit and writes fail with a storage error.

The cap applies to **serialized size** of all stored properties — not key count. Large objects, cached API responses, or user lists will fill it fast.

!!! danger "Do not use for large data"
    Never store big payloads, user lists, or API caches with `Bot.set`. Use [`db.bot`](../db-instance/bot.md) — limits scale with your [plan](../globals/plan.md).

---

## What to use where

**Use `db.bot` for:**

- Feature flags and maintenance modes
- Counters and analytics (`db.bot.incr`)
- Cached API responses with TTL
- Data you need in webhooks or webapps
- Anything that might grow over time

**Only keep `Bot.set` / `Bot.get` if:**

- Existing commands already use them
- You're doing a one-off sync read during migration

**Never use bot properties for:**

- Secrets or API keys — dashboard [ENV variables](../globals/process.md)
- Per-user data — [`db.user`](../db-instance/user.md)
- Account-wide data across bots — [`db.global`](../db-instance/global.md)
- Large or unbounded data — you'll hit 1 MB and cry

**Migration path:** Replace `Bot.set`/`get`/`del` with `await db.bot.set`/`get`/`del` one command at a time. Both can coexist during migration.

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

Writes return `{ success, key, bot_id, cached: true }` immediately — persistence happens asynchronously and may fail silently if the 1 MB limit is exceeded.

---

## Availability

Bot property methods are **not available** in webhook or webapp commands. Use [`db.bot`](../db-instance/bot.md) in those contexts.
