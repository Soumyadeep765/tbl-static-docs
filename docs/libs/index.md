# TBL Libraries (Libs)

The **Libs instance** provides direct access to **TBL's built-in helper libraries**.

These libraries handle common bot tasks: randomization, date and time operations, resource tracking, referrals, and Telegram-specific utilities.

## Usage

```js
Libs.random.int(1, 100)
Libs.dateTimeFormat.now()
Libs.tgutil.getFullName(user)
```

Most methods return **Promises**. Using `await` is optional unless you need the returned value.

## What Libs Is Used For

Libs helps you avoid repetitive logic by offering ready-to-use helpers for:

- Tracking counters, balances, and shared values
- Formatting and calculating dates and times
- Checking user membership in channels or groups
- Generating random values
- Building referral systems
- Working with Telegram names, mentions, and formatting

## Available Libraries

| Library | Description |
| --- | --- |
| [ResourcesLib](resourceslib.md) | User-level or global counters, balances, and persistent values |
| [dateTimeFormat](date-time-format.md) | Format dates, add or subtract time, calculate differences |
| [MCL](mcl.md) | Check channel or group membership |
| [random](random.md) | Generate random numbers, strings, colors, and dates |
| [refLib](reflib.md) | Create referral links and track invited users |
| [tgutil](tgutil.md) | Telegram names, mentions, links, and text escaping |

## Notes

- Libs is available globally in TBL
- No setup or imports are required
- Designed for simplicity and performance
- Works seamlessly with commands and callbacks

For general-purpose npm-style utilities, see [Modules](../modules/index.md).
