## Basic Operations

Use the Global instance to **store and read data at the account level**.

All operations here use the **string-based method format** and apply to the **entire owner account**.

Data stored here is shared across **all bots** under the same account.

## Saving Global Data

Use `Global.set()` to store values.

```js
Global.set("version", "1.0.0")
Global.set("max_limit", 100, "number")
```

- First argument: key  
- Second argument: value  
- Third argument (optional): data type  

If the type is not provided, it is auto-detected.

## Reading Global Data

Use `Global.get()` to read stored values.

```js
let version = Global.get("version")
let limit = Global.get("max_limit")

Bot.sendMessage("Version: " + version + ", Limit: " + limit)
```

Reading data is **synchronous** and returns the value directly.

If a key does not exist, it returns `null`.

## Deleting a Single Value

Remove a specific global value.

```js
Global.del("max_limit")

let limit = Global.get("max_limit")   // null
Bot.sendMessage("After delete, limit = " + limit)
```

Deleting a non-existing key does nothing and does not throw an error.

## Bulk Operations

Bulk operations let you **work with all global data at once**.

These are useful for inspecting or resetting account-level data.

### Get All Global Data

```js
let all = Global.getAll()
Bot.inspect(all)
```

Example output:

```json
{
  "version": "1.0.0",
  "maintenance": false
}
```

This returns an object containing **all stored global keys and values**.

### Delete All Global Data

```js
Global.delAll()

let all2 = Global.getAll()
Bot.inspect(all2)
```

This clears **all global data for the account**.

## Notes

- Data is stored at the **account level**
- Shared across all bots under the same owner
- Only string-based methods are used here
- Reading (`get`, `getAll`) is synchronous
- Saving and deleting do not require `await`
- Missing keys always return `null`
