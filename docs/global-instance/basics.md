# Basic Global Operations (Removed)

!!! danger "Removed"
    `Global.set`, `Global.get`, `Global.del`, `Global.getAll`, and `Global.delAll` have been **removed**. They are not available in any command context.

Use [`db.global`](../db-instance/global.md) for all account-level storage.

## Replacement

See [Unified Methods](../db-instance/unified-methods.md) for the full `db.global` API. Common operations:

- `await db.global.set(key, value)`
- `await db.global.get(key, defaultValue)`
- `await db.global.del(key)`
- `await db.global.getAll()`
- `await db.global.delAll()`

All `db.global` methods are asynchronous. See [Account-Level Storage](../db-instance/global.md) for examples.
