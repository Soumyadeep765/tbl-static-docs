# Distributed Broadcasting

The `Bot` namespace provides built-in methods to initialize and control high-throughput, distributed broadcasts across your bot's users.

---

## 1. `Bot.broadcast(params)`
Initiates a broadcast job. TBL handles chunking, execution routing, flood limits, and queue management in the background.

### Parameters:
*   `command` *(string)*: TBL command name (e.g. `"promo"`) to execute for each user.
*   `method` *(string)*: Telegram method to invoke (defaults to `"sendMessage"` if `command` is omitted).
*   `body` *(object)*: Body parameters for the Telegram method.
*   `filters` *(object)*: Query filters to target specific user groups (e.g., `{ chatType: "private" }`).
*   `plan` *(string)*: Speed plan, either `"fast"` or `"slow"`. Defaults to automatic owner plan resolution.

### Usage Example:
```javascript
// Start a promo broadcast to all private chats
const job = await Bot.broadcast({
  command: "send_promo",
  filters: { chatType: "private" }
});
Bot.sendMessage(`Broadcast started! Job ID: ${job.broadcastId}`);
```

---

## 2. Managing Broadcasts

### `Bot.stopBroadcast(broadcastId)`
Stops a currently running broadcast job immediately.
```javascript
await Bot.stopBroadcast("job-12345");
```

### `Bot.getBroadcastStats(broadcastId)`
Retrieves real-time processing statistics for a job.
```javascript
const stats = await Bot.getBroadcastStats("job-12345");
/* returns: {
  processed_count,
  success_count,
  fail_count,
  pruned_count,
  status: "processing" | "completed" | "stopped"
} */
```

### `Bot.listBroadcasts(status)`
Retrieves a list of broadcast jobs filtered by their current status.
```javascript
const activeJobs = await Bot.listBroadcasts(['processing', 'queued']);
```

---

## 3. Important Broadcast Constraints

To ensure optimal performance and security during large broadcasts, the execution context of commands triggered via broadcast has the following limitations:

1.  **Disabled Global Namespaces**:
    *   `TBL` and `HTTP` objects are **not accessible** during broadcast runs.
    *   `User` storage operations are **disabled** inside broadcast commands.
    *   Calling `sleep()` is **disabled** to avoid halting the batch throughput.
2.  **Early Termination Rules**:
    *   **Failed Deliveries**: If the first **20 consecutive** dispatches fail (e.g. token invalid or blocked), the broadcast stops automatically.
    *   **Script Failures**: If the command script throws runtime/compilation errors **15 times** across any batch, the broadcast is aborted to prevent error loops.
