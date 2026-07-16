# Cloning Bots (TBL.clone)

Make an exact copy of a bot, including its settings and commands.

## How it works

`TBL.clone` takes a source bot you own and creates a new copy of it on the platform. If you provide a new Telegram token, the platform can start the copy immediately. You can also copy over some or all custom properties in the process.

The platform executes the core cloning request first. If you choose to copy properties, the system handles that step in the background right after creating the new bot.

---

## Usage

```js
const response = await TBL.clone({
  bot_id: 123,
  bot_token: "123456:ABC-DEF",
  run_now: true,
  all_props: true
});
```

---

## Parameters

Pass an object to `TBL.clone` containing the parameters below.

### bot_id (or botId)
* **Type**: `number`
* **Required**: Yes
* **Purpose**: This tells the platform which bot you want to clone.
* **Details**: Use the unique numerical ID of your source bot. You can find this ID in your dashboard. The system checks if you own this bot before proceeding. If you pass an ID of a bot you do not own, the clone request fails with an access denied error.

### bot_token
* **Type**: `string`
* **Required**: No (unless `run_now` or `start_now` is set to `true`)
* **Purpose**: The Telegram bot token for the newly created clone bot.
* **Details**: This is the token you get from Telegram's @BotFather. You only need to provide this if you want the clone bot to start running immediately. If you plan to leave the bot inactive or run it manually later, you can omit this field.

### run_now (or start_now)
* **Type**: `boolean`
* **Required**: No
* **Default**: `false`
* **Purpose**: Instructs the platform to boot up and run the clone bot right after creation.
* **Details**: Set this to `true` to make the new bot go live immediately. Remember that setting this option to `true` requires a valid Telegram token in the `bot_token` field.

### is_child (or isChild)
* **Type**: `boolean`
* **Required**: No
* **Default**: `false`
* **Purpose**: Declares the new clone bot as a child bot of the parent.
* **Details**: In multi-bot architectures, setting this to `true` tells the system that the cloned bot should act as a child bot under your primary bot. This affects command sharing and routing rules if your setup utilizes parent-child bot relationships.

### all_props
* **Type**: `boolean`
* **Required**: No
* **Default**: `false`
* **Purpose**: Copies all configuration properties from the source bot to the new clone.
* **Details**: Set this to `true` if you want the cloned bot to inherit every custom property from the original bot. The platform copies properties in the background.

### bot_props
* **Type**: `object`
* **Required**: No
* **Purpose**: Lets you copy only specific settings or properties.
* **Details**: Pass a key-value object containing the exact properties you want to carry over to the clone. Use this when you do not want a full property migration but need to seed specific configurations, like API keys or custom flags.

---

## Response structure

The method returns a promise. It resolves to a response object:

### Successful clone

```json
{
  "ok": true,
  "result": {
    "id": 456,
    "bot_id": 987654321,
    "username": "my_new_clone_bot",
    "status": "working"
  }
}
```

### Failed clone

```json
{
  "ok": false,
  "result": "Missing owner.mail"
}
```

---

## Things to watch out for

1. **Permissions**: You can only clone bots that belong to your account. The platform checks this and blocks the request if you attempt to copy someone else's bot.
2. **Tokens**: If you want the clone to start running right away (`run_now: true`), you must supply a valid `bot_token`.
3. **Property Copying**: Property copying is handled in the background. If you set `all_props: true` but your source bot has no properties, the clone finishes but no property copying step takes place.
