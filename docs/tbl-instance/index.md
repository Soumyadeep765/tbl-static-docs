# TBL

Manage bot lifecycles directly from your commands.

## What is TBL?

The global `TBL` instance lets you manage bot lifecycle actions from your scripts. You can duplicate a bot, move it to another account, or carry settings over during the process.

It functions like the [Bot](../bot-instance/index.md) and [Api](../api-instance/index.md) instances. TeleBotHost exposes it in your command environment without any imports.

| You get | You skip |
| --- | --- |
| Direct bot duplication | Creating bots manually and copy-pasting code |
| Instant bot transfers | Sharing credentials or config files |
| Property copying | Re-entering environment keys and database settings |

---

## How to use it

Use the `TBL` instance to perform actions on bots you own. Note that these operations only run in standard Telegram command executions. They return `null` in webhooks, webapps, and broadcasts.

---

## What's in this section

| Page | What it covers |
| --- | --- |
| [Cloning Bots](clone.md) | How to duplicate a bot, assign a new token, and copy settings. |
| [Transferring Bots](transfer.md) | How to move ownership of a bot to another account. |

For detailed parameters, examples, and response shapes, check the individual pages.
