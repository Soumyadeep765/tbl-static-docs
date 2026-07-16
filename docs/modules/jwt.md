# JWT

Signed payloads in a string — sessions, API tokens, and "trust me" credentials.

## What is it?

**JWT** (JSON Web Tokens) lets you create tamper-proof, signed payloads. Sign a token with a secret, hand it to a user, verify it later. Common uses: login sessions, API auth, and passing data between commands without a database round-trip.

Access it as `modules.JWT`.

---

## How to use

Sign a token with a payload and secret:

```js
let token = modules.JWT.sign(
  { userId: user.id },
  process.env.JWT_SECRET,
  { expiresIn: "7d" }
)
```

Verify it on the other end:

```js
let payload = modules.JWT.verify(token, process.env.JWT_SECRET)
// { userId: 123, iat: ..., exp: ... }
```

Store your secret in dashboard ENV settings — read it via [`process.env`](../globals/process.md). Never hard-code secrets in command logic.

All JWT methods are **synchronous** — no `await` needed.

---

## Methods

| Method | Description |
| --- | --- |
| `sign(payload, secret, options?)` | Create a signed token |
| `verify(token, secret, options?)` | Verify and decode — throws if invalid |
| `decode(token, options?)` | Decode without verification |

Payload and token size are checked against your plan's buffer limit (512 KB – 10 MB).

---

## Sign options

| Option | Example |
| --- | --- |
| `expiresIn` | `"1h"`, `"7d"`, `3600` (seconds) |
| `algorithm` | `"HS256"` (default) |
| `issuer` | `"my-bot"` |
| `subject` | `"user-session"` |

```js
let token = modules.JWT.sign(
  { userId: user.id, role: "member" },
  process.env.JWT_SECRET,
  { expiresIn: "24h" }
)
```

---

## Verify

```js
try {
  let payload = modules.JWT.verify(token, process.env.JWT_SECRET)
  Bot.sendMessage("Welcome back, user " + payload.userId)
} catch (err) {
  Bot.sendMessage("Invalid or expired token.")
}
```

Throws on expired, tampered, or wrong-secret tokens.

---

## Decode (no verification)

```js
let payload = modules.JWT.decode(token)
// { userId: 123, iat: ..., exp: ... } or null
```

Use only for **inspecting** tokens — never for security checks. That's what `verify` is for.

---

## Try it

### Login session flow

[`user`](../globals/user.md) triggers `/login`. [Bot](../bot-instance/index.md) replies in [chat](../globals/chat.md). Save the token in [db](../db-instance/index.md), validate later:

```js
// /login — generate session
let session = modules.JWT.sign(
  { uid: user.id, chat: chat.id },
  process.env.JWT_SECRET,
  { expiresIn: "30d" }
)
db.user.set("session_token", session)
Bot.sendMessage("Logged in. Session saved.")

// /dashboard — validate session
let stored = db.user.get("session_token")
try {
  let data = modules.JWT.verify(stored, process.env.JWT_SECRET)
  Bot.sendMessage("Session valid for user " + data.uid)
} catch (err) {
  Bot.sendMessage("Session expired. Use /login again.")
}
```

---

## Notes

- **Sync** — all methods run synchronously
- Store secrets in [`process.env`](../globals/process.md) — use 32+ random characters
- `sign` payload is JSON-stringified and size-checked against plan limits
- `decode` does not verify signatures — use `verify` for auth decisions
- Official package: [jsonwebtoken on npm](https://www.npmjs.com/package/jsonwebtoken)
