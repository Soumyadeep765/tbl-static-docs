# tgutil

`Libs.tgutil` provides Telegram-specific helpers for user names, mentions, chat links, message links, and text escaping. All methods are **synchronous**.

```js
let name = Libs.tgutil.getFullName(user)
let mention = Libs.tgutil.getUserMention(user, { parseMode: "html" })
let safe = Libs.tgutil.escapeText("*bold*", "markdown")
```

---

## User methods

### `getNameFor(member, options?)`

Best display name — prefers `@username` unless `preferFullName: true`.

```js
Libs.tgutil.getNameFor(user)                              // "@johndoe" or "John"
Libs.tgutil.getNameFor(user, { preferFullName: true })    // "John Doe"
```

Returns `""` if the user has no username, first name, or last name.

### `getFullName(member)`

First name + last name joined. Falls back to `getNameFor()` if no names.

```js
Libs.tgutil.getFullName(user)  // "John Doe"
```

### `getLinkFor(member, parseMode?)`

Clickable user link. `parseMode`: `"markdown"` (default) or `"html"`.

```js
// Markdown: [John](tg://user?id=123456)
Libs.tgutil.getLinkFor(user, "markdown")

// HTML: <a href="tg://user?id=123456">John</a>
Libs.tgutil.getLinkFor(user, "html")
```

Uses `member.telegramid` or `member.id` for the link target.

### `formatUser(member, options?)`

Flexible user display with optional link and ID.

| Option | Default | Description |
| --- | --- | --- |
| `showId` | `false` | Append user ID |
| `useFullName` | `false` | Use full name instead of username |
| `link` | `true` | Wrap in clickable link |
| `parseMode` | `"markdown"` | `"markdown"` or `"html"` |
| `fallbackText` | `"Unknown User"` | Text when no name available |

```js
Libs.tgutil.formatUser(user, { showId: true, parseMode: "html" })
// '<a href="tg://user?id=123">John</a> (123)'
```

### `getUserMention(member, options?)`

Shorthand for `formatUser(member, { link: true, ...options })`.

```js
Bot.sendMessage(chat.id,
  "Hello " + Libs.tgutil.getUserMention(user, { parseMode: "html" }) + "!",
  { parse_mode: "HTML" }
)
```

### `isBot(member)`

Returns `true` if `member.is_bot` is set or username ends with `"bot"`.

```js
if (Libs.tgutil.isBot(user)) {
  Bot.sendMessage(chat.id, "Bots are not allowed.")
}
```

---

## Chat methods

### `getChatLink(chat, parseMode?)`

Clickable link to a chat or group.

```js
Libs.tgutil.getChatLink(chat, "html")
// Public: https://t.me/groupname
// Private: uses invite_link or t.me/c/... format
```

Uses `chat.username`, `chat.invite_link`, or derives a private link from `chat.id`.

### `formatMessageLink(chatId, messageId, parseMode?)`

Link to a specific message in a chat.

```js
let link = Libs.tgutil.formatMessageLink(msg.chat.id, msg.message_id, "html")
Bot.sendMessage(chat.id, "See " + link, { parse_mode: "HTML" })
```

---

## Text formatting

### `escapeText(text, parseMode?)`

Escape special characters so user input does not break formatting.

```js
// MarkdownV2-style escaping
Libs.tgutil.escapeText("*hello*", "markdown")  // "\*hello\*"

// HTML escaping
Libs.tgutil.escapeText("<b>hi</b>", "html")    // "&lt;b&gt;hi&lt;/b&gt;"
```

### `parseEntities(text, entities, parseMode?)`

Convert Telegram message entities (bold, italic, links, etc.) into formatted text.

```js
let formatted = Libs.tgutil.parseEntities(
  msg.text,
  msg.entities,
  "markdown"
)
```

Supported entity types: `bold`, `italic`, `code`, `pre`, `text_link`, `mention`.

---

## Method reference

| Method | Returns | Async |
| --- | --- | --- |
| `getNameFor(member, options?)` | `string` | No |
| `getFullName(member)` | `string` | No |
| `getLinkFor(member, parseMode?)` | `string` | No |
| `formatUser(member, options?)` | `string` | No |
| `getUserMention(member, options?)` | `string` | No |
| `isBot(member)` | `boolean` | No |
| `getChatLink(chat, parseMode?)` | `string` | No |
| `formatMessageLink(chatId, messageId, parseMode?)` | `string` | No |
| `escapeText(text, parseMode?)` | `string` | No |
| `parseEntities(text, entities, parseMode?)` | `string` | No |

---

## Examples

### Welcome message with mention

```js
let mention = Libs.tgutil.getUserMention(user, { parseMode: "html" })
Bot.sendMessage(chat.id, "Welcome " + mention + "!", { parse_mode: "HTML" })
```

### Safe user input in bold

```js
let safe = Libs.tgutil.escapeText(params, "html")
Bot.sendMessage(chat.id, "<b>You said:</b> " + safe, { parse_mode: "HTML" })
```

### User info card

```js
let info = [
  "Name: " + Libs.tgutil.getFullName(user),
  "Username: " + (user.username ? "@" + user.username : "none"),
  "Bot: " + (Libs.tgutil.isBot(user) ? "yes" : "no")
].join("\n")

Bot.sendMessage(chat.id, info)
```

---

## Notes

- Pass `parseMode: "html"` when sending with `parse_mode: "HTML"` on `Bot.sendMessage`
- `getLinkFor` and `formatUser` use `tg://user?id=` links — works in all chats
- `getChatLink` for private groups requires `chat.invite_link` or a `-100` chat ID
- All methods are sync — no `await`
