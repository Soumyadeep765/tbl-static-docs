## moment

moment is a powerful library for **date and time manipulation**.

It allows you to easily format, parse, and calculate dates and times.

moment functionality is available through the `modules` object.

## Formatting the Current Date

```js
const dateStr = modules.moment()
  .format("YYYY-MM-DD")
```

This returns the current date formatted as a string.

## Example Output

```
dateStr → "2025-09-19"
```

## Notes

- Supports parsing, formatting, and date calculations
- Works with time zones and locales
- Commonly used for human-readable dates

## Official Documentation

[moment Docs]

[moment Docs]: https://momentjs.com/docs/