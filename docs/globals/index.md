# Global Variables

TBL provides built-in **global variables** in every command. They give you access to the current update, user, chat, and runtime context without any setup or imports.

## How to Use This Section

Each variable below is documented on its own page with examples and field descriptions. Variables are **read-only** during command execution unless noted otherwise.

## Available Variables

| Variable | Description |
| --- | --- |
| [update](update.md) | Full Telegram update object that triggered the command |
| [update_type](update_type.md) | String name of the update type (e.g. `message`, `callback_query`) |
| [request](request.md) | Incoming HTTP request data in webhook mode |
| [message](message.md) | The message object when the update includes one |
| [user](user.md) | The user who triggered the update |
| [chat](chat.md) | The chat where the update occurred |
| [bot](bot.md) | Metadata about the current bot |
| [owner](owner.md) | The bot owner's account information |
| [plan](plan.md) | The bot owner's subscription plan details |
| [params](params.md) | URL query parameters in webhook and Webapp commands |
| [options](options.md) | Custom data passed when running a command programmatically |
| [tbl_options](tbl_options.md) | Internal options set by TBL for HTTP callbacks and flows |
| [content](content.md) | Parsed content from the current update |
| [msg (global)](msg.md) | Shortcut to the current message context (distinct from the [msg instance](../msg-instance/index.md)) |
| [error](error.md) | Error details inside the `!` error handler command |
| [http_response](http_response.md) | Response data from HTTP callback commands |
| [process](process.md) | Environment and runtime process information |

## Important Notes

- Global variables exist only while a command is running
- Not every variable is available in every command type (e.g. `request` is webhook-only)
- The global `msg` variable is different from the [msg instance](../msg-instance/index.md) — see both pages before using message methods
