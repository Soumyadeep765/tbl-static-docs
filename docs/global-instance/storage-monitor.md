# Storage Monitoring (Removed)

!!! danger "Removed"
    `Global.getStorageInfo`, `Global.getStorageUsage`, `Global.isStorageNearLimit`, and `Global.getAvailableStorage` have been **removed**. They are not available in command scripts.

Use [`db.getStorageStats()`](../db-instance/analytics.md) instead.

## Replacement

Storage analytics are now part of the `db` instance. See [Analytics & Stats](../db-instance/analytics.md) for current monitoring methods and usage.
