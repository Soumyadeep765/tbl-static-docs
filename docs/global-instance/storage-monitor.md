# Storage Monitoring (Removed)

!!! danger "Removed"
    `Global.getStorageInfo`, `Global.getStorageUsage`, `Global.isStorageNearLimit`, and `Global.getAvailableStorage` have been **removed**. They are not available in command scripts.

Storage analytics moved to the `db` instance. One place to check quotas, one API to learn.

---

## What to use instead

Use [`db.getStorageStats()`](../db-instance/analytics.md) for current monitoring:

```js
let stats = await db.getStorageStats()
// Inspect plan limits, usage per scope, etc.
```

See [Analytics & Stats](../db-instance/analytics.md) for the full method list and example output.

---

## Quick comparison

| Removed | Use instead |
| --- | --- |
| `Global.getStorageInfo()` | `await db.getStorageStats()` |
| `Global.getStorageUsage()` | `await db.getStorageStats()` |
| `Global.isStorageNearLimit()` | Check limits in `getStorageStats()` result |
| `Global.getAvailableStorage()` | Check limits in `getStorageStats()` result |

---

## See also

- [Analytics & Stats](../db-instance/analytics.md)
- [Basic Global Operations](basics.md) — removed `Global.*` storage methods
