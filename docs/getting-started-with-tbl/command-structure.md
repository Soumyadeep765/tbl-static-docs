# Command Structure in TBL

Commands are the foundation of how bots work in **TBL (Tele Bot Lang)**. Every action, response, or behavior in a TeleBotHost bot is driven by a command.

Instead of registering listeners or callbacks, TBL follows a **command-driven execution model**: each incoming update triggers exactly one command.

---

## Learn More Part-by-Part:

*   **[Command Matching & Execution Flow](matching-order.md)**: How TBL resolves and runs commands sequentially.
*   **[Special Commands](special-commands.md)**: Reserved commands like `@`, `!`, `@@`, `/start`, and `*`.
*   **[Dynamic & Update-Specific Commands](dynamic-commands.md)**: Triggering updates automatically with `/handle_{update_type}`.