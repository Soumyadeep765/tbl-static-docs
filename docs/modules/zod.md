# zod

Schemas that catch bad data before it wrecks your command logic.

## What is it?

**zod** is a schema validation library. Define what your data should look like — "email must be a string, age must be a number between 1 and 120" — and zod tells you exactly what's wrong when input doesn't match. Much nicer error messages than `if` chains.

Access it as `modules.zod` — the full Zod library.

---

## How to use

Define a schema, parse data:

```js
let schema = modules.zod.object({
  name: modules.zod.string(),
  age: modules.zod.number().min(1).max(120)
})

let result = schema.parse({ name: "Alice", age: 25 })
// { name: "Alice", age: 25 }
```

If validation fails, `parse()` throws with a detailed error. Use `safeParse()` when you prefer not to catch:

```js
let check = schema.safeParse({ name: "Alice", age: "not a number" })
// { success: false, error: ZodError { ... } }
```

**Sync** — no `await` needed.

---

## Core schema types

| Schema | Validates |
| --- | --- |
| `z.string()` | String |
| `z.number()` | Number |
| `z.boolean()` | Boolean |
| `z.array(z.string())` | Array of strings |
| `z.object({ ... })` | Object with shaped fields |
| `z.enum(["a", "b"])` | One of listed values |
| `z.optional()` | Field may be undefined |
| `z.nullable()` | Field may be null |

Chain modifiers: `.min()`, `.max()`, `.email()`, `.url()`, `.regex()`, `.default(value)`.

---

## Methods on schemas

| Method | Description |
| --- | --- |
| `.parse(data)` | Validate — throws `ZodError` on failure |
| `.safeParse(data)` | Validate — returns `{ success, data }` or `{ success: false, error }` |
| `.optional()` | Make field optional |
| `.default(value)` | Use default if missing |

---

## Try it

### Validate command input

[Bot](../bot-instance/index.md) replies in [chat](../globals/chat.md). [`params`](../globals/params.md) might be JSON the user sent. Parse and validate before using:

```js
let schema = modules.zod.object({
  email: modules.zod.string().email(),
  amount: modules.zod.number().positive()
})

let check = schema.safeParse(JSON.parse(params))

if (!check.success) {
  let issues = check.error.issues.map(i => i.path.join(".") + ": " + i.message)
  return Bot.sendMessage("Invalid input:\n" + issues.join("\n"))
}

Bot.sendMessage("Payment of $" + check.data.amount + " for " + check.data.email)
```

### Validate and save user profile

Save to [db](../db-instance/index.md) after validation:

```js
let profileSchema = modules.zod.object({
  displayName: modules.zod.string().min(1).max(50),
  age: modules.zod.number().int().min(13).max(120).optional()
})

try {
  let profile = profileSchema.parse(JSON.parse(params))
  db.user.set("profile", profile)
  Bot.sendMessage("Profile saved, " + profile.displayName + "!")
} catch (err) {
  Bot.sendMessage("Profile invalid: " + err.issues[0].message)
}
```

### Simple string check

```js
let name = modules.zod.string().min(2).parse(params)
Bot.sendMessage("Hello, " + name + "!")
```

---

## Notes

- **Sync** — no `await` needed
- Use `safeParse()` in bot commands to avoid try/catch boilerplate
- For single-field checks (just an email, just a URL), [validator](validator.md) may be simpler
- Official docs: [zod.dev](https://zod.dev/)
