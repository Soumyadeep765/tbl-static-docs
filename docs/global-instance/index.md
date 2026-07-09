# Global Instance (Removed)

If your old commands still say `Global.set` or `Global.get`, they'll fail at runtime. The sync `Global` API is gone — `db.global` is the replacement.

Same use case (account-level data shared across all your bots), modern async API.

---

## What was `Global`?

The old **Global instance** stored data at the **account level**, shared across all bots under the same owner. That use case is unchanged; only the API changed.

| Old (removed) | Replacement |
| --- | --- |
| `Global.set(key, value, type)` | `await db.global.set(key, value)` |
| `Global.get(key)` | `await db.global.get(key, defaultValue)` |
| `Global.del(key)` | `await db.global.del(key)` |
| `Global.getAll()` | `await db.global.getAll()` |
| `Global.delAll()` | `await db.global.delAll()` |
| `Global.getStorageInfo()` etc. | [`db.getStorageStats()`](../db-instance/analytics.md) |

!!! danger "Removed API"
    The synchronous `Global` instance has been **completely removed**.  
    `Global.set`, `Global.get`, `Global.del`, and all other `Global.*` methods are **no longer available** in command scripts.

Use [`db.global`](../db-instance/global.md) instead — the modern, asynchronous account-level storage API.

---

## How to migrate

Replace every `Global.*` call with the matching `await db.global.*` call. All `db` methods are **async** — use `await` or `.then()`.

```javascript
// Before (no longer works)
// Global.set('counter', 1)

// After
await db.global.set('counter', 1)
let count = await db.global.get('counter', 0)
```

If you have old commands still using `Global`, update them before deploying — they will fail at runtime.

!!! tip "New to TBL?"
    New to storage? Start with the [Database overview](../db-instance/index.md). Quick intro: [Learning TBL](../learning-tbl.md).

---

## Where to go next

- [Account-level storage (`db.global`)](../db-instance/global.md) — shared data across all your bots
- [Database overview](../db-instance/index.md) — `db.bot`, `db.user`, and `db.global`
- [Unified CRUD methods](../db-instance/unified-methods.md) — shared method reference for all collections
