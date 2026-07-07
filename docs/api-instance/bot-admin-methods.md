# Bot Admin Methods

Some `Api` methods operate on the **bot itself** rather than a specific chat — fetching bot info, managing webhooks, setting commands, or configuring the bot profile. Think of them as bot-level settings, not chat-level messages.

Most accept an optional **`bot_token`** parameter to act on behalf of another bot. Handy for multi-bot setups. Dangerous if you hard-code tokens. Don't do that.

---

## What are admin methods?

Methods that configure or query the bot account — not individual chats:

| Category | Examples |
| --- | --- |
| Bot identity | `getMe`, `getUpdates` |
| Webhooks | `setWebhook`, `deleteWebhook`, `getWebhookInfo` |
| Commands & profile | `setMyCommands`, `setMyDescription`, `setMyProfilePhoto` |
| Managed bots (Bot API 9.0+) | `getManagedBotToken`, `replaceManagedBotToken` |

Full parameter details: [Telegram Bot API docs](https://core.telegram.org/bots/api#available-methods).

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Secrets like API keys go in dashboard ENV vars — see [`process.env`](../globals/process.md).

---

## How `bot_token` works

| `bot_token` passed? | Behavior |
| --- | --- |
| No | Uses the **current bot's token** (normal case) |
| Yes | Uses the provided token for that single call |

```js
// Current bot — no token needed
let me = await Api.getMe()

// Another bot — token from dashboard ENV
let other = await Api.getMe({ bot_token: process.env.PARTNER_BOT_TOKEN })
```

!!! warning "Security"
    Store tokens in dashboard [environment variables](../globals/process.md). Never hard-code tokens or expose them to users.  
    The `bot_token` field is consumed internally and is **not** sent to Telegram as a request parameter.

---

## Try it — copy-paste examples

### Validate a bot token

```js
let res = await Api.getMe({ bot_token: process.env.STORED_TOKEN })

if (res.ok) {
  Bot.sendMessage("Token valid — bot @" + res.result.username)
} else {
  Bot.sendMessage("Token is invalid or revoked.")
}
```

### Set commands on the current bot

```js
await Api.setMyCommands({
  commands: [
    { command: "start", description: "Start the bot" },
    { command: "help", description: "Show help" }
  ]
})
```

### Configure webhook for another bot

```js
await Api.setWebhook({
  bot_token: process.env.SECONDARY_BOT_TOKEN,
  url: "https://example.com/webhook/secondary",
  allowed_updates: ["message", "callback_query"]
})
```

### Get webhook status

```js
let info = await Api.getWebhookInfo()

if (info.ok) {
  Bot.inspect(info.result)
}
```

---

## Methods that support `bot_token`

### Bot identity and webhooks

| Method | Description |
| --- | --- |
| `Api.getMe` | Get bot user object (`id`, `username`, `can_join_groups`, etc.) |
| `Api.getUpdates` | Fetch pending updates (polling mode) |
| `Api.setWebhook` | Set webhook URL (requires `url`) |
| `Api.deleteWebhook` | Remove webhook |
| `Api.getWebhookInfo` | Get current webhook status |

### Bot commands and profile

| Method | Description |
| --- | --- |
| `Api.setMyCommands` | Set bot command menu (requires `commands` array) |
| `Api.deleteMyCommands` | Clear bot commands |
| `Api.getMyCommands` | Get current command list |
| `Api.getMyName` | Get bot display name |
| `Api.setMyDescription` | Set bot description |
| `Api.getMyDescription` | Get bot description |
| `Api.setMyShortDescription` | Set short description |
| `Api.getMyShortDescription` | Get short description |
| `Api.setMyProfilePhoto` | Set bot profile photo (`photo` with `type: "static"` or `"animated"`) |
| `Api.removeMyProfilePhoto` | Remove bot profile photo |
| `Api.setChatMenuButton` | Configure the menu button |
| `Api.setMyDefaultAdministratorRights` | Set default admin rights for groups/channels |
| `Api.getMyDefaultAdministratorRights` | Get default admin rights |

### Managed bots (Bot API 9.0+)

| Method | Description |
| --- | --- |
| `Api.getManagedBotToken` | Get token for a managed bot (requires `user_id`) |
| `Api.replaceManagedBotToken` | Replace managed bot token (requires `user_id`) |
| `Api.getManagedBotAccessSettings` | Get access settings (requires `user_id`) |
| `Api.setManagedBotAccessSettings` | Update access settings (requires `user_id`, `is_access_restricted`) |

### Gifts

| Method | Description |
| --- | --- |
| `Api.getAvailableGifts` | List gifts available for sending |

---

## Methods without `bot_token` support

Most chat-facing methods (`sendMessage`, `editMessageText`, `answerCallbackQuery`, etc.) always use the **current bot's token**. To call Telegram with a different token, use one of the admin methods above.

`Api.call()` does **not** accept `bot_token` — only the built-in admin methods listed here do.

---

## Important notes

- Always store alternate tokens in dashboard [ENV variables](../globals/process.md)
- Use `await` and check `res.ok` when the result matters
- Case-sensitive: `Api.getMe`, not `Api.getme`
