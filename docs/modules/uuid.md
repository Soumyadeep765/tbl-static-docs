# UUID

IDs so unique, collision odds are basically science fiction.

## What is it?

**UUID** generates universally unique identifiers — those long `550e8400-e29b-41d4-a716-446655440000` strings you see everywhere. Use them for session IDs, order references, file keys, or anywhere "probably unique" isn't good enough.

Access it as `modules.UUID`.

---

## How to use

Generate a random UUID:

```js
let id = modules.UUID.uuidv4()
// "550e8400-e29b-41d4-a716-446655440000"
```

Both methods are **synchronous** — no `await` needed.

---

## Methods

| Method | Description |
| --- | --- |
| `uuidv4()` | Random UUID (most common) |
| `uuidv6()` | Time-ordered UUID (sortable by creation time) |

---

## uuidv4

The standard choice — random, collision-resistant:

```js
let sessionId = modules.UUID.uuidv4()
db.user.set("session", sessionId)
```

---

## uuidv6

Time-ordered — newer IDs sort after older ones lexicographically. Handy for ordered records:

```js
let recordId = modules.UUID.uuidv6()
// "018e1234-5678-7890-abcd-ef1234567890"
```

---

## Try it

### Short order reference

[Bot](../bot-instance/index.md) sends to [chat](../globals/chat.md):

```js
let ref = modules.UUID.uuidv4().slice(0, 8).toUpperCase()
Bot.sendMessage(chat.id, "Your order reference: #" + ref)
```

### Unique file key

Tie an upload to [user](../globals/user.md) in [db](../db-instance/index.md):

```js
let fileKey = modules.UUID.uuidv4() + ".json"
db.bot.set("uploads/" + fileKey, { user: user.id, data: params })
Bot.sendMessage(chat.id, "File saved as " + fileKey)
```

### Ordered event log

```js
let eventId = modules.UUID.uuidv6()
db.bot.set("events/" + eventId, {
  type: "signup",
  user: user.id,
  at: Date.now()
})
```

---

## Notes

- **Sync** — no `await` needed
- Collision-resistant for practical bot use
- No configuration required
- For short random strings (promo codes, PINs), see [randomstring](randomstring.md)
- Official package: [uuid on npm](https://www.npmjs.com/package/uuid)
