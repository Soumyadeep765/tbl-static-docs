# User Instance (Deprecated)

The old way to save per-user data — synchronous, current-user-only, and officially retired. New code should use [`db.user`](../db-instance/user.md) instead.

If you're starting fresh, skip this page entirely and go straight to `db.user`. If you're maintaining old commands, here's what you need to migrate.

---

## What was `User`?

The synchronous **`User`** instance stored **per-user key-value data** for the **current user only** — the Telegram user who triggered the command. Data was scoped to one user on one bot and was not shared with others.

| Old (`User`) | New (`db.user`) |
| --- | --- |
| Sync reads, fire-and-forget writes | `await` on all operations |
| Current user only | Current user or `{ user_id }` |
| No error feedback on writes | Returns `{ ok: true/false }` |
| Manual counters | `incr`, `decr`, `push`, `pull` |

!!! warning "Use `db.user` instead"
    The synchronous **`User`** instance is **deprecated**. All new code should use [`db.user`](../db-instance/user.md) — async, persistent, with `incr`, `push`, TTL, and proper error handling.

---

## How to migrate

Replace every `User.*` call with the matching `await db.user.*` call:

```js
// ❌ Deprecated
User.set("level", 5)
let level = User.get("level")

// ✅ Use instead
await db.user.set("level", 5)
let level = await db.user.get("level", 0)
```

!!! tip "New to TBL?"
    `user` is a global variable (read-only profile info), not storage. Quick intro: [Learning TBL](../learning-tbl.md). Full storage guide: [`db.user`](../db-instance/user.md).

---

## Quick migration table

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

## Related

- [`db.user`](../db-instance/user.md) — **recommended** per-user storage (supports `{ user_id }`)
- [`user` global](../globals/user.md) — Telegram user profile (read-only, not storage)
- [Unified Methods](../db-instance/unified-methods.md) — `db` CRUD reference
