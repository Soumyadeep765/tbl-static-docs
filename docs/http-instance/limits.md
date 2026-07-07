# Limits & Timeouts

Public limits for the `HTTP` instance. Values outside allowed ranges are **clamped automatically**.

## Request timeout

| Setting | Value |
| --- | --- |
| Minimum | 100 ms |
| Default | Your plan's script timeout |
| Maximum | Your plan's script timeout |

| Plan | Max timeout |
| --- | --- |
| Free / Freemium | 15 seconds (15,000 ms) |
| Premium | 30 seconds (30,000 ms) |
| Elite | 60 seconds (60,000 ms) |

```js
// Uses plan default
await HTTP.get("https://api.example.com/data")

// Custom (clamped to plan max)
await HTTP.get("https://api.example.com/data", { timeout: 5000 })
```

On timeout: `res.ok === false`, `res.status === 408`, `res.error.code === "TIMEOUT"`.

---

## Response size

| Setting | Value |
| --- | --- |
| Default max response | **2 MB** |
| Hard maximum | **10 MB** |

Responses larger than the limit return `res.ok === false` with `error.code` of `"RESPONSE_SIZE_EXCEEDED"` or `"RESPONSE_TOO_LARGE"`.

For very large payloads, use `responseType: "stream"` and read incrementally — see [Streaming](streaming.md).

---

## Redirects

| Setting | Default | Maximum |
| --- | --- | --- |
| `maxRedirect` | 3 | 10 |
| `redirect` | `true` | — |

Followed status codes: 301, 302, 303, 307, 308.

When the redirect limit is exceeded: `res.error.code === "REDIRECT_LIMIT_EXCEEDED"`, `res.status === 310`.

```js
await HTTP.get(url, { maxRedirect: 5 })   // up to 5
await HTTP.get(url, { maxRedirect: 0 })   // no redirects
await HTTP.get(url, { redirect: false })  // disable following
```

---

## Streaming limits

Full guide: [Streaming](streaming.md). Summary from the implementation:

| Setting | Value |
| --- | --- |
| Enabled by | `responseType: "stream"` only (never auto) |
| Chunk format | UTF-8 string per chunk (not binary) |
| Max chunk size | 1 MB per chunk |
| Idle timeout | 15 seconds (no data received) |
| Cumulative size | 2 MB default (`maxResponseSize`) |
| Lifetime timer | Starts when response is parsed — not when you start reading |

### Stream lifetime by plan

| Plan | Max stream lifetime |
| --- | --- |
| Free / Freemium | 30 seconds |
| Premium | 60 seconds |
| Elite | 120 seconds |

Streams are cancelled when lifetime or idle timeout is exceeded.

---

## Command chain limit

Each `success` or `error` HTTP callback counts toward the **6 nested command** limit per execution (shared with `Bot.run`).

---

## Proxy

| Setting | Value |
| --- | --- |
| Supported protocols | `http`, `https`, `socks`, `socks4`, `socks4a`, `socks5`, `socks5h` |
| Port range | 1–65535 |
| Agent cache TTL | 5 minutes (internal, automatic) |

---

## Cloudflare Worker proxy

| Requirement | Value |
| --- | --- |
| Protocol | `http://` or `https://` |
| Hostname | Must end with `.workers.dev` |

---

## Validation limits

| Option | Constraint |
| --- | --- |
| `url` | Required, valid URL with protocol |
| `maxRedirect` | Number between 0 and 10 |
| `headers` | Must be an object |
| `query` / `params` | Must be an object |
| `success` / `error` | Must be strings (command names) |
| `proxy` | Valid URL with supported protocol |

Invalid options throw before the request is sent.

---

## Quick reference

| Limit | Free/Freemium | Premium | Elite |
| --- | --- | --- | --- |
| Request timeout | 15s | 30s | 60s |
| Stream lifetime | 30s | 60s | 120s |
| Response size | 2 MB (10 MB hard max) | same | same |
| Max redirects | 10 | 10 | 10 |
| Stream idle | 15s | 15s | 15s |
| Chunk size | 1 MB | 1 MB | 1 MB |

See your full plan details on the [`plan`](../globals/plan.md) global.
