# Listing Users

`Bot.getUsers()` queries the database for users and chats that have interacted with your bot. Returns a **Promise** — always use `await`.

## Basic usage

```js
// All user IDs (channels excluded by default)
let ids = await Bot.getUsers()
// [5723455420, 1234567890, ...]

Bot.sendMessage(`Total users: ${ids.length}`)
```

By default, returns an **array of user/chat IDs** (numbers). Channels are excluded unless you explicitly filter for them.

## Return modes

| Mode | How to request | Returns |
| --- | --- | --- |
| IDs only (default) | `await Bot.getUsers()` | `[id, id, ...]` |
| Full objects | `{ full: true }` or `{ return: "objects" }` | `[{ user_id, first_name, ... }, ...]` |
| Count only | `{ countOnly: true }` | `number` |
| With metadata | `{ meta: true }` | `{ users, count, limit, skip, total? }` |

```js
// Count without fetching all IDs
let total = await Bot.getUsers({ countOnly: true })

// Full user objects
let users = await Bot.getUsers({ full: true, limit: 50 })

// Paginated with total count
let page = await Bot.getUsers({
  full: true,
  page: 1,
  pageSize: 100,
  meta: true,
  withTotal: true
})
// { users: [...], count: 100, limit: 100, skip: 0, total: 4523 }
```

## Filters

All filters are optional and passed as a single object.

### Chat type

| Value | Description |
| --- | --- |
| `"private"` | Private chats only |
| `"group"` | Groups and supergroups |
| `"channel"` | Channels only |
| `"all"` | All chat types |
| `["private", "group"]` | Multiple types (array) |

Default: private + groups (channels excluded).

```js
let groups = await Bot.getUsers({ chatType: "group" })
let channels = await Bot.getUsers({ chatType: "channel" })
```

### Premium and blocked

| Filter | Value | Description |
| --- | --- | --- |
| `premiumOnly` | `true` | Premium users only |
| `premiumOnly` | `false` | Non-premium users only |
| `blockedOnly` | `true` | Blocked users only |
| `excludeBlocked` | `true` | Exclude blocked users |

```js
let premium = await Bot.getUsers({ premiumOnly: true })
let active = await Bot.getUsers({ excludeBlocked: true })
```

### User targeting

| Filter | Type | Description |
| --- | --- | --- |
| `userIds` / `ids` | `number \| array` | Include only these IDs |
| `excludeUserIds` / `excludeIds` | `number \| array` | Exclude these IDs |
| `username` | `string` | Exact username match (with or without `@`) |
| `hasUsername` | `boolean` | `true` = has username, `false` = no username |
| `search` | `string` | Search `first_name`, `last_name`, `username`, `chat_title` |

```js
let admins = await Bot.getUsers({ userIds: [111, 222, 333] })
let found = await Bot.getUsers({ search: "alice" })
```

### Date ranges

| Filter | Description |
| --- | --- |
| `createdAfter` | Users created after this date |
| `createdBefore` | Users created before this date |
| `activeAfter` / `lastInteractionAfter` | Last interaction after this date |
| `activeBefore` / `lastInteractionBefore` | Last interaction before this date |

```js
let recent = await Bot.getUsers({
  activeAfter: "2025-07-01",
  chatType: "private"
})
```

### Pagination and sorting

| Filter | Type | Description |
| --- | --- | --- |
| `limit` | `number` | Max results (max 100,000) |
| `skip` | `number` | Offset |
| `page` + `pageSize` | `number` | Page-based pagination |
| `sortBy` / `sortField` | `string` | Sort field (`user_id`, `created_at`, `last_interaction`, `first_name`, `username`, `chat_type`) |
| `sortOrder` / `order` | `"asc"` / `"desc"` | Sort direction |
| `fields` | `string[]` | Project specific fields (with `full: true`) |

```js
let page2 = await Bot.getUsers({
  full: true,
  page: 2,
  pageSize: 50,
  sortBy: "last_interaction",
  sortOrder: "desc"
})
```

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

## Examples

```js
// Premium private users
let vip = await Bot.getUsers({
  chatType: "private",
  premiumOnly: true,
  excludeBlocked: true
})

// Search and paginate
let results = await Bot.getUsers({
  search: "john",
  full: true,
  limit: 20,
  meta: true
})

// Use IDs in a loop
let ids = await Bot.getUsers({ chatType: "private", limit: 1000 })
for (let id of ids) {
  // process each user
}
```

## Important notes

- Always `await` — `Bot.getUsers()` returns a Promise
- Default return is an **array of IDs**, not full objects
- Channels are **excluded by default** — use `chatType: "channel"` to include them
- For broadcast targeting, see [Broadcasting](broadcasting.md) which uses similar filters internally
