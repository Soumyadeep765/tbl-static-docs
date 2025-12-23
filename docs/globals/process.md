# The `process` Object

In TBL, `process` provides **runtime information** about the current execution environment.

It is mainly used to **access environment variables** that you configure from the bot dashboard.

## Accessing Environment Variables

Environment variables are available inside:

- `process.env`

These values come directly from the bot’s **Environment (ENV) settings** in the dashboard.

For example, if you set an env key named `API_KEY`, you can access it using:

process.env.API_KEY

## Demo `process` Object

Example structure of the `process` object:

```json
{
  "env": {
    "22": "Ok",
    "Test": "true",
    "Yest3": "Ok"
  },
  "pid": 652434,
  "MESSAGE": "For getting Env just use process.env.YOUR_ENV_NAME"
}
```

## What `process` Contains

Common properties include:

- `process.env` → all configured environment variables
- `process.pid` → current execution process ID
- Additional runtime metadata

## Important Notes

- `process` is read-only
- Environment values are always strings
- Values exist only during command execution

The `process` object is the correct and safe way to store **secrets, keys, and configuration** for your bot.
