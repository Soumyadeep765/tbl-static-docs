# Broadcasting

Need to tell 4,000 users about a sale? **`Bot.broadcast()`** starts a mass-messaging job that runs a command (or sends a Telegram method) for every matching user — chunking, queues, rate limits, and flood protection handled in the background.

You kick it off. The platform delivers. You go get coffee.

---

## What is broadcasting?

A **distributed job** that targets many users at once. Two ways to send:

| Approach | When to use |
| --- | --- |
| Run a **command** per user | Personalized messages, dynamic content, logic per recipient |
| Send a **Telegram method** directly | Simple identical text to everyone |

Each target user gets a simulated private-chat context — inside your broadcast command, [`user`](../learning-tbl.md) and [`chat`](../learning-tbl.md) reflect that recipient.

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md).

---

## How to use it

### Quick start

```js
let job = await Bot.broadcast({
  command: "send_promo",
  filters: { chatType: "private" }
})

Bot.sendMessage("Broadcast started! ID: " + job.broadcastId + ", targets: " + job.totalTargetChats)
```

**Returns:**

```js
{
  broadcastId: "uuid-string",
  totalTargetChats: 4523,
  totalBatches: 10
}
```

### Using a command

Your command runs once per user with that user's context:

```js
await Bot.broadcast({
  command: "weekly_digest",
  filters: { chatType: "private", premiumOnly: true }
})
```

Inside `/weekly_digest`, globals like `user` and `chat` reflect each target user.

### Using a Telegram method directly

Skip a command — send raw API calls:

```js
await Bot.broadcast({
  method: "sendMessage",
  body: { text: "System maintenance tonight at 2 AM." },
  filters: { chatType: "all" }
})
```

---

## Try it — copy-paste examples

### Simple promo to all private users

```js
let job = await Bot.broadcast({
  command: "promo_message",
  filters: { chatType: "private" }
})

Bot.sendMessage("Sending to " + job.totalTargetChats + " users.")
```

### Premium groups only

```js
await Bot.broadcast({
  command: "vip_alert",
  filters: { chatType: "group", premiumOnly: true }
})
```

### Lifecycle hooks

Run commands when the job starts or finishes. Hook commands receive job data in [`options`](../globals/options.md):

```js
await Bot.broadcast({
  command: "newsletter",
  filters: { chatType: "private" },
  on_create: "broadcast_started",
  on_complete: "broadcast_finished"
})
```

### Check progress and stop if needed

```js
let stats = await Bot.getBroadcastStats(job.broadcastId)
Bot.sendMessage("Progress: " + stats.processed_count + "/" + stats.total_chats)

await Bot.stopBroadcast(job.broadcastId)
// { success: true, message: "Broadcast stopped successfully" }
```

---

## Filters

| Filter | Values | Description |
| --- | --- | --- |
| `chatType` | `"private"`, `"group"`, `"channel"`, `"all"`, or array | Target chat types. `"group"` includes supergroups |
| `premiumOnly` | `true` / `false` | Filter by Telegram Premium status |

Blocked users are always excluded. No exceptions. They opted out.

---

## Speed plans

| Plan | When used |
| --- | --- |
| `"fast"` | Premium/Elite owner plans (auto-selected) |
| `"slow"` | Free/Freemium plans (auto-selected) |

Override explicitly: `plan: "fast"` or `plan: "slow"`.

---

## Managing broadcasts

### `Bot.stopBroadcast(broadcastId)`

Stop a running job immediately.

### `Bot.getBroadcastStats(broadcastId)`

Real-time job record:

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

```js
let active = await Bot.listBroadcasts()
let all = await Bot.listBroadcasts(["processing", "queued", "pending", "completed"])
```

Default filter: `["processing", "queued", "pending"]`.

---

## Broadcast execution limits

Commands triggered by broadcast run in a **restricted context** — designed to keep batches fast and reliable:

| Not available in broadcast commands | Why |
| --- | --- |
| Bot clone/transfer tools | Prevents accidental duplication during batch runs |
| Outbound HTTP calls | Would block batch workers |
| Legacy `User` storage | Disabled inside broadcast context |
| `sleep()` | Would halt batch throughput |
| `msg` global | `null` in broadcast context |

**Available:** `Bot`, `Api`, `db`, and globals (`user`, `chat`, `options`, etc.).

Design broadcast commands to be **fast and self-contained** — send a message, update a counter, done.

---

## Auto-termination rules

Broadcasts stop automatically when things go wrong:

| Condition | Threshold |
| --- | --- |
| Consecutive delivery failures | **20** in a row (invalid token, blocked, etc.) |
| Script runtime errors | **15** total across any batch |

---

## Method reference

### `Bot.broadcast(params)`

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `command` | `string` | One of `command` or `body` | Command to run per user (e.g. `"promo"`) |
| `method` | `string` | No | Telegram method if no command (default: `"sendMessage"`) |
| `body` | `object` | One of `command` or `body` | Telegram method body (e.g. `{ text: "Hello!" }`) |
| `filters` | `object` | No | User targeting filters |
| `plan` | `string` | No | Speed: `"fast"` or `"slow"`. Auto-resolved from owner plan if omitted |
| `on_create` | `string` | No | Command to run when job is created |
| `on_complete` | `string` | No | Command to run when job finishes |

---

## Important notes

- `Bot.broadcast()` must be **awaited** — it returns a Promise
- At least one of `command` or `body` is required
- The current bot ID is set automatically
- To query users without broadcasting, use [`Bot.getUsers`](listing-users.md)
