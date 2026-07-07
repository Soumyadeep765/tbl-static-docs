# Bot Admin Methods

Some `Api` methods operate on the **bot itself** rather than a specific chat — fetching bot info, managing webhooks, setting commands, or configuring the bot profile. These methods accept an optional **`bot_token`** parameter.

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
    The `bot_token` field is consumed by TBL internally and is **not** sent to Telegram as a request parameter.

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

## Examples

### Validate a bot token

```js
let res = await Api.getMe({ bot_token: process.env.STORED_TOKEN })

if (res.ok) {
  Bot.sendMessage(chat.id, `Token valid — bot @${res.result.username}`)
} else {
  Bot.sendMessage(chat.id, 'Token is invalid or revoked.')
}
```

### Configure webhook for another bot

```js
await Api.setWebhook({
  bot_token: process.env.SECONDARY_BOT_TOKEN,
  url: 'https://example.com/webhook/secondary',
  allowed_updates: ['message', 'callback_query']
})
```

### Set commands on the current bot

```js
await Api.setMyCommands({
  commands: [
    { command: 'start', description: 'Start the bot' },
    { command: 'help', description: 'Show help' }
  ]
})
```

### Get webhook status

```js
let info = await Api.getWebhookInfo()

if (info.ok) {
  Bot.inspect(info.result)
}
```

## Methods without `bot_token` support

Most chat-facing methods (`sendMessage`, `editMessageText`, `answerCallbackQuery`, etc.) always use the **current bot's token**. To call Telegram with a different token, use one of the methods listed above or `Api.call()` — but `Api.call()` does **not** accept `bot_token`; only the built-in admin methods above do.

## Reference

Full parameter details for each method are in the [Telegram Bot API docs](https://core.telegram.org/bots/api#available-methods).
