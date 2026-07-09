# translate

Multi-language translation for multilingual bots. Uses [`HTTP`](../http-instance/index.md) + [`db`](../db-instance/index.md). Access: **`Libs.translate`**. **All storage/translate methods need `await`.** v1.0.0

---

## What is it?

`Libs.translate` translates text to a user's preferred language using a provider fallback chain:

**Google → MyMemory → Lingva → LibreTranslate**

| Feature | Detail |
| --- | --- |
| Languages | 20 supported (en, hi, es, fr, de, …) |
| User lang | `db.user` key `user_lang` |
| Usage quota | `db.bot` key `translate_daily_usage` (MyMemory only) |
| Safe API | `tryTranslate()` never throws |

---

## Quick start

```js
// Set language
await Libs.translate.setUserLang(user.id, "hi")

// Translate to user's language
let text = await Libs.translate.translate("Welcome to our bot!")

// Shorthand
let hi = await Libs.translate.t("Hello", "hi")
```

---

## Core methods

| Method | Description |
| --- | --- |
| `translate(text, options)` | Main translate API (throws on failure) |
| `tryTranslate(text, options)` | Safe — returns `{ ok, text, provider, error }` |
| `t(text, to)` | Shorthand translate |
| `setUserLang(userId, code)` | Save preference |
| `getUserLang(userId?)` | Get preference |
| `getUsageInfo()` | Daily word quota stats |
| `canTranslate(text)` | Check quota before translating |
| `batch(texts, options)` | Translate array sequentially |
| `stats(userId?)` | Lang + usage bundle |
| `configure(options)` | Limits, providers, timeout, cfProxy |
| `langButtons(options)` | Inline keyboard rows for language picker |
| `parseLangCallback(data, prefix?)` | Parse callback from picker |
| `formatLangList()` | Display string of all languages |
| `listLanguages()` | `[{ code, name }]` sorted |
| `resetUsage()` | Reset daily counter |

### `translate` / `tryTranslate` options

| Option | Description |
| --- | --- |
| `to` | Target language code |
| `from` | Source language (`"auto"` default) |
| `userId` | Use this user's saved lang |
| `fallback` | Return value if all providers fail |
| `silent` | Return original text instead of throwing |

---

## Examples

### Safe translate (no try/catch)

```js
let r = await Libs.translate.tryTranslate("Hello!", { to: "es" })
if (r.ok) {
  Bot.sendMessage(chat.id, r.text)
} else {
  Bot.sendMessage(chat.id, "Translation unavailable")
}
```

### Language picker

```js
// Command: /language
let rows = Libs.translate.langButtons({ perRow: 2, prefix: "lang_" })
Bot.sendMessage(chat.id, "Choose language:", {
  reply_markup: { inline_keyboard: rows }
})

// Callback handler
let code = Libs.translate.parseLangCallback(callback_data, "lang_")
if (code) {
  await Libs.translate.setUserLang(user.id, code)
  Bot.sendMessage(chat.id, "Language set to " + Libs.translate.langName(code))
}
```

### Auto-reply in user's language

```js
let reply = await Libs.translate.translate(
  "Your order has been confirmed!",
  { userId: user.id, silent: true }
)
Bot.sendMessage(chat.id, reply)
```

### Configure providers

```js
Libs.translate.configure({
  dailyLimit: 1000,
  maxLength: 500,
  timeout: 10000,
  providers: ["google", "mymemory", "lingva"],
  cfProxy: process.env.CF_PROXY_URL  // optional
})
```

---

## Storage keys

| Key | Scope | Purpose |
| --- | --- | --- |
| `user_lang` | `db.user` | Language preference |
| `translate_daily_usage` | `db.bot` | Daily MyMemory word count |

---

## HTTP notes

- Providers check `res.ok` per [HTTP docs](../http-instance/responses.md)
- Uses `responseType: "json"` and object `body` for POST
- MyMemory quota tracked; Google/Lingva/Libre are free fallback
- Max text length: 500 chars (configurable)

### Legacy

`autoTranslate(text, lang)` still works — alias for `translate()`.

[HTTP overview](../http-instance/index.md) · [db.user](../db-instance/user.md)
