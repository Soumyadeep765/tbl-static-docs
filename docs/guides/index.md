# Guides

These pages answer questions that come up once you've got a bot running but aren't sure which tool to reach for.

They sit between the [Command Flow](../getting-started-with-tbl/index.md) guides (how commands work) and the reference sections (method lists and variable docs).

## Command & interaction guides

| Guide | When to read |
| --- | --- |
| [Command Flow](../getting-started-with-tbl/index.md) | Understand matching, execution, fields |
| [Handling Callbacks](../getting-started-with-tbl/handling-callbacks.md) | Inline buttons, `answerCallbackQuery`, edit message |
| [Markdown & Formatting](../getting-started-with-tbl/markdown-and-formatting.md) | Bold/italic answers, `md2html` |
| [Public Web Commands](../getting-started-with-tbl/public-web-commands.md) | Static `is_web` pages per bot |
| [Handling User Input](../getting-started-with-tbl/handle-need-reply.md) | Multi-step input flows |

## Instance comparison

**[Bot vs Api](bot-vs-api.md)** — lives in the sidebar after the [Bot](../bot-instance/index.md) and [Api](../api-instance/index.md) sections. Read those overviews first, then use the comparison when both objects start to blur together.

## Choosing a web surface

| Need | Use |
| --- | --- |
| Static landing page | [Public web](../webapp-instance/public-web.md) (`is_web`) |
| Dynamic API with `db` | [Webapp](../webapp-instance/index.md) |
| Signed per-user action | [User webhook](../webhook-instance/user-webhook.md) |
| Cron / system trigger | [Global webhook](../webhook-instance/global-webhook.md) |

## Where to go next

Haven't built a bot yet? [Getting Started](../getting-started.md) → [Your First Bot](../getting-started-with-tbl/first-hello-bot.md).

For context in every command: [Global Variables](../globals/index.md).

For instance reference: [Bot](../bot-instance/index.md), [Api](../api-instance/index.md), [Bot vs Api](bot-vs-api.md).
