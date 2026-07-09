# randomstring

Random characters on demand — codes, temp passwords, and "guess this" tokens.

## What is it?

**randomstring** generates random alphanumeric strings with configurable length and character sets. Shorter and more flexible than a full UUID when you need a promo code, one-time password, or referral slug.

Access it as `modules.randomstring`.

---

## How to use

Generate a 10-character string:

```js
let str = modules.randomstring.generate(10)
// "a1b2c3d4e5"
```

Pass a number for length, or an options object for finer control.

---

## API reference

| Call | Description |
| --- | --- |
| `generate(length)` | Random string of given length |
| `generate(options)` | Random string with custom options |

Options object:

| Option | Description |
| --- | --- |
| `length` | String length (1–256) |
| `charset` | Predefined: `"alphanumeric"`, `"numeric"`, `"alphabetic"` |
| `readable` | Exclude ambiguous chars (`0`, `O`, `l`, `1`) |
| `charset` (custom) | Your own character set string |

---

## Try it

### Generate a promo code

[Bot](../bot-instance/index.md) sends to [chat](../globals/chat.md):

```js
let code = modules.randomstring.generate({
  length: 8,
  charset: "alphanumeric",
  readable: true
}).toUpperCase()

Bot.sendMessage(chat.id, "Your promo code: " + code)
```

### Create a one-time password

Save it in [db](../db-instance/index.md) for [user](../globals/user.md) to verify later:

```js
let otp = modules.randomstring.generate({ length: 6, charset: "numeric" })
db.user.set("otp", otp)
db.user.set("otp_expires", Date.now() + 300000)  // 5 minutes

Bot.sendMessage(chat.id, "Your one-time code: " + otp + " (expires in 5 min)")
```

### Numeric PIN

```js
let pin = modules.randomstring.generate({ length: 4, charset: "numeric" })
Bot.sendMessage(chat.id, "Your PIN: " + pin)
```

---

## Limits

| Limit | Value |
| --- | --- |
| `generate` length | 1–256 characters |
| Method | Sync |

---

## Notes

- **Sync** — no `await` needed
- For standard UUIDs (longer, collision-resistant), see [UUID](uuid.md)
- `readable: true` helps when humans need to type the code
- Official package: [randomstring on npm](https://www.npmjs.com/package/randomstring)
