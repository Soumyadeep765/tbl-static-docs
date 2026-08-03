# marketHub

Live crypto and fiat prices — cached, refreshed, and ready before your command runs.

## What is it?

**marketHub** gives you live cryptocurrency and fiat exchange rates without making HTTP calls in your bot. Data refreshes automatically in the background (crypto ~every 2 minutes, fiat ~every 30 minutes) and is cached platform-wide. Just ask for `"BTC"` or `"INR"` and get a price.

Access it as `modules.marketHub`.

---

## How to use

Check a price and send it to the user:

```js
let btc = modules.marketHub.getCrypto("BTC")
Bot.sendMessage("BTC: $" + modules.marketHub.formatPrice("BTC"))
```

Fiat example:

```js
let inr = modules.marketHub.getFiat("INR")
Bot.sendMessage(inr.displayName + ": " + inr.rate + " per USD")
// 🇮🇳 Indian Rupee: 95.34 per USD
```

Symbols are **case-insensitive** — `"btc"`, `"BTC"`, and `"Btc"` all work.

All marketHub methods are **synchronous** — data is pre-cached, no `await` needed.

---

## Price lookups

| Method | Returns | Description |
| --- | --- | --- |
| `getPrice(symbol)` | `number` or `null` | USD price (crypto) or rate vs USD (fiat) |
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
//   price: 67234.5,          // USD
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
let inr = modules.marketHub.getFiat("INR")
// {
//   symbol: "INR",
//   code: "INR",
//   iso_code: "INR",
//   name: "Indian Rupee",
//   flag: "🇮🇳",
//   displayName: "🇮🇳 Indian Rupee",
//   rate: 95.34,             // INR per 1 USD
//   base: "USD",
//   timestamp: "2026-08-03",
//   hasRate: true
// }
```

`rate` is **units of that currency per 1 USD**. So `100 USD → INR` is `100 * rate`.

If `hasRate` is `false`, the currency has a name/flag but no convertible rate — check before converting.

---

## Search and lists

| Method | Description |
| --- | --- |
| `getTopCrypto(limit?)` | Top coins by market cap (default 50, max 200) |
| `searchCrypto(query, limit?)` | Search crypto by symbol or name |
| `searchFiat(query, limit?)` | Search fiat by symbol or name (e.g. `"rupee"`) |
| `search(query, limit?)` | Both — returns `{ crypto: [], fiat: [] }` |
| `listCryptoSymbols()` | All cached crypto symbols |
| `listFiatSymbols()` | All cached fiat symbols |
| `getAllFiatWithFlags()` | All fiat with flag display names |
| `getFiatWithFlag(symbol)` | Same as `getFiat(symbol)` |

---

## Currency conversion

`convert(amount, from, to)` — converts between any cached crypto or fiat symbols via USD:

```js
let result = modules.marketHub.convert(1, "BTC", "EUR")
// {
//   from: "BTC", to: "EUR", amount: 1,
//   result: 61856.34, usdValue: 67234.5,
//   timestamp: 1751895045000
// }

let inr = modules.marketHub.convert(100, "USD", "INR")
// { from: "USD", to: "INR", amount: 100, result: 9534, usdValue: 100, ... }
```

Returns `null` if either symbol is unknown or has no rate.

---

## Map-style access

```js
let eth = modules.marketHub.crypto.ETH
let usd = modules.marketHub.fiat.USD
"BTC" in modules.marketHub.crypto  // true
"INR" in modules.marketHub.fiat    // true
```

---

## Status methods

| Method | Returns |
| --- | --- |
| `isReady()` | `true` if any data is loaded |
| `getAge("crypto")` | Milliseconds since last crypto refresh, or `null` |
| `getAge("fiat")` | Milliseconds since last fiat refresh, or `null` |

---

## Data sources

| Type | Source | Refresh |
| --- | --- | --- |
| Crypto (top 200) | [CoinGecko](https://www.coingecko.com/) | ~2 minutes |
| Fiat rates | [Frankfurter](https://frankfurter.dev/) | ~30 minutes |

Fiat entries also include display names and flags (e.g. `INR` → 🇮🇳 Indian Rupee).

---

## Try it

### /price command

[Bot](../bot-instance/index.md) replies in [chat](../globals/chat.md). [`params`](../globals/params.md) is what the user typed after the command:

```js
if (!modules.marketHub.isReady()) {
  return Bot.sendMessage("Market data is still loading. Try again shortly.")
}

let symbol = params.toUpperCase()

if (!modules.marketHub.has(symbol)) {
  let found = modules.marketHub.search(symbol, 5)
  let list = found.crypto.map(c => c.symbol)
    .concat(found.fiat.map(f => f.symbol))
    .join(", ")
  return Bot.sendMessage("Unknown symbol. Try: " + list)
}

let type = modules.marketHub.getType(symbol)
let formatted = modules.marketHub.formatPrice(symbol)

if (type === "crypto") {
  let coin = modules.marketHub.getCrypto(symbol)
  Bot.sendMessage(coin.name + " (" + symbol + ")\n" +
    "Price: $" + formatted + "\n" +
    "24h: " + (coin.change_24h?.toFixed(2) || "—") + "%"
  )
} else {
  let fiat = modules.marketHub.getFiat(symbol)
  Bot.sendMessage(fiat.displayName + "\n" +
    "Rate: " + formatted + " per USD"
  )
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

Bot.sendMessage("Portfolio: $" + total.toLocaleString("en-US", { maximumFractionDigits: 2 }))
```

### Top 5 coins

```js
let top = modules.marketHub.getTopCrypto(5)
let lines = top.map((c, i) =>
  (i + 1) + ". " + c.name + " ($" + modules.marketHub.formatPrice(c.symbol) + ")"
)
Bot.sendMessage("Top 5:\n" + lines.join("\n"))
```

### Fiat search

```js
let hits = modules.marketHub.searchFiat("rupee", 5)
// INR, LKR, MUR, NPR, PKR — with names and flags
Bot.sendMessage(hits.map(f => f.displayName).join("\n"))
```

---

## Notes

- All methods are synchronous — no `await`
- Prices are indicative — not for financial trading decisions
- Crypto prices are in **USD**; fiat rates are vs **USD** base
- If `isReady()` is false, data may still be loading — retry shortly
- For on-chain data (balances, transactions), use [ethers](ethers.md)
