# TBL Libraries (Libs)

Dice rolls, referral links, coin balances, cooldowns, translations, channel gates — **`Libs`** is the bot-shaped toolbox. No imports, no setup. Type `Libs.` and go.

---

## What are Libs?

**Libs** are TBL-built helper libraries for Telegram bot tasks. They load lazily on first access and run inside your command **Logic** field.

| You get | You skip |
| --- | --- |
| Bot-focused systems (economy, referrals, cooldowns) | Writing glue from scratch |
| One global: `Libs` | Import statements |
| Sync + async libraries | External services for simple bot logic |

Access: `Libs.<libraryName>.<method>()` — **case-sensitive** (`Libs.random` works, `Libs.Random` does not).

!!! tip "Storage"
    New libraries use async [`db`](../db-instance/index.md) (`db.user`, `db.bot`) — not deprecated `Bot.set` / `User.set`. Always `await` db-backed libs.

---

## Pick a library

| Library | Access | Async? | Storage | Page |
| --- | --- | --- | --- | --- |
| `random` | `Libs.random.*` | No | — | [random](random.md) |
| `dateTimeFormat` | `Libs.dateTimeFormat.*` | No | — | [dateTimeFormat](date-time-format.md) |
| `tgutil` | `Libs.tgutil.*` | No | — | [tgutil](tgutil.md) |
| `mcl` | `Libs.mcl.*` | **Yes** | — | [MCL](mcl.md) |
| `ResourcesLibv2` | `Libs.ResourcesLibv2.*` | **Yes** | `db.bot` | [ResourcesLib](resourceslib.md) |
| `refLib` | `Libs.refLib.*` | **Yes** | `db.user` + `db.bot` | [refLib](reflib.md) |
| `translate` | `Libs.translate.*` | **Yes** | `db.user` + `db.bot` | [translate](translate.md) |
| `cooldown` | `Libs.cooldown.*` | **Yes** | `db.user` + `db.bot` | [cooldown](cooldown.md) |

Source: [telebothost/tbl-libs](https://github.com/telebothost/tbl-libs) (`libsv2/` folder — 9 files, 8 active + 1 deprecated `ResourcesLib.js` copy).

---

## Sync vs async

| Type | Libraries | Rule |
| --- | --- | --- |
| **Sync** | `random`, `dateTimeFormat`, `tgutil`, `mcl.getBtn()` | Call directly |
| **Async** | `mcl.check/quick/...`, `refLib`, `ResourcesLibv2`, `translate`, `cooldown` | Always `await` |

```js
// Async
let ok = await Libs.mcl.quick(user.id, ["@Channel"])
let count = await Libs.refLib.count()
await Libs.cooldown.tryRun("daily", 86400)

// Sync
let roll = Libs.random.randomInt(1, 6)
let name = Libs.tgutil.getNameFor(user)
```

`.then()` is not supported in TBL — use `await` only.

---

## Try it — quick examples

### Roll a dice

```js
let roll = Libs.random.randomInt(1, 6)
Bot.sendMessage("You rolled: " + roll)
```

### Coin balance (async economy)

```js
let gold = Libs.ResourcesLibv2.userRes("gold")
await gold.add(50)
Bot.sendMessage("Gold: " + await gold.value())
```

### Referral tracking

```js
let result = await Libs.refLib.track({
  onJoin: async ({ referrer, count }) => {
    Bot.sendMessage("Referred by " + referrer.first_name + "! They have " + count + " refs.")
  }
})
let link = await Libs.refLib.register()
```

### Daily cooldown

```js
let run = await Libs.cooldown.tryRun("daily_bonus", 86400)
if (!run.ok) {
  return Bot.sendMessage("Come back in " + await Libs.cooldown.format("daily_bonus"))
}
```

### Translate to user's language

```js
let text = await Libs.translate.translate("Welcome!", { to: "hi" })
Bot.sendMessage(text)
```

### Channel gate

```js
let ok = await Libs.mcl.quick(user.id, ["@MyChannel"])
if (!ok) {
  let buttons = Libs.mcl.getBtn(["@MyChannel"])
  Api.sendMessage({ chat_id: chat.id, text: "Join first!", reply_markup: { inline_keyboard: buttons } })
}
```

---

## Libs or Modules?

| | `Libs` | `modules` |
| --- | --- | --- |
| What | Bot systems (economy, refs, cooldowns) | npm-style (JWT, bcrypt, CSV) |
| Access | `Libs.random.randomInt(1, 6)` | `modules.crypto.randomBytes(16)` |
| Best for | Telegram bot glue + `db` persistence | Crypto, parsing, validation |

[Modules docs](../modules/index.md)

---

## How Libs works

| Behaviour | Detail |
| --- | --- |
| Lazy loading | Loads on first `Libs.<name>` access |
| Immutable | Cannot modify `Libs` object |
| Method timeout | 2 seconds max per call |
| Async methods | Return Promises — use `await` |
| Globals | Libs can use `Bot`, `Api`, `user`, `chat`, `db`, `HTTP` |

---

## Legacy note

Older sync libs used deprecated `Bot.getProperty` / `User.setProperty`. They still exist in `Libs/` for backward compatibility but are **deprecated**. Migrate to `libsv2` versions that use [`db`](../db-instance/index.md).

| Legacy (sync) | Replacement (async) |
| --- | --- |
| `Libs.ResourcesLib` (Bot properties) | `Libs.ResourcesLibv2` (`db.bot`) |
| Old `refLib` (`REFLIB_*` keys) | `Libs.refLib` (`rfl:*` keys) |
| Old `translate` (`User.setProperty`) | `Libs.translate` (`db.user`) |

Legacy and async `db` data are **separate** — migration requires a one-time copy command.

---

## Pages in this section

| Page | Covers |
| --- | --- |
| [random](random.md) | Numbers, strings, UUIDs, distributions |
| [dateTimeFormat](date-time-format.md) | Formatting, timestamps, diffs |
| [tgutil](tgutil.md) | Names, mentions, escaping |
| [ResourcesLib](resourceslib.md) | Economy, growth, transfers, batch spend |
| [refLib](reflib.md) | Referral engine, leaderboard, stats |
| [translate](translate.md) | Multi-language, providers, language picker |
| [cooldown](cooldown.md) | Per-user and global cooldowns |
| [MCL](mcl.md) | Channel membership checks |
