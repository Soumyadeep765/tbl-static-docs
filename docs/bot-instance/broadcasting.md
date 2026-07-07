# Broadcasting

`Bot.broadcast()` starts a **distributed mass-messaging job** that runs a command (or sends a Telegram method) for every matching user. TBL handles chunking, queue management, rate limits, and flood protection in the background.

## Quick start

```js
let job = await Bot.broadcast({
  command: "send_promo",
  filters: { chatType: "private" }
})

Bot.sendMessage(`Broadcast started! ID: ${job.broadcastId}, targets: ${job.totalTargetChats}`)
```

## `Bot.broadcast(params)`

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `command` | `string` | One of `command` or `body` | TBL command to run per user (e.g. `"promo"`) |
| `method` | `string` | No | Telegram method if no command (default: `"sendMessage"`) |
| `body` | `object` | One of `command` or `body` | Telegram method body (e.g. `{ text: "Hello!" }`) |
| `filters` | `object` | No | User targeting filters (see below) |
| `plan` | `string` | No | Speed: `"fast"` or `"slow"`. Auto-resolved from owner plan if omitted |
| `on_create` | `string` | No | Command to run when the job is created (receives job data in `options`) |
| `on_complete` | `string` | No | Command to run when the job finishes |

**Returns:**

```js
{
  broadcastId: "uuid-string",
  totalTargetChats: 4523,
  totalBatches: 10
}
```

### Using a command

The command runs once per user with a fake update context (private chat, that user's ID):

```js
await Bot.broadcast({
  command: "weekly_digest",
  filters: { chatType: "private", premiumOnly: true }
})
```

Inside `/weekly_digest`, globals like `user` and `chat` reflect each target user.

### Using a Telegram method directly

Skip a command and send a raw Telegram API call:

```js
await Bot.broadcast({
  method: "sendMessage",
  body: { text: "System maintenance tonight at 2 AM." },
  filters: { chatType: "all" }
})
```

### Filters

| Filter | Values | Description |
| --- | --- | --- |
| `chatType` | `"private"`, `"group"`, `"channel"`, `"all"`, or array | Target chat types. `"group"` includes supergroups |
| `premiumOnly` | `true` / `false` | Filter by Telegram Premium status |

```js
// All non-blocked private users
await Bot.broadcast({ command: "promo", filters: { chatType: "private" } })

// Premium groups only
await Bot.broadcast({ command: "vip_alert", filters: { chatType: "group", premiumOnly: true } })

// Multiple chat types
await Bot.broadcast({ command: "update", filters: { chatType: ["private", "group"] } })
```

Blocked users are always excluded from broadcasts.

### Speed plans

| Plan | When used |
| --- | --- |
| `"fast"` | Premium/Elite owner plans (auto-selected) |
| `"slow"` | Free/Freemium plans (auto-selected) |

Override explicitly: `plan: "fast"` or `plan: "slow"`.

### Lifecycle hooks

```js
await Bot.broadcast({
  command: "newsletter",
  filters: { chatType: "private" },
  on_create: "broadcast_started",    // runs once when job is created
  on_complete: "broadcast_finished"  // runs when all batches complete
})
```

Hook commands receive the job record in [`options`](../globals/options.md).

## Managing broadcasts

### `Bot.stopBroadcast(broadcastId)`

Stop a running job immediately.

```js
await Bot.stopBroadcast(job.broadcastId)
// { success: true, message: "Broadcast stopped successfully" }
```

### `Bot.getBroadcastStats(broadcastId)`

Get the full job record with real-time counters.

```js
let stats = await Bot.getBroadcastStats(job.broadcastId)
```

| Field | Description |
| --- | --- |
| `broadcast_id` | Job UUID |
| `status` | `"processing"`, `"completed"`, `"stopped"` |
| `total_chats` | Total target users |
| `processed_count` | Users processed so far |
| `success_count` | Successful deliveries |
| `fail_count` | Failed deliveries |
| `pruned_count` | Skipped (blocked/deleted) |
| `total_batches` | Total batch count |
| `completed_batches` | Batches finished |
| `created_at` | Job start time |
| `finished_at` | Job end time (if done) |

### `Bot.listBroadcasts(status?)`

List broadcast jobs for the current bot.

```js
// Active jobs (default)
let active = await Bot.listBroadcasts()

// Specific statuses
let all = await Bot.listBroadcasts(["processing", "queued", "pending", "completed"])
```

Default filter: `["processing", "queued", "pending"]`.

## Broadcast execution limits

Commands triggered by broadcast run in a **restricted context**:

| Disabled | Reason |
| --- | --- |
| `TBL` instance | Prevents clone/transfer during batch |
| `HTTP` instance | Prevents blocking the batch worker |
| `User` storage | Disabled inside broadcast commands |
| `sleep()` | Prevents halting batch throughput |
| `msg` global | `null` in broadcast context |

Available: `Bot`, `Api`, `db`, globals (`user`, `chat`, `options`, etc.).

## Auto-termination rules

Broadcasts stop automatically when:

| Condition | Threshold |
| --- | --- |
| Consecutive delivery failures | **20** in a row (invalid token, blocked, etc.) |
| Script runtime errors | **15** total across any batch |

## Full example

```js
// /admin_broadcast command
let job = await Bot.broadcast({
  command: "promo_message",
  filters: {
    chatType: "private",
    premiumOnly: false
  },
  on_create: "on_broadcast_start"
})

Bot.sendMessage(`Started broadcast ${job.broadcastId} for ${job.totalTargetChats} users.`)

// Later — check progress
let stats = await Bot.getBroadcastStats(job.broadcastId)
Bot.sendMessage(`Progress: ${stats.processed_count}/${stats.total_chats} (${stats.success_count} ok)`)

// Stop if needed
await Bot.stopBroadcast(job.broadcastId)
```

## Important notes

- `Bot.broadcast()` must be **awaited** — it returns a Promise
- At least one of `command` or `body` is required
- The current bot ID is set automatically — no need to pass `botIds`
- Design broadcast commands to be fast and self-contained — no `sleep()`, no HTTP calls
- For querying users without broadcasting, use [`Bot.getUsers`](listing-users.md)
