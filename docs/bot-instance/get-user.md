## Getting Bot Users

`Bot.getUsers()` returns an **array of user or chat IDs** that have interacted with your bot.

This method returns a **Promise**, so it **must be awaited**.

It removes the need to manually store user IDs in bot properties.

!!! info
    This feature is available in TBL but is **not 100% stable yet**.

## Basic Usage

Get all users who interacted with the bot:

```js
let data = await Bot.getUsers()
```

- Return type: Array
- Must be awaited
- By default, channel IDs are excluded

You can use the result directly:

```js
Bot.sendMessage({ text: data })
```

## Available Filters

Filters are **optional**.  
If no filter is provided, all users are returned (excluding channels).

### chatType

Filter by chat type:

- `private`
- `group`
- `channel`

### premiumOnly

Filter only premium users  
(only applies to private chats)

## Examples with Filters

### Get Only Group Chats

```js
let groupUsers = await Bot.getUsers({
  chatType: "group"
})
```

### Get Only Private Chats

```js
let privateUsers = await Bot.getUsers({
  chatType: "private"
})
```

### Get Only Premium Users

```js
let premiumUsers = await Bot.getUsers({
  premiumOnly: true
})
```

These results contain **private chat IDs only**.

## Sending Results

```js
Bot.sendMessage("Group users: " + groupUsers.length)
Bot.sendMessage("Premium users: " + premiumUsers.length)
```

## Channel IDs Note

!!! note
    By default, channel IDs are excluded.

To include channels, you must explicitly use:

chatType: "channel"

## Important Notes

- `Bot.getUsers()` must be awaited
- Returns an array of IDs
- Filters are optional
- Channel chats are excluded by default
- Feature is still under development
