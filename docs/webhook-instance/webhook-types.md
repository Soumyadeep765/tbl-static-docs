# Webhook Types

The Webhook instance supports two types of webhook execution, depending on how the webhook is created and used.

## User-Based Webhook

A **user-based webhook** executes a command **in the context of a specific user**.

In this type:

- `user` is available
- `chat` is available
- The command behaves like a normal user-triggered command

This is useful when:

- A web action should act on behalf of a user
- You need access to user-specific or chat-specific data
- The webhook is linked to a logged-in user or session

User-based webhooks allow full interaction with user and chat data.

## Global Webhook

A **global webhook** is **not tied to any user**.

In this type:

- `user` is `null`
- `chat` is `null`
- The command runs at a global level

This is useful when:

- The webhook is triggered by a system or service
- No user context is required
- You want to perform background or account-level actions


## Notes

- Both webhook types are secure and signed
- Both trigger normal TBL commands
- The difference is only the availability of `user` and `chat`
