# dayjs

Moment.js retired. dayjs kept the date formatting, lost the baggage.

## What is it?

**dayjs** is a tiny library for parsing, formatting, and comparing dates. Need "today as YYYY-MM-DD", "3 days from now", or "how long until Friday"? dayjs handles it without pulling in a small moon's worth of JavaScript.

Access it as `modules.dayjs`.

---

## How to use

Call it like a function — no setup required:

```js
let today = modules.dayjs().format("YYYY-MM-DD")
// "2025-09-19"
```

Format tokens follow standard dayjs conventions: `YYYY`, `MM`, `DD`, `HH`, `mm`, `ss`, and friends.

---

## Common methods

| Method | Example | Result |
| --- | --- | --- |
| `.format(pattern)` | `modules.dayjs().format("DD/MM/YYYY")` | `"19/09/2025"` |
| `.add(n, unit)` | `modules.dayjs().add(7, "day")` | Date 7 days ahead |
| `.subtract(n, unit)` | `modules.dayjs().subtract(1, "month")` | Date 1 month ago |
| `.diff(other, unit)` | `modules.dayjs().diff(target, "day")` | Difference in days |
| `.isBefore(other)` | `modules.dayjs().isBefore(deadline)` | `true` / `false` |
| `.unix()` | `modules.dayjs().unix()` | Unix timestamp (seconds) |

Units include `"day"`, `"hour"`, `"minute"`, `"month"`, `"year"`, etc.

---

## Try it

### Show today's date in a message

[Bot](../bot-instance/index.md) sends to the current [chat](../globals/chat.md):

```js
let formatted = modules.dayjs().format("dddd, MMMM D, YYYY")
Bot.sendMessage("Today is " + formatted)
```

### Countdown to a deadline

```js
let deadline = modules.dayjs("2025-12-31")
let daysLeft = deadline.diff(modules.dayjs(), "day")

if (daysLeft > 0) {
  Bot.sendMessage(daysLeft + " days until the deadline. No pressure.")
} else {
  Bot.sendMessage("Deadline passed. Hope you finished.")
}
```

### Store a timestamp

```js
let now = modules.dayjs().format()
db.user.set("last_seen", now)
Bot.sendMessage("Logged your visit at " + now)
```

---

## Notes

- **Sync** — no `await` needed
- Replaces the retired `moment` module — see [Retired modules](index.md#retired-modules)
- For human-readable durations ("3 hours" instead of `10800000`), see [humanizeDuration](humanize-duration.md)
- For TBL-specific date helpers, [Libs.dateTimeFormat](../libs/date-time-format.md) is also available
- Official docs: [dayjs on npm](https://www.npmjs.com/package/dayjs)
