# Advanced User Operations & Migration

Legacy **`User`** helpers and migration to [`db.user`](../db-instance/user.md).

!!! warning "Deprecated — current user only"
    `User` does **not** support cross-user operations. Use `db.user` with `{ user_id }` for admin or multi-user logic.

---

## Object syntax for `set` / `del`

For the **current user** only:

```js
User.set({
  key: "credits",
  value: 100,
  type: "integer",
  ttl: 86400
})

User.del({ key: "warned" })
```

| Field | Description |
| --- | --- |
| `key` | Storage key |
| `value` | Value to store (`set` only) |
| `type` | Optional type hint |
| `ttl` | Optional seconds until expiry |

Do **not** pass `user_id` — not supported on `User`. Use `db.user` instead.

**`db.user` equivalent (including other users):**

```js
await db.user.set({
  key: "credits",
  value: 100,
  type: "integer",
  ttl: 86400,
  user_id: 123456789
})

await db.user.del("warned", { user_id: 123456789 })
```

---

## Cross-user access

**Not supported on `User`.** The legacy API only loads storage for the user who triggered the update.

For admin commands, lookups, or writing another user's data:

```js
// Read another user
let level = await db.user.get("level", 0, { user_id: 123456789 })

// Write another user
await db.user.set("credits", 0, { user_id: 123456789 })

// List another user's keys
let data = await db.user.getAll({ user_id: 123456789, limit: 50 })

// Reset another user
await db.user.delAll({ user_id: 123456789 })
```

See [`db.user`](../db-instance/user.md) scoping rules.

---

## `User.batchSet(properties)`

Set multiple keys at once for the **current user** (fire-and-forget persistence).

```js
User.batchSet({
  language: "en",
  theme: "dark",
  onboarded: true
})
```

**`db.user` equivalent:**

```js
await db.user.set("language", "en")
await db.user.set("theme", "dark")
await db.user.set("onboarded", true)
```

---

## `User.refresh()`

Reload the **current user's** props from persistent storage into memory.

```js
let result = await User.refresh()
if (result.success) {
  let data = result.data
}
```

Use when you need fresh sync-storage state mid-command for the active user. With `db.user`, every `get` reads from storage directly — no refresh step needed.

---

## Full migration table

| Legacy `User` (current user) | Modern `db.user` |
| --- | --- |
| `User.get("key")` | `await db.user.get("key", fallback)` |
| `User.set("key", val)` | `await db.user.set("key", val)` |
| `User.set("key", val, type, ttl)` | `await db.user.set("key", val, { type, ttl })` |
| `User.set({ key, value, ttl })` | `await db.user.set({ key, value, ttl })` |
| `User.del("key")` | `await db.user.del("key")` |
| `User.has("key")` | `await db.user.has("key")` |
| `User.getAll()` | `await db.user.getAll()` |
| `User.delAll()` | `await db.user.delAll({ user_id: user.id })` |
| `User.batchSet(obj)` | Multiple `await db.user.set(...)` |
| `User.refresh()` | Not needed — `db.user.get` hits storage |
| Manual counter `get` + `set` | `await db.user.incr("key", n)` |
| Manual array append | `await db.user.push("key", item)` |
| Cross-user admin (not on `User`) | `await db.user.get/set/delAll({ user_id })` |

---

## New features only in `db.user`

```js
// Atomic counter
let balance = await db.user.incr("credits", 10)
await db.user.decr("lives", 1)

// List operations
await db.user.push("history", "page_settings")
await db.user.pull("tags", "inactive")

// Batch read
let profile = await db.user.mget(["language", "credits", "level"])

// Check result
let res = await db.user.set("key", value)
if (!res.ok) {
  Bot.sendMessage("Save failed: " + res.message)
}
```

See [Advanced Operations](../db-instance/advanced-operations.md).

---

## Migration example

### Before (deprecated)

```js
let visits = User.get("visits") || 0
visits++
User.set("visits", visits)

let name = User.get("display_name") || user.first_name
Bot.sendMessage("Visit #" + visits + ", " + name)
```

### After (`db.user`)

```js
let visits = await db.user.incr("visits", 1)
let name = await db.user.get("display_name", user.first_name)
Bot.sendMessage("Visit #" + visits + ", " + name)
```

---

## Admin: another user's data (`db.user` only)

```js
let targetId = Number(params.user_id)
if (!targetId) return Bot.sendMessage("Usage: /reset USER_ID")

await db.user.delAll({ user_id: targetId })
await db.user.set("reset_at", Date.now(), { user_id: targetId })

Bot.sendMessage("Reset user " + targetId)
```

---

## Webhook note

In **user webhooks**, `User` (deprecated) and `db.user` both work for the **webhook user**:

```js
// ✅ Preferred
let progress = await db.user.get("progress", 0)

// ⚠️ Legacy — current webhook user only
let progress = User.get("progress") || 0
```

In **global webhooks** and **webapps**, `User` is `null`. Use `db.user` with `{ user_id }` when you have an ID from `params`.

---

## Storage limits

`db.user` enforces plan-based storage limits and returns `{ ok: false, message }` when exceeded. Legacy `User` sync writes may fail silently in the background.

Check usage: `await db.getStorageStats()`

---

## See also

- [User Instance overview](index.md)
- [`db.user`](../db-instance/user.md)
- [Unified Methods](../db-instance/unified-methods.md)
