# Special Commands

TBL defines several special reserved commands that have unique behaviors and trigger points in the lifecycle of an update.

---

## 1. `/start` (Entry Command)
The primary entry point when a user starts a conversation with the bot.

*   **Trigger**: Sent when a user clicks the "Start" button or sends `/start`.
*   **Purpose**: Welcoming users, showing main menus, or initializing state.

---

## 2. `@` (Initialization Command)
Runs automatically **before** any other matched command for every single update.

*   **Purpose**:
    *   Initialize global variables or helper state.
    *   Run authorization checks or rate limiter checks.
    *   Load common configurations.

---

## 3. `!` (Error Handler Command)
Executed automatically if any runtime error or exception occurs during the execution of another command.

*   **Purpose**:
    *   Catch errors cleanly without causing silent failures.
    *   Alert developers or send a fallback error message to the user.

---

## 4. `@@` (Post-Processor Command)
Runs automatically **after** any command execution finishes, regardless of whether it succeeded or failed.

*   **Purpose**:
    *   Run analytics or log metrics.
    *   Perform cleanup operations.

---

## 5. `*` (Fallback Command)
Triggered when no other command matches the incoming text or update trigger.

*   **Purpose**:
    *   Acts as a catch-all safety net.
    *   Provides user guidance or menu prompts for unrecognized inputs.
