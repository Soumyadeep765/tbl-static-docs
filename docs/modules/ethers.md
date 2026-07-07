# ethers

`modules.ethers` is the [ethers.js v6](https://docs.ethers.org/v6/) library with a **sandboxed RPC layer**. Connect to public Ethereum JSON-RPC endpoints, read contracts, and format values — with HTTP-only providers and call limits.

```js
let provider = new modules.ethers.JsonRpcProvider("https://eth.llamarpc.com")
let block = await provider.getBlockNumber()
```

---

## What's available

Most of ethers v6 works as documented — utilities, ABI encoding, wallets (local signing), formatting, etc.

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

---

## Common patterns

### Read block number

```js
let provider = new modules.ethers.JsonRpcProvider(process.env.ETH_RPC)
let block = await provider.getBlockNumber()
Bot.sendMessage(chat.id, "Current block: " + block)
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

### Format values

```js
modules.ethers.formatEther("1000000000000000000")   // "1.0"
modules.ethers.parseEther("1.5")                   // 1500000000000000000n
modules.ethers.getAddress("0x...")                 // checksum address
modules.ethers.isAddress("0x...")                  // true/false
```

### Local wallet (no RPC needed for signing)

```js
let wallet = new modules.ethers.Wallet(process.env.PRIVATE_KEY)
let message = "Hello"
let signature = await wallet.signMessage(message)
```

---

## Provider wrapping

`JsonRpcProvider`, `FallbackProvider`, and `Contract` instances are wrapped:

- Every async RPC method counts toward the call limit
- Every async RPC method has a plan-timeout race
- Nested `.provider` objects are wrapped recursively

Sync methods (encoding, formatting, address checks) are not limited.

---

## Error handling

```js
try {
  let provider = new modules.ethers.JsonRpcProvider(rpcUrl)
  let block = await provider.getBlockNumber()
  Bot.sendMessage(chat.id, "Block: " + block)
} catch (err) {
  Bot.sendMessage(chat.id, "RPC error: " + err.message)
}
```

Common errors:

| Error | Cause |
| --- | --- |
| `WebSocketProvider is not allowed` | Used a blocked provider type |
| `RPC URL must be a valid HTTP(S) URL` | Invalid or missing URL |
| `ethers RPC call limit exceeded` | Too many RPC calls in one command |
| `ethers.getBlockNumber timed out after Nms` | RPC call exceeded plan timeout |

---

## Notes

- Store RPC URLs and private keys in [ENV variables](../globals/process.md)
- Use a reliable public RPC or your own HTTP endpoint
- Wallet signing is local — does not count as an RPC call
- For price lookups without RPC, see [marketHub](market-hub.md)
- Official ethers v6 docs: [docs.ethers.org](https://docs.ethers.org/v6/)
