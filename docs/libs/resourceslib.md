# ResourcesLib

`Libs.ResourcesLib` manages **persistent numeric resources** — coins, XP, health, points — scoped to a user, chat, or the whole bot. Supports passive growth over time. All methods are **synchronous**.

```js
let coins = Libs.ResourcesLib.userRes("coins")
coins.add(50)
Bot.sendMessage(chat.id, "Balance: " + coins.value())
```

Values persist via bot properties (`ResourcesLib_*` keys). Growth state is stored as JSON.

---

## Creating resources

| Method | Scope | Description |
| --- | --- | --- |
| `userRes(name)` | Current user | Per-user resource |
| `chatRes(name)` | Current chat | Per-chat/group resource |
| `globalRes(name)` | Entire bot | Bot-wide shared resource |
| `anotherUserRes(name, telegramId)` | Specific user | Another user's resource |
| `anotherChatRes(name, chatId)` | Specific chat | Another chat's resource |
| `growthFor(resource)` | — | Growth controller for a resource |

```js
let myCoins = Libs.ResourcesLib.userRes("coins")
let groupScore = Libs.ResourcesLib.chatRes("score")
let totalVisits = Libs.ResourcesLib.globalRes("visits")
let friendGold = Libs.ResourcesLib.anotherUserRes("gold", 123456789)
```

Uses `user.telegramid` and `chat.chatid` for the current user/chat scope.

---

## Basic operations

Every resource object supports:

| Method | Description | Throws |
| --- | --- | --- |
| `.value()` | Current value (includes growth calculation) | — |
| `.set(amount)` | Set to exact number | if not a number |
| `.add(amount)` | Add to current value | if not a number |
| `.have(amount)` | `true` if value ≥ amount | — |
| `.remove(amount)` | Subtract if enough available | if insufficient |
| `.removeAnyway(amount)` | Subtract regardless of balance | if not a number |

```js
let gold = Libs.ResourcesLib.userRes("gold")

// Initialize new player
if (gold.value() === 0) {
  gold.set(100)
}

gold.add(25)
Bot.sendMessage(chat.id, "Gold: " + gold.value())

if (gold.have(30)) {
  gold.remove(30)
  Bot.sendMessage(chat.id, "Purchased! Remaining: " + gold.value())
}
```

String values passed to `.set()` / `.add()` are auto-converted to numbers. Non-numeric values throw `ResLib: value must be number only`.

---

## Transfers

Move resources between resource objects of the **same name**:

| Method | Description |
| --- | --- |
| `.transferTo(other, amount)` | Move if enough balance |
| `.transferToAnyway(other, amount)` | Force move |
| `.takeFromAnother(other, amount)` | Pull from another into this |
| `.takeFromAnotherAnyway(other, amount)` | Force pull |
| `.exchangeTo(other, options)` | Exchange at a custom rate |

```js
let myGold = Libs.ResourcesLib.userRes("gold")
let friendGold = Libs.ResourcesLib.anotherUserRes("gold", friendId)

myGold.transferTo(friendGold, 20)

// Exchange: 1 gold → 100 silver
let silver = Libs.ResourcesLib.userRes("silver")
gold.exchangeTo(silver, { remove_amount: 1, add_amount: 100 })
```

Transfer between different resource names throws `ResLib: can not transfer different resources`.

---

## Passive growth

Attach automatic growth to any resource with `growthFor()`:

```js
let gold = Libs.ResourcesLib.userRes("gold")
let growth = Libs.ResourcesLib.growthFor(gold)
```

### Growth types

**Simple** — fixed amount per interval:

```js
Libs.ResourcesLib.growthFor(gold).add({
  value: 1,       // +1 per interval
  interval: 60,   // every 60 seconds
  max: 1000       // cap at 1000
})
```

**Percent** — percentage of base value per interval:

```js
Libs.ResourcesLib.growthFor(gold).addPercent({
  percent: 5,     // 5% of base per interval
  interval: 300,  // every 5 minutes
  min: 0,
  max: 5000
})
```

**Compound interest** — exponential growth:

```js
Libs.ResourcesLib.growthFor(gold).addCompoundInterest({
  percent: 2,                  // 2% compound
  interval: 3600,            // every hour
  max_iterations_count: 100  // stop after 100 cycles
})
```

### Growth management

| Method | Description |
| --- | --- |
| `.isEnabled()` | Whether growth is active |
| `.progress()` | Current cycle progress 0–100% |
| `.willCompleteAfter()` | Seconds until next growth tick |
| `.stop()` | Disable growth |

```js
let g = Libs.ResourcesLib.growthFor(gold)

if (g.isEnabled()) {
  Bot.sendMessage(chat.id, "Next tick in " + g.willCompleteAfter() + "s")
}

g.stop()  // pause passive income
```

Growth is calculated when `.value()` is called — not on a background timer.

---

## Growth options

| Option | Used in | Description |
| --- | --- | --- |
| `value` | `.add()` | Fixed increment per interval |
| `percent` | `.addPercent()`, `.addCompoundInterest()` | Percentage rate |
| `interval` | All types | Seconds between growth ticks |
| `min` | Percent | Minimum value floor |
| `max` | Simple, percent | Maximum value ceiling |
| `max_iterations_count` | Compound | Max number of growth cycles |

---

## Full example — game economy

```js
let health = Libs.ResourcesLib.userRes("health")
let gold = Libs.ResourcesLib.userRes("gold")

// New player setup
if (gold.value() === 0) {
  gold.set(100)
  health.set(100)

  Libs.ResourcesLib.growthFor(gold).add({ value: 1, interval: 60, max: 1000 })
  Libs.ResourcesLib.growthFor(health).addPercent({ percent: 2, interval: 30, max: 100 })
}

// Combat
function takeDamage(amount) {
  health.removeAnyway(amount)
  if (health.value() <= 0) {
    health.set(50)
    gold.remove(Math.floor(gold.value() * 0.1))
    Bot.sendMessage(chat.id, "You died! Lost 10% gold. Respawned with 50 HP.")
  }
}
```

---

## Scopes compared

| Scope | Method | Shared between |
| --- | --- | --- |
| User | `userRes("coins")` | Only that user |
| Chat | `chatRes("points")` | All members of that chat |
| Global | `globalRes("visits")` | All users of this bot |
| Other user | `anotherUserRes("coins", id)` | That specific user |
| Other chat | `anotherChatRes("score", id)` | That specific chat |

Global resources are **per-bot**, not shared across different bots.

---

## Notes

- All methods are **sync** — no `await`
- `.value()` triggers growth calculation if growth is enabled
- Resource names are arbitrary strings — created automatically on first use
- Stored internally via `Bot.getProperty` / `Bot.setProperty`
- For new projects, consider [`db.user`](../db-instance/user.md) / [`db.bot`](../db-instance/bot.md) for complex non-numeric data
