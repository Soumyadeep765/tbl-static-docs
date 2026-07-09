# ResourcesLib (v2)

Economy engine — coins, XP, health, passive growth, transfers. Uses async [`db.bot`](../db-instance/bot.md). Access as **`Libs.ResourcesLibv2`**. **All resource methods need `await`.**

---

## What is it?

`Libs.ResourcesLibv2` manages persistent numeric resources scoped to a user, chat, or your whole bot. Passive growth over time included.

| Scope | Factory | Key pattern |
| --- | --- | --- |
| User | `userRes("gold")` | `ResourcesLib_user_{id}_gold` |
| Chat | `chatRes("points")` | `ResourcesLib_chat_{id}_points` |
| Global | `globalRes("pool")` | `ResourcesLib_global_global_pool` |
| Other user | `anotherUserRes("gold", id)` | Same as user scope |

!!! info "Same keys as v1"
    Storage keys match legacy `ResourcesLib_*` format but live on async `db.bot` instead of deprecated `Bot.getProperty`.

---

## How to use it

```js
let gold = Libs.ResourcesLibv2.userRes("gold")
await gold.add(50)
let balance = await gold.value()
Bot.sendMessage(chat.id, "Gold: " + balance)
```

---

## Resource methods

| Method | Description |
| --- | --- |
| `value()` | Current value (applies growth) |
| `peek()` | Raw stored value (fast, no growth) |
| `preview()` | Simulated value after growth (no write) |
| `set(n)` | Set value |
| `add(n)` | Add (uses `db.bot.incr`) |
| `have(n)` | Has enough? |
| `remove(n)` | Remove if enough (throws if not) |
| `removeAnyway(n)` | Force remove |
| `spend(n)` | Returns true/false |
| `tryRemove(n)` | `{ ok, removed, balance }` |
| `reset()` | Set to 0 |
| `ensureAtLeast(min)` | Floor value |
| `fillTo(target)` | Add until target |
| `setClamped(n, min, max)` | Set within bounds |
| `format({ suffix, compact })` | `"1.2K gold"` |
| `stats()` | Dashboard bundle (one mget) |
| `transferTo(other, n)` | Transfer between resources |
| `exchangeTo(other, { remove_amount, add_amount })` | Different rates |

---

## Growth

```js
let gold = Libs.ResourcesLibv2.userRes("gold")
let g = Libs.ResourcesLibv2.growthFor(gold)

await g.add({ value: 1, interval: 60, max: 1000 })           // +1 per minute
await g.addPercent({ percent: 5, interval: 300 })             // +5% of base
await g.addCompoundInterest({ percent: 2, interval: 3600 })   // compound

await g.stop()
await g.resume()
let pending = await g.previewGain()
```

Growth keys: `{propName}_growth` on `db.bot`.

---

## Module helpers

```js
// Load multiple resources in one mget
let bag = await Libs.ResourcesLibv2.loadAll([gold, wood, energy], { withGrowth: true })

// Crafting — check all, deduct in parallel
let craft = await Libs.ResourcesLibv2.spendAll([
  { res: gold, amount: 50 },
  { res: wood, amount: 10 }
])
if (!craft.ok) Bot.sendMessage(chat.id, "Need " + craft.need + " " + craft.missing)
```

---

## Examples

### Shop purchase

```js
let gold = Libs.ResourcesLibv2.userRes("gold")
if (await gold.spend(30)) {
  Bot.sendMessage(chat.id, "Purchased! Balance: " + await gold.peek())
} else {
  Bot.sendMessage(chat.id, "Not enough gold.")
}
```

### Transfer between users

```js
let myGold = Libs.ResourcesLibv2.userRes("gold")
let theirGold = Libs.ResourcesLibv2.anotherUserRes("gold", friendId)
await myGold.transferTo(theirGold, 20)
```

### Player HUD

```js
let s = await gold.stats()
Bot.sendMessage(chat.id,
  await gold.format({ suffix: "gold", compact: true }) +
  "\nPending: +" + s.pending +
  "\nNext tick: " + Math.ceil(s.growth?.nextTickIn || 0) + "s"
)
```

---

## Legacy `Libs.ResourcesLib`

The original sync `Libs.ResourcesLib` used deprecated `Bot.getProperty`. It is **deprecated**. Migrate to `Libs.ResourcesLibv2` and add `await` to every resource call.

```js
// Old (deprecated)
gold.add(10)
gold.value()

// New
await gold.add(10)
await gold.value()
```

[Database overview](../db-instance/index.md) · [Advanced ops (incr/push)](../db-instance/advanced-operations.md)
