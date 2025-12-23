# The `message` Variable

In TBL, `message` contains **only the text of a message**.

Example value:  
"Hello bot"

## How `message` Works

- If the update type is a **text message**, `message` contains that text
- If the update is **not a text message**, `message` is `null`

This means:

- Text message → `message` has value
- Photo, sticker, button, webhook, etc. → `message` is null

## Important Notes

- `message` contains text only
- It does not include media or metadata
- It exists only during command execution

For simple bots, `message` is the easiest way to read user input.
