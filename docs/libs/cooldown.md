# cooldown

Per-user and bot-wide cooldowns using [`db`](../db-instance/index.md) + TTL. Access: **`Libs.cooldown`**. **All methods need `await`.** v1.0.0

---

## What is it?

Stop users from spamming commands, claiming daily rewards too often, or re-using abilities before a timer expires.

| Type | Scope | Use for |
| --- | --- | --- |
| User cooldown | `db.user` | Per-player timers (daily bonus, attack, spin) |
| Global cooldown | `db.bot` | Bot-wide events (maintenance, global event) |

Storage key: `cd:{name}` — stores expiry timestamp. TTL auto-cleans expired keys.

!!! note "TTL minimum"
    Platform minimum TTL is **60 seconds**. Shorter durations are clamped up automatically.

---

## Quick start

```js
let run = await Libs.cooldown.tryRun("daily_bonus", 86400)
if (!run.ok) {
  return Bot.sendMessage(chat.id,
    "Wait " + await Libs.cooldown.format("daily_bonus")
  )
}
Bot.sendMessage(chat.id, "Bonus claimed!")
```

---

## Core methods

| Method | Description |
| --- | --- |
| `set(name, seconds, userId?)` | Start user cooldown |
| `setGlobal(name, seconds)` | Start bot-wide cooldown |
| `active(name, userId?)` | Is user cooldown active? |
| `activeGlobal(name)` | Is global cooldown active? |
| `remaining(name, userId?)` | Seconds left (0 = ready) |
| `remainingGlobal(name)` | Global seconds left |
| `until(name, userId?)` | Expiry timestamp (ms) |
| `clear(name, userId?)` | Remove user cooldown |
| `clearGlobal(name)` | Remove global cooldown |
| `tryRun(name, seconds, userId?)` | Run if ready, else `{ ok: false, remaining }` |
| `tryRunGlobal(name, seconds)` | Global version |
| `format(name, userId?)` | Human-readable (`"4m 30s"`) |
| `formatGlobal(name)` | Global format |
| `formatSeconds(n)` | Format raw seconds |
| `checkAll(names, userId?)` | Batch check (one mget) |
| `clearCache()` | Reset session cache |

---

## Examples

### Command cooldown (5 min)

```js
if (await Libs.cooldown.active("attack")) {
  return Bot.sendMessage(chat.id,
    "Attack ready in " + await Libs.cooldown.format("attack")
  )
}
await Libs.cooldown.set("attack", 300)
// ... do attack logic
```

### Daily reward with tryRun

```js
let claim = await Libs.cooldown.tryRun("daily", 86400)
if (!claim.ok) {
  return Bot.sendMessage(chat.id, "Daily reward in " + claim.remaining + "s")
}
let gold = Libs.ResourcesLibv2.userRes("gold")
await gold.add(100)
Bot.sendMessage(chat.id, "Daily +100 gold!")
```

### Global event lock

```js
await Libs.cooldown.setGlobal("tournament", 3600)
if (await Libs.cooldown.activeGlobal("tournament")) {
  Bot.sendMessage(chat.id, "Tournament running! Ends in " +
    await Libs.cooldown.formatGlobal("tournament"))
}
```

### Check multiple cooldowns

```js
let cds = await Libs.cooldown.checkAll(["daily", "spin", "attack"])
if (cds.spin.active) {
  Bot.sendMessage(chat.id, "Spin ready in " + cds.spin.remaining + "s")
}
```

### With ResourcesLib + refLib

```js
// Only reward referrals once per hour per referrer
let ok = await Libs.cooldown.tryRun("ref_notify_" + referrer.id, 3600, referrer.id)
if (ok.ok) {
  await Libs.ResourcesLibv2.anotherUserRes("gold", referrer.id).add(5)
}
```

---

## Storage

| Key | Scope | Value |
| --- | --- | --- |
| `cd:{name}` | `db.user` | Expiry timestamp (ms) |
| `cd:{name}` | `db.bot` | Global expiry timestamp |

[db.user TTL](../db-instance/user.md) · [db.bot](../db-instance/bot.md)
