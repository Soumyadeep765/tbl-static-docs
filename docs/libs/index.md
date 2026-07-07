# TBL Libraries (Libs)

Imagine a Swiss Army knife that only opens Telegram-bot-shaped problems — dice rolls, referral links, coin balances, "did they join the channel?" gates. That's **`Libs`**.

No imports, no setup, no "where do I put this file?" Type `Libs.` and pick your tool. Roll a die, format a date, check channel membership — all from your command's **Logic** field.

---

## What are Libs?

**Libs** are TBL-built helper libraries for bot-specific tasks: random values, dates, Telegram formatting, persistent resources, referrals, and channel membership checks.

| You get | You skip |
| --- | --- |
| Bot-focused helpers (MCL, refLib, ResourcesLib) | Writing glue code from scratch |
| One global object: `Libs` | Import statements |
| Works in commands, webhooks, webapps | External services for simple stuff |

Every library is accessed as `Libs.<libraryName>.<method>()` — **case-sensitive**. `Libs.random` works. `Libs.Random` does not. Consistency is a lifestyle choice.

---

## How to use them

Drop this in any command's **Logic** field:

```js
let roll = Libs.random.randomInt(1, 6)
Bot.sendMessage(chat.id, "You rolled: " + roll)
```

Three things worth knowing upfront:

1. **`Libs` is already there** — you never import or initialize it.
2. **The object is frozen** — you can't add your own properties to `Libs`. Nice try though.
3. **Some methods need `await`** — MCL talks to Telegram's API and returns Promises. More on that [below](#sync-vs-async).

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md). For general npm-style utilities (JWT, bcrypt, CSV), see [Modules](../modules/index.md).

---

## Libs or Modules?

TBL has two toolboxes. Pick the right drawer before you rummage:

| | `Libs` | `modules` |
| --- | --- | --- |
| What | TBL-built bot helpers (referrals, dice rolls, channel checks) | npm-style packages (crypto, parsing, Web3) |
| Access | `Libs.random.randomInt(1, 6)` | `modules.validator.isEmail(email)` |
| Best for | MCL, referral links, resource balances, Telegram names | JWT, bcrypt, CSV, YAML, Ethereum |

Full Modules docs: [Modules](../modules/index.md).

Still not sure? Rule of thumb: if it's Telegram-bot glue or game economy stuff, check `Libs` first. If you'd normally `npm install` it, check `modules`.

---

## Pick a library

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

## Try it — copy-paste examples

Start simple. Each example only introduces what it needs.

### Roll a dice

No setup — just randomness:

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

Telegram HTML is picky. `tgutil` builds the mention for you:

```js
let mention = Libs.tgutil.getUserMention(user, { parseMode: "html" })
Bot.sendMessage(chat.id, "Hello " + mention + "!", { parse_mode: "HTML" })
```

### User coin balance

Resources persist between command runs — perfect for game economies:

```js
let coins = Libs.ResourcesLib.userRes("coins")
coins.add(10)
Bot.sendMessage(chat.id, "Balance: " + coins.value())
```

### Referral link

Call `track()` once (usually in `/start`) so deep links get detected:

```js
Libs.refLib.track({ onAttracted: (referrer) => {
  Bot.sendMessage(chat.id, "Referred by " + referrer.first_name)
}})

let link = Libs.refLib.getLink()
Bot.sendMessage(chat.id, "Share: " + link)
```

### Force channel join (async)

MCL checks live membership via Telegram — **always `await`**:

```js
let ok = await Libs.mcl.quick(user.id, ["@MyChannel", "@MyGroup"])

if (!ok) {
  let text = await Libs.mcl.summaryText(user.id, ["@MyChannel", "@MyGroup"])
  let buttons = Libs.mcl.getBtn(["@MyChannel", "@MyGroup"])
  Api.sendMessage({ chat_id: chat.id, text, reply_markup: { inline_keyboard: buttons } })
}
```

MCL details: [MCL](mcl.md)

---

## How Libs works

The internals — useful when something breaks, skippable when you're vibing:

| Behaviour | Detail |
| --- | --- |
| Lazy loading | Each library loads on first access (`Libs.random`, `Libs.mcl`, etc.) |
| Immutable | `Libs` cannot be modified — assignments throw `[LibsError] Immutable` |
| Method timeout | Each method call is capped at **2 seconds** (max), minimum **500 ms** |
| Init timeout | Library initialization also capped at **2 seconds** |
| Async methods | Return Promises — always use `await` (`.then` is not supported in TBL) |
| Sync methods | Return values directly — no `await` needed |
| Circular deps | Detected and throw `[LibsError] Circular dependency` |
| Globals access | Libraries can use `Bot`, `Api`, `user`, `chat`, and other globals during execution |

---

## Sync vs async

Most Libs methods are synchronous — call them like any function. **MCL is the exception** — it asks Telegram whether someone joined a channel, so every check method returns a Promise:

| Library | Async methods |
| --- | --- |
| `mcl.check()`, `quick()`, `getLeftChannels()`, etc. | Yes — returns Promise |
| `mcl.getBtn()` | No — sync |
| `random`, `dateTimeFormat`, `tgutil`, `ResourcesLib`, `refLib` | Sync |

```js
// Async — don't forget await
let ok = await Libs.mcl.quick(user.id, ["@Channel1"])
let result = await Libs.mcl.check(user.id, ["@Channel1"])

// Sync — just call it
let roll = Libs.random.randomInt(1, 6)
let name = Libs.tgutil.getFullName(user)
let buttons = Libs.mcl.getBtn(["@Channel1"])  // no await here
```

Forget `await` on an async MCL method and you'll get a Promise object instead of `true`/`false`. JavaScript's favorite prank — and your gate will let everyone through.

---

## Error format

Lib errors are prefixed with `[LibsError]`:

| Error | Cause |
| --- | --- |
| `[LibsError] Timeout: mcl.check` | Method exceeded 2-second limit |
| `[LibsError] InitFail: mcl -> ...` | Library failed to initialize |
| `[LibsError] Immutable: Cannot modify libraries` | Attempted to assign to `Libs` |
| `[LibsError] Circular dependency: X` | Lib A imports Lib B which imports Lib A |

---

## Where Libs works

| Context | `Libs` available? |
| --- | --- |
| Normal Telegram commands | ✓ |
| Webhook / webapp | ✓ |
| HTTP callback commands | ✓ |
| Broadcast commands | ✓ |

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
