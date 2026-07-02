# The plan Variable

In TBL, `plan` contains subscription and feature details of the bot owner's plan. It specifies the resource limits, rate limits, and features available for the current bot.

---

## Subscription Tier Limits Reference

Below is a detailed comparison of resource and rate limits across the different TBL subscription tiers.

| Tier Name | Premium Status | Timeout (seconds) | Buffer Size (KB/MB) | Parallel Processes | Max Sleep (seconds) | Rate Limits (Min / Day) |
| --- | --- | --- | --- | --- | --- | --- |
| **Free** | false | 15s | 512 KB | 10 | 10s | 15 / min, 5,000 / day |
| **Freemium** | false | 15s | 512 KB | 10 | 10s | 30 / min, 5,000 / day |
| **Premium** | true | 30s | 5 MB | 20 | 20s | 60 / min, 10,000 / day |
| **Elite** | true | 60s | 10 MB | 40 | 50s | 120 / min, 20,000 / day |

---

## What the Limits Mean

*   **Timeout**: The maximum time (in seconds) a command script is allowed to execute before being forcefully terminated.
*   **Buffer Size**: The maximum memory allocation allowed for safe buffer creations within scripts.
*   **Parallel Processes**: The maximum number of concurrently executing updates or RPC calls allowed per instance.
*   **Max Sleep**: The maximum duration allowed when calling `sleep()`.
*   **Rate Limits**: The fixed-window limits applied to incoming updates (per minute and per day) to protect system resources.

---

## Example plan Object Structure

```json
{
  "name": "Elite",
  "premium": true,
  "ads": false,
  "prop_limit": {
    "per_account": 100
  },
  "timeout": 60000,
  "buffer_size": 10485760,
  "parallel_process": 40,
  "support_contact": true,
  "sleep": 50,
  "rate_limit": {
    "perMinute": 120,
    "perDay": 20000
  }
}
```
