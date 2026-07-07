# Modules

`modules` exposes **curated npm-style utilities** inside TBL — JWT, crypto, parsing, validation, Web3, and more. No `require()` or install step needed.

```js
let token = modules.JWT.sign({ userId: user.id }, process.env.JWT_SECRET)
let html = modules.md2html("**Hello** *world*")
let price = modules.marketHub.getPrice("BTC")
```

Access as `modules.<name>` (case-sensitive). The object is frozen per command execution.

---

## Available modules

### Security and crypto

| Module | Access | Description |
| --- | --- | --- |
| [JWT](jwt.md) | `modules.JWT` | Sign, verify, decode JSON Web Tokens |
| [bcrypt](bcrypt.md) | `modules.bcrypt` | Password hashing |
| [crypto](crypto.md) | `modules.crypto` | Node.js crypto — hashes, HMAC, random bytes |
| [UUID](uuid.md) | `modules.UUID` | `uuidv4()` and `uuidv6()` |

### Parsing and data

| Module | Access | Description |
| --- | --- | --- |
| [ParseCSV](parse-csv.md) | `modules.ParseCSV` | Parse CSV strings (async) |
| [ParseYML](parse-yml.md) | `modules.ParseYML` | Parse/stringify YAML (safe schema) |
| [qs](qs.md) | `modules.qs` | Query string parse and stringify |
| [cheerio](cheerio.md) | `modules.cheerio` | HTML parsing and DOM traversal |
| [lodash](lodash.md) | `modules.lodash` | Array/object utilities |
| [deepmerge](deepmerge.md) | `modules.deepmerge` | Deep-merge objects |
| [zod](zod.md) | `modules.zod` | Schema validation |

### Dates and text

| Module | Access | Description |
| --- | --- | --- |
| [dayjs](dayjs.md) | `modules.dayjs` | Lightweight date formatting |
| [humanizeDuration](humanize-duration.md) | `modules.humanizeDuration` | Human-readable durations |
| [md2html](md2html.md) | `modules.md2html` | Telegram Markdown → HTML |
| [validator](validator.md) | `modules.validator` | Email, URL, and input validation |
| [uaParser](uaparser.md) | `modules.uaParser` | Parse User-Agent strings |

### Random and IDs

| Module | Access | Description |
| --- | --- | --- |
| [randomstring](randomstring.md) | `modules.randomstring` | Configurable random strings |

### Web3 and markets

| Module | Access | Description |
| --- | --- | --- |
| [ethers](ethers.md) | `modules.ethers` | Ethereum library (sandboxed RPC) |
| [marketHub](market-hub.md) | `modules.marketHub` | Live crypto and fiat prices |

---

## How modules work

| Behaviour | Detail |
| --- | --- |
| Injection | `TBL.modules` created per command with plan limits |
| Caching | Modules loaded once and cached in memory |
| Frozen | The `modules` object cannot be modified |
| Input limits | Parse-heavy modules enforce plan `buffer_size` |
| Abort | Operations check execution abort signal |

### Input size limits

Parsing modules (`ParseCSV`, `ParseYML`, `cheerio`, `md2html`, `qs.parse`, `JWT`) enforce your plan buffer size:

| Plan | Max input |
| --- | --- |
| Free / Freemium | 512 KB |
| Premium | 5 MB |
| Elite | 10 MB |

Exceeding the limit throws: `Input exceeds plan limit (N bytes)`.

### Module-specific caps

| Module | Extra limit |
| --- | --- |
| `ParseCSV` | Max record size: 256 KB |
| `randomstring.generate` | Length: 1–256 characters |
| `qs.parse` | Max 1000 parameters, array limit 100 |
| `ParseYML.parse` | Uses `FAILSAFE_SCHEMA` (strings only) |
| `ethers` RPC | Max calls = `parallel_process × 5` (min 10), plan timeout per call |

---

## Sync vs async

| Module | Async methods |
| --- | --- |
| `ParseCSV.parse()` | Yes — returns Promise |
| `bcrypt.hash()` / `bcrypt.compare()` | Yes |
| `ethers` provider calls | Yes |
| Most others | Sync |

```js
// Async
let rows = await modules.ParseCSV.parse(csvText)
let hash = await modules.bcrypt.hash(password, 10)

// Sync
let id = modules.UUID.uuidv4()
let valid = modules.validator.isEmail(email)
```

---

## Quick examples

### JWT session token

```js
let token = modules.JWT.sign(
  { uid: user.id },
  process.env.JWT_SECRET,
  { expiresIn: "7d" }
)
```

### Markdown to HTML message

```js
let html = modules.md2html("**Sale!** Visit [our site](https://example.com)")
Bot.sendMessage(chat.id, html, { parse_mode: "HTML" })
```

### BTC price

```js
let btc = modules.marketHub.getCrypto("BTC")
if (btc) {
  Bot.sendMessage(chat.id, "BTC: $" + modules.marketHub.formatPrice("BTC"))
}
```

### Validate and parse

```js
if (!modules.validator.isEmail(params)) {
  return Bot.sendMessage(chat.id, "Invalid email.")
}

let data = modules.zod.object({ email: modules.zod.string().email() }).parse({ email: params })
```

---

## Removed modules

These are **no longer available** in TBL:

| Module | Replacement |
| --- | --- |
| `moment` | Use [dayjs](dayjs.md) |
| `chance` | Use [Libs.random](../libs/random.md) |
| `math` | Use native JavaScript `Math` |
| `shortid` | Use [UUID](uuid.md) or [randomstring](randomstring.md) |

---

## Modules vs Libs

| | `modules` | `Libs` |
| --- | --- | --- |
| Source | npm packages (sandboxed) | TBL built-in libraries |
| Access | `modules.lodash.map()` | `Libs.random.randomInt()` |
| Best for | Crypto, parsing, validation, Web3 | Bot helpers (MCL, referrals, resources) |

See [TBL Libraries](../libs/index.md) for Libs documentation.

---

## Availability

| Context | `modules` |
| --- | --- |
| Normal Telegram commands | ✓ |
| Webhook / webapp | ✓ |
| HTTP callback commands | ✓ |
| Broadcast commands | ✓ |

---

## Pages in this section

All module pages are listed in the tables above. New modules: [ethers](ethers.md), [marketHub](market-hub.md), [md2html](md2html.md).
