# The `request` Variable

In TBL, `request` is a **simplified version of `update`**

TBL automatically detects the type of Telegram update and maps the relevant part into `request`.

## How `request` Works

For normal Telegram updates:

- If the update type is `message`, then `request` is equal to `update.message`
- If the update type is something else, `request` points to that specific part of the update

This means you don’t need to manually check update types in most cases.

!!! info
    `request` helps you work with the useful data directly, without parsing the full update JSON.

## `request` in Webhook Mode

!!! info 
     ignore if you don't know abou `Webhook` feature in TBL.

When a command is triggered via **webhook**, `request` contains HTTP request data instead of Telegram message data.

It may include:

- Request IP
- Request body
- URL parameters
- Headers
- Method and metadata

This makes `request` useful for building APIs, dashboards, and external integrations.

## Important Notes

- `request` is read-only
- It exists only during command execution
- Its structure depends on how the command was triggered

For simple bots, you can use `request` instead of working with raw `update`.
