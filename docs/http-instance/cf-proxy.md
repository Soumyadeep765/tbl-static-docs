# Cloudflare Worker Proxy (cfProxy)

Want your API calls to appear from a Cloudflare edge IP instead of the platform's servers? Deploy a tiny Worker, point `cfProxy` at it, and route requests through Cloudflare's global network.

It's not magic — it won't bypass API quotas or defeat anti-bot systems. But it *does* change the visible egress IP, which helps with IP-based rate limits and hiding your origin.

---

## What is cfProxy?

Normally, `HTTP` requests go directly from the platform to the target URL. With `cfProxy`, the path looks like this:

```
Your bot command
    → HTTP client
        → Your Cloudflare Worker (*.workers.dev)
            → Target API (api.example.com)
                → Response flows back the same way
```

The target API sees a **Cloudflare edge IP**, not the platform server IP.

```js
await HTTP.get("https://api.example.com/data", {
  cfProxy: "https://my-router.workers.dev"
})
```

---

## Why use it?

| Benefit | Explanation |
| --- | --- |
| **Different egress IP** | Requests appear to come from Cloudflare's global network |
| **Reduce IP-based rate limits** | Some APIs rate-limit by IP — Cloudflare edge IPs can help spread load |
| **Hide origin** | Your target server does not see the platform server address |
| **Edge caching** | Add caching logic inside your Worker for frequently requested data |
| **Custom routing** | Rewrite headers, add auth, or route to different backends in Worker code |
| **Free tier available** | Cloudflare Workers free plan covers light bot traffic |

### What cfProxy does NOT do

Per the [cf-http-router](https://github.com/Soumyadeep765/cf-http-router) project:

- Does **not** bypass API key quotas or account-level rate limits
- Does **not** defeat application-level auth or anti-bot systems
- Only changes the **visible egress IP** to Cloudflare's edge network

---

## Requirements

| Rule | Value |
| --- | --- |
| Protocol | `http://` or `https://` |
| Hostname | Must end with `.workers.dev` |
| Example | `https://my-router.workers.dev` |

Custom domains (e.g. `proxy.yourdomain.com`) are **not** accepted — only `*.workers.dev` URLs.

---

## Where to get a Worker

You need to **deploy your own** Cloudflare Worker. There is no shared cfProxy endpoint — roll your own.

The recommended open-source router is **[cf-http-router](https://github.com/Soumyadeep765/cf-http-router)** — a universal HTTP proxy router for Cloudflare Workers that:

- Supports all HTTP methods (GET, POST, PUT, DELETE, PATCH, etc.)
- Preserves headers and response format
- Handles streaming responses (SSE, large files)
- Requires no KV storage or paid add-ons
- Is MIT licensed

---

## Deploy cf-http-router

### Prerequisites

- A [Cloudflare account](https://dash.cloudflare.com/sign-up) (free tier works)
- [Node.js](https://nodejs.org/) installed locally
- [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/) (installed via the repo)

### Step 1 — Clone the repository

```bash
git clone https://github.com/Soumyadeep765/cf-http-router.git
cd cf-http-router
```

### Step 2 — Install dependencies

```bash
npm install
```

### Step 3 — Log in to Cloudflare

```bash
npx wrangler login
```

### Step 4 — Deploy

```bash
npm run deploy
```

After deployment, Wrangler prints your Worker URL:

```
Published my-router (X.XX sec)
  https://my-router.<your-subdomain>.workers.dev
```

That URL is your `cfProxy` value. Copy it. You'll need it twice — once in ENV, once in your head.

### One-click deploy

The repository also supports deploying directly from GitHub via Cloudflare's deploy button — see the README on [cf-http-router](https://github.com/Soumyadeep765/cf-http-router).

---

## Using cfProxy in your bot

Store the Worker URL in an ENV variable:

```
CF_PROXY=https://my-router.your-subdomain.workers.dev
```

Then reference it in commands:

```js
// GET request
let res = await HTTP.get("https://api.example.com/status", {
  cfProxy: process.env.CF_PROXY
})

// POST with body and headers
let res = await HTTP.post("https://api.example.com/users", {
  body: { name: user.first_name },
  headers: { Authorization: "Bearer " + process.env.API_TOKEN },
  cfProxy: process.env.CF_PROXY
})

// With fallback commands
HTTP.get({
  url: "https://api.example.com/data",
  cfProxy: process.env.CF_PROXY,
  success: "/onData",
  error: "/onDataError"
})
```

Successful cfProxy responses include `usedWorkerProxy: true` on the response object.

---

## How requests reach your Worker

The HTTP client automatically formats requests for compatible Workers like cf-http-router:

**GET requests** — query parameters on the Worker URL:

```
GET https://my-router.workers.dev?url=https://api.example.com/data
```

**POST / PUT / PATCH / DELETE** — JSON body to the Worker:

```json
{
  "method": "POST",
  "url": "https://api.example.com/users",
  "headers": { "Authorization": "Bearer token" },
  "body": { "name": "Alice" }
}
```

You do not need to construct this yourself — just set `cfProxy` and the client handles it.

---

## cf-http-router API reference

If you build a custom Worker, it should accept the same payload format as [cf-http-router](https://github.com/Soumyadeep765/cf-http-router):

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `method` | `string` | Yes | HTTP method (GET, POST, PUT, etc.) |
| `url` | `string` | Yes | Target URL to forward to |
| `headers` | `object` | No | Headers to send to the target |
| `body` | `any` | No | Request body for POST, PUT, PATCH |

---

## Latency note

Using a Cloudflare Worker adds one extra network hop. In most cases this is only a few milliseconds — often offset by Cloudflare's edge proximity to the target API.

---

## Error handling

| `error.code` | `status` | Cause |
| --- | --- | --- |
| `WORKER_PROXY_ERROR` | 502 | Worker unreachable, timed out, or returned an error |
| Validation error (throws) | — | `cfProxy` URL is not `*.workers.dev` |

```js
let res = await HTTP.get("https://api.example.com/data", {
  cfProxy: process.env.CF_PROXY
})

if (!res.ok) {
  if (res.error?.code === "WORKER_PROXY_ERROR") {
    Bot.sendMessage("Worker proxy failed — check your Worker is deployed.")
  } else {
    Bot.sendMessage("API error: " + res.status)
  }
}
```

---

## cfProxy vs regular proxy

| | `cfProxy` | `proxy` |
| --- | --- | --- |
| Infrastructure | Your Cloudflare Worker (free tier OK) | Any HTTP/SOCKS server |
| URL | `https://name.workers.dev` | `http://`, `socks5://`, etc. |
| Setup effort | Deploy once, use everywhere | Need a running proxy service |
| Edge network | Yes — Cloudflare global CDN | Depends on your proxy provider |
| Streaming | Supported via cf-http-router | Supported |

See [HTTP Proxies](proxies.md) for the `proxy` option in detail.

---

## Quick start checklist

1. Create a [Cloudflare account](https://dash.cloudflare.com/sign-up)
2. Clone and deploy [cf-http-router](https://github.com/Soumyadeep765/cf-http-router)
3. Copy the `*.workers.dev` URL from the deploy output
4. Add it as `CF_PROXY` in your bot's ENV variables on the dashboard
5. Use `cfProxy: process.env.CF_PROXY` in your `HTTP` calls
