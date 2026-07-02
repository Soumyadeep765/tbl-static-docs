# Storage Monitoring (Deprecated)

!!! warning "Deprecated"
    The synchronous `Global` storage metrics API is deprecated. Please transition to [`db.getStorageStats()`](../db-instance/analytics.md) instead.

For legacy support, the following monitoring calls are available:

*   `Global.getStorageInfo()`: Detailed storage metrics.
*   `Global.getStorageUsage()`: Storage usage percentage (0-100).
*   `Global.isStorageNearLimit()`: Returns `true` if usage exceeds 90%.
*   `Global.getAvailableStorage()`: Available storage in MB.
