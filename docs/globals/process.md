# The `process` Object

In TBL, `process` provides **runtime information** about the current command execution. It is mainly used to access **environment variables** you configure from the bot dashboard, and to check how long the bot has been running.

## Accessing Environment Variables

Environment variables are available at:

- `process.env`
- `env` (same object — a convenience alias)

These values come from the bot's **Environment (ENV) settings** in the dashboard. Only variables you configure there are exposed — platform server secrets are never available to command scripts.

```javascript
// Read a dashboard env variable
let apiUrl = process.env.API_URL

// env is an alias for process.env
let debug = env.DEBUG === 'true'
```

## Bot Uptime

`process.uptime` shows how long the bot has been running since its last start. Values reset when the bot is stopped and restarted.

| Field | Type | Description |
| --- | --- | --- |
| `days` | `number` | Full days since the bot started |
| `hours` | `number` | Remaining hours (0–23) |
| `minutes` | `number` | Remaining minutes (0–59) |

When the bot is stopped or has no start timestamp, all values are `0`.

```javascript
if (process.uptime.days >= 1) {
  Bot.sendMessage(user.id, `Bot has been online for ${process.uptime.days} day(s)!`)
}
```

## Example `process` Object

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

## Properties

| Property | Type | Description |
| --- | --- | --- |
| `env` | `Object` | Key-value map of dashboard environment variables (all values are strings) |
| `pid` | `string` | Internal execution identifier for the current bot session |
| `MESSAGE` | `string` | Static hint text about accessing env vars |
| `uptime` | `Object` | Bot uptime since last start (`days`, `hours`, `minutes`) |

## The `env` Alias

`env` is set to the same object as `process.env`. Use whichever reads more naturally in your script:

```javascript
let key = process.env.MY_KEY   // explicit
let key = env.MY_KEY           // shorthand
```

## Important Notes

- `process` is read-only
- Environment values are always strings — convert numbers or booleans in your logic
- Values exist only during command execution
- Store secrets, API keys, and configuration in dashboard ENV settings — never hard-code them in commands
