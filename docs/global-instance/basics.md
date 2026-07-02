# Basic Global Operations (Deprecated)

!!! warning "Deprecated"
    The synchronous `Global` API is deprecated. Please transition to [`db.global`](../db-instance/index.md) instead.

For legacy support, the basic synchronous operations on the `Global` object are:

*   **Set data**: `Global.set(key, value, type)`
*   **Get data**: `Global.get(key)`
*   **Delete data**: `Global.del(key)`
*   **Get all data**: `Global.getAll()`
*   **Delete all data**: `Global.delAll()`
