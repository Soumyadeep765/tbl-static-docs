# validator

"Is this a real email?" — and a dozen other sanity checks before you process input.

## What is it?

**validator** validates and sanitizes strings: emails, URLs, phone numbers, credit cards, dates, and more. Run a quick check before you save data, send a confirmation, or let a user proceed to the next step.

Access it as `modules.validator` — the full [validator.js](https://github.com/validatorjs/validator.js) library.

---

## How to use

Check if a string is a valid email:

```js
let valid = modules.validator.isEmail("email@example.com")
// true
```

Returns `true` or `false`. No throwing, no drama.

**Sync** — no `await` needed.

---

## Popular methods

| Method | Checks |
| --- | --- |
| `isEmail(str)` | Valid email format |
| `isURL(str, options?)` | Valid URL |
| `isMobilePhone(str, locale?)` | Phone number |
| `isNumeric(str)` | Numeric string |
| `isAlphanumeric(str)` | Letters and numbers only |
| `isLength(str, options)` | Min/max length (`{ min: 3, max: 20 }`) |
| `isInt(str, options?)` | Integer |
| `isFloat(str, options?)` | Float |
| `isUUID(str, version?)` | UUID format |
| `isJSON(str)` | Valid JSON string |
| `isCreditCard(str)` | Credit card number (Luhn check) |
| `isDate(str)` | Date string |
| `contains(str, seed)` | Contains substring |
| `equals(str, comparison)` | Exact match |
| `trim(str)` | Trim whitespace (sanitizer) |
| `escape(str)` | Escape HTML entities (sanitizer) |

See the [full method list](https://github.com/validatorjs/validator.js) for 50+ validators and sanitizers.

---

## Try it

### Validate email from command input

[Bot](../bot-instance/index.md) replies in [chat](../globals/chat.md). [`params`](../globals/params.md) is what the user typed after your command:

```js
if (!modules.validator.isEmail(params)) {
  return Bot.sendMessage("That doesn't look like an email. Try again.")
}
Bot.sendMessage("Email accepted. Welcome aboard!")
```

### Validate a URL before fetching

```js
let url = params.trim()

if (!modules.validator.isURL(url, { require_protocol: true })) {
  return Bot.sendMessage("Please send a valid URL starting with http:// or https://")
}

Bot.sendMessage("URL looks good. Fetching...")
```

### Check password length

```js
let password = params

if (!modules.validator.isLength(password, { min: 8, max: 128 })) {
  return Bot.sendMessage("Password must be 8–128 characters.")
}

Bot.sendMessage("Password length OK. Now hash it with bcrypt.")
```

---

## Notes

- **Sync** — no `await` needed
- Validators check **format**, not whether an email actually exists or a URL returns 200
- For structured object validation (schemas with multiple fields), see [zod](zod.md)
- Official docs: [validator.js on GitHub](https://github.com/validatorjs/validator.js)
