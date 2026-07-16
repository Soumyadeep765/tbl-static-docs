# refLib

Referral engine — build invite links, track who brought whom, maintain a leaderboard. Uses async [`db.user`](../db-instance/user.md) and [`db.bot`](../db-instance/bot.md). **All methods need `await`.**

---

## What is it?

`Libs.refLib` handles the full referral lifecycle:

1. User shares `https://t.me/YourBot?start=ref123456`
2. New user opens link → `/start ref123456`
3. `track()` parses `params`, attributes the referral, updates counts
4. Leaderboard cache updates automatically

| Feature | Implementation |
| --- | --- |
| Referral count | `db.user.incr` (atomic) |
| Referral list | `db.user.push` (append-only) |
| Leaderboard | Bounded top-50 cache on `db.bot` |
| Profile cache | `db.bot` on `register()` |

!!! warning "Storage keys changed"
    v1 used `REFLIB_*` (deprecated `Bot`/`User` properties). v1.0.0 uses `rfl:*` keys on async `db`. Data does not auto-migrate.

---

## How to use it

**Step 1** — Track in `/start`:

```js
let result = await Libs.refLib.track({
  prefixes: ["ref", "vip"],
  onJoin: async ({ referrer, count }) => {
    Bot.sendMessage("Welcome! Referred by " + referrer.first_name)
    Api.sendMessage({
      chat_id: referrer.id,
      text: user.first_name + " joined! You now have " + count + " referrals."
    })
  },
  onSelf: async () => Bot.sendMessage("That's your own link!"),
  onRepeat: async () => Bot.sendMessage("Already registered."),
  onOrganic: async () => {} // normal /start, no code
})
```

`result.type` is `"join"` | `"self"` | `"repeat"` | `"organic"`.

**Step 2** — Give users their link (in `/mylink`):

```js
let url = await Libs.refLib.register({ prefix: "ref" })
Bot.sendMessage("Share: " + url)
```

`register()` caches profile + saves prefix. `link()` builds the URL string with zero db I/O.

---

## Core methods

| Method | Returns | Description |
| --- | --- | --- |
| `track(handlers)` | `{ type, ... }` | Process current update + fire events |
| `configure({ prefixes })` | void | Set default link prefixes (skip db read) |
| `link({ bot, prefix })` | string | Build URL (sync, no db) |
| `register({ prefix, bot })` | string | Cache profile + register prefix + return URL |
| `count(userId?)` | number | Referral count |
| `referrer()` | object\|null | Who referred current user |
| `isReferred()` | boolean | Has a referrer |
| `list(userId?, { limit })` | array | Referral list |
| `leaderboard(top?)` | array | `[{ userId, count, rank }]` |
| `rank(userId?)` | number | Leaderboard rank (0 = unranked) |
| `stats(userId?)` | object | Dashboard bundle (one mget) |
| `addCount(userId, amount?)` | number | Manual increment (admin/rewards) |

### Legacy aliases (still work)

| Old | New |
| --- | --- |
| `getLink()` | `register()` |
| `getRefCount()` | `count()` |
| `getAttractedBy()` | `referrer()` |
| `getRefList()` | `list()` |
| `getTopList()` | `leaderboardMap()` |
| `onAttracted` | `onJoin` |
| `onTouchOwnLink` | `onSelf` |
| `onAlreadyAttracted` | `onRepeat` |

---

## Examples

### /mylink command

```js
let s = await Libs.refLib.stats()
Bot.sendMessage("Referrals: " + s.count + "\n" +
  "Rank: " + (s.rank || "unranked") + "\n" +
  "Link: " + s.link
)
```

### Leaderboard

```js
let top = await Libs.refLib.leaderboard(10)
let text = top.map(r => r.rank + ". User " + r.userId + ": " + r.count).join("\n")
Bot.sendMessage("Top referrers:\n" + text)
```

### Reward on join

```js
await Libs.refLib.track({
  onJoin: async ({ referrer, count }) => {
    let gold = Libs.ResourcesLibv2.userRes("gold")
    // reward referrer via anotherUserRes
    let refGold = Libs.ResourcesLibv2.anotherUserRes("gold", referrer.telegramid || referrer.id)
    await refGold.add(10)
    if (count % 10 === 0) await refGold.add(50) // milestone bonus
  }
})
```

---

## Storage keys

| Key | Scope | Purpose |
| --- | --- | --- |
| `rfl:ct` | `db.user` | Referral count (incr) |
| `rfl:by` | `db.user` | Referrer snapshot |
| `rfl:ls` | `db.user` | Referral list (push) |
| `rfl:og` | `db.user` | Organic user flag |
| `rfl:top` | `db.bot` | Top 50 leaderboard |
| `rfl:px` | `db.bot` | Registered link prefixes |
| `rfl:lk:{id}` | `db.bot` | Profile cache |

---

## Important notes

- Always `await` — every method is async
- Call `track()` in `/start` (or master script) so `params` is parsed
- Use `register()` in `/mylink`, not on every message
- `configure({ prefixes: ["ref"] })` avoids a db read on the hot path
- `db` rate limit: 10 calls/second per command — attribution uses ~5 calls

[Database overview](../db-instance/index.md)
