# Unified CRUD Methods

All three collections (`db.bot`, `db.user`, and `db.global`) share a unified set of standard CRUD (Create, Read, Update, Delete) methods.

---

## 1. `get(keyOrOptions, fallback, options)`

Retrieve a value from the database. It will fall back to the provided fallback value if the key does not exist.

*   **Positional Syntax:**
    ```javascript
    const score = await db.bot.get('score', 0);
    ```
*   **Object Syntax:**
    ```javascript
    const level = await db.user.get({
      key: 'level',
      fallback: 1,
      user_id: '123456789' // Custom user scoping if needed
    });
    ```

---

## 2. `set(keyOrOptions, value, options)`

Store or update a value. If you pass `null`, `undefined`, or `""`, the key is automatically deleted.

*   **Positional Syntax:**
    ```javascript
    // Set a value with a 24-hour expiration (TTL in seconds)
    await db.bot.set('active', true, { ttl: 86400 });
    ```
*   **Object Syntax:**
    ```javascript
    await db.user.set({
      key: 'referrals',
      value: 12,
      ttl: 604800,
      type: 'integer' // Explicit type casting
    });
    ```

---

## 3. `has(keyOrOptions, options)`

Checks if a key exists in the cache or database. Returns `true` or `false`.

*   **Positional Syntax:**
    ```javascript
    const hasJoined = await db.user.has('joined_date');
    ```
*   **Object Syntax:**
    ```javascript
    const exists = await db.bot.has({ key: 'admin_locked' });
    ```

---

## 4. `del(keyOrOptions, options)`

Delete a single key from the cache and database.

*   **Positional Syntax:**
    ```javascript
    await db.bot.del('temp_token');
    ```
*   **Object Syntax:**
    ```javascript
    await db.user.del({ key: 'draft' });
    ```

---

## 5. `getAll(options)`

Retrieves all properties matching the collection. Returns a mapped dictionary object `{ [key]: value }`.

*   **Usage:**
    ```javascript
    const allUserData = await db.user.getAll();
    ```

---

## 6. `delAll(options)`

Delete all properties in the collection.

*   **Usage:**
    ```javascript
    await db.user.delAll();
    ```
