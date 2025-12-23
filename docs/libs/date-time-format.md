## dateTimeFormat

dateTimeFormat provides utilities for **date and time formatting, calculations, and comparisons**.

It is useful for working with timestamps, scheduling logic, and displaying dates in a human-readable format.

dateTimeFormat is available through the `Libs` instance.

## Get Current Date and Time

Get the current date/time using a custom format mask.

```js
let now = Libs.dateTimeFormat.getCurrentDate(
  "yyyy-mm-dd HH:MM:ss"
)
```

This returns the current date formatted as a string.

## Add Days to a Date

You can add days to a given date.

```js
let future = Libs.dateTimeFormat.addDays(
  new Date(),
  7
)
```

This returns a new date object representing a future date.

## Get Time Difference

Calculate the difference between two dates.

```js
let diff = Libs.dateTimeFormat.getTimeDifference(
  "2025-01-01",
  "2025-02-01"
)
```

This returns the time difference between the two dates.

## Notes

- Supports custom date masks
- Works with both strings and Date objects
- Useful for scheduling, cooldowns, and expiration logic

## Full Documentation

[dateTimeFormat Documentation]

[dateTimeFormat Documentation]: https://github.com/telebothost/tbl-libs/blob/main/Lib-Docs/dateTimeFormat.md