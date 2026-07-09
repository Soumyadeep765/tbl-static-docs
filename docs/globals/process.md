# process

Your bot's runtime toolbox — secrets, uptime, and environment config.

## What is it?

**`process`** gives you **runtime information** about the current command execution. Its star feature is **`process.env`** — a key-value map of environment variables you configure in the bot dashboard. No hard-coded API keys. No secrets in your command scripts. Just `process.env.MY_KEY` and you're set.

There's also `process.uptime` for checking how long the bot has been running, and `env` — a shorthand alias because typing `process.env` gets old fast.

## When would you use it?

- Read API keys, URLs, and config from dashboard ENV settings
- Check feature flags (`env.DEBUG === "true"`)
- Gate messages based on bot uptime
- Access any secret that shouldn't live in command logic

This is where JWT secrets, API tokens, and webhook URLs belong. Not in your Logic field. Your future self will thank you.

!!! tip "New to ENV vars?"
    Set them in your bot dashboard under **Environment (ENV) settings**. Only variables you configure there are exposed — platform server secrets never reach your scripts.

---

## Try it — environment variables

```js
// Read a dashboard env variable
let apiUrl = process.env.API_URL

// Shorthand alias — same object
let debug = env.DEBUG === "true"

// Guard against missing config
let apiKey = process.env.MY_API_KEY
if (!apiKey) {
  return Bot.sendMessage(chat.id, "API key not configured.")
}
```

Used with [JWT](../modules/jwt.md), [ethers](../modules/ethers.md), and any external API:

```js
let token = modules.JWT.sign(
  { uid: user.id },
  process.env.JWT_SECRET,
  { expiresIn: "7d" }
)
```

---

## Try it — bot uptime

`process.uptime` shows how long the bot has been running since its last start. Values reset when the bot is stopped and restarted.

```js
if (process.uptime.days >= 1) {
  Bot.sendMessage(user.id,
    "Bot has been online for " + process.uptime.days + " day(s)!"
  )
}
```

| Field | Type | Description |
| --- | --- | --- |
| `days` | `number` | Full days since the bot started |
| `hours` | `number` | Remaining hours (0–23) |
| `minutes` | `number` | Remaining minutes (0–59) |

When the bot is stopped or has no start timestamp, all values are `0`.

---

## Fields

| Property | Type | Description |
| --- | --- | --- |
| `env` | `Object` | Key-value map of dashboard environment variables (all values are strings) |
| `pid` | `string` | Internal execution identifier for the current bot session |
| `MESSAGE` | `string` | Static hint text about accessing env vars |
| `uptime` | `Object` | Bot uptime since last start (`days`, `hours`, `minutes`) |

### Example object

```json
{
  "env": {
    "API_URL": "https://api.example.com",
    "DEBUG": "true"
  },
  "pid": "421234567890",
  "MESSAGE": "Use process.env.KEY to access env vars",
  "uptime": {
    "days": 2,
    "hours": 5,
    "minutes": 30
  }
}
```

---

## The `env` alias

`env` is the same object as `process.env`. Use whichever reads more naturally:

```js
let key = process.env.MY_KEY   // explicit
let key = env.MY_KEY           // shorthand
```

Both work. Both are strings. Both are read-only.

---

## Good to know

- `process` is read-only and exists only during command execution
- Environment values are always **strings** — convert numbers or booleans in your logic (`Number(env.PORT)`, `env.DEBUG === "true"`)
- Never hard-code secrets in commands — dashboard ENV is the right place
- Overview of all globals: [Global Variables](index.md)
