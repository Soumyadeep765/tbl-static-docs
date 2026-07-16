# Modules

Imagine npm packages that already live inside your bot — no `require()`, no `package.json`, no "works on my machine" excuses. That's `modules`.

Hash a password, sign a JWT, parse a CSV, check if an email looks real, grab the BTC price — all from your command's **Logic** field. Type `modules.` and autocomplete your way to happiness.

---

## What are modules?

**Modules** are curated third-party utilities (JWT, bcrypt, lodash, zod, ethers, and friends) that TeleBotHost loads and sandboxes for you.

| You get | You skip |
| --- | --- |
| Battle-tested libraries | `npm install` |
| One global object: `modules` | Import statements |
| Works in commands, webhooks, webapps | Server setup |

Every module is accessed as `modules.<name>` — **case-sensitive**. `modules.JWT` works. `modules.jwt` does not. The universe is cruel but consistent.

---

## How to use them

Drop this in any command's **Logic** field:

```js
let id = modules.UUID.uuidv4()
Bot.sendMessage("Your order ID: " + id)
```

Three things worth knowing upfront:

1. **`modules` is already there** — you never import or initialize it.
2. **The object is frozen** — you can't add your own properties to `modules`. Nice try though.
3. **Some methods need `await`** — parsing and crypto hashing often return Promises. More on that [below](#sync-vs-async).

!!! tip "New to TBL?"
    `Bot`, `chat`, and `user` are globals available in every command. Quick intro: [Learning TBL](../learning-tbl.md). Secrets like API keys go in dashboard ENV vars — see [`process.env`](../globals/process.md).

---

## Modules or Libs?

TBL has two toolboxes. Pick the right drawer before you rummage:

| | `modules` | `Libs` |
| --- | --- | --- |
| What | npm-style packages (crypto, parsing, Web3) | TBL-built bot helpers (referrals, dice rolls, channel checks) |
| Access | `modules.validator.isEmail(email)` | `Libs.random.randomInt(1, 6)` |
| Best for | JWT, bcrypt, CSV, YAML, Ethereum | MCL, referral links, resource balances |

Full Libs docs: [TBL Libraries](../libs/index.md).

Still not sure? Rule of thumb: if you'd normally `npm install` it, check `modules` first. If it's Telegram-bot-specific glue, check `Libs`.

---

## Pick a module

### Security and crypto

| Module | Access | What it does |
| --- | --- | --- |
| [JWT](jwt.md) | `modules.JWT` | Sign, verify, decode JSON Web Tokens |
| [bcrypt](bcrypt.md) | `modules.bcrypt` | Password hashing (the slow kind — on purpose) |
| [crypto](crypto.md) | `modules.crypto` | Hashes, HMAC, random bytes |
| [UUID](uuid.md) | `modules.UUID` | `uuidv4()` and `uuidv6()` — IDs that won't collide |

### Parsing and data

| Module | Access | What it does |
| --- | --- | --- |
| [ParseCSV](parse-csv.md) | `modules.ParseCSV` | Turn CSV text into row objects |
| [ParseYML](parse-yml.md) | `modules.ParseYML` | Parse/stringify YAML (safe schema) |
| [qs](qs.md) | `modules.qs` | Query string parse and stringify |
| [cheerio](cheerio.md) | `modules.cheerio` | HTML parsing — jQuery vibes, no browser |
| [lodash](lodash.md) | `modules.lodash` | Array/object utilities |
| [deepmerge](deepmerge.md) | `modules.deepmerge` | Deep-merge objects without crying |
| [zod](zod.md) | `modules.zod` | Schema validation with nice error messages |

### Dates and text

| Module | Access | What it does |
| --- | --- | --- |
| [dayjs](dayjs.md) | `modules.dayjs` | Lightweight date formatting |
| [humanizeDuration](humanize-duration.md) | `modules.humanizeDuration` | `"3 hours"` instead of `10800000` |
| [md2html](md2html.md) | `modules.md2html` | Telegram Markdown → HTML |
| [validator](validator.md) | `modules.validator` | Email, URL, and input validation |
| [uaParser](uaparser.md) | `modules.uaParser` | Decode User-Agent strings |

### Random and IDs

| Module | Access | What it does |
| --- | --- | --- |
| [randomstring](randomstring.md) | `modules.randomstring` | Configurable random strings |

### Web3 and markets

| Module | Access | What it does |
| --- | --- | --- |
| [ethers](ethers.md) | `modules.ethers` | Ethereum library (sandboxed RPC) |
| [marketHub](market-hub.md) | `modules.marketHub` | Live crypto and fiat prices |

---

## Try it — copy-paste examples

Start simple. Each example only introduces what it needs.

### Generate a unique ID

No setup, no secrets — just an ID:

```js
let ref = modules.UUID.uuidv4().slice(0, 8).toUpperCase()
Bot.sendMessage("Your reference: #" + ref)
```

### Validate an email

`params` is whatever the user typed after your command:

```js
if (!modules.validator.isEmail(params)) {
  return Bot.sendMessage("That doesn't look like an email. Try again.")
}
Bot.sendMessage("Email accepted. Welcome aboard!")
```

### Markdown → HTML for Telegram

Telegram's HTML mode is picky. `md2html` translates your Markdown:

```js
let html = modules.md2html("**Sale!** Visit [our site](https://example.com)")
Bot.sendMessage(html, { parse_mode: "HTML" })
```

### Sign a session token

Store your secret in dashboard **ENV** settings, then read it via `process.env`:

```js
let token = modules.JWT.sign(
  { uid: user.id },
  process.env.JWT_SECRET,
  { expiresIn: "7d" }
)
Bot.sendMessage("Logged in. Token saved.")
```

ENV setup: [`process.env`](../globals/process.md) · JWT details: [JWT module](jwt.md)

### Check BTC price

```js
let btc = modules.marketHub.getCrypto("BTC")
if (btc) {
  Bot.sendMessage("BTC: $" + modules.marketHub.formatPrice("BTC"))
} else {
  Bot.sendMessage("Price feed is taking a coffee break. Try again soon.")
}
```

### Parse CSV (async)

`ParseCSV` returns a Promise — add `await`:

```js
let csvText = "name,score\nAlice,9001\nBob,42"
let rows = await modules.ParseCSV.parse(csvText)

for (let row of rows) {
  Bot.sendMessage(row.name + " scored " + row.score)
}
```

---

## How modules work

The internals — useful when something breaks, skippable when you're vibing:

| Behaviour | Detail |
| --- | --- |
| Injection | `modules` is created fresh for each command run, with your plan's limits applied |
| Caching | Each module loads once and stays in memory for the rest of that run |
| Frozen | The `modules` object cannot be modified |
| Input limits | Parse-heavy modules enforce your plan's `buffer_size` |
| Abort | Long operations respect the command's abort signal |

---

## Size limits

Parsing modules (`ParseCSV`, `ParseYML`, `cheerio`, `md2html`, `qs.parse`, `JWT`) enforce your plan's max input size:

| Plan | Max input |
| --- | --- |
| Free / Freemium | 512 KB |
| Premium | 5 MB |
| Elite | 10 MB |

Go over the limit and you'll see: `Input exceeds plan limit (N bytes)`. The docs didn't write themselves — they had to draw a line somewhere.

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

Most modules are synchronous — call them like any function. A few need `await`:

| Module | Async methods |
| --- | --- |
| `ParseCSV.parse()` | Yes — returns Promise |
| `bcrypt.hash()` / `bcrypt.compare()` | Yes |
| `ethers` provider calls | Yes |
| Most others | Sync |

```js
// Async — don't forget await
let rows = await modules.ParseCSV.parse(csvText)
let hash = await modules.bcrypt.hash(password, 10)

// Sync — just call it
let id = modules.UUID.uuidv4()
let valid = modules.validator.isEmail(email)
```

Forget `await` on an async method and you'll get a Promise object instead of the result. JavaScript's favorite prank.

---

## Retired modules

These used to exist. They don't anymore. We're sorry for the inconvenience:

| Module | Use instead |
| --- | --- |
| `moment` | [dayjs](dayjs.md) |
| `chance` | [Libs.random](../libs/random.md) |
| `math` | Native JavaScript `Math` |
| `shortid` | [UUID](uuid.md) or [randomstring](randomstring.md) |

---

## Where modules work

| Context | `modules` available? |
| --- | --- |
| Normal Telegram commands | ✓ |
| Webhook / webapp | ✓ |
| HTTP callback commands | ✓ |
| Broadcast commands | ✓ |

---

## Pages in this section

Every module has its own page — linked in the tables above. Recently added: [ethers](ethers.md), [marketHub](market-hub.md), [md2html](md2html.md).
