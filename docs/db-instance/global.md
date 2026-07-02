# Account-Level Storage (db.global)

The `db.global` collection is used to store data shared across all bots owned by the same user account.

---

## Isolation and Scope

*   **Scope**: Shared across all bots under the same owner account.
*   **Isolation**: Scoped to the entire owner account. Any bot belonging to the account can read or modify this data.

---

## Common Use Cases

*   **Cross-Bot Balances**: Implementing shared virtual credits across a network of companion bots.
*   **Unified Blacklists/Bans**: Restricting abusive users from all bots under your account simultaneously.
*   **Shared Settings**: Distributing global API keys or system-wide configurations to all instances.

---

## Code Examples

### 1. Checking Banned Status Network-Wide
```javascript
const isBanned = await db.global.get(`banned:${user.id}`, false);

if (isBanned) {
  return Bot.sendMessage('Access denied: You have been blocked across this network of bots.');
}
```

### 2. Sharing Configuration Across All Bots
```javascript
// Retrieve a shared external service configuration token
const apiToken = await db.global.get('external_api_token', '');
```

### 3. Setting a Global Lock
```javascript
// Enable system-wide lock for maintenance across all bots
await db.global.set('global_maintenance', true);
```
