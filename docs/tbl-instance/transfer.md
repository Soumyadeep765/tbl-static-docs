# Transferring Bots (TBL.transfer)

Move a bot to another user account.

## How it works

`TBL.transfer` lets you transfer ownership of a bot. You specify the bot ID and the email address of the recipient. Once the transfer completes, the bot moves to the new owner's account.

Just like cloning, you can choose to migrate settings and custom properties to the transferred bot.

---

## Usage

```js
const response = await TBL.transfer({
  bot_id: 123,
  email: "partner@example.com",
  is_child: false
});
```

---

## Parameters

Pass an object to `TBL.transfer` containing the parameters below.

### bot_id (or botId)
* **Type**: `number`
* **Required**: Yes
* **Purpose**: Identifies the bot you want to transfer.
* **Details**: Use the unique numerical ID of your bot (available in the dashboard). The platform checks ownership first. If the bot does not belong to your account, the transfer request fails immediately.

### email (or to_mail or mail)
* **Type**: `string`
* **Required**: Yes
* **Purpose**: The email address of the account receiving the bot.
* **Details**: Provide the registered email address of the user who will receive the bot. The platform checks if this email exists on the system before initiating the transfer. If no user is found with this email, the operation fails.

### is_child (or isChild)
* **Type**: `boolean`
* **Required**: No
* **Default**: `false`
* **Purpose**: Marks the bot as a child bot on the recipient's account.
* **Details**: If you set this to `true`, the bot becomes a child bot of the target account's primary bot setup after the transfer. This affects how commands and data are structured on the recipient's end.

### bot_props
* **Type**: `object`
* **Required**: No
* **Purpose**: Specifies a select list of properties to copy.
* **Details**: Pass a key-value object containing only the custom properties you want to carry over to the target account. Useful when you want to migrate specific settings without copying the entire configuration history.

---

## Response structure

The method returns a promise. It resolves to a response object:

### Successful transfer

```json
{
  "ok": true,
  "result": {
    "id": 123,
    "owner_id": "new-owner-id-string",
    "status": "working"
  }
}
```

### Failed transfer

```json
{
  "ok": false,
  "result": "Invalid or missing \"email\" or \"to_mail\""
}
```

---

## Things to watch out for

1. **Ownership**: You must own the bot to transfer it. If you try to transfer a bot you do not own, the system throws an access denied error.
2. **Recipient Email**: The target email address must belong to a registered account on the platform. The transfer fails if the system cannot find the user email.
3. **Property Copying**: The platform handles property copying asynchronously. The copy step queues immediately after a successful transfer.
