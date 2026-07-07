# User Instance (Deprecated)

!!! warning "Use `db.user` instead"
    The synchronous **`User`** instance is **deprecated**. All new code should use [`db.user`](../db-instance/user.md) — async, persistent, with `incr`, `push`, TTL, and proper error handling.

`User` stores **per-user key-value data** for the **current user only** — the Telegram user who triggered the command. Data is scoped to one user on one bot and is not shared with others.

```js
// ❌ Deprecated
User.set("level", 5)
let level = User.get("level")

// ✅ Use instead
await db.user.set("level", 5)
let level = await db.user.get("level", 0)
```

---

## Current user only

`User` does **not** support cross-user access. All reads and writes apply to the user who sent the update.

| Supported | Not supported |
| --- | --- |
| `User.get("key")` for current user | `User.get("key", otherUserId)` |
| `User.set("key", val)` for current user | `User.set({ ..., user_id: other })` |
| `User.delAll()` for current user | Admin reads/writes for another user |

To read or write **another user's** data, use [`db.user`](../db-instance/user.md) with `{ user_id }`.

---

## What it was used for

- User preferences (language, theme)
- Game progress and flow state
- Balances and counters (use `db.user.incr` instead now)
- Any data tied to the **active** user on one bot

---

## When `User` is available

| Context | `User` |
| --- | --- |
| Message / callback / inline query | Available |
| User webhook | Available |
| Global webhook | `null` |
| Webapp | `null` |
| Public web | N/A |
| Broadcast | `null` |

`User` requires a Telegram **`user.id`** in the update. Same rule as the global [`user`](../globals/user.md) variable.

---

## Why migrate to `db.user`

| | `User` (deprecated) | `db.user` |
| --- | --- | --- |
| Scope | **Current user only** | Current user or `{ user_id }` |
| Calls | Sync reads; writes are fire-and-forget | `await` on all operations |
| Persistence | Background sync; may roll back silently | Returns `{ ok: true/false }` |
| Counters | Manual read + write | `incr`, `decr` |
| Lists | Manual arrays | `push`, `pull` |
| Cross-user admin | **Not supported** | `get` / `set` / `delAll` with `{ user_id }` |
| Storage stats | Not in `getStorageStats` | Included in account analytics |

---

## Pages in this section

| Page | Content |
| --- | --- |
| [Basics](basics.md) | `get`, `set`, `del`, `getAll`, `has` — current user only |
| [Advanced & Migration](advanced-use.md) | `batchSet`, `refresh`, migration to `db.user` |

---

## Quick migration

| Deprecated | Replacement |
| --- | --- |
| `User.get("key")` | `await db.user.get("key", fallback)` |
| `User.set("key", val)` | `await db.user.set("key", val)` |
| `User.del("key")` | `await db.user.del("key")` |
| `User.getAll()` | `await db.user.getAll()` |
| `User.delAll()` | `await db.user.delAll({ user_id: user.id })` |
| `User.has("key")` | `await db.user.has("key")` |

Full guide: [Advanced & Migration](advanced-use.md).

---

## Related

- [`db.user`](../db-instance/user.md) — **recommended** per-user storage (supports `{ user_id }`)
- [`user` global](../globals/user.md) — Telegram user profile (read-only, not storage)
- [Unified Methods](../db-instance/unified-methods.md) — `db` CRUD reference
