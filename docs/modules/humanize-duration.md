# humanizeDuration

`10800000` means nothing to humans. "3 hours" means everything.

## What is it?

**humanizeDuration** turns milliseconds into readable text — `"1 hour"`, `"2 days, 5 hours"`, `"45 minutes"`. Use it anywhere you'd otherwise show a raw number and watch users squint.

Access it as `modules.humanizeDuration` (it's a function).

---

## How to use

Pass milliseconds, get words:

```js
let duration = modules.humanizeDuration(3600000)
// "1 hour"
```

One hour = 3,600,000 ms. Math is optional when you have this.

---

## API reference

| Call | Description |
| --- | --- |
| `humanizeDuration(ms)` | Convert milliseconds to human-readable text |
| `humanizeDuration(ms, options)` | With language, units, and formatting options |

Common options:

| Option | Description |
| --- | --- |
| `language` | Locale string (e.g. `"en"`, `"de"`) |
| `units` | Which units to include (`["h", "m"]`, etc.) |
| `largest` | Max number of units to show |
| `round` | Round values |
| `delimiter` | Separator between units |

---

## Try it

### Show time until an event

[Bot](../bot-instance/index.md) sends to [chat](../globals/chat.md):

```js
let ms = 9000000  // 2.5 hours
let readable = modules.humanizeDuration(ms, { largest: 2 })

Bot.sendMessage("Event starts in " + readable)
```

### Format a cooldown for the user

Store a cooldown end timestamp in [db](../db-instance/index.md), then explain the wait:

```js
let cooldownEnd = db.user.get("cooldown_until") || 0
let remaining = cooldownEnd - Date.now()

if (remaining > 0) {
  let wait = modules.humanizeDuration(remaining, { largest: 1 })
  Bot.sendMessage("Slow down — try again in " + wait + ".")
} else {
  Bot.sendMessage("You're good to go!")
}
```

### Compare two timestamps with dayjs

Pair with [dayjs](dayjs.md) to compute the gap, then humanize it:

```js
let expires = modules.dayjs(db.user.get("sub_expires"))
let ms = expires.diff(modules.dayjs())

if (ms > 0) {
  Bot.sendMessage("Subscription expires in " + modules.humanizeDuration(ms))
} else {
  Bot.sendMessage("Subscription expired. Time to renew.")
}
```

---

## Notes

- **Sync** — no `await` needed
- Input is always **milliseconds** — convert seconds with `× 1000`
- For date formatting (not durations), use [dayjs](dayjs.md)
- Official package: [humanize-duration on npm](https://www.npmjs.com/package/humanize-duration)
