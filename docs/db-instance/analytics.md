# Analytics & Stats

The `db` instance provides top-level methods to inspect storage usage and list available collections.

!!! note "Async storage only"
    `getStorageStats()` tracks **async `db` storage** only. It does not include legacy sync data from deprecated `Bot.set` / `User.set` / removed `Global` APIs.

---

## `db.getStorageStats()`

Returns a storage usage report for your account.

```js
let stats = await db.getStorageStats()
Bot.inspect(stats)
```

### Return shape

```json
{
  "total_bytes": 409600,
  "total_mb": "0.39",
  "by_collection": [
    { "_id": "bot", "total": 102400, "count": 12 },
    { "_id": "user", "total": 307200, "count": 48 },
    { "_id": "global", "total": 0, "count": 0 }
  ],
  "top_bots": [
    { "_id": "42", "total": 307200, "count": 22 }
  ]
}
```

| Field | Description |
| --- | --- |
| `total_bytes` | Total async storage bytes across all collections |
| `total_mb` | Total in megabytes (string, 2 decimal places) |
| `by_collection` | Breakdown per collection (`bot`, `user`, `global`) with byte total and key count |
| `top_bots` | Up to 10 bots sorted by storage usage |

### Storage limits

Compare `total_mb` against your [plan](../globals/plan.md) limit:

| Plan | `prop_limit.per_account` |
| --- | --- |
| Free / Freemium | 20 MB |
| Premium | 50 MB |
| Elite | 100 MB |

When approaching the limit, `set` operations return `{ ok: false, message: "Storage limit exceeded" }`.

### Example: usage warning

```js
let stats = await db.getStorageStats()
let usedMB = parseFloat(stats.total_mb)
let limitMB = plan.prop_limit.per_account

if (usedMB > limitMB * 0.9) {
  Bot.sendMessage(owner.mail, `Storage at ${usedMB}/${limitMB} MB`)
}
```

---

## `db.getCollections()`

Returns the list of available collection names.

```js
let collections = await db.getCollections()
// ["user", "bot", "global"]
```

Useful for dynamic admin tools or debugging.

---

## Monitoring tips

- Call `getStorageStats()` in owner-only admin commands
- Use TTL on cached data to avoid unbounded growth: `await db.bot.set("cache", data, { ttl: 3600 })`
- Use `db.bot.getAll({ limit: 30 })` to audit large key sets page by page
- Migrate off deprecated `Bot.set` (1 MB cap) to `db.bot` for accurate tracking here
- Delete stale data with `del`, `delAll`, or `db.bot.clearAllData()` for full bot resets

## Important notes

- Stats reflect persisted async `db` data tracked in MongoDB
- There is no per-key size breakdown in `getStorageStats` — use `getAll` with pagination to audit keys
- Rate limiting applies: `getStorageStats` counts toward the 10 calls/second `db` limit
