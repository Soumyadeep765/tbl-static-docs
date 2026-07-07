# marketHub

`modules.marketHub` provides **live cryptocurrency and fiat exchange rates** cached platform-wide. Data refreshes automatically in the background — no HTTP calls needed in your bot.

```js
let btc = modules.marketHub.getCrypto("BTC")
Bot.sendMessage(chat.id, "BTC: $" + modules.marketHub.formatPrice("BTC"))
```

---

## Data sources

| Type | Source | Refresh interval |
| --- | --- | --- |
| Crypto (top 200) | [CoinGecko](https://www.coingecko.com/) markets API | ~2 minutes |
| Fiat currencies | [Frankfurter](https://www.frankfurter.app/) | ~30 minutes |

Data is cached in Redis and shared across all bots on the platform. The hub starts automatically when TBL servers boot.

---

## Quick start

```js
// Check if data is loaded
if (!modules.marketHub.isReady()) {
  Bot.sendMessage(chat.id, "Market data loading, try again shortly.")
  return
}

let price = modules.marketHub.getPrice("BTC")
Bot.sendMessage(chat.id, "BTC: $" + modules.marketHub.formatPrice("BTC", 2))
```

Symbols are **case-insensitive** — `"btc"`, `"BTC"`, and `"Btc"` all work.

---

## Price lookups

| Method | Returns | Description |
| --- | --- | --- |
| `getPrice(symbol)` | `number` or `null` | USD price (crypto) or rate (fiat) |
| `formatPrice(symbol, digits?)` | `string` or `null` | Locale-formatted price |
| `getCrypto(symbol)` | `object` or `null` | Full crypto entry |
| `getFiat(symbol)` | `object` or `null` | Full fiat entry with flag |
| `has(symbol)` | `boolean` | Whether symbol exists |
| `getType(symbol)` | `"crypto"` / `"fiat"` / `null` | Asset type |

### Crypto entry fields

```js
let btc = modules.marketHub.getCrypto("BTC")
// {
//   symbol: "BTC",
//   name: "Bitcoin",
//   price: 67234.5,
//   market_cap: 1320000000000,
//   rank: 1,
//   volume_24h: 28000000000,
//   change_24h: 2.34,
//   supply: { circulating, total, max },
//   ath: { price, change, date },
//   atl: { price, change, date },
//   range_24h: { high, low },
//   last_updated: "..."
// }
```

### Fiat entry fields

```js
let eur = modules.marketHub.getFiat("EUR")
// {
//   symbol: "EUR",
//   name: "Euro",
//   rate: 0.92,          // vs USD
//   flag: "🇪🇺",
//   displayName: "🇪🇺 Euro",
//   base: "USD",
//   timestamp: "2025-07-07"
// }
```

---

## Search and lists

| Method | Description |
| --- | --- |
| `getTopCrypto(limit?)` | Top coins by market cap (default 50, max 200) |
| `searchCrypto(query, limit?)` | Search crypto by symbol or name |
| `searchFiat(query, limit?)` | Search fiat by symbol or name |
| `search(query, limit?)` | Both — returns `{ crypto: [], fiat: [] }` |
| `listCryptoSymbols()` | All cached crypto symbols |
| `listFiatSymbols()` | All cached fiat symbols |
| `getAllFiatWithFlags()` | All fiat with flag display names |

```js
let results = modules.marketHub.search("bit")
// { crypto: [{ symbol: "BTC", name: "Bitcoin", ... }, ...], fiat: [] }

let top10 = modules.marketHub.getTopCrypto(10)
```

---

## Currency conversion

`convert(amount, from, to)` — converts between any cached crypto or fiat symbols via USD.

```js
let result = modules.marketHub.convert(1, "BTC", "EUR")
// {
//   from: "BTC",
//   to: "EUR",
//   amount: 1,
//   result: 61856.34,
//   usdValue: 67234.5,
//   timestamp: 1751895045000
// }

if (result) {
  Bot.sendMessage(chat.id,
    "1 BTC = " + result.result.toFixed(2) + " EUR"
  )
}
```

Returns `null` if either symbol is unknown or has no rate.

---

## Map-style access

`marketHub.crypto` and `marketHub.fiat` behave like read-only symbol maps:

```js
let eth = modules.marketHub.crypto.ETH
let usd = modules.marketHub.fiat.USD

"BTC" in modules.marketHub.crypto  // true
```

---

## Status methods

| Method | Returns |
| --- | --- |
| `isReady()` | `true` if any data is loaded |
| `isRunning()` | `true` if background refresh is active |
| `getStats()` | Counts, last update times, age in ms |
| `getAge("crypto")` | Milliseconds since last crypto refresh |
| `getAge("fiat")` | Milliseconds since last fiat refresh |

```js
let stats = modules.marketHub.getStats()
// {
//   crypto: { count: 200, lastUpdate: ..., ageMs: 45000, updating: false },
//   fiat: { count: 170, lastUpdate: ..., ageMs: 120000, updating: false },
//   running: true,
//   ready: true
// }
```

---

## Examples

### /price command

```js
let symbol = params.toUpperCase()

if (!modules.marketHub.has(symbol)) {
  let found = modules.marketHub.search(symbol, 5)
  let list = found.crypto.map(c => c.symbol).join(", ")
  Bot.sendMessage(chat.id, "Unknown symbol. Try: " + list)
  return
}

let type = modules.marketHub.getType(symbol)
let formatted = modules.marketHub.formatPrice(symbol)

if (type === "crypto") {
  let coin = modules.marketHub.getCrypto(symbol)
  Bot.sendMessage(chat.id,
    coin.name + " (" + symbol + ")\n" +
    "Price: $" + formatted + "\n" +
    "24h: " + (coin.change_24h?.toFixed(2) || "—") + "%"
  )
} else {
  Bot.sendMessage(chat.id, symbol + " rate: " + formatted + " (vs USD)")
}
```

### Portfolio value

```js
let holdings = { BTC: 0.5, ETH: 2.0 }
let total = 0

for (let [symbol, amount] of Object.entries(holdings)) {
  let price = modules.marketHub.getPrice(symbol)
  if (price) total += amount * price
}

Bot.sendMessage(chat.id, "Portfolio: $" + total.toLocaleString("en-US", { maximumFractionDigits: 2 }))
```

### Top 5 coins

```js
let top = modules.marketHub.getTopCrypto(5)
let lines = top.map((c, i) =>
  (i + 1) + ". " + c.name + " ($" + modules.marketHub.formatPrice(c.symbol) + ")"
)
Bot.sendMessage(chat.id, "Top 5:\n" + lines.join("\n"))
```

---

## Notes

- All methods are **sync** — data is pre-cached, no `await` needed
- Prices are indicative — not for financial trading decisions
- Crypto prices are in **USD**; fiat rates are vs **USD** base
- If `isReady()` is false, the server may still be loading initial data
- For on-chain data (balances, transactions), use [ethers](ethers.md)
