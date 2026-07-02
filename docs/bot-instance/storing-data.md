# Bot Data Store (Deprecated)

!!! warning "Deprecated"
    The synchronous `Bot` storage API is deprecated. Please transition to [`db.bot`](../db-instance/index.md) instead.

For legacy support, the synchronous operations on the `Bot` object are:

*   **Set data**: `Bot.set(key, value, type)`
*   **Get data**: `Bot.get(key)`
*   **Delete data**: `Bot.del(key)`
*   **Delete all data**: `Bot.delAll()`
*   **Check key exists**: `Bot.has(key)`
*   **Get all data**: `Bot.getAll()`
*   **Count total keys**: `Bot.count()`
*   **Get key list**: `Bot.getNames()`
