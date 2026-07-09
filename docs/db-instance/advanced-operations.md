# Advanced Operations

Basic CRUD gets you storage. Counters, lists, and batch reads get you *useful* storage — without hand-rolling read-modify-write loops that race under load.

All three collections (`db.bot`, `db.user`, `db.global`) support these operations. They're all `async` and accept an optional `options` object for scoping (`bot_id`, `user_id`, `ttl`, `type`).

---

## What can you do beyond CRUD?

| Category | Methods | Best for |
| --- | --- | --- |
| Counters | `incr`, `decr` | Credits, lives, visit counts |
| Lists | `push`, `pull` | History logs, tag lists, achievements |
| Batch read | `mget` | Loading a profile in one call |

For plain get/set/has/del, see [Unified Methods](unified-methods.md).

---

## Counters

### `incr(key, amount?, options?)`

Increment a numeric value. Missing keys start at `0`.

```js
let balance = await db.user.incr("credits", 10)
let visits = await db.bot.incr("page_views")        // +1 default
let network = await db.global.incr("total_signups", 1)
```

**Returns:** the new number.

**Throws:** `Error` if the underlying `set` fails (e.g. storage limit exceeded).

### `decr(key, amount?, options?)`

Decrement a numeric value. Same behavior as `incr` with a negative amount.

```js
let remaining = await db.user.decr("lives", 1)
let pool = await db.bot.decr("credits_pool", 5)
```

!!! note "Concurrency"
    `incr` and `decr` use read-modify-write (get → add → set) with a pending-write flush. They're safe for typical bot workloads but not Redis-atomic under extreme concurrent writes to the same key. If two users hammer the same key at the exact same millisecond, one might win. For most bots, that's fine.

---

## List operations

### `push(key, value, options?)`

Append a value to an array. If the current value is not an array, it is wrapped first.

```js
await db.user.push("history", "settings_page")
// ["settings_page"]

await db.user.push("history", "profile_page")
// ["settings_page", "profile_page"]
```

**Returns:** the updated array. **Throws** on failure.

### `pull(key, value, options?)`

Remove all occurrences of `value` from an array (strict equality `===`).

```js
await db.bot.pull("tags", "beta")
await db.user.pull("achievements", "first_login")
```

If the current value is not an array, returns it unchanged. **Throws** on failure.

---

## Batch read

### `mget(keys, options?)`

Read multiple keys in one call. More efficient than separate `get` calls.

```js
let data = await db.user.mget(["credits", "level", "language"])

let credits = data.credits ?? 0
let level = data.level ?? 1
```

**Returns:** `{ key: value, ... }` — keys that don't exist are **omitted** (not `null`).

```js
// Bot supports object syntax for keys
let props = await db.bot.mget({ keys: ["a", "b", "c"] })
```

There is no `mset` — write keys individually with `set`. One day, maybe. Today, loop.

---

## Options by collection

| Option | `db.bot` | `db.user` | `db.global` |
| --- | --- | --- | --- |
| `bot_id` | ✓ | ✓ | — |
| `user_id` | — | ✓ | — |
| `ttl` | ✓ (via set) | ✓ (via set) | ✓ (via set) |
| `type` | ✓ (via set) | ✓ (via set) | ✓ (via set) |

---

## Try it — copy-paste examples

### Reward system

```js
let cost = 50
let balance = await db.user.get("credits", 0)

if (balance < cost) {
  return Bot.sendMessage(chat.id, "Not enough credits.")
}

await db.user.decr("credits", cost)
await db.user.push("purchases", "item_sword")
Bot.sendMessage(chat.id, "Purchased!")
```

### Tag management

```js
await db.bot.push("active_features", "dark_mode")

if (params === "remove_dark_mode") {
  await db.bot.pull("active_features", "dark_mode")
}

let features = await db.bot.get("active_features", [])
```

### Leaderboard counter

```js
let score = await db.user.incr("weekly_score", 10)
let highScore = await db.bot.get("high_score", 0)

if (score > highScore) {
  await db.bot.set("high_score", score)
  Bot.sendMessage(chat.id, "New high score!")
}
```

---

## Error handling — two personalities

| Operation | On failure |
| --- | --- |
| `set`, `del`, `delAll` | Returns `{ ok: false, message }` — no throw |
| `incr`, `decr`, `push`, `pull` | **Throws** `Error` |

Wrap advanced ops in try/catch, or use the `!` error handler. Don't mix up the patterns.

---

## Important notes

- `incr` / `decr` / `push` / `pull` **throw** on failure — wrap in try/catch or use the `!` handler
- `set` / `del` return `{ ok: false }` instead of throwing — different error pattern
- All operations count toward the **10 calls/second** rate limit
- See [Unified Methods](unified-methods.md) for CRUD and [Analytics](analytics.md) for storage monitoring
