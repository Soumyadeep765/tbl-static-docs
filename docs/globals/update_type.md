# The `update_type` Variable

In TBL, `update_type` is a **string** that tells you what kind of update triggered the command. Use it to branch logic without inspecting the full `update` object.

## Common Values

### Message updates

- `message`
- `edited_message`
- `channel_post`
- `edited_channel_post`
- `business_message`
- `edited_business_message`

### Interactive updates

- `callback_query`
- `inline_query`
- `chosen_inline_result`

### Member and chat updates

- `chat_member`
- `my_chat_member`
- `chat_join_request`
- `chat_boost`
- `removed_chat_boost`

### Other Telegram updates

- `poll`, `poll_answer`
- `message_reaction`, `message_reaction_count`
- `shipping_query`, `pre_checkout_query`
- `purchased_paid_media`
- `business_connection`, `deleted_business_messages`
- `managed_bot`
- `guest_message`

### HTTP-triggered updates

- `web_request` — command triggered via webhook or webapp

If TBL cannot determine the type, the value is `"unknown"`.

## Usage

```javascript
if (update_type === 'message') {
  Bot.sendMessage(chat.id, `You wrote: ${message}`)
}

if (update_type === 'callback_query') {
  Bot.sendMessage(request.from.id, `Button: ${request.data}`)
}

if (update_type === 'web_request') {
  res.send({ status: 'ok' })
}
```

## Important Notes

- `update_type` is read-only and exists only during command execution
- Values match Telegram update type names where applicable
- See the [Telegram Bot API Update object](https://core.telegram.org/bots/api#update) for the full upstream list
