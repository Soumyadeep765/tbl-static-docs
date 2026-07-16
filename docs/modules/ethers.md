# ethers

Read the blockchain without running your own node — or signing a blank cheque.

## What is it?

**ethers** is the [ethers.js v6](https://docs.ethers.org/v6/) library for Ethereum: read balances, call smart contracts, format wei, sign messages locally. In TBL it ships with a **sandboxed RPC layer** — HTTP providers only, with call limits and timeouts so one command can't hammer an endpoint forever.

Access it as `modules.ethers`.

---

## How to use

Connect to a public JSON-RPC endpoint and read the current block — **provider calls are async, use `await`**:

```js
let provider = new modules.ethers.JsonRpcProvider("https://eth.llamarpc.com")
let block = await provider.getBlockNumber()
```

Store your RPC URL in dashboard ENV settings and read it via [`process.env`](../globals/process.md) instead of hard-coding URLs.

---

## What's available

Most of ethers v6 works as documented — utilities, ABI encoding, wallets (local signing), formatting, and more.

### Sandboxed providers

Only **HTTP/HTTPS JSON-RPC** providers are allowed:

| Allowed | Blocked |
| --- | --- |
| `JsonRpcProvider` | `WebSocketProvider` |
| `FallbackProvider` (HTTP URLs) | `IpcProvider` |
| `FetchRequest` | `getDefaultProvider()` |
| `Contract` with HTTP runner | WebSocket / IPC connections |

```js
// Allowed
let provider = new modules.ethers.JsonRpcProvider("https://rpc.example.com")

// Blocked — throws
new modules.ethers.WebSocketProvider("wss://...")
modules.ethers.getDefaultProvider()
```

RPC URLs must be valid public `http://` or `https://` URLs (SSRF-validated).

---

## RPC limits

| Limit | Value |
| --- | --- |
| Max RPC calls per command | `parallel_process × 5` (minimum 10) |
| Per-call timeout | Your plan's script timeout |
| Provider types | HTTP/HTTPS only |

Exceeding the call limit throws: `ethers RPC call limit exceeded (N)`.

```js
// Free plan (parallel_process: 10) → max 50 RPC calls per command
let provider = new modules.ethers.JsonRpcProvider(process.env.ETH_RPC)
let balance = await provider.getBalance("0x...")
```

Every async RPC method on wrapped providers counts toward the limit and races against your plan timeout.

---

## Common patterns

### Read block number

```js
let provider = new modules.ethers.JsonRpcProvider(process.env.ETH_RPC)
let block = await provider.getBlockNumber()
Bot.sendMessage("Current block: " + block)
```

### Read contract

```js
let provider = new modules.ethers.JsonRpcProvider(process.env.ETH_RPC)
let abi = ["function balanceOf(address) view returns (uint256)"]
let contract = new modules.ethers.Contract(tokenAddress, abi, provider)
let balance = await contract.balanceOf(walletAddress)
let formatted = modules.ethers.formatEther(balance)
```

### Fallback provider

```js
let provider = new modules.ethers.FallbackProvider([
  "https://rpc1.example.com",
  "https://rpc2.example.com"
])
```

### Format values (sync — no RPC)

```js
modules.ethers.formatEther("1000000000000000000")   // "1.0"
modules.ethers.parseEther("1.5")                   // 1500000000000000000n
modules.ethers.getAddress("0x...")                 // checksum address
modules.ethers.isAddress("0x...")                  // true/false
```

### Local wallet (signing doesn't count as RPC)

```js
let wallet = new modules.ethers.Wallet(process.env.PRIVATE_KEY)
let signature = await wallet.signMessage("Hello")
```

---

## Try it

### Check an ETH balance

[Bot](../bot-instance/index.md) replies in the current [chat](../globals/chat.md):

```js
let address = params.trim()

if (!modules.ethers.isAddress(address)) {
  return Bot.sendMessage("That doesn't look like a valid address.")
}

let provider = new modules.ethers.JsonRpcProvider(process.env.ETH_RPC)
let balance = await provider.getBalance(address)
let eth = modules.ethers.formatEther(balance)

Bot.sendMessage("Balance: " + eth + " ETH")
```

### Handle RPC errors gracefully

```js
try {
  let provider = new modules.ethers.JsonRpcProvider(process.env.ETH_RPC)
  let block = await provider.getBlockNumber()
  Bot.sendMessage("Block: " + block)
} catch (err) {
  Bot.sendMessage("RPC error: " + err.message)
}
```

---

## Error reference

| Error | Cause |
| --- | --- |
| `WebSocketProvider is not allowed` | Used a blocked provider type |
| `RPC URL must be a valid HTTP(S) URL` | Invalid or missing URL |
| `ethers RPC call limit exceeded` | Too many RPC calls in one command |
| `ethers.getBlockNumber timed out after Nms` | RPC call exceeded plan timeout |

---

## Notes

- **Provider calls need `await`** — encoding, formatting, and `isAddress()` are sync
- Store RPC URLs and private keys in [`process.env`](../globals/process.md) — never hard-code
- Wallet signing is local — does not count as an RPC call
- For price lookups without RPC, see [marketHub](market-hub.md)
- Official ethers v6 docs: [docs.ethers.org](https://docs.ethers.org/v6/)
