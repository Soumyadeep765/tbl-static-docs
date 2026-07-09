# Basic User Operations (Deprecated)

!!! warning "Deprecated — current user only"
    Use [`db.user`](../db-instance/user.md) for all new code. **`User` only supports the current user** who triggered the command. No cross-user reads or writes.

This page documents the legacy `User` API for existing bots. New projects should skip straight to `db.user`.

---

## How `User` works

Four steps, one caveat:

1. At command start, the **current user's** props are preloaded into `botState.user_props`
2. **`User.get`** reads from that in-memory cache — instant, synchronous
3. **`User.set`** / **`User.del`** update memory immediately, then **persist in the background**
4. If persistence fails, the in-memory value is **rolled back** (logged server-side)

Because writes are fire-and-forget, you cannot reliably `set` then `get` a new value in the same command and assume it persisted — use [`db.user`](../db-instance/user.md) when you need confirmed writes.

---

## `User.get(key)`

Read a value for the **current user**.

```js
let lang = User.get("language")
let level = User.get("level") || 1
```

Returns `null` if the key does not exist.

**`db.user` replacement:**

```js
let lang = await db.user.get("language", "en")
```

---

## `User.set(key, value, type?, ttl?)`

Write a value for the **current user**. Updates cache immediately; persists asynchronously.

```js
User.set("language", "en")
User.set("level", 5, "integer")
User.set("otp", "482910", "string", 300)
```

| Parameter | Description |
| --- | --- |
| `key` | Storage key |
| `value` | Value to store |
| `type` | Optional type hint (`string`, `integer`, `boolean`, …) |
| `ttl` | Optional TTL in seconds |

Returns `{ success: true, key, user_id, cached: true }` — does **not** mean persistence succeeded.

Alias: `User.setProperty(...)` — same behavior.

Object syntax with `key` / `value` / `type` / `ttl` is supported. **`user_id` in object form is not supported** for bot use — use `db.user` for other users.

**`db.user` replacement:**

```js
await db.user.set("language", "en")
await db.user.set("otp", "482910", { ttl: 300, type: "string" })
```

---

## `User.del(key)`

Delete one key for the **current user**.

```js
User.del("draft")
```

Object form: `User.del({ key: "draft" })` — no `user_id`.

Alias: `User.delProperty(...)`

**`db.user` replacement:**

```js
await db.user.del("draft")
```

---

## `User.has(key)`

Check if a key exists for the **current user**.

```js
if (User.has("agreed_terms")) {
  Bot.sendMessage("Welcome back!")
}
```

**`db.user` replacement:**

```js
if (await db.user.has("agreed_terms")) {
  Bot.sendMessage("Welcome back!")
}
```

---

## `User.getAll()`

Return a shallow copy of all cached keys for the **current user**.

```js
let all = User.getAll()
// { language: "en", level: 5, ... }
```

**`db.user` replacement:**

```js
let all = await db.user.getAll({ limit: 50 })
```

---

## `User.delAll()`

Clear all cached keys for the **current user** and trigger background delete.

```js
User.delAll()
```

Aliases: `User.delAllProperty(...)`, `User.clear(...)`

**`db.user` replacement:**

```js
await db.user.delAll({ user_id: user.id })
```

---

## Helper methods

| Method | Returns |
| --- | --- |
| `User.keys()` | Key names for current user |
| `User.values()` | Values for current user |
| `User.size()` | Number of keys |
| `User.getUserId()` | Current user's Telegram ID string |
| `User.getOwnerId()` | Owner account ID |
| `User.isOwnerValid()` | Whether owner ID is configured |

---

## Try it — legacy vs modern

### Save language preference (legacy)

```js
User.set("language", user.language_code || "en")
let lang = User.get("language")
Bot.sendMessage("Language: " + lang)
```

### Modern equivalent

```js
await db.user.set("language", user.language_code || "en")
let lang = await db.user.get("language", "en")
Bot.sendMessage("Language: " + lang)
```

---

## Limitations

- **Current user only** — no cross-user access
- **No `incr` / `decr` / `push` / `pull`** — use `db.user`
- **No `mget`** batch reads — use `db.user`
- **Writes not awaited** — race conditions in the same command
- **Not available** in webapp, global webhook, or broadcast

---

## See also

- [Advanced & Migration](advanced-use.md)
- [`db.user`](../db-instance/user.md)
