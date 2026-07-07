# JWT

`modules.JWT` creates and verifies **JSON Web Tokens** — for sessions, API auth, and signed payloads.

```js
let token = modules.JWT.sign({ userId: user.id }, process.env.JWT_SECRET, { expiresIn: "7d" })
let payload = modules.JWT.verify(token, process.env.JWT_SECRET)
```

---

## Methods

| Method | Description |
| --- | --- |
| `sign(payload, secret, options?)` | Create a signed token |
| `verify(token, secret, options?)` | Verify and decode — throws if invalid |
| `decode(token, options?)` | Decode without verification |

All methods are **synchronous**. Payload and token size are checked against your plan buffer limit.

---

## Sign

```js
let token = modules.JWT.sign(
  { userId: user.id, role: "member" },
  process.env.JWT_SECRET,
  { expiresIn: "24h" }
)
```

Common `options`:

| Option | Example |
| --- | --- |
| `expiresIn` | `"1h"`, `"7d"`, `3600` (seconds) |
| `algorithm` | `"HS256"` (default) |
| `issuer` | `"my-bot"` |
| `subject` | `"user-session"` |

---

## Verify

```js
try {
  let payload = modules.JWT.verify(token, process.env.JWT_SECRET)
  Bot.sendMessage(chat.id, "Welcome back, user " + payload.userId)
} catch (err) {
  Bot.sendMessage(chat.id, "Invalid or expired token.")
}
```

Throws on expired, tampered, or wrong-secret tokens.

---

## Decode (no verification)

```js
let payload = modules.JWT.decode(token)
// { userId: 123, iat: ..., exp: ... } or null
```

Use only for inspecting tokens — not for security checks.

---

## Example — login token

```js
// Generate on /login
let session = modules.JWT.sign(
  { uid: user.id, chat: chat.id },
  process.env.JWT_SECRET,
  { expiresIn: "30d" }
)
db.user.set("session_token", session)

// Validate on /dashboard
let stored = db.user.get("session_token")
try {
  let data = modules.JWT.verify(stored, process.env.JWT_SECRET)
  Bot.sendMessage(chat.id, "Session valid for user " + data.uid)
} catch (err) {
  Bot.sendMessage(chat.id, "Session expired. Use /login again.")
}
```

---

## Notes

- Store secrets in [ENV variables](../globals/process.md) — never hard-code
- `sign` payload is JSON-stringified and size-checked
- Use strong secrets (32+ random characters)
- Official package: [jsonwebtoken on npm](https://www.npmjs.com/package/jsonwebtoken)
