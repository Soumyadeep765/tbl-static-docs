# User Instance

The **User instance** is used to **store and manage data at the user level**.

Just like the Bot instance stores data for the bot, the User instance stores data **separately for each user**.

Each user has their **own private storage**, and data saved for one user is not shared with others.

This is useful for:

- User preferences
- User-specific settings
- Progress or flow state
- Any per-user information

User-level data is automatically scoped to the current user, so you don’t need to manage user IDs manually.