# Database Storage (db) Overview

The Database Storage API (`db`) is the modern, secure, and asynchronous way to store state, configuration, and user data in your bots.

Unlike the legacy synchronous properties (`User`, `Global`, `Bot`), the `db` interface is built for scale, using local caches and atomic operations backed by MongoDB and Redis.

---

## Detailed Collections Reference

The database interface is divided into three separate collections under the global `db` variable, each serving a distinct scope and isolation level:

*   **[Bot-Level Storage (db.bot)](bot.md)**: Store settings, configuration, and state shared bot-wide.
*   **[User-Level Storage (db.user)](user.md)**: Store isolated user-specific profiles, balances, and history logs.
*   **[Account-Level Storage (db.global)](global.md)**: Share states, configurations, or bans across all bots in your network.

---

## Positional vs. Object Syntax

Every method in the `db` API supports both positional and object-based parameter options.

### Positional Parameter Example
```javascript
// Retrieve a value with a fallback of 0
const score = await db.bot.get('score', 0);
```

### Object Parameter Example
```javascript
// Retrieve a value by passing a structured options object
const level = await db.user.get({
  key: 'level',
  fallback: 1
});
```

---

## Key Benefits of the New API

*   **Asynchronous & Non-Blocking**: Operations use `await` and do not block the execution flow.
*   **Atomic Updates**: Includes atomic counters (`incr`, `decr`) and lists (`push`, `pull`) to avoid race conditions.
*   **Automatic TTL & Type Casting**: Set expiration times natively on keys and auto-detect data types.
*   **Storage Limits Protection**: Protects database size using built-in account-level limits.
