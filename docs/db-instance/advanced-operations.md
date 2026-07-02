# Advanced Operations

The `db` API provides high-value atomic functions to safely increment numeric values and modify list arrays without race conditions.

---

## Atomic Counters

### `incr(key, amount, options)`
Increment a numeric field by a specified amount (defaults to `1`). Returns the new value. If the key does not exist, it defaults to `0` before incrementing.

```javascript
// Increment user balance by 10
const newBalance = await db.user.incr('balance', 10);
// newBalance = 10 (or current balance + 10)
```

### `decr(key, amount, options)`
Decrement a numeric field by a specified amount (defaults to `1`). Returns the new value.

```javascript
// Deduct 1 credit from bot remaining credits
const remaining = await db.bot.decr('credits', 1);
```

---

## List Operations

### `push(key, value, options)`
Natively append an item to an array field. If the key does not exist, it creates a new array with the item. Returns the updated array.

```javascript
// Append a page index to the user's history log
const history = await db.user.push('history', 'settings_page');
// history = ['settings_page']
```

### `pull(key, value, options)`
Remove all occurrences of a specified value from an array field. Returns the updated array.

```javascript
// Remove 'active' status tag from a bot tags list
const remainingTags = await db.bot.pull('tags', 'active');
```
