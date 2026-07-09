# Listing Users

"How many people use my bot?" **`Bot.getUsers()`** answers that — and a lot more. Query user IDs, full profiles, counts, and filters without writing SQL or staring at spreadsheets.

Always returns a **Promise**. Always use `await`. Forgetting `await` gives you a Promise object instead of users. JavaScript's favorite prank.

---

## What does it return?

By default: an **array of user/chat IDs** (numbers). Channels excluded unless you ask for them.

```js
let ids = await Bot.getUsers()
// [5723455420, 1234567890, ...]

Bot.sendMessage("Total users: " + ids.length)
```

| Mode | How to request | Returns |
| --- | --- | --- |
| IDs only (default) | `await Bot.getUsers()` | `[id, id, ...]` |
| Full objects | `{ full: true }` or `{ return: "objects" }` | `[{ user_id, first_name, ... }, ...]` |
| Count only | `{ countOnly: true }` | `number` |
| With metadata | `{ meta: true }` | `{ users, count, limit, skip, total? }` |

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md).

---

## How to use it

### Count without fetching every ID

```js
let total = await Bot.getUsers({ countOnly: true })
Bot.sendMessage("You have " + total + " users.")
```

### Full user objects (paginated)

```js
let users = await Bot.getUsers({ full: true, limit: 50 })

for (let u of users) {
  // u.first_name, u.username, u.last_interaction, etc.
}
```

### Page with total count

```js
let page = await Bot.getUsers({
  full: true,
  page: 1,
  pageSize: 100,
  meta: true,
  withTotal: true
})
// { users: [...], count: 100, limit: 100, skip: 0, total: 4523 }
```

---

## Try it — copy-paste examples

### Premium private users (VIP list)

```js
let vip = await Bot.getUsers({
  chatType: "private",
  premiumOnly: true,
  excludeBlocked: true
})

Bot.sendMessage("VIP count: " + vip.length)
```

### Search by name

```js
let found = await Bot.getUsers({
  search: "alice",
  full: true,
  limit: 20
})
```

### Groups only

```js
let groups = await Bot.getUsers({ chatType: "group" })
```

### Recently active users

```js
let recent = await Bot.getUsers({
  activeAfter: "2025-07-01",
  chatType: "private"
})
```

---

## Filters

All filters are optional — pass them as a single object.

### Chat type

| Value | Description |
| --- | --- |
| `"private"` | Private chats only |
| `"group"` | Groups and supergroups |
| `"channel"` | Channels only |
| `"all"` | All chat types |
| `["private", "group"]` | Multiple types (array) |

Default: private + groups (channels excluded).

### Premium and blocked

| Filter | Value | Description |
| --- | --- | --- |
| `premiumOnly` | `true` | Premium users only |
| `premiumOnly` | `false` | Non-premium users only |
| `blockedOnly` | `true` | Blocked users only |
| `excludeBlocked` | `true` | Exclude blocked users |

### User targeting

| Filter | Type | Description |
| --- | --- | --- |
| `userIds` / `ids` | `number \| array` | Include only these IDs |
| `excludeUserIds` / `excludeIds` | `number \| array` | Exclude these IDs |
| `username` | `string` | Exact username match (with or without `@`) |
| `hasUsername` | `boolean` | `true` = has username, `false` = no username |
| `search` | `string` | Search `first_name`, `last_name`, `username`, `chat_title` |

### Date ranges

| Filter | Description |
| --- | --- |
| `createdAfter` | Users created after this date |
| `createdBefore` | Users created before this date |
| `activeAfter` / `lastInteractionAfter` | Last interaction after this date |
| `activeBefore` / `lastInteractionBefore` | Last interaction before this date |

### Pagination and sorting

| Filter | Type | Description |
| --- | --- | --- |
| `limit` | `number` | Max results (max 100,000) |
| `skip` | `number` | Offset |
| `page` + `pageSize` | `number` | Page-based pagination |
| `sortBy` / `sortField` | `string` | Sort field (`user_id`, `created_at`, `last_interaction`, `first_name`, `username`, `chat_type`) |
| `sortOrder` / `order` | `"asc"` / `"desc"` | Sort direction |
| `fields` | `string[]` | Project specific fields (with `full: true`) |

---

## Full object fields

When `full: true`, each object may include:

| Field | Description |
| --- | --- |
| `user_id` | Telegram user/chat ID |
| `first_name` | First name |
| `last_name` | Last name |
| `username` | @username |
| `chat_type` | `private`, `group`, `supergroup`, `channel` |
| `premium` | Premium status |
| `block` | Whether user blocked the bot |
| `created_at` | First interaction date |
| `last_interaction` | Last interaction date |
| `chat_title` | Group/channel title |

---

## Important notes

- Always `await` — `Bot.getUsers()` returns a Promise
- Default return is an **array of IDs**, not full objects
- Channels are **excluded by default** — use `chatType: "channel"` to include them
- To actually *message* everyone matching filters, see [Broadcasting](broadcasting.md)
