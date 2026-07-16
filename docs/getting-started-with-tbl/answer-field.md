# Answer Field Reference

The **Answer** field in a command allows you to automatically send a message to the user before your logic script executes. It is perfect for lightning-fast greetings, static menus, or prompting users for input.

It supports two modes: **Plain Text** (with simple variable placeholders) and **JS-like Syntax** (for conditional responses).

---

## 1. Plain Text Mode

By default, any text you write is sent exactly as written. You can inject dynamic values using `{{variable.path}}` placeholders.

### Example
```
Hey {{user.first_name}}! Welcome to the bot.
Your user ID is {{user.id}}.
```

If a variable is missing or resolving to `undefined`, it will gracefully render as an empty string.

---

## 2. Advanced JS-like Syntax

If the Answer field contains the pattern `answer(`, the engine automatically upgrades it to **JS-like Syntax Mode**. In this mode, the entire field is evaluated as a sandboxed mini-language where you call `answer(...)` to send your message.

### Use Case Examples

**VIP check:**
```js
if (user.is_premium) {
  answer("Welcome VIP member {{user.first_name}}!");
} else {
  answer("Hello {{user.first_name}}!");
}
```

**Route by language code:**
```js
if (user.language_code == "es") {
  answer("¡Hola {{user.first_name}}!");
} else if (user.language_code == "fr") {
  answer("Bonjour {{user.first_name}}!");
} else {
  answer("Hello {{user.first_name}}!");
}
```

---

## Available Variables & Objects

Here is a full list of all objects and properties available for reading within your placeholders and conditions:

### `user`
Information about the user who triggered the command:
- `user.id`: Telegram ID of the user (number)
- `user.first_name`: First name (string)
- `user.last_name`: Last name (string, optional)
- `user.username`: @username (string, optional)
- `user.language_code`: User language tag (string, e.g., `"en"`)
- `user.is_premium`: `true` if they have Telegram Premium (boolean)
- `user.is_bot`: `true` if the sender is another bot (boolean)

### `chat`
Details about the current chat context:
- `chat.id`: Telegram ID of the chat (number)
- `chat.type`: The chat type — `"private"`, `"group"`, `"supergroup"`, or `"channel"` (string)
- `chat.title`: Title of the group or channel (string, optional)
- `chat.username`: Public username of the chat (string, optional)

### `bot`
Details about your bot:
- `bot.id`: Telegram ID of the bot (number)
- `bot.first_name`: Display name of the bot (string)
- `bot.username`: Username of the bot (string)
- `bot.status`: `"working"` or `"stopped"` (string)

### `env` & `process.env`
Dictionary of custom environment variables configured for your bot:
- `{{env.API_KEY}}` or `{{process.env.API_KEY}}`

### `account` & `owner`
Details about the bot owner:
- `account.mail` / `owner.mail`: Owner's email address
- `account.id` / `owner.id`: Owner's database ID

### `plan`
Information about the active subscription tier:
- `plan.name`: Pricing plan name (e.g. `"VIP"`, `"Free"`)

### `message`
The raw text string of the message that triggered the command (or `null` if the update has no text).

### `params`
The text payload passed after the command name (e.g. `/start abc` -> `params = "abc"`).

### `update`
The full, raw Telegram update payload. Great for traversing custom payload shapes.

### `request`
The processed HTTP request metadata (payload, headers, query params) for web/webhook/webapp triggers.

### `options`
The execution context options object.

### `http_response`
The response metadata for HTTP triggers (such as `http_response.status`).

---

## Syntax & Language Rules

### 1. Conditional Logic
You can use `if`, `else if`, and `else` blocks with standard curly braces `{}`.

### 2. Operators
- **Comparison Operators**: `==` (equals), `!=` (does not equal), `<` (less than), `>` (greater than), `<=` (less or equal), `>=` (greater or equal).
- **Logical Operators**: `&&` (AND), `||` (OR), `!` (NOT).
- **Grouping**: Parentheses `(...)` to prioritize condition evaluations.

### 3. Literal Values
The following literal values are recognized:
- **Strings**: `"hello"`, `'hello'`, `` `hello` ``
- **Numbers**: `42`, `-15`, `3.14`
- **Booleans**: `true`, `false`
- **Null & Undefined**: `null`, `undefined`

---

## Formatting & Auto-Escaping

Values replaced in placeholders (`{{...}}`) are automatically escaped based on the command's **Parse mode** to keep formatting crisp and avoid Telegram API errors:

- **HTML Mode**: Converts `<`, `>`, and `&` to their safe entities.
- **Markdown Mode**: Escapes special characters `_`, `*`, `[`, `]`, `` ` ``, and `\`.
- **MarkdownV2 Mode**: Escapes all V2 markdown characters (`_`, `*`, `[`, `]`, `(`, `)`, `~`, `` ` ``, `>`, `#`, `+`, `-`, `=`, `|`, `{`, `}`, `.`, `!`, `\`).

---

### Graceful Syntax Error Fallback
If you accidentally write a typo or syntactically invalid code in JS-like mode, the engine won't crash your bot. It logs the issue to the database and falls back to treating the text as plain text, still safely interpolating any valid variable placeholders.
