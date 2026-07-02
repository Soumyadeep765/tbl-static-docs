# Advanced User Operations (Deprecated)

!!! warning "Deprecated"
    The synchronous `User` API is deprecated. Please transition to [`db.user`](../db-instance/index.md) instead.

For legacy support, you can pass options or target a specific user ID:

*   **Set data with Object**: `User.set({ key, value, user_id })`
*   **Get data with Object**: `User.get({ key, user_id })`
*   **Delete data with Object**: `User.del({ key, user_id })`
