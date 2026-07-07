# TBL Libraries (Libs)

`Libs` provides **built-in helper libraries** for common bot tasks — random values, dates, resources, referrals, Telegram formatting, and channel membership checks.

```js
let roll = Libs.random.randomInt(1, 6)
let now = Libs.dateTimeFormat.getCurrentDate("isoDateTime")
let joined = await Libs.mcl.quick(user.id, ["@MyChannel"])
```

No imports or setup required. Access any library as `Libs.<libraryName>.<method>()`.

---

## Available libraries

| Library | Access | Sync / Async | Page |
| --- | --- | --- | --- |
| `random` | `Libs.random.*` | Sync | [random](random.md) |
| `dateTimeFormat` | `Libs.dateTimeFormat.*` | Sync | [dateTimeFormat](date-time-format.md) |
| `tgutil` | `Libs.tgutil.*` | Sync | [tgutil](tgutil.md) |
| `ResourcesLib` | `Libs.ResourcesLib.*` | Sync | [ResourcesLib](resourceslib.md) |
| `refLib` | `Libs.refLib.*` | Sync | [refLib](reflib.md) |
| `mcl` | `Libs.mcl.*` | **Async** — use `await` | [MCL](mcl.md) |

Source code: [telebothost/tbl-libs](https://github.com/telebothost/tbl-libs) on GitHub.

---

## How Libs works

Libraries are loaded from TBL's global lib registry and run inside a **sandboxed VM**:

| Behaviour | Detail |
| --- | --- |
| Lazy loading | Each library loads on first access (`Libs.random`, `Libs.mcl`, etc.) |
| Immutable | `Libs` cannot be modified — assignments throw `[LibsError] Immutable` |
| Method timeout | Each method call is capped at **2 seconds** (max), minimum **500 ms** |
| Init timeout | Library initialization also capped at **2 seconds** |
| Async methods | Return Promises — always use `await` (`.then` is not supported in TBL) |
| Sync methods | Return values directly — no `await` needed |
| Circular deps | Detected and throw `[LibsError] Circular dependency` |
| TBL access | Libraries can use `Bot`, `Api`, `user`, `chat`, and other TBL globals during execution |

### Sync vs async

```js
// Sync — immediate return
let n = Libs.random.randomInt(1, 100)
let name = Libs.tgutil.getFullName(user)

// Async — must await
let result = await Libs.mcl.check(user.id, ["@Channel1"])
let ok = await Libs.mcl.quick(user.id, ["@Channel1"])
```

### Error format

Lib errors are prefixed with `[LibsError]`:

| Error | Cause |
| --- | --- |
| `[LibsError] Timeout: mcl.check` | Method exceeded 2-second limit |
| `[LibsError] InitFail: mcl -> ...` | Library failed to initialize |
| `[LibsError] Immutable: Cannot modify libraries` | Attempted to assign to `Libs` |
| `[LibsError] Circular dependency: X` | Lib A imports Lib B which imports Lib A |

---

## Quick examples by task

### Random dice roll

```js
let roll = Libs.random.randomInt(1, 6)
Bot.sendMessage(chat.id, "You rolled: " + roll)
```

### Format today's date

```js
let today = Libs.dateTimeFormat.getCurrentDate("isoDate")
Bot.sendMessage(chat.id, "Today: " + today)
```

### Mention a user safely

```js
let mention = Libs.tgutil.getUserMention(user, { parseMode: "html" })
Bot.sendMessage(chat.id, "Hello " + mention, { parse_mode: "HTML" })
```

### User coin balance

```js
let coins = Libs.ResourcesLib.userRes("coins")
coins.add(10)
Bot.sendMessage(chat.id, "Balance: " + coins.value())
```

### Referral link

```js
Libs.refLib.track({ onAttracted: (referrer) => {
  Bot.sendMessage(chat.id, "Referred by " + referrer.first_name)
}})

let link = Libs.refLib.getLink()
Bot.sendMessage(chat.id, "Share: " + link)
```

### Force channel join

```js
let ok = await Libs.mcl.quick(user.id, ["@MyChannel", "@MyGroup"])

if (!ok) {
  let text = await Libs.mcl.summaryText(user.id, ["@MyChannel", "@MyGroup"])
  let buttons = Libs.mcl.getBtn(["@MyChannel", "@MyGroup"])
  Api.sendMessage({ chat_id: chat.id, text, reply_markup: { inline_keyboard: buttons } })
}
```

---

## Availability

| Context | `Libs` |
| --- | --- |
| Normal Telegram commands | ✓ |
| Webhook / webapp | ✓ |
| HTTP callback commands | ✓ |
| Broadcast commands | ✓ |

---

## Libs vs Modules

| | `Libs` | `Modules` |
| --- | --- | --- |
| What | Built-in TBL helper libraries | Curated npm-style packages |
| Access | `Libs.random.randomInt()` | `Modules.crypto`, etc. |
| Setup | None | None |
| Best for | Bot-specific helpers (referrals, MCL, resources) | General utilities (crypto, encoding) |

See [Modules](../modules/index.md) for the modules reference.

---

## Pages in this section

| Page | Covers |
| --- | --- |
| [random](random.md) | Numbers, strings, colors, UUIDs, distributions |
| [dateTimeFormat](date-time-format.md) | Formatting, arithmetic, timestamps, diffs |
| [tgutil](tgutil.md) | Names, mentions, links, escaping |
| [ResourcesLib](resourceslib.md) | User/chat/global numeric resources, growth |
| [refLib](reflib.md) | Referral links, tracking, leaderboard |
| [MCL](mcl.md) | Channel/group membership checks |
