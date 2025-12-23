## Custom Usage

This section covers **advanced User instance usage**.

It includes object-based operations and working with user data beyond simple string-based calls.

## Object-Based Operations

In addition to string-based methods, the User instance supports **object-style usage**.

This allows passing extra options when needed.

### Setting Data with Object Format

```js
User.set({
  key: "score",
  value: 100
})
```

This behaves the same as string-based `User.set`, but allows more flexibility.

## Working with a Specific User

You can explicitly target a specific user by passing `user_id`.

This is useful for admin tools or background logic.

### Example

```js
User.set({
  key: "status",
  value: "verified",
  user_id: 123456789
})
```

If `user_id` is not provided, the **current user** is used automatically.

## Reading Data for a Specific User

```js
let status = User.get({
  key: "status",
  user_id: 123456789
})
```

This reads data from the specified user instead of the current one.

## Deleting Data for a Specific User

```js
User.del({
  key: "status",
  user_id: 123456789
})
```

Only the targeted user’s data is affected.

## Notes

- Object format is optional
- Useful for advanced flows and admin logic
- All data remains isolated per user
- User-level storage is independent from Bot-level storage
- Use this carefully to avoid unintended changes to other users
