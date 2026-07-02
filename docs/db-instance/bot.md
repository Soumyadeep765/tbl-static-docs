# Bot-Level Storage (db.bot)

The `db.bot` collection is used to store settings, configuration, and state that apply bot-wide.

---

## Isolation and Scope

*   **Scope**: Shared across all users interacting with the same bot.
*   **Isolation**: Private to the specific bot. Data saved in `db.bot` cannot be accessed by other bots on the same owner account unless explicitly shared.

---

## Common Use Cases

*   **Maintenance Modes**: Disabling or restricting bot commands globally.
*   **Global Feature Flags**: Enabling or disabling specific features for all users.
*   **External API Caching**: Caching expensive query results to optimize API rate limits.
*   **Aggregate Metrics**: Tracking total clicks, messages, or overall command execution counts.

---

## Code Examples

### 1. Checking Maintenance Mode
```javascript
const isMaintenance = await db.bot.get('maintenance_mode', false);

if (isMaintenance) {
  return Bot.sendMessage('The bot is currently undergoing maintenance. Please try again later.');
}
```

### 2. Incrementing Global Command Run Count
```javascript
const totalRuns = await db.bot.incr('total_commands_run', 1);
logger.info(`Commands have been run ${totalRuns} times bot-wide.`);
```

### 3. Setting a Cache Expiration (TTL)
```javascript
// Cache the list of active promotions for 1 hour (3600 seconds)
await db.bot.set('promotions_cache', activePromotions, { ttl: 3600 });
```
