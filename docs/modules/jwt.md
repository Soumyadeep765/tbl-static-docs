## JWT

JWT is used for creating and verifying **JSON Web Tokens**.

It is commonly used for:

- Authentication
- Session management
- Secure data transfer between systems

JWT functionality is available through the `modules` object.

## Creating a Token

```js
const token = modules.JWT.sign(
  { userId: 123 },
  "secret"
)
```

This generates a signed token string.

## Verifying a Token

```js
const decoded = modules.JWT.verify(
  token,
  "secret"
)
```

This verifies the token and returns the decoded payload.

## Example Output

```
token   → "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
decoded → { userId: 123, iat: 1690000000 }
```

## Notes

- Tokens are cryptographically signed
- Use strong secrets or keys
- Verification fails if the token is invalid or expired

## Official Documentation
[JWT Docs]

[JWT Docs]: https://www.npmjs.com/package/jsonwebtoken
