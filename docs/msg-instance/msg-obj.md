## msg as an Object

The **msg instance** also acts as a **message object**.

It contains the full Telegram message data for the current update.

## Common Properties

- `msg.text`  
  Message text (if any)

- `msg.chat`  
  Chat information (id, type, title, etc.)

- `msg.from`  
  Sender information

- `msg.message_id`  
  Unique message identifier

- `msg.date`  
  Message timestamp

All standard Telegram **Message fields** are available through `msg`.

## Availability

- The msg object exists only for **message-based updates**
- It is not available for non-message updates (like callbacks or webhooks)
- All message-related actions rely on this object

## Notes

- All msg methods are case-insensitive  
  Example: `msg.replyPhoto()` and `msg.replyphoto()` both work

- Markdown parsing is enabled by default for text replies

- msg provides both **data access** and **action methods** in one place
