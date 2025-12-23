## refLib

refLib provides tools for **creating and tracking referral systems**.

It is useful for invite programs, growth tracking, and reward-based user onboarding.

refLib is available through the `Libs` instance.

## Create a Referral Link

Generate a referral link for the bot.

```js
let refLink = Libs.refLib.getRefLink(bot.name)
```

This creates a unique referral link that can be shared with others.

## Count User Referrals

Get the number of users referred by a specific user.

```js
let count = Libs.refLib.getRefCount(user.id)
```

This returns the total referral count for that user.

## Notes

- Referral tracking is handled automatically
- Works across user sessions
- Useful for reward or invite-based systems

## Full Documentation

[refLib Documentation]

[refLib Documentation]: https://github.com/telebothost/tbl-libs/blob/main/Lib-Docs/refLib.md