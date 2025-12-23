# Api Instance

The **Api instance** is used to interact with Telegram.

It is a simple wrapper around the **Telegram Bot API**, so you don’t need to work with raw HTTP requests.

In TBL, `Api` is already available in every command.  
You never create or import it.

## Why Api Exists

Telegram’s raw Bot API is low-level and complex.

Using it directly would require:

- Building HTTP requests manually
- Passing chat IDs every time
- Handling responses and errors

The Api instance simplifies all of this.

You just call:

Api.xxx({ ... })

And TBL handles the rest.

## Chat Context

By default, **Api methods use the current chat** — the chat where the command was triggered.

You can also explicitly pass a `chat_id` if you want to send a message to a different chat.

## What Api Is Used For

Using Api, your bot can:

- Send messages
- Send photos and media
- Edit or delete messages
- Create interactive buttons

The Api instance is the main way your bot communicates with Telegram.
