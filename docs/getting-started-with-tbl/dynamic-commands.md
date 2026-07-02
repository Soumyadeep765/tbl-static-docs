# Dynamic and Update-Specific Commands

TBL routes specific Telegram updates directly to dedicated commands, removing the need for manual parsing or custom listeners.

---

## 1. Dynamic Handlers (`/handle_{update_type}`)
Any Telegram update containing a specific event type is automatically routed to a command matching the pattern `/handle_{update_type}`.

### Common Examples:
*   **`/handle_channel_post`**: Triggers when a new post is added to a channel where the bot is an administrator.
*   **`/handle_chat_member`**: Triggers when a user's chat member status changes (e.g. joining/leaving group).
*   **`/handle_poll_answer`**: Triggers when a user votes in a bot-generated poll.
*   **`/handle_message_reaction`**: Triggers when a user adds or changes a reaction to a message.

---

## 2. `/inline_query` (Inline Query Command)
Handles Telegram's inline mode, which occurs when a user types `@yourbot query` in any chat.

*   **Trigger**: Triggered automatically on incoming inline queries.
*   **Purpose**: Returns inline search results or dynamic buttons.

---

## 3. `/channel_update` (Channel Fallback Command)
Serves as the fallback command specifically for all channel-related posts or edits if the more specific `/handle_channel_post` is not defined.
