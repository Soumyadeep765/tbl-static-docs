# Basic User Operations (Deprecated)

!!! warning "Deprecated"
    The synchronous `User` API is deprecated. Please transition to [`db.user`](../db-instance/index.md) instead.

For legacy support, the basic synchronous operations on the `User` object are:

*   **Set data**: `User.set(key, value, type)`
*   **Get data**: `User.get(key)`
*   **Delete data**: `User.del(key)`
*   **Get all data**: `User.getAll()`
*   **Delete all data**: `User.delAll()`

These calls are synchronous and execute without using `await`.
