# crypto

Hashes, HMACs, and random bytes — the cryptographic toolbox Node.js ships with.

## What is it?

**crypto** gives you cryptographic primitives: SHA hashes, HMAC signatures, random bytes, and more. Use it for checksums, API signature verification, generating secure tokens, or anything that needs "math that attackers can't reverse easily."

You can use it two ways — both work identically:

- `crypto.createHash(...)` — direct global
- `modules.crypto.createHash(...)` — through the modules object

---

## How to use

Create a SHA-256 hash of a string:

```js
let hash = crypto
  .createHash("sha256")
  .update("data")
  .digest("hex")
// "3a6eb0790f39ac87c94f386e92ef2ab3..." 
```

Same thing via modules:

```js
let hash = modules.crypto
  .createHash("sha256")
  .update("data")
  .digest("hex")
```

---

## Common patterns

| Pattern | Example |
| --- | --- |
| SHA-256 hash | `crypto.createHash("sha256").update(data).digest("hex")` |
| HMAC-SHA256 | `crypto.createHmac("sha256", secret).update(data).digest("hex")` |
| Random bytes | `crypto.randomBytes(32).toString("hex")` |
| MD5 (legacy only) | `crypto.createHash("md5").update(data).digest("hex")` |

Output format depends on `.digest()` — `"hex"`, `"base64"`, or a Buffer.

---

## Try it

### Verify a webhook signature

Store your API secret in dashboard ENV settings, then read it via [`process.env`](../globals/process.md):

```js
let secret = process.env.WEBHOOK_SECRET
let payload = params

let expected = crypto
  .createHmac("sha256", secret)
  .update(payload)
  .digest("hex")

if (expected === request.headers["x-signature"]) {
  Bot.sendMessage("Webhook verified. All good.")
} else {
  Bot.sendMessage("Signature mismatch. Nice try.")
}
```

### Generate a secure random token

[Bot](../bot-instance/index.md) sends to [chat](../globals/chat.md). Store the token in [db](../db-instance/index.md):

```js
let token = crypto.randomBytes(16).toString("hex")
db.user.set("api_token", token)

Bot.sendMessage("Your API token: " + token)
```

---

## Notes

- All crypto operations here are **synchronous** — no `await`
- Prefer `sha256` or stronger for security-sensitive hashing; avoid MD5 for anything new
- For password storage, use [bcrypt](bcrypt.md) instead — it's designed for that job
- Official reference: [Node.js crypto docs](https://nodejs.org/api/crypto.html)
