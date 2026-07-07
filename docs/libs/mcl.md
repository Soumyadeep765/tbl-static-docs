# MCL (Membership Checker)

"Join our channel to unlock this feature" — classic bot move. **`Libs.mcl`** checks whether a user actually joined, builds join buttons, and writes the nag message for you.

**Every check method is async.** You must use `await`. No exceptions. Well, one exception: `getBtn()` is sync.

---

## What is it?

`Libs.mcl` checks whether a user has joined required Telegram channels or groups. It calls Telegram's `getChatMember` API live — not cached, not guessed.

Access: `Libs.mcl.<method>()`

**Requirements:**

- Your bot must be a member of every channel/group you check
- The bot needs permission to call `getChatMember`
- Max **10 channels** per call

If the bot isn't in the channel, that channel lands in `invalid` — and your gate silently fails in confusing ways. Add the bot first. Future you will thank present you.

---

## How to use it — and why `await` matters

MCL talks to Telegram's servers. That takes time. Async methods return **Promises** — you need `await` to get the actual result:

```js
// Wrong — ok is a Promise, not true/false. Gate broken. Everyone gets in.
let ok = Libs.mcl.quick(user.id, ["@MyChannel"])

// Correct
let ok = await Libs.mcl.quick(user.id, ["@MyChannel"])

if (ok) {
  Bot.sendMessage(chat.id, "Thanks for joining! Here's your reward.")
} else {
  Bot.sendMessage(chat.id, "Join @MyChannel first, then try again.")
}
```

**Rule of thumb:** if the method checks membership, `await` it. If it builds buttons (`getBtn`), don't.

TBL doesn't support `.then()` chains — always use `await`.

!!! tip "Globals"
    `user.id` is the Telegram user ID. `Api.sendMessage` sends with inline keyboards. See [Global Variables](../globals/index.md) and [Api](../api-instance/index.md).

---

## Try it — beginner examples

### Simple gate

```js
if (await Libs.mcl.quick(user.id, ["@Chan1", "@Chan2"])) {
  Bot.run("/premiumFeature")
} else {
  Bot.sendMessage(chat.id, "Join our channels first.")
}
```

### Gate with join buttons

```js
let channels = ["@MyChannel", "@MyGroup"]
let ok = await Libs.mcl.quick(user.id, channels)

if (!ok) {
  let text = await Libs.mcl.summaryText(user.id, channels)
  let buttons = Libs.mcl.getBtn(channels)  // sync — no await
  Api.sendMessage({
    chat_id: chat.id,
    text,
    reply_markup: { inline_keyboard: buttons }
  })
}
```

---

## Methods

| Method | Async | Description |
| --- | --- | --- |
| `check(userId, channels)` | Yes | Full membership breakdown |
| `quick(userId, channels)` | Yes | `true` if all channels joined |
| `getLeftChannels(userId, channels)` | Yes | Channels user has left |
| `getInvalidChannels(userId, channels)` | Yes | Invalid or inaccessible channels |
| `summaryText(userId, channels)` | Yes | Human-readable status message |
| `getBtn(channels)` | No | Inline keyboard join buttons |

---

## `check(userId, channels)`

Main method — returns a detailed result object.

### Parameters

| Param | Type | Description |
| --- | --- | --- |
| `userId` | `number` | Telegram user ID |
| `channels` | `string[]` | Channel usernames (`"@Chan"`) or numeric chat IDs — **max 10** |

### Returns

```js
{
  all_joined: true,
  valid: ["@Channel1", "@Channel2"],
  left: [],
  invalid: [],
  details: [
    { channel: "@Channel1", member: { /* getChatMember result */ } }
  ]
}
```

| Field | Description |
| --- | --- |
| `all_joined` | `true` only if user joined every valid channel |
| `valid` | Channels where membership was confirmed |
| `left` | Channels where status is `left` or `kicked` |
| `invalid` | Channels the bot cannot access or that don't exist |
| `details` | Per-channel `getChatMember` response |

```js
let result = await Libs.mcl.check(user.id, ["@NewsChannel", "@CommunityGroup"])

if (!result.all_joined) {
  Bot.sendMessage(chat.id, "Please join: " + result.left.join(", "))
}
```

---

## `quick(userId, channels)`

Returns `true` or `false` — shortcut for `check().all_joined`.

```js
if (await Libs.mcl.quick(user.id, ["@Chan1", "@Chan2"])) {
  Bot.run("/premiumFeature")
} else {
  Bot.sendMessage(chat.id, "Join our channels first.")
}
```

---

## `getLeftChannels(userId, channels)`

Returns only the channels the user has **not** joined:

```js
let left = await Libs.mcl.getLeftChannels(user.id, ["@Chan1", "@Chan2"])
// ["@Chan2"]
```

---

## `getInvalidChannels(userId, channels)`

Returns channels the bot cannot check (wrong ID, bot not admin, channel deleted):

```js
let bad = await Libs.mcl.getInvalidChannels(user.id, ["@FakeChannel"])
```

---

## `summaryText(userId, channels)`

Ready-to-send status message:

```js
let text = await Libs.mcl.summaryText(user.id, ["@Chan1", "@Chan2"])
// "✅ You have joined all required channels."
// or "🚫 Please join the required channels:\n\n📤 Left:\n• @Chan2"
```

---

## `getBtn(channels)`

Generates inline keyboard rows for join links. **Sync** — no `await`.

Only works with `@username` strings (not numeric IDs):

```js
let buttons = Libs.mcl.getBtn(["@Chan1", "@Chan2"])
// [
//   [{ text: "📢 Join @Chan1", url: "https://t.me/Chan1" }],
//   [{ text: "📢 Join @Chan2", url: "https://t.me/Chan2" }]
// ]

Api.sendMessage({
  chat_id: chat.id,
  text: "Join to continue:",
  reply_markup: { inline_keyboard: buttons }
})
```

---

## Full gate example

```js
let channels = ["@MyChannel", "@MyGroup"]
let result = await Libs.mcl.check(user.id, channels)

if (result.all_joined) {
  Bot.run("/mainMenu")
  return
}

await Api.sendMessage({
  chat_id: chat.id,
  text: await Libs.mcl.summaryText(user.id, channels),
  reply_markup: {
    inline_keyboard: Libs.mcl.getBtn(result.left.length ? result.left : channels)
  }
})
```

---

## Limits and requirements

| Rule | Value |
| --- | --- |
| Max channels per call | **10** |
| Channel format | `"@username"` or numeric chat ID |
| `getBtn` usernames | Only `"@username"` — numeric IDs are skipped |
| Bot requirement | Bot must be in the channel/group |
| Method timeout | 2 seconds per Libs method call |

Throws `[LibsError]` if channels array is empty or exceeds 10 items.

---

## Common mistakes

```js
// Wrong — returns a Promise, not a boolean
let ok = Libs.mcl.quick(user.id, ["@Chan1"])

// Correct
let ok = await Libs.mcl.quick(user.id, ["@Chan1"])
```

```js
// Wrong — numeric ID won't appear in getBtn output
Libs.mcl.getBtn([-1001234567890])

// Correct — use @username for join buttons
Libs.mcl.getBtn(["@MyChannel"])
```

---

## Notes

- Every async method must use `await`
- Membership is checked live via Telegram `getChatMember` — not cached
- Use `quick()` for simple gates; use `check()` when you need per-channel detail
- `getBtn()` is sync and safe to call without `await`
