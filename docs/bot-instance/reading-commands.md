# Reading Commands and Their Code

TBL allows you to **read existing commands programmatically** using the Bot instance.

This is useful for:

- Debugging command logic
- Building admin or moderation tools
- Showing command previews
- Creating documentation bots
- Auditing or inspecting commands safely

## Reading Command Code Only

The `Bot.read()` method returns **only the raw source code** of a command.

It does not include command settings like answer, keyboard, aliases, or reply behavior.

The returned value is a **plain string**.

### Example

```js
// Read the raw code of a command
let code = Bot.read("/start")

// it returns a String
```

Use this when you only care about **how the command works internally**.

!!! tip
    `Bot.read()` is ideal for code previews, AI analysis, or debugging logic issues.

## Reading Full Command Object

The `Bot.readCommand()` method returns the **entire command definition**.

This includes:

- The command code
- Answer text
- Keyboard configuration
- Aliases
- need_reply flag
- Other command settings

### Example

```js
// Read full command structure
let cmd = Bot.readCommand("/start")
```

### Example Response

```json
{
  "code": "const {random} = require(\"/send\");\n\nconst x = random(1, 100);\nBot.sendMessage(\"Random: \" + x);",
  "answer": null,
  "keyboard": null,
  "aliases": [],
  "allow_only_group": false,
  "need_reply": false
}
```

Use this when you need **both the logic and the configuration** of a command.

!!! info
    `Bot.readCommand()` is commonly used in admin panels, editors, and bot management systems.

## Important Notes

- Both methods are read-only
- The target command must exist
- Missing commands will throw an error
- Errors can be handled using the `!` command
- Returned data never executes automatically
