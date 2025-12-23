## Basic Operations

Use the User instance to **store and read data at the user level**.

All operations here use the **string-based method format** and apply only to the **current user**.

## Saving User Data

Use `User.set()` to store values.

```js
User.set("name", "Alice")
User.set("age", 25, "number")
```

- First argument: key  
- Second argument: value  
- Third argument (optional): data type  

If the type is not provided, TBL will auto-detect it.

## Reading User Data

Use `User.get()` to read stored values.

```js
let name = User.get("name")
let age = User.get("age")

Bot.sendMessage("Name: " + name + ", Age: " + age)
```

Reading data is **synchronous** and returns the value directly.

If a key does not exist, it returns `null`.

## Deleting a Single Value

Remove a specific value when it’s no longer needed.

```js
User.del("age")

let age = User.get("age")   // null
Bot.sendMessage("After delete, age = " + age)
```

Deleting a non-existing key does nothing and does not throw an error.

## Bulk Operations

Bulk operations let you **work with all stored user data at once**.

These are useful when you want to inspect or reset the user’s data.

### Get All User Data

```js
let all = User.getAll()
Bot.inspect(all)
```

Example output:

```json
{
  "name": "Alice",
  "age": 25
}
```

This returns an object containing **all stored keys and values** for the user.

### Delete All User Data

```js
User.delAll()

let all2 = User.getAll()
Bot.inspect(all2)
```

This clears **all data for the current user**.

## Notes

- All data is stored at the **user level**
- Data is private and isolated per user
- Only string-based methods are used here
- Reading (`get`, `getAll`) is synchronous
- Saving and deleting do not require `await`
- Missing keys always return `null`
