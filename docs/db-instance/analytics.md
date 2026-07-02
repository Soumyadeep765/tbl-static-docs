# Analytics & Stats

The database interface provides built-in analytics methods at the top level of the `db` namespace to generate storage reports and inspect collections.

---

## 1. `db.getStorageStats()`

Generates a detailed storage size report for your account. This is useful for displaying storage allocation on user dashboards or monitoring limits.

### Usage
```javascript
const stats = await db.getStorageStats();
Bot.inspect(stats);
```

### Example Output
```json
{
  "total_bytes": 409600,
  "total_mb": "0.39",
  "by_collection": [
    { "_id": "bot", "total": 102400, "count": 12 },
    { "_id": "user", "total": 307200, "count": 48 }
  ],
  "top_bots": [
    { "_id": "bot123", "total": 307200, "count": 22 }
  ]
}
```

---

## 2. `db.getCollections()`

Returns a list of safe collections accessible by the platform interface.

### Usage
```javascript
const collections = await db.getCollections();
// returns ["user", "bot", "global"]
```
