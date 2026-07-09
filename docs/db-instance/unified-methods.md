# Unified CRUD Methods

`db.bot`, `db.user`, and `db.global` all speak the same language — `get`, `set`, `has`, `del`, and friends. The method names match; the scoping rules differ. This page is the authoritative reference for every signature.

Before you memorize anything, pick your collection. Bot-wide? [`db.bot`](bot.md). Per-user? [`db.user`](user.md). Account-wide? [`db.global`](global.md).

---

## What methods are shared?

Every collection supports the same core CRUD operations:

| Method | What it does |
| --- | --- |
| `get` | Read a value (returns `fallback` if missing) |
| `set` | Store or update a value |
| `has` | Check if a key exists |
| `del` | Delete a single key |
| `mget` | Batch-read multiple keys |
| `getAll` | List keys (paginated) |
| `delAll` | Delete all keys in scope |

`db.bot` also has `clearAllData()` — see [below](#clearalldataoptions--bot-only).

---

## Syntax support matrix

Not every method accepts every call style. Check before you copy-paste:

| Method | `db.bot` | `db.user` | `db.global` |
| --- | --- | --- | --- |
| `get` | positional + object | positional + object | positional + object |
| `set` | positional + object | positional + object | **positional only** |
| `has` | positional + object | positional + object | positional + object |
| `del` | positional + object | **positional only** | positional only |
| `mget` | positional + object | positional only | positional only |
| `getAll` | optional object | optional object | optional object |
| `delAll` | optional object | optional object | no params |

Object syntax looks like `db.user.get({ key: "level", fallback: 1 })`. Positional looks like `db.user.get("level", 1)`. Same result, different handwriting.

---

## `get(key, fallback?, options?)`

Retrieve a value. Returns `fallback` if the key is missing or access is denied.

```js
// Bot — current bot
let score = await db.bot.get("score", 0)

// User — current user (auto-scoped)
let level = await db.user.get("level", 1)

// User — specific user (admin)
let balance = await db.user.get("credits", 0, { user_id: 123456789 })

// Object syntax (bot and user)
let lang = await db.user.get({ key: "language", fallback: "en", user_id: 123456789 })

// Global
let banned = await db.global.get("banned:" + user.id, false)
let flag = await db.global.get({ key: "maintenance", fallback: false })
```

### Options

| Option | Collections | Description |
| --- | --- | --- |
| `bot_id` | bot, user | Target a different bot you own |
| `user_id` | user | Target a specific user |

---

## `set(key, value, options?)`

Store or update a value. Pass `null`, `undefined`, or `""` to **delete** the key.

```js
// Simple set
await db.bot.set("maintenance", true)

// With TTL and type
await db.user.set("credits", 100, { ttl: 86400, type: "integer" })

// Object syntax (bot and user)
await db.bot.set({ key: "version", value: 2, ttl: 604800 })

// Global — positional only
await db.global.set("lock", true, { ttl: 3600, type: "boolean" })
```

### Options

| Option | Collections | Description |
| --- | --- | --- |
| `ttl` | all | Expiration in seconds (60 min – 1 year max) |
| `type` | all | Force type: `string`, `integer`, `boolean`, `array`, `object`, etc. |
| `bot_id` | bot, user | Target a different bot you own |
| `user_id` | user | **Required context** for writes to a specific user |

**Returns:** `{ ok: true }` or `{ ok: false, message }` — always check `ok`.

---

## `has(key, options?)`

Check if a key exists.

```js
let joined = await db.user.has("joined_date")
let exists = await db.bot.has({ key: "admin_locked" })
let globalFlag = await db.global.has("maintenance")
```

---

## `del(key, options?)`

Delete a single key.

```js
await db.bot.del("temp_token")
await db.bot.del({ key: "temp_token", bot_id: 42 })

// User — positional only
await db.user.del("draft")
await db.user.del("draft", { user_id: 123456789 })

// Global
await db.global.del("old_key")
```

**Returns:** `{ ok: true }` or `{ ok: false, message }`.

---

## `mget(keys, options?)`

Batch-read multiple keys in one call. Missing keys are **omitted** from the result (not set to `null`).

```js
let data = await db.bot.mget(["score", "level", "name"])
// { score: 10, level: 5 }  — "name" omitted if missing

// Bot object syntax
let props = await db.bot.mget({ keys: ["a", "b"], bot_id: 42 })

// User
let userData = await db.user.mget(["credits", "language"], { user_id: 123456789 })
```

---

## `getAll(options?)`

Return a key-value map. Paginated — default `limit: 10`, max `30`.

```js
// First page of current user's data
let data = await db.user.getAll()

// Paginated
let page = await db.user.getAll({ offset: 0, limit: 30 })

// All bot-level keys
let botData = await db.bot.getAll({ limit: 30 })

// Specific bot
let other = await db.bot.getAll({ bot_id: 42, offset: 0, limit: 30 })
```

### Options

| Option | Collections | Default | Max |
| --- | --- | --- | --- |
| `offset` | all | `0` | — |
| `limit` | all | `10` | `30` |
| `bot_id` | bot, user | current bot | — |
| `user_id` | user | current user | — |

`db.user.getAll` always returns data for **one user** (defaults to the current user).

---

## `delAll(options?)`

Delete all keys in the collection scope.

```js
// Delete all bot-level keys for current bot
await db.bot.delAll()

// Delete all keys for one user
await db.user.delAll({ user_id: 123456789 })

// Delete ALL user data for entire bot (all users) — use carefully
await db.user.delAll()

// Delete all global keys for the account
await db.global.delAll()
```

| Call | What it deletes |
| --- | --- |
| `db.bot.delAll()` | All **bot-level** keys for the current bot |
| `db.user.delAll({ user_id })` | All keys for **one user** |
| `db.user.delAll()` | All **user** keys for the **entire bot** (every user) |
| `db.global.delAll()` | All **global** keys for the account |

**Returns:** `{ ok: true }` or `{ ok: false, message }`.

---

## `clearAllData(options?)` — bot only

Nuclear option: deletes **all bot-level AND all user-level** async data for a bot.

```js
let res = await db.bot.clearAllData()
// { ok: true, bot_props_deleted: 12, user_props_deleted: 450, total_deleted: 462 }

// Another bot you own
await db.bot.clearAllData({ bot_id: 42 })
```

Does not affect `db.global` data. Use with extreme caution — there's no undo button.

---

## Quick reference

```js
// Typical bot command flow
let step = await db.user.get("onboard_step", 0)

if (step === 0) {
  await db.user.set("onboard_step", 1)
  Bot.sendMessage(chat.id, "Step 1 complete.")
}

// Check storage result
let res = await db.bot.set("cache", largeObject)
if (!res.ok) Bot.sendMessage(chat.id, res.message)
```

For counters and lists, see [Advanced Operations](advanced-operations.md).
