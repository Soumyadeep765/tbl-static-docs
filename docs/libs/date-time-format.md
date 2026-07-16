# dateTimeFormat

Dates in JavaScript are powerful and also a little cursed. **`Libs.dateTimeFormat`** handles the boring parts — formatting, arithmetic, comparisons, Unix timestamps — so you can focus on bot logic instead of googling "javascript date add 7 days" for the fifteenth time.

All methods are **synchronous**. No `await`.

---

## What is it?

`Libs.dateTimeFormat` formats dates, adds/subtracts time, compares dates, and converts to/from Unix timestamps. Think of it as your bot's calendar assistant — minus the passive-aggressive meeting reminders.

Access: `Libs.dateTimeFormat.<method>()`

---

## How to use it

The quickest win — today's date as an ISO string:

```js
let today = Libs.dateTimeFormat.getCurrentDate("isoDate")
Bot.sendMessage("Today: " + today)
```

Need a date seven days from now?

```js
let nextWeek = Libs.dateTimeFormat.addDays(new Date(), 7)
Bot.sendMessage("Event date: " + Libs.dateTimeFormat.format(nextWeek, "isoDate"))
```

All methods return immediately — **no `await` needed**.

---

## Try it — beginner examples

### Countdown to an event

```js
let eventDate = Libs.dateTimeFormat.addDays(new Date(), 7)
let diff = Libs.dateTimeFormat.getTimeDifference(new Date(), eventDate)

Bot.sendMessage("Event in " + diff.days + " days, " + (diff.hours % 24) + " hours"
)
```

### Subscription expiry check

```js
let expiry = Libs.dateTimeFormat.addTime(new Date(), { months: 1 })

if (new Date() > expiry) {
  Bot.sendMessage("Subscription expired.")
} else {
  let left = Libs.dateTimeFormat.getTimeDifference(new Date(), expiry)
  Bot.sendMessage("Active — " + left.days + " days left.")
}
```

### Display a join date

```js
let formatted = Libs.dateTimeFormat.format(
  user.joined_at,
  "dddd, mmmm d 'at' h:MM TT"
)
Bot.sendMessage("You joined on " + formatted)
```

---

## Formatting

### `format(date, mask?, utc?, locale?)`

Format any date with a mask string or named preset.

```js
Libs.dateTimeFormat.format(new Date(), "yyyy-mm-dd HH:MM:ss")
// "2025-07-07 14:30:45"

Libs.dateTimeFormat.format(new Date(), "fullDate")
// "Monday, July 7, 2025"
```

| Parameter | Default | Description |
| --- | --- | --- |
| `date` | — | `Date` object or parseable string |
| `mask` | `"default"` | Format pattern or preset name |
| `utc` | `false` | Use UTC |
| `locale` | `"en"` | Locale code |

### Named mask presets

| Preset | Output example |
| --- | --- |
| `"default"` | `Mon Jul 07 2025 14:30:45` |
| `"shortDate"` | `7/7/25` |
| `"mediumDate"` | `Jul 7, 2025` |
| `"longDate"` | `July 7, 2025` |
| `"fullDate"` | `Monday, July 7, 2025` |
| `"shortTime"` | `2:30 PM` |
| `"mediumTime"` | `2:30:45 PM` |
| `"longTime"` | `2:30:45 PM EST` |
| `"isoDate"` | `2025-07-07` |
| `"isoTime"` | `14:30:45` |
| `"isoDateTime"` | `2025-07-07T14:30:45` |
| `"isoUtcDateTime"` | UTC ISO with `Z` suffix |
| `"custom"` | `2025-07-07 14:30:45 EST` |

### `getCurrentDate(mask?, utc?, locale?)`

Shorthand for formatting `new Date()`:

```js
Libs.dateTimeFormat.getCurrentDate("isoDate")     // "2025-07-07"
Libs.dateTimeFormat.getCurrentDate("mediumTime")  // "2:30:45 PM"
```

---

## Format tokens

| Token | Output | Example |
| --- | --- | --- |
| `yyyy` | 4-digit year | `2025` |
| `yy` | 2-digit year | `25` |
| `mmmm` | Full month | `July` |
| `mmm` | Short month | `Jul` |
| `mm` | Padded month | `07` |
| `m` | Month number | `7` |
| `dddd` | Full weekday | `Monday` |
| `ddd` | Short weekday | `Mon` |
| `dd` | Padded day | `07` |
| `d` | Day number | `7` |
| `HH` | 24-hour padded | `14` |
| `H` | 24-hour | `14` |
| `hh` | 12-hour padded | `02` |
| `h` | 12-hour | `2` |
| `MM` | Minutes padded | `30` |
| `ss` | Seconds padded | `45` |
| `TT` | AM/PM | `PM` |
| `Z` | Timezone | `EST` |

---

## Date arithmetic

| Method | Description |
| --- | --- |
| `addDays(date, days)` | Add days — returns new `Date` |
| `subtractDays(date, days)` | Subtract days |
| `addTime(date, { years, months, days, hours, minutes, seconds })` | Add multiple units |
| `subtractTime(date, { years, months, days, hours, minutes, seconds })` | Subtract multiple units |

```js
let tomorrow = Libs.dateTimeFormat.addDays(new Date(), 1)

let expiry = Libs.dateTimeFormat.addTime(new Date(), {
  months: 1,
  days: 0
})

let cooldownEnd = Libs.dateTimeFormat.addTime(new Date(), {
  hours: 0,
  minutes: 30,
  seconds: 0
})
```

---

## Comparison and validation

### `getTimeDifference(date1, date2)`

Returns an object with the difference from `date1` to `date2`:

```js
let diff = Libs.dateTimeFormat.getTimeDifference("2025-01-01", "2025-02-01")
// { milliseconds, seconds, minutes, hours, days }
// days: 31
```

### `isValidDate(date)`

```js
Libs.dateTimeFormat.isValidDate("2025-07-07")  // true
Libs.dateTimeFormat.isValidDate("not-a-date")  // false
```

Always validate user-provided date strings before formatting — invalid dates in `format()` throw `SyntaxError: invalid date`.

### `getTimeZoneOffset(date?)`

Returns timezone offset in minutes (e.g. `-300` for EST).

---

## Unix timestamps

| Method | Description |
| --- | --- |
| `toUnixTimestamp(date)` | Date → Unix seconds |
| `fromUnixTimestamp(timestamp)` | Unix seconds → `Date` |

```js
let ts = Libs.dateTimeFormat.toUnixTimestamp(new Date())  // 1751895045
let date = Libs.dateTimeFormat.fromUnixTimestamp(ts)
```

---

## Localization

Built-in locales: **`en`** (English) and **`hi`** (Hindi). Pass `locale` to `format()` and `getCurrentDate()`.

### `registerLocale(localeCode, localeData)`

Add or update a locale at runtime. Returns the library object (chainable).

| Field | Requirement |
| --- | --- |
| `dayNames` | Exactly 7 short day names (Sun–Sat) |
| `monthNames` | Exactly 12 short month names (Jan–Dec) |

Full weekday and month names (`dddd`, `mmmm`) are auto-generated from the short names.

```js
Libs.dateTimeFormat.registerLocale("es", {
  dayNames: ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"],
  monthNames: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
})

Libs.dateTimeFormat.format(new Date(), "fullDate", false, "es")
// "lunes, abril 7, 2025"
```

### `getLocale(localeCode)`

Returns locale data object or `null` if not registered.

### `getAvailableLocales()`

Returns an array of registered locale codes (e.g. `["en", "hi", "es"]`).

---

## Relative time

### `toRelativeTime(date, now?, locale?)`

Human-readable relative time using `Intl.RelativeTimeFormat`. Falls back to English phrases if the locale is unsupported.

```js
Libs.dateTimeFormat.toRelativeTime(new Date(Date.now() - 3600000))
// "1 hour ago"

Libs.dateTimeFormat.toRelativeTime(new Date(Date.now() + 86400000), new Date(), "hi")
// Hindi relative string when supported
```

| Parameter | Default | Description |
| --- | --- | --- |
| `date` | — | Target date |
| `now` | `new Date()` | Reference point |
| `locale` | `"en"` | BCP 47 locale code |

---

## Notes

- All methods are **sync** — no `await`
- Invalid dates in `format()` throw `SyntaxError: invalid date`
- Use `isValidDate()` before parsing user-provided date strings
- For UTC-sensitive logic, pass `utc: true` to `format()` / `getCurrentDate()`
- Use `toRelativeTime()` for "2 hours ago" style UI; use `format()` for fixed calendar dates
