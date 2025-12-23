## Libs Instance

The **Libs instance** provides direct access to **TBL’s built-in helper libraries**.

These libraries are designed to handle common tasks such as randomization, date and time operations, resource tracking, referrals, and Telegram-specific utilities.

You can access any library using:

Libs.<library>.<method>()

Most methods return **Promises**.  
Using `await` is optional unless you need the returned value.

## What Libs Is Used For

Libs helps you avoid writing repetitive logic by offering ready-to-use helpers for:

- Tracking counters, balances, and shared values
- Formatting and calculating dates and times
- Checking user membership in channels or groups
- Generating random values
- Building referral systems
- Working with Telegram names, mentions, and formatting

## Available Libraries

- **ResourcesLib**  
  Manage user-level or global counters, balances, and other persistent values.

- **dateTimeFormat**  
  Format dates, add or subtract time, and calculate differences between dates.

- **MCL (Membership Checker Lib)**  
  Check whether a user is a member of specific channels or groups and perform related checks.

- **random**  
  Generate random numbers, strings, colors, dates, and more.

- **refLib**  
  Create referral links and track invited or referred users.

- **tgutil**  
  Telegram-specific utilities for names, mentions, links, and text escaping.

## Notes

- Libs is available globally in TBL
- No setup or imports are required
- Designed for simplicity and performance
- Works seamlessly with commands and callbacks
