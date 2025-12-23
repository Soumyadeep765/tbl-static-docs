## ResourcesLib

ResourcesLib is used to manage **persistent numeric resources** at both **user level** and **global level**.

It is commonly used for things like balances, counters, credits, points, or usage tracking.

Resources created with ResourcesLib are **stored persistently** and automatically handled by TBL.

## User-Level Resources

User resources are scoped to the **current user**.

Example:

```js
let coins = Libs.ResourcesLib.userRes("coins")

coins.add(50)
let current = coins.value()
```

- Each user has their own independent value
- Useful for coins, XP, credits, or limits

## Global Resources

Global resources are **shared across all users of the same bot**.

Any update to a global resource affects **every user interacting with that bot**.

Example:

```js
let globalCounter = Libs.ResourcesLib.anotherRes("visits")

globalCounter.add(1)
```

- One shared value for the entire bot
- Useful for visits, totals, or bot-wide counters

!!! info
    Global resources are **bot-wide**, not user-specific.
    They are not shared between different bots.

## Common Operations

Resources support simple operations such as:

- Adding values
- Reading current value
- Persistent storage without manual save logic

## Notes

- Resources are created automatically if they don’t exist
- Values are stored persistently
- No setup or schema required
- Safe to use in commands and callbacks

## Full Documentation

[ResourcesLib Documentation]

[ResourcesLib Documentation]: https://github.com/telebothost/tbl-libs/blob/main/Lib-Docs/ResourcesLib.md
