## MCL (Membership Checker Lib)

MCL is used to **validate whether a user is a member of one or more Telegram channels or groups**.

It is commonly used to enforce join requirements before allowing users to access bot features.

MCL is available through the `Libs` instance.

## Check User Membership

You can check if a user has joined specific channels or groups.

```js
let joined = await Libs.mcl.check(
  user.id,
  ["@Chan1", "@Chan2"]
)
```

This validates the user’s membership across all provided channels.

## Example Response

```
{
  all_joined: true,
  valid: ["@Channel1", "@Channel2"],
  left: [],
  invalid: [],
  details: [
    {
      channel: "@Channel1",
      member: { /* full getChatMember response */ }
    }
  ]
}
```

## Response Fields

- `all_joined`  
  Indicates whether the user joined all required channels

- `valid`  
  Channels where the user is a valid member

- `left`  
  Channels the user has left or not joined

- `invalid`  
  Channels that are invalid or inaccessible

- `details`  
  Detailed membership data from Telegram

## Notes

- Works with both channels and groups
- Requires the bot to be present in the target chats
- Useful for subscription-gated bots

## Full Documentation

[MCL Documentation]

[MCL Documentation]: https://github.com/telebothost/tbl-libs/blob/main/Lib-Docs/mcl.md