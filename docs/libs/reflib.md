# refLib

Want users to invite friends and track who brought whom? **`Libs.refLib`** builds referral links, detects when someone arrives via a link, and keeps a leaderboard — without you hand-rolling deep-link parsing.

All methods are **synchronous**. No `await`.

---

## What is it?

`Libs.refLib` builds referral links, tracks who invited whom, and maintains a leaderboard.

Access: `Libs.refLib.<method>()`

The flow in plain English:

1. User shares `https://t.me/YourBot?start=user123456`
2. New user opens the link → `/start user123456`
3. `track()` detects the deep link via `params` and records the referral
4. Referrer's count and leaderboard update automatically

Referral data is stored in user and bot properties (`REFLIB_*` keys).

---

## How to use it

**Step 1:** Call `track()` once per session — typically in your `/start` command or master script:

```js
Libs.refLib.track({
  onAttracted: (referrer) => {
    Bot.sendMessage(chat.id, "Welcome! Referred by " + referrer.first_name)
  }
})
```

**Step 2:** Give users their link:

```js
let link = Libs.refLib.getLink()
Bot.sendMessage(chat.id, "Share this: " + link)
```

Without `track()`, deep links won't be detected. The library can't read minds — only `params`.

!!! tip "Globals"
    `params` holds the text after `/start` (e.g. `/start user123` → `params` is `"user123"`). See [Global Variables](../globals/index.md).

---

## Try it — beginner examples

### /mylink command

```js
// Command: /mylink
Bot.sendMessage(chat.id,
  "Your referral link:\n" + Libs.refLib.getLink() +
  "\n\nReferrals: " + Libs.refLib.getRefCount()
)
```

### Reward the referrer

```js
Libs.refLib.track({
  onAttracted: (referrer) => {
    let count = Libs.refLib.getRefCount(referrer.id)
    let reward = 10 + (count % 10 === 0 ? 50 : 0)

    Api.sendMessage({
      chat_id: referrer.id,
      text: user.first_name + " joined via your link! +" + reward + " points (total: " + count + ")"
    })
  }
})
```

### Leaderboard command

```js
// Command: /toprefs
let leaders = Libs.refLib.getTopList()
let lines = Object.entries(leaders)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 10)
  .map(([id, count], i) => (i + 1) + ". User " + id + ": " + count)

Bot.sendMessage(chat.id, "Top referrers:\n" + lines.join("\n"))
```

---

## Setup — `track(options)`

Initialize tracking. Call once per session when a user interacts with the bot.

```js
Libs.refLib.track({
  onAttracted: (referrer) => {
    // New user arrived via someone's link
    Bot.sendMessage(chat.id, "Referred by " + referrer.first_name)
  },

  onTouchOwnLink: () => {
    // User clicked their own referral link
    Bot.sendMessage(chat.id, "That's your own link — share it with friends!")
  },

  onAlreadyAttracted: () => {
    // User already has a referrer
    let ref = Libs.refLib.getAttractedBy()
    if (ref) {
      Bot.sendMessage(chat.id, "You were invited by " + ref.first_name)
    }
  }
})
```

| Event | When it fires |
| --- | --- |
| `onAttracted(referrer)` | New user joined via a valid referral link |
| `onTouchOwnLink()` | User opened their own referral link |
| `onAlreadyAttracted()` | User already attributed to a referrer |

`track()` only processes deep links when `message` starts with `/start` and `params` contains the referral prefix.

---

## Generating links — `getLink(botName?, prefix?)`

| Param | Default | Description |
| --- | --- | --- |
| `botName` | `bot.name` | Bot username for the `t.me` URL |
| `prefix` | `"user"` | Start parameter prefix |

```js
// Default: https://t.me/MyBot?start=user5723455420
let link = Libs.refLib.getLink()

// Custom bot name and prefix
let promo = Libs.refLib.getLink("MyBot", "promo")
// https://t.me/MyBot?start=promo5723455420
```

Also stores referrer info in bot properties so attracted users can be resolved later.

---

## Data methods

### `getRefCount(userId?)`

Referral count for a user. Defaults to current user.

```js
let myCount = Libs.refLib.getRefCount()
let theirCount = Libs.refLib.getRefCount(123456789)
```

### `getRefList(userId?)`

Array of referral objects:

```js
let list = Libs.refLib.getRefList()
// [{ id, username, first_name, last_name, date }, ...]
```

### `getAttractedBy()`

Who referred the current user — or `null`.

```js
let referrer = Libs.refLib.getAttractedBy()
if (referrer) {
  Bot.sendMessage(chat.id, "Invited by " + referrer.first_name)
}
```

### `getTopList()`

All users' referral counts as an object `{ userId: count, ... }`.

```js
let leaders = Libs.refLib.getTopList()
let top = Object.entries(leaders)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 10)
```

---

## Method reference

| Method | Parameters | Returns |
| --- | --- | --- |
| `track(options)` | event handlers object | `void` |
| `getLink(botName?, prefix?)` | optional bot name, prefix | referral URL string |
| `getRefCount(userId?)` | optional user ID | `number` |
| `getRefList(userId?)` | optional user ID | array of referral objects |
| `getAttractedBy()` | — | referrer object or `null` |
| `getTopList()` | — | `{ userId: count }` object |

---

## Master script pattern

```js
// In your @ master script or /start command
Libs.refLib.track({
  onAttracted: (referrer) => {
    Bot.sendMessage(chat.id, "Welcome! Invited by " + referrer.first_name)
  }
})
```

---

## Storage

refLib uses internal property keys prefixed with `REFLIB_`:

| Key | Scope | Content |
| --- | --- | --- |
| `REFLIB_refList` | Per user | Array of referred users |
| `REFLIB_refsCount` | Per user | Referral count |
| `REFLIB_attracted_by_user` | Per user | Referrer info |
| `REFLIB_topList` | Bot-wide | Leaderboard |
| `REFLIB_refLinkPrefix` | Bot-wide | Registered link prefixes |

---

## Notes

- Method name is `getLink()` — not `getRefLink()`
- `track()` must be called for deep-link detection to work
- Deep links use the `params` global (e.g. `/start user123` → `params` is `"user123"`)
- A user can only be attributed to one referrer
- All methods are sync — no `await`
