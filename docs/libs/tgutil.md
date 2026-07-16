# tgutil

Telegram has opinions about how names, mentions, and links should look — and those opinions change depending on whether you're using Markdown or HTML. **`Libs.tgutil`** handles the formatting so you don't accidentally send a broken mention or escape character soup.

All methods are **synchronous**. No `await`.

---

## What is it?

`Libs.tgutil` provides Telegram-specific helpers for user names, clickable mentions, chat links, message links, WebApp data, long-message splitting, and text escaping.

Access: `Libs.tgutil.<method>()` (file: `libsv2/tgutil.js`).

| You pass in | You get back |
| --- | --- |
| `user` / `chat` objects | Properly formatted names and links |
| Raw user text | Safely escaped strings for Markdown or HTML |
| WebApp init data | Validated, parsed payload |

!!! tip "Globals"
    `user`, `chat`, and `bot.token` are available in command Logic. See [Global Variables](../globals/index.md).

---

## How to use it

The most common pattern — greet someone with a clickable mention:

```js
let mention = Libs.tgutil.getUserMention(user, "html")
Bot.sendMessage("Hello " + mention + "!", { parse_mode: "HTML" })
```

**Important:** match the `parseMode` argument in tgutil to `parse_mode` on `Bot.sendMessage`. HTML mention + Markdown parse mode = sad bot.

---

## Try it — beginner examples

### Welcome message with mention

```js
let mention = Libs.tgutil.getUserMention(user, "html")
Bot.sendMessage("Welcome " + mention + "!", { parse_mode: "HTML" })
```

### Safe user input in bold

```js
let safe = Libs.tgutil.escapeText(params, "html")
Bot.sendMessage("<b>You said:</b> " + safe, { parse_mode: "HTML" })
```

### Split a long reply

```js
let chunks = Libs.tgutil.splitMessage(longText, 4096)
for (let part of chunks) {
  Bot.sendMessage(part)
}
```

### User info card

```js
let info = [
  "Name: " + Libs.tgutil.getFullName(user),
  "Username: " + (user.username ? "@" + user.username : "none"),
  "Bot: " + (Libs.tgutil.isBot(user) ? "yes" : "no"),
  "Photo: " + (Libs.tgutil.getProfilePhotoUrl(user) || "none")
].join("\n")

Bot.sendMessage(info)
```

---

## User methods

### `getNameFor(member, options?)`

Best display name. Default order: username → first name → last name.

| Option | Default | Description |
| --- | --- | --- |
| `preferFullName` | `false` | Use first + last name when available |
| `preferUsername` | `false` | Prefer `@username` first |

```js
Libs.tgutil.getNameFor(user)                           // "@johndoe" or "John"
Libs.tgutil.getNameFor(user, { preferFullName: true }) // "John Doe"
```

### `getFullName(member)`

First name + last name joined. Falls back to `getNameFor()` if no names.

### `getLinkFor(member, parseMode?, customText?)`

Clickable user link. `parseMode`: `"markdown"` (default), `"html"`, or `"markdownv2"`.

Uses `member.telegramid` or `member.id` for the `tg://user?id=` target.

### `formatUser(member, options?)`

Flexible user display with optional link and ID.

| Option | Default | Description |
| --- | --- | --- |
| `showId` | `false` | Append user ID |
| `useFullName` | `false` | Use full name instead of username |
| `link` | `true` | Wrap in clickable link |
| `parseMode` | `"markdown"` | Output parse mode |
| `fallbackText` | `"Unknown User"` | Text when no name available |
| `customName` | `null` | Override display name |

### `getUserMention(member, parseMode?)`

Alias for `getLinkFor(member, parseMode)` — a clickable mention string.

```js
Libs.tgutil.getUserMention(user, "html")
// <a href="tg://user?id=123">John</a>
```

### `isBot(member)`

Returns `true` if `member.is_bot` is set or username contains `"bot"`.

### `getProfilePhotoUrl(member)`

Returns `https://t.me/i/userpic/320/{username}.jpg` when the user has a username, otherwise `null`.

---

## Chat and message methods

### `getChatLink(chat, parseMode?)`

Clickable link to a chat or group.

- Public: `https://t.me/{username}`
- Private: `chat.invite_link` or `https://t.me/c/{id}`

### `formatMessageLink(chatId, messageId, parseMode?, text?)`

Link to a specific message. `text` defaults to `"Message"`.

```js
let link = Libs.tgutil.formatMessageLink(msg.chat.id, msg.message_id, "html", "this message")
```

### `createDeepLink(botUsername, command?, params?)`

Build a `t.me` deep link with optional start command and query params.

```js
Libs.tgutil.createDeepLink("MyBot", "start", { ref: "abc123" })
// https://t.me/MyBot/start?ref=abc123
```

---

## Text formatting

### `escapeText(text, parseMode?)`

Escape special characters so user input does not break formatting.

| `parseMode` | Escapes |
| --- | --- |
| `"html"` | `&`, `<`, `>` |
| `"markdown"` / `"markdownv2"` | `_ * [ ] ( ) ~ \` > # + - = \| { } . !` |

### `parseEntities(text, entities, parseMode?)`

Convert Telegram `MessageEntity` arrays into formatted text. Processes entities from end to start to preserve offsets.

Supported types:

| Entity | Markdown | HTML |
| --- | --- | --- |
| `bold`, `italic` | `*`, `_` | `<b>`, `<i>` |
| `underline`, `strikethrough` | `__`, `~` | `<u>`, `<s>` |
| `spoiler` | `\|\|` | `<span class="tg-spoiler">` |
| `code`, `pre` | backticks | `<code>`, `<pre>` |
| `blockquote`, `expandable_blockquote` | `> ` prefix | `<blockquote>`, `<details>` |
| `text_link`, `text_mention` | `[text](url)` | `<a href="...">` |
| `custom_emoji` | emoji id | `<tg-emoji>` |

```js
let formatted = Libs.tgutil.parseEntities(msg.text, msg.entities, "html")
```

---

## WebApp helpers

### `validateWebAppData(rawData, botToken?)`

Parse and optionally verify Telegram WebApp init data. Uses HMAC-SHA256 with `bot.token` by default.

Returns:

```js
// success
{ valid: true, data: { user, chat, auth_date, query_id, hash, ... } }

// failure
{ valid: false, error: "Invalid hash signature", data: null }
```

```js
let result = Libs.tgutil.validateWebAppData(params.webapp_data)
if (!result.valid) {
  return Bot.sendMessage("Invalid WebApp data: " + result.error)
}
let webUser = result.data.user
```

### `createWebAppData(data)`

Serialize an object into URL-encoded WebApp data (objects are JSON-stringified).

```js
let payload = Libs.tgutil.createWebAppData({ user: { id: 123 }, ref: "abc" })
```

---

## Utility methods

### `splitMessage(text, maxLength?)`

Split long text into Telegram-safe chunks (default max **4096**). Splits on newlines first, then spaces, then hard-cuts.

### `formatNumber(num)`

Compact number display: `1500` → `"1.5K"`, `2500000` → `"2.5M"`, `1200000000` → `"1.2B"`.

---

## Method reference

| Method | Returns | Async |
| --- | --- | --- |
| `getNameFor(member, options?)` | `string` | No |
| `getFullName(member)` | `string` | No |
| `getLinkFor(member, parseMode?, customText?)` | `string` | No |
| `formatUser(member, options?)` | `string` | No |
| `getUserMention(member, parseMode?)` | `string` | No |
| `isBot(member)` | `boolean` | No |
| `getProfilePhotoUrl(member)` | `string \| null` | No |
| `getChatLink(chat, parseMode?)` | `string` | No |
| `formatMessageLink(chatId, messageId, parseMode?, text?)` | `string` | No |
| `createDeepLink(botUsername, command?, params?)` | `string` | No |
| `escapeText(text, parseMode?)` | `string` | No |
| `parseEntities(text, entities, parseMode?)` | `string` | No |
| `validateWebAppData(rawData, botToken?)` | `object` | No |
| `createWebAppData(data)` | `string` | No |
| `splitMessage(text, maxLength?)` | `string[]` | No |
| `formatNumber(num)` | `string` | No |

---

## Notes

- Access name is **`Libs.tgutil`** — matches `libsv2/tgutil.js`
- Pass `"html"` / `"markdownv2"` parse modes to match `Bot.sendMessage` `parse_mode`
- `getLinkFor` uses `tg://user?id=` links — works in all chats
- `validateWebAppData` uses `modules.crypto` internally for HMAC verification
- `getProfilePhotoUrl` requires a public username — not a guaranteed live photo URL for all users
- All methods are sync — no `await`
