# HTTP Proxies

Sometimes the direct path doesn't work — corporate firewalls, IP-based rate limits, APIs that expect traffic from a specific network. Route your outbound requests through a proxy and pretend you're somewhere else.

The `proxy` option accepts a full URL with protocol, host, port, and optional credentials. Point it at your infrastructure and go.

---

## How to use a proxy

```js
await HTTP.get("https://api.example.com/data", {
  proxy: "http://proxy.example.com:8080"
})
```

Store credentials in [ENV variables](../globals/process.md), not in script source:

```js
await HTTP.get("https://api.example.com/data", {
  proxy: process.env.MY_PROXY_URL
})
```

---

## Supported protocols

| Protocol | URL prefix | Description |
| --- | --- | --- |
| HTTP | `http://` | Standard HTTP proxy |
| HTTPS | `https://` | HTTPS proxy tunnel |
| SOCKS (generic) | `socks://` | Generic SOCKS proxy |
| SOCKS4 | `socks4://` | SOCKS4 — no remote DNS |
| SOCKS4a | `socks4a://` | SOCKS4a — remote DNS via proxy |
| SOCKS5 | `socks5://` | SOCKS5 — auth + UDP support |
| SOCKS5h | `socks5h://` | SOCKS5 with remote hostname resolution |

Any other protocol throws a validation error before the request is sent. No surprises mid-flight.

---

## URL format

```
protocol://[username:password@]hostname[:port]
```

### Examples

```js
// HTTP — no auth
proxy: "http://proxy.example.com:8080"

// HTTP — with auth
proxy: "http://user:pass@proxy.example.com:8080"

// HTTPS proxy
proxy: "https://secure-proxy.example.com:443"

// SOCKS5
proxy: "socks5://socks.example.com:1080"

// SOCKS5 with credentials
proxy: "socks5://myuser:mypass@socks.example.com:1080"

// SOCKS4
proxy: "socks4://proxy.example.com:1080"
```

| Rule | Value |
| --- | --- |
| Hostname | Required |
| Port | Optional (defaults: HTTP 80, HTTPS 443, SOCKS 1080) |
| Port range | 1–65535 |
| Credentials | Optional — URL-encoded username and password |

---

## HTTP vs SOCKS — which to use?

| Type | Best for |
| --- | --- |
| **HTTP/HTTPS proxy** | Simple web API forwarding, corporate proxies, most REST APIs |
| **SOCKS5** | VPN tunnels, non-HTTP traffic paths, remote DNS resolution (`socks5h://`) |
| **SOCKS4/4a** | Legacy proxy servers that do not support SOCKS5 |

For most bot integrations with REST APIs, `http://` or `https://` is enough. SOCKS is for when you need to get fancy.

---

## Proxy vs cfProxy

| | `proxy` | `cfProxy` |
| --- | --- | --- |
| What it is | Any HTTP/SOCKS proxy server | Your own Cloudflare Worker |
| Setup | Provide a proxy URL | Deploy a Worker (see [Cloudflare Worker Proxy](cf-proxy.md)) |
| Typical use | Existing proxy/VPN infrastructure | Edge routing, IP masking via Cloudflare |
| URL format | `http://`, `socks5://`, etc. | `https://name.workers.dev` only |

Use `proxy` when you already have a proxy service. Use `cfProxy` when you want a free, self-hosted Cloudflare edge router.

When `cfProxy` is set, `proxy` is ignored — `cfProxy` handles routing instead.

---

## Try it — copy-paste examples

### Rotating through your own proxy pool

```js
let proxies = process.env.PROXY_POOL.split(",")
let proxy = proxies[user.id % proxies.length]

await HTTP.get("https://api.example.com/data", { proxy })
```

### POST through a corporate HTTP proxy

```js
await HTTP.post("https://internal-api.company.com/report", {
  proxy: "http://corp-proxy.internal:3128",
  body: { bot_id: bot.id, event: "daily_stats" },
  headers: { "X-Internal-Key": process.env.INTERNAL_KEY }
})
```

### SOCKS5 for APIs that check egress IP

```js
await HTTP.get("https://partner-api.com/v1/status", {
  proxy: process.env.SOCKS5_PROXY,
  timeout: 15000
})
```

### With other request options

Proxy works alongside every other `HTTP` option:

```js
let res = await HTTP.post("https://api.example.com/submit", {
  proxy: process.env.PROXY_URL,
  body: { event: "signup", user_id: user.id },
  headers: { Authorization: "Bearer " + process.env.API_TOKEN },
  timeout: 10000,
  responseType: "json",
  success: "/onSubmitDone",
  error: "/onSubmitFailed"
})
```

---

## Behaviour notes

- Proxy agents are cached internally for **5 minutes** to improve performance on repeated requests to the same proxy
- When `proxy` is set, it takes priority over any platform default routing
- Proxy URLs are validated before the request fires — invalid format throws immediately
- Failed proxy connections return `res.ok === false` with connection details in `res.error`

---

## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Validation error on `proxy` | Wrong protocol or bad URL | Use a supported protocol; include `http://` or `socks5://` |
| `res.ok === false`, connection refused | Proxy host down or wrong port | Verify proxy is reachable; check port |
| `res.ok === false`, 407 | Proxy requires auth | Add `user:pass@` to the proxy URL |
| Slow responses | High-latency proxy path | Try a closer proxy or reduce `timeout` |
| Works locally, fails in bot | Proxy not reachable from platform servers | Use a publicly reachable proxy or [cfProxy](cf-proxy.md) |

See [Limits & Timeouts](limits.md) for timeout and response size caps.
