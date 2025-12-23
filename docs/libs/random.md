## random

The **random** library provides utilities for generating **random values** of different types.

It is useful for simulations, testing, games, unique identifiers, and dynamic content generation.

random is available through the `Libs` instance.

## Random Integer

Generate a random integer within a range.

```js
let num = Libs.random.randomInt(1, 10)
```

This returns a number between `1` and `10`.

## Random String

Generate a random string with custom length and character set.

```js
let str = Libs.random.randomString(
  8,
  { charset: "alpha" }
)
```

This generates an 8-character alphabetic string.

## Random Date

Generate a random date within a given range.

```js
let date = Libs.random.randomDate(
  new Date(2023, 0, 1),
  new Date(2025, 0, 1)
)
```

## Random Color

Generate a random color value.

```js
let color = Libs.random.randomColor("rgb")
```

## Notes

- Supports numbers, strings, dates, and colors
- Useful for games, testing, and mock data
- No setup required

## Full Documentation

[random Documentation]

[random Documentation]: https://github.com/telebothost/tbl-libs/blob/main/Lib-Docs/random.md