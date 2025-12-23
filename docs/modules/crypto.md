## crypto

The **crypto** utility provides **cryptographic functions** such as hashing, encryption, and decryption.

It is useful for:

- Hashing data
- Generating secure values
- Working with cryptographic algorithms

## Availability

The `crypto` utility is available **by default**.

You can use it in **two ways**:

- Directly:
  crypto.xxx

- Through modules:
  modules.crypto.xxx

Both forms work the same.

## Creating a SHA256 Hash

```js
const hash = crypto
  .createHash("sha256")
  .update("data")
  .digest("hex")
```

The same example using `modules`:

```js
const hash = modules.crypto
  .createHash("sha256")
  .update("data")
  .digest("hex")
```

## Example Output

```
hash → "3a6eb...9f1"
```

## Notes

- Cryptographic operations are synchronous
- Output format depends on the digest method used
- Use strong algorithms like `sha256` or higher

## Official Documentation

[Node.js crypto Docs]

[Node.js crypto Docs]: https://nodejs.org/api/crypto.html
