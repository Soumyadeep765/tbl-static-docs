# random

`Libs.random` generates random values — numbers, strings, colors, dates, UUIDs, and more. All methods are **synchronous** (no `await` needed).

```js
let roll = Libs.random.randomInt(1, 6)
let code = Libs.random.randomString(8, { charset: "numeric" })
```

---

## Basic numbers

| Method | Parameters | Returns | Example |
| --- | --- | --- | --- |
| `randomInt(min, max, inclusive?)` | min, max, inclusive (default `true`) | `number` | `randomInt(1, 6)` → `4` |
| `randomFloat(min, max, precision?)` | min, max, decimal places | `number` | `randomFloat(0, 1, 3)` → `0.573` |
| `randomBoolean(probability?)` | 0–1 chance of `true` (default `0.5`) | `boolean` | `randomBoolean(0.3)` |
| `randomRange(min, max, step?)` | min, max, optional step | `number` | `randomRange(0, 100, 5)` → `25` |
| `randomUniqueInts(min, max, count, sorted?)` | range, count, sort flag | `number[]` | `randomUniqueInts(1, 50, 6, true)` |

```js
// Dice
let dice = Libs.random.randomInt(1, 6)

// Lottery numbers (sorted, unique)
let picks = Libs.random.randomUniqueInts(1, 50, 6, true)
Bot.sendMessage(chat.id, picks.join(", "))
```

---

## Collections

| Method | Parameters | Returns |
| --- | --- | --- |
| `randomChoice(arr, count?, unique?)` | array, count (default 1), unique flag | element or array |
| `randomShuffle(arr, inPlace?)` | array, mutate original? | shuffled array |
| `randomWeighted(items, weights, normalize?)` | items, weight array | one item |
| `randomSample(arr, n, weights?)` | array, sample size | array of items |
| `randomFromObject(obj, deep?)` | object, deep traverse? | random value |

```js
let prize = Libs.random.randomChoice(["gold", "silver", "bronze"])
let hand = Libs.random.randomChoice(["A","K","Q","J","10"], 5, true)
let winner = Libs.random.randomWeighted(["A","B","C"], [1, 3, 10])
```

---

## Strings and tokens

| Method | Parameters | Returns |
| --- | --- | --- |
| `randomString(length?, options?)` | length (default 10), `{ charset, custom }` | `string` |
| `randomPassword(length?, options?)` | length, `{ upper, lower, numbers, special }` | `string` |
| `randomToken(length?)` | hex length (default 32) | `string` |
| `randomUuid(version?)` | `4` (default) or `1` | `string` |

### `charset` values for `randomString`

| Value | Characters |
| --- | --- |
| `"alphanumeric"` | A–Z, a–z, 0–9 (default) |
| `"alpha"` | A–Z, a–z |
| `"numeric"` | 0–9 |
| `"symbols"` | `!@#$%^&*()_+-=[]{}|;:,.<>?` |
| custom | Pass `{ custom: "ABC123" }` |

```js
let pin = Libs.random.randomString(6, { charset: "numeric" })
let token = Libs.random.randomToken(32)
let id = Libs.random.randomUuid()
let pwd = Libs.random.randomPassword(16, { upper: 3, lower: 3, numbers: 4, special: 2 })
```

---

## Colors

`randomColor(type?, alpha?)` — types: `"hex"` (default), `"rgb"`, `"hsl"`.

```js
Libs.random.randomColor()              // "#a3f5c2"
Libs.random.randomColor("rgb")         // "rgb(120, 45, 200)"
Libs.random.randomColor("rgb", true)   // "rgba(120, 45, 200, 0.73)"
```

---

## Dates

`randomDate(startDate, endDate, format?)` — returns a `Date` object, or a locale string if `format` is provided.

```js
let randomDay = Libs.random.randomDate(
  new Date(2024, 0, 1),
  new Date()
)
```

---

## Network and geo

| Method | Parameters | Returns |
| --- | --- | --- |
| `randomIp(version?)` | `4` (default) or `6` | IP string |
| `randomGeoPoint(latRange?, lonRange?, precision?)` | coordinate ranges | `{ latitude, longitude }` |
| `randomEmail(domains?)` | domain array | email string |

```js
let ip = Libs.random.randomIp(4)       // "192.168.1.42"
let email = Libs.random.randomEmail(["company.com", "test.org"])
```

---

## Statistical distributions

| Method | Parameters | Description |
| --- | --- | --- |
| `randomNormal(mean?, stdDev?, truncate?)` | mean, std dev, `[min,max]` clip | Gaussian distribution |
| `randomExponential(lambda?)` | rate parameter | Exponential distribution |
| `randomBinomial(n, p)` | trials, probability | Binomial count |
| `randomNoise(length, amplitude?, frequency?)` | signal params | Sine noise array |

```js
let sample = Libs.random.randomNormal(0, 1, [-3, 3])
let failures = Libs.random.randomBinomial(10, 0.3)
```

---

## Matrices and sequences

| Method | Parameters | Returns |
| --- | --- | --- |
| `randomMatrix(rows, cols, generator?, args?)` | dimensions, fn, args | 2D array |
| `randomSequence(length, generator?, args?)` | length, fn, args | array |
| `randomPermutation(n)` | size n | shuffled index array |
| `randomLorem(words?)` | word count (default 10) | lorem ipsum string |

```js
let grid = Libs.random.randomMatrix(3, 3, Libs.random.randomInt, [1, 9])
let digits = Libs.random.randomSequence(6, Libs.random.randomInt, [0, 9])
```

---

## Practical examples

### Coin flip

```js
let flip = Libs.random.randomBoolean()
Bot.sendMessage(chat.id, flip ? "Heads!" : "Tails!")
```

### Giveaway winner

```js
let entrants = [111, 222, 333, 444]
let winner = Libs.random.randomChoice(entrants)
Bot.sendMessage(chat.id, "Winner: " + winner)
```

### Promo code

```js
let code = Libs.random.randomString(8, { charset: "alphanumeric" })
Bot.sendMessage(chat.id, "Your code: " + code.toUpperCase())
```

---

## Notes

- All methods are **sync** — no `await`
- Uses `Math.random()` — not cryptographically secure; use `Modules.crypto` for security-sensitive tokens
- Methods are capped at the Libs **2-second timeout** (only relevant for very heavy custom generators passed to `randomMatrix` / `randomSequence`)
