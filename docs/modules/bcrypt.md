## bcrypt

bcrypt is used for **secure password hashing and verification**.

It is essential for safely storing passwords instead of saving them as plain text.

bcrypt functionality is available through the `modules` object.

## Hashing a Password

```js
const hash = await modules.bcrypt.hash(
  "password123",
  10
)
```

- The second argument is the **salt rounds**
- Higher values increase security but take more time

## Verifying a Password

```js
const match = await modules.bcrypt.compare(
  "password123",
  hash
)
```

This checks whether the password matches the stored hash.

## Example Output

```
hash  → "$2b$10$e0N...."
match → true
```

## Notes

- Always store **hashes**, never raw passwords
- Use a reasonable salt round value (e.g. 10–12)
- Comparison is safe against timing attacks

## Official Documentation

[bcrypt Docs]

[bcrypt Docs]: https://www.npmjs.com/package/bcrypt
