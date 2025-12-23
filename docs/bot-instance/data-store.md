## Bot Data Store

The **Bot Data Store** is a simple **key–value storage** that belongs to the bot itself.

It is **not user-specific** and **not chat-specific**.  
Anything stored here is shared across the entire bot.

All data store methods are **synchronous**, so you do **not** need `await`.

## Setting Data

You can store values using `Bot.set()`.

```js
// Set values
Bot.set("version", "1.2.3", "String")
Bot.set("config", { apiKey: "xyz" }, "Json")
```

- The first argument is the key
- The second argument is the value
- The third argument is the data type (optional)

!!! info
    If the type is not provided, TBL automatically detects it.

## Reading Data

You can read stored values using `Bot.get()`.

```js
let v = Bot.get("version")   // "1.2.3"
let c = Bot.get("config")    // { apiKey: "xyz" }
```

If the key does not exist, the result will be `null`.

## Deleting Data

Delete a single key:

```js
Bot.del("version")
```

Delete all stored data:

```js
Bot.delAll()
```

!!! warning
    `Bot.delAll()` permanently removes all bot-level data.
    Use it carefully.

## Checking Existence

Check if a key exists:

```js
let has = Bot.has("config")  // true
```

This is useful before reading or overwriting values.

## Listing Stored Data

Get all stored key–value pairs:

```js
let all = Bot.getAll()
```

Get the total number of stored keys:

```js
let count = Bot.count()
```

Get all stored key names:

```js
let names = Bot.getNames()   // ["config"]
```

## Supported Data Types

The following data types are supported:

- **String** – Plain text or auto-converted values
- **Number** – Integers or floats
- **Boolean** – true or false
- **List** – Arrays (ordered lists)
- **Date** – Date objects
- **Json** – Objects or arrays stored as JSON

!!! note
    When storing complex data, `Json` is recommended for consistency.

## Important Notes

- Data is stored at the **bot level**
- Values persist across command executions
- Data is shared between all users
- Methods are synchronous
- Keys are case-sensitive

!!! tip
    Use the Bot Data Store for configuration, feature flags, counters, or bot state — not for user-specific data.
