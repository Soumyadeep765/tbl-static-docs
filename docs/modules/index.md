# Modules

The **modules** object provides access to **preloaded utility libraries** inside TBL.

It lets you perform common tasks — data processing, validation, formatting, and more — without importing or installing anything.

## Usage

```js
modules.lodash.filter(array, predicate)
modules.jwt.sign(payload, secret)
modules.validator.isEmail("user@example.com")
```

All modules are sandboxed and safe to use within TBL.

## Available Modules

| Module | Purpose |
| --- | --- |
| [jwt](jwt.md) | Create and verify JSON Web Tokens |
| [bcrypt](bcrypt.md) | Hash and verify passwords |
| [crypto](crypto.md) | Cryptographic hashing |
| [ParseCSV](parse-csv.md) | Parse CSV strings |
| [ParseYML](parse-yml.md) | Parse YAML strings |
| [UUID](uuid.md) | Generate UUIDs |
| [moment](moment.md) | Date formatting and manipulation |
| [lodash](lodash.md) | Array and object utilities |
| [uaParser](uaparser.md) | Parse user-agent strings |
| [randomstring](randomstring.md) | Generate random strings |
| [validator](validator.md) | Validate emails, URLs, and more |
| [chance](chance.md) | Random data generation |
| [math](math.md) | Math utilities |
| [qs](qs.md) | Query string parsing |
| [cheerio](cheerio.md) | HTML parsing |
| [dayjs](dayjs.md) | Lightweight date formatting |
| [zod](zod.md) | Schema validation |
| [shortid](shortid.md) | Generate short unique IDs |
| [deepmerge](deepmerge.md) | Deep-merge objects |
| [humanizeDuration](humanize-duration.md) | Human-readable durations |

## Notes

- `modules` is available globally in every command
- No setup or imports are required
- Only approved libraries are exposed
- Designed for convenience and security

For TBL-specific helpers (ResourcesLib, tgutil, etc.), see [TBL Libraries](../libs/index.md).
