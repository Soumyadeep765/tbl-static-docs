# deepmerge

Two config objects walk into a bar. One leaves with the other's nested keys.

## What is it?

**deepmerge** combines objects recursively — nested properties get merged, not overwritten wholesale. Perfect for layering default settings with user overrides, or merging two partial configs without losing data three levels deep.

Access it as `modules.deepmerge` (it's a function, not an object with methods).

---

## How to use

Pass two objects. Get one merged result:

```js
let merged = modules.deepmerge(
  { a: 1, b: { x: 1 } },
  { b: { y: 2 }, c: 3 }
)
// { a: 1, b: { x: 1, y: 2 }, c: 3 }
```

Notice `b.x` survived while `b.y` was added. Shallow spread (`{...a, ...b}`) would have replaced `b` entirely.

---

## API reference

| Call | Description |
| --- | --- |
| `deepmerge(target, source)` | Deep-merge `source` into a clone of `target` |
| `deepmerge(target, source, options)` | Merge with options (see below) |

Common options:

| Option | Default | Description |
| --- | --- | --- |
| `arrayMerge` | Replace | How to merge arrays when both sides have one |
| `clone` | `true` | Clone objects before merging |
| `customMerge` | — | Custom merge function for specific keys |

---

## Try it

### Merge defaults with user settings

[Bot](../bot-instance/index.md) sends to [chat](../globals/chat.md). Load saved preferences from [db](../db-instance/index.md), layer over bot defaults:

```js
let defaults = {
  notifications: true,
  theme: { color: "blue", size: "medium" },
  language: "en"
}

let saved = db.user.get("settings") || {}
let settings = modules.deepmerge(defaults, saved)

Bot.sendMessage("Theme: " + settings.theme.color + ", size: " + settings.theme.size)
```

### Apply a partial config update

[`params`](../globals/params.md) might be JSON the user sent — merge it into existing config:

```js
let current = db.bot.get("config") || {}
let update = JSON.parse(params)

let config = modules.deepmerge(current, update)
db.bot.set("config", config)

Bot.sendMessage("Config updated.")
```

---

## Notes

- **Sync** — no `await` needed
- Arrays are replaced by default (not concatenated). Pass a custom `arrayMerge` if you need different behaviour
- For simple flat objects, native spread (`{...a, ...b}`) may be enough — use deepmerge when nesting matters
- Official package: [deepmerge on npm](https://www.npmjs.com/package/deepmerge)
