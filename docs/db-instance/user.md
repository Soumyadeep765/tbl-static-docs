# User-Level Storage (db.user)

The `db.user` collection is used to store data that is unique to an individual user's interaction with the bot.

---

## Isolation and Scope

*   **Scope**: Scoped and isolated to each unique user interacting with the bot.
*   **Isolation**: Private to each user-bot pair. A user's properties are completely separate from another user's properties. By default, the current user ID is automatically extracted and scoped from the incoming update context.

---

## Common Use Cases

*   **User Profiles**: Storing names, registration dates, and custom preferences.
*   **Balances and Currency**: Managing credits, virtual coins, or referral counts.
*   **State and Progress**: Saving the current step in a multi-stage conversational flow or game progression.

---

## Code Examples

### 1. Awarding Referral Credits
```javascript
// Increment the balance for the current user by 10 credits
const newBalance = await db.user.incr('credits_balance', 10);
Bot.sendMessage(`Thank you for the referral! New balance: ${newBalance}`);
```

### 2. Saving User Language Preference
```javascript
// Store preferences for the current user
await db.user.set('language', 'Spanish');
```

### 3. Accessing Data for a Specific User ID
```javascript
// Check another user's balance (e.g. for admin commands)
const userBalance = await db.user.get({
  key: 'credits_balance',
  fallback: 0,
  user_id: '123456789'
});
```
