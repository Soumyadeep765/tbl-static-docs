## Storage Monitoring

The **Global instance** can be used to **monitor storage usage at the account level**.

It gives visibility into total storage consumed across:

- Bot data
- User data
- Global data

This helps you track usage, prevent limits from being reached, and plan cleanups.

## Get Detailed Storage Information

Retrieve detailed storage stats for your account.

```js
let storageInfo = Global.getStorageInfo()
Bot.inspect(storageInfo)
```

Example output:

```json
{
  "size": 1572864,
  "prop_count": 42,
  "last_calc": "2024-01-15T10:30:00.000Z"
}
```

- `size` → total storage used (bytes)
- `prop_count` → total stored entries
- `last_calc` → last calculation timestamp

## Get Storage Usage Percentage

Check how much storage is used as a percentage (0–100).

```js
let usagePercent = Global.getStorageUsage()
Bot.sendMessage("Storage usage: " + usagePercent + "%")
```

This is useful for dashboards or alerts.

## Check If Storage Is Near Limit

You can quickly detect when storage is close to full.

```js
if (Global.isStorageNearLimit()) {
  Bot.sendMessage("⚠️ Storage almost full! Please clean up some data.")
}
```

By default, this checks against a **90% threshold**.

## Get Available Storage

Find out how much storage is still available.

```js
let availableMB = Global.getAvailableStorage()
Bot.sendMessage("Available storage: " + availableMB + " MB")
```

This value is returned in **megabytes (MB)**.

## Notes

- All storage metrics are **account-wide**
- Includes Bot, User, and Global data
- Useful for monitoring, alerts, and maintenance
- Helps avoid unexpected storage limits

The Global instance provides a simple way to **observe and manage your account’s storage usage**.
