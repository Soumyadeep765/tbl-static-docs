# bcrypt

Slow hashes on purpose — that's a feature, not a bug.

## What is it?

**bcrypt** hashes passwords so you can store them safely. Instead of saving `"password123"` in plain text (please don't), you save a one-way hash and check logins with `compare`. It's the industry standard for "I forgot my password but attackers shouldn't either."

Access it as `modules.bcrypt`.

---

## How to use

Hash a password — **both methods return Promises, so use `await`**:

```js
let hash = await modules.bcrypt.hash("password123", 10)
```

The second argument is **salt rounds**. Higher = more secure, slower. `10`–`12` is a sensible range for bots.

Verify a login the same way:

```js
let match = await modules.bcrypt.compare("password123", hash)
// true or false
```

!!! warning "Async — don't skip await"
    `hash()` and `compare()` are **async**. Forget `await` and you'll get a Promise object instead of a hash or boolean. JavaScript's favorite prank.

---

## Methods

| Method | Returns | Description |
| --- | --- | --- |
| `hash(plainText, saltRounds)` | `Promise<string>` | Hash a password |
| `compare(plainText, hash)` | `Promise<boolean>` | Check if password matches hash |

---

## Try it

### Store a hashed password on signup

[`user`](../globals/user.md) is whoever triggered the command. [Bot](../bot-instance/index.md) replies in [chat](../globals/chat.md). Save the hash — never the raw password — in [db](../db-instance/index.md):

```js
let password = params  // what the user typed after /setpassword

let hash = await modules.bcrypt.hash(password, 10)
db.user.set("password_hash", hash)

Bot.sendMessage("Password saved. We never store the plain version.")
```

### Check a password on login

```js
let attempt = params
let stored = db.user.get("password_hash")

if (!stored) {
  return Bot.sendMessage("No password set yet. Use /setpassword first.")
}

let match = await modules.bcrypt.compare(attempt, stored)

if (match) {
  Bot.sendMessage("Welcome back, " + user.first_name + "!")
} else {
  Bot.sendMessage("Wrong password. Try again.")
}
```

---

## Notes

- Always store **hashes**, never raw passwords
- Salt rounds `10`–`12` balance security and speed for typical bot workloads
- `compare()` is safe against timing attacks
- Official package: [bcrypt on npm](https://www.npmjs.com/package/bcrypt)
