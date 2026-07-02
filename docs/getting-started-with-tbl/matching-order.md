# Command Matching & Execution Flow

TBL uses a strict, deterministic resolution order to determine which command matches an incoming Telegram update.

---

## 1. Matching Priority Order

When an update is received, TBL matches commands in this exact order:

1.  **Exact Command Match**: Matches if the user input text matches a slash or text command name exactly (e.g., `/start` or `Help`).
2.  **Aliases Match**: Matches if the input matches any registered aliases of a command.
3.  **Dynamic Update Handlers**: Matches `/handle_{update_type}` matching the incoming event.
4.  **Fallback/Wildcard**: Matches the fallback command (`*`).

---

## 2. Command Execution Flow

Each incoming update triggers exactly one matching command and follows a structured execution path:

```
Update Received
      │
      ▼
Execute `@` Initialization Command
      │
      ▼
Execute Matched Command (e.g. `/start` or text match)
      │
 ┌────┴────┐ (If runtime error occurs)
 │         ▼
 │    Execute `!` Error Handler Command
 │         │
 └────┬────┘
      ▼
Execute `@@` Post-Processor Command
      │
      ▼
Execution Complete
```
