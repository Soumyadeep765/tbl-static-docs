## tgutil

tgutil provides **Telegram-specific helper utilities** for working with users, text formatting, links, and buttons.

It helps simplify common Telegram-related tasks and ensures safe formatting across messages.

tgutil is available through the `Libs` instance.

## Get User’s Full Name

Combine first name and last name safely.

```js
let fullName = Libs.tgutil.getFullName(user)
```

This returns a properly formatted full name for the user.

## Create a Clickable User Link

Generate a clickable link to a user profile.

```js
let link = Libs.tgutil.getLinkFor(
  user,
  "html"
)
```

The format can be `html` or `markdown`.

## Escape Text Safely

Escape text to prevent formatting issues.

```js
let safeText = Libs.tgutil.escapeText(
  "*Hello*",
  "markdown"
)
```

This ensures the text is safe to send in messages.

## Create an Inline Button

Generate an inline keyboard button.

```js
let btn = Libs.tgutil.createInlineButton(
  "Press Me",
  "/callback_data"
)
```

The returned button can be used in `reply_markup`.

## Notes

- Useful for mentions, links, and formatting
- Prevents Markdown and HTML injection issues
- Designed for Telegram-specific workflows

## Full Documentation

[tgutil Documentation]

[tgutil Documentation]: https://github.com/telebothost/tbl-libs/blob/main/Lib-Docs/tgutil.md