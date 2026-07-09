# lodash

Arrays, objects, and the boilerplate you were about to write by hand.

## What is it?

**lodash** is a utility belt for JavaScript data. Filter arrays, pick object keys, group items, debounce functions, deep-clone nested structures — if you've written a `for` loop and thought "surely someone solved this," lodash probably did.

Access it as `modules.lodash` — the full lodash library.

---

## How to use

Call methods directly on the lodash object:

```js
let result = modules.lodash.filter([1, 2, 3, 4], n => n > 2)
// [3, 4]
```

No imports, no setup. Just `modules.lodash.<method>()`.

---

## Popular methods

| Method | What it does |
| --- | --- |
| `filter(collection, predicate)` | Keep items matching a test |
| `map(collection, iteratee)` | Transform each item |
| `find(collection, predicate)` | First item matching a test |
| `groupBy(collection, key)` | Group items by a property |
| `sortBy(collection, key)` | Sort by property or function |
| `uniq(array)` | Remove duplicates |
| `pick(object, keys)` | Keep only listed keys |
| `omit(object, keys)` | Remove listed keys |
| `merge(target, source)` | Shallow merge objects |
| `cloneDeep(value)` | Deep clone |
| `get(object, path, default)` | Safe nested access (`"a.b.c"`) |
| `isEmpty(value)` | Check for empty array/object/string |
| `chunk(array, size)` | Split array into groups |

This is a sampler, not the full menu — see [lodash docs](https://lodash.com/docs) for everything else.

---

## Try it

### Filter active users from a list

[Bot](../bot-instance/index.md) sends to [chat](../globals/chat.md). Data comes from [db](../db-instance/index.md):

```js
let users = db.bot.get("members") || []
let active = modules.lodash.filter(users, u => u.lastSeen > Date.now() - 86400000)

Bot.sendMessage(chat.id, active.length + " users active in the last 24 hours.")
```

### Group scores by team

[`params`](../globals/params.md) might not be involved here — this works on data you already have:

```js
let scores = [
  { name: "Alice", team: "A", score: 90 },
  { name: "Bob", team: "B", score: 85 },
  { name: "Carol", team: "A", score: 95 }
]

let byTeam = modules.lodash.groupBy(scores, "team")
let summary = Object.entries(byTeam).map(([team, players]) =>
  team + ": " + players.map(p => p.name).join(", ")
).join("\n")

Bot.sendMessage(chat.id, "Teams:\n" + summary)
```

### Safe nested read

```js
let config = db.bot.get("config") || {}
let color = modules.lodash.get(config, "theme.color", "blue")

Bot.sendMessage(chat.id, "Theme color: " + color)
```

---

## Notes

- **Sync** — no `await` needed
- Works with arrays, objects, strings, and collections
- For deep-merging nested configs (not just cloning), see [deepmerge](deepmerge.md)
- Official docs: [lodash.com](https://lodash.com/docs)
