# update_type

A plain string that tells you *what just happened* — no detective work required.

## What is it?

**`update_type`** is a string naming the kind of Telegram update that triggered your command. Instead of poking through the entire [`update`](update.md) object asking "was it a message? a button? a poll?", you get a clean label like `"message"` or `"callback_query"`.

It's the difference between reading a novel and reading the chapter title. Sometimes you need the novel. Often the title is enough.

## When would you use it?

Use `update_type` whenever your command handles **more than one kind of event** and you need to branch:

- Echo text messages but ignore photos
- Route callback buttons to different logic
- Detect webhook traffic vs normal Telegram updates
- Skip processing for update types your command doesn't care about

Pair it with [`request`](request.md) — `update_type` tells you *what*, `request` gives you the *details*.

---

## Try it

```js
if (update_type === "message") {
  Bot.sendMessage("You wrote: " + message)
}

if (update_type === "callback_query") {
  Bot.sendMessage(request.from.id, "Button pressed: " + request.data)
}

if (update_type === "web_request") {
  res.send({ status: "ok" })
}
```

---

## Common values

### Messages

- `message`
- `edited_message`
- `channel_post`
- `edited_channel_post`
- `business_message`
- `edited_business_message`

### Interactive

- `callback_query` — inline keyboard button taps ([Handling Callbacks](../getting-started-with-tbl/handling-callbacks.md))
- `inline_query`
- `chosen_inline_result`

### Members and chats

- `chat_member`
- `my_chat_member`
- `chat_join_request`
- `chat_boost`
- `removed_chat_boost`

### Everything else

- `poll`, `poll_answer`
- `message_reaction`, `message_reaction_count`
- `shipping_query`, `pre_checkout_query`
- `purchased_paid_media`
- `business_connection`, `deleted_business_messages`
- `managed_bot`
- `guest_message`

### HTTP-triggered

- `web_request` — command fired via [Webhook](../webhook-instance/index.md) or [Webapp](../webapp-instance/index.md)

If the type can't be determined, the value is `"unknown"`. The universe is mysterious sometimes.

---

## Good to know

- `update_type` is read-only and exists only during command execution
- Values match [Telegram update type names](https://core.telegram.org/bots/api#update) where applicable
- For quick text-only checks, [`message`](message.md) is even simpler — but only works for text messages
