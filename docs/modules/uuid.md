## UUID

UUID is used to generate **unique identifiers**.

It is useful for:

- Unique keys
- Transaction IDs
- Session identifiers
- Request or reference IDs

UUID functionality is available through the `modules` object.

## Generating a UUID (v4)

```js
const id = modules.UUID.uuidv4()
```

This generates a random UUID (version 4).

## Example Output

```
id → "550e8400-e29b-41d4-a716-446655440000"
```

Each generated value is globally unique.

## Notes

- UUIDs are collision-resistant
- Safe to use for identifiers across systems
- Does not require any configuration

## Official Documentation

[UUID Docs]

[UUID Docs]: https://www.npmjs.com/package/uuid