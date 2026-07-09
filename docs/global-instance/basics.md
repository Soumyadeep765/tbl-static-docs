# Basic Global Operations (Removed)

!!! danger "Removed"
    `Global.set`, `Global.get`, `Global.del`, `Global.getAll`, and `Global.delAll` have been **removed**. They are not available in any command context.

If you have old commands that still reference `Global.*`, they need updating. Use [`db.global`](../db-instance/global.md) for all account-level storage.

---

## What to use instead

See [Unified Methods](../db-instance/unified-methods.md) for the full `db.global` API. Common operations:

```js
await db.global.set("maintenance", false)
let flag = await db.global.get("maintenance", false)
await db.global.del("temp_key")
let all = await db.global.getAll()
await db.global.delAll()
```

All `db.global` methods are asynchronous — add `await`. See [Account-Level Storage](../db-instance/global.md) for examples and scoping rules.

---

## Quick comparison

| Removed | Use instead |
| --- | --- |
| `Global.get(key)` | `await db.global.get(key, fallback)` |
| `Global.set(key, val)` | `await db.global.set(key, val)` |
| `Global.del(key)` | `await db.global.del(key)` |
| `Global.getAll()` | `await db.global.getAll()` |
| `Global.delAll()` | `await db.global.delAll()` |

---

## See also

- [`db.global`](../db-instance/global.md)
- [Storage Monitoring](storage-monitor.md) — removed `Global.getStorageInfo` and friends
