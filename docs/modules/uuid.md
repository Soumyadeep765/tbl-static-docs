# UUID

`modules.UUID` generates **universally unique identifiers**. Two versions are exposed.

```js
let id = modules.UUID.uuidv4()
let ordered = modules.UUID.uuidv6()
```

Both methods are **synchronous**.

---

## Methods

| Method | Description |
| --- | --- |
| `uuidv4()` | Random UUID (most common) |
| `uuidv6()` | Time-ordered UUID (sortable by creation time) |

---

## uuidv4

Standard random UUID — use for session IDs, request IDs, unique keys:

```js
let sessionId = modules.UUID.uuidv4()
// "550e8400-e29b-41d4-a716-446655440000"

db.user.set("session", sessionId)
```

---

## uuidv6

Time-ordered UUID — lexicographically sortable, useful for ordered records:

```js
let recordId = modules.UUID.uuidv6()
// "018e1234-5678-7890-abcd-ef1234567890"
```

---

## Examples

### Transaction reference

```js
let ref = modules.UUID.uuidv4().slice(0, 8).toUpperCase()
Bot.sendMessage(chat.id, "Order reference: #" + ref)
```

### Unique filename key

```js
let fileKey = modules.UUID.uuidv4() + ".json"
db.bot.set("uploads/" + fileKey, { user: user.id, data: params })
```

---

## Notes

- Collision-resistant for practical bot use
- No configuration required
- For short random strings, see [randomstring](randomstring.md)
- Official package: [uuid on npm](https://www.npmjs.com/package/uuid)
