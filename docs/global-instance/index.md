## Global Instance

The **Global instance** is used to **store and manage data at the account level**.

All data stored using the Global instance is **shared across all bots** under the same owner account.

Any bot belonging to the account can read or modify this data.

This is useful for:

- Shared configuration across bots
- Account-wide settings
- Common flags or counters
- Data that should not belong to a single bot or user

Global data is scoped to the **owner account**, not to an individual bot or user.
