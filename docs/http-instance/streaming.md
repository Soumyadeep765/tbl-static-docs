# Streaming Responses

Most APIs return a small JSON blob you can read in one gulp. Some don't — live feeds, Server-Sent Events, newline-delimited logs. For those, load the body **chunk by chunk** with `responseType: "stream"`.

Streaming is opt-in only. It is never auto-detected. If you didn't ask for it, you get the whole body at once.

---

## How to stream

```js
let res = await HTTP.get("https://api.example.com/events", {
  responseType: "stream"
})
```

When `responseType` is `"stream"`:

1. Response **headers** arrive first (status, `Content-Type`, cookies, etc.)
2. The call returns immediately with a `stream` object — body is **not** pre-loaded
3. You read chunks via `stream.read()`, `for await`, or `stream.collect()`
4. Two internal timers guard the connection (lifetime + idle)
5. Cumulative bytes read are capped at the response size limit (2 MB default)

```
HTTP.get({ responseType: "stream" })
    → headers received, cookies parsed
    → res.stream created, timers start
    → you read chunks one at a time
    → stream ends (done), cancel(), or timer/limit hit
```

For non-stream requests, the full body is read first, `Content-Length` is checked, then `data` and `content` are returned. Streams **skip** the upfront `Content-Length` check — the size limit is enforced as you read.

---

## What streaming is good for

| Use case | Why |
| --- | --- |
| **Server-Sent Events (SSE)** | `text/event-stream` — process events as they arrive |
| **Chunked text APIs** | Newline-delimited JSON, log lines, partial text |
| **Responses near the 2 MB cap** | Start processing before the full body is buffered |
| **Early exit** | Read until you have enough, then `stream.cancel()` |

For typical small JSON APIs, use `responseType: "auto"` — simpler and returns `res.data` directly. Don't stream what you can swallow whole.

---

## What is NOT possible

These are hard limits from the implementation:

| Limitation | Detail |
| --- | --- |
| **Text-only chunks** | Every chunk is converted to a **UTF-8 string** via `.toString()` — not suitable for binary files, images, or raw bytes |
| **2 MB cumulative cap** | Total bytes read cannot exceed `maxResponseSize` (default 2 MB) |
| **1 MB per chunk** | A single chunk larger than 1 MB throws immediately |
| **Lifetime timer** | Stream is killed after 30s / 60s / 120s (by plan) — timer starts when the response is parsed, not when you start reading |
| **15s idle timeout** | If no chunk arrives for 15 seconds, the stream is aborted |
| **No `res.data` / `res.content`** | Body is only available through `res.stream` |
| **One consumer only** | Do not run two `for await` loops on the same `stream` — they share one underlying reader |
| **cfProxy + long upstream streams** | Direct requests disable body timeout for streams; cfProxy worker requests still use the full `timeout` on the worker call |

---

## Stream response object

Fields present when `responseType: "stream"`:

| Field | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | `true` for HTTP 2xx |
| `status` | `number` | HTTP status code |
| `statusText` | `string` | HTTP status text |
| `headers` | `object` | Response headers (lowercase keys) |
| `url` | `string` | Final URL after redirects |
| `redirected` | `boolean` | Whether redirects were followed |
| `redirectCount` | `number` | Number of redirects followed |
| `cookies` | `object` | Parsed cookies — available **before** you read any chunk |
| `isStream` | `boolean` | Always `true` |
| `responseType` | `string` | Always `"stream"` |
| `contentType` | `string` | `Content-Type` header value |
| `stream` | `object` | Stream interface — `read`, `collect`, `cancel`, async iterator |

Fields **not** present on stream responses:

| Missing field | Why |
| --- | --- |
| `data` | Body not parsed — read via `stream` |
| `content` | Body not buffered — read via `stream` |
| `isJson` | No JSON parsing on streams |
| `error` | Stream read errors are **thrown** during iteration, not returned here |

Non-2xx responses still return a `stream` object — you can read the error body as chunks if the server sends one.

---

## Stream interface

`res.stream` exposes exactly three methods plus async iteration:

### `stream.read()` → `{ value, done }`

Reads one chunk at a time:

```js
while (true) {
  let result = await res.stream.read()

  if (result.done) break          // stream finished normally

  let chunk = result.value        // UTF-8 string
  Bot.inspect(chunk)
}
```

| Return shape | Meaning |
| --- | --- |
| `{ value: string, done: false }` | One chunk of data |
| `{ done: true }` | Stream ended — no `value` field |

Throws if the stream was aborted, timed out, or hit a size limit.

### `for await (chunk of res.stream)`

Same as repeated `read()` calls — each `chunk` is a UTF-8 string:

```js
for await (let chunk of res.stream) {
  Bot.inspect(chunk)
}
```

### `stream.collect(maxSize?)` → `string`

Reads **all** remaining chunks and joins them into one UTF-8 string.

```js
let fullBody = await res.stream.collect()           // default max: 2 MB
let partial  = await res.stream.collect(512 * 1024) // custom max: 512 KB
```

- Uses the same guarded reader as `read()` — respects chunk and cumulative limits
- Throws if total collected size exceeds `maxSize`
- Clears timers on successful completion

### `stream.cancel()` → `void`

Stops the stream immediately. Synchronous — does not return a promise.

```js
for await (let chunk of res.stream) {
  if (chunk.includes("END")) {
    res.stream.cancel()
    break
  }
}
```

Destroys the underlying connection and clears both timers. Any subsequent `read()` throws `"Stream cancelled by user"` or `"Stream has been closed or aborted"`.

---

## Timers

Two independent timers start the moment the response is parsed (when `await HTTP.get(...)` resolves or just before a callback command runs):

### Lifetime timer (plan-based)

| Plan | Max lifetime |
| --- | --- |
| Free / Freemium | **30 seconds** |
| Premium | **60 seconds** |
| Elite | **120 seconds** |

Counts from response parse time — **not** from your first `read()`. If you do other work after `await` before reading, that time counts. Procrastination has consequences.

Error message: `Stream lifetime limit of Xs exceeded`

### Idle timer (fixed)

**15 seconds** without receiving any chunk → stream aborted.

Resets every time a chunk arrives. Error message: `Stream idle timeout of 15s exceeded (no data received)`

---

## Size limits during read

| Check | Limit | Error |
| --- | --- | --- |
| Single chunk | 1 MB max | `Chunk size exceeds 1MB limit` |
| Cumulative total | 2 MB default (`maxResponseSize`) | `Stream cumulative size exceeded maximum limit of N bytes` |
| `collect(maxSize)` | Your `maxSize` argument | `Stream exceeded size limit of N bytes` |

---

## Request timeout vs stream timers

For **direct** requests (no `cfProxy`):

| Setting | Stream behaviour |
| --- | --- |
| `timeout` | Applies to **headers only** (`headersTimeout`) — waiting for response headers |
| Body timeout | Disabled (`bodyTimeout: 0`) — body duration is controlled by stream timers |
| `AbortSignal` | Not attached for streams — no request-level abort on body read |

For **cfProxy** requests:

| Setting | Stream behaviour |
| --- | --- |
| `timeout` | Applies to the **entire worker call** (headers + body) via `AbortSignal.timeout` |
| Upstream streaming | Depends on your Worker — cf-http-router buffers the upstream response before returning it |

So for long-lived SSE feeds, a **direct** request gives you up to the plan lifetime (30–120s). Through **cfProxy**, the worker must respond within `timeout`.

---

## Try it — copy-paste examples

### SSE (text event stream)

```js
let res = await HTTP.get("https://api.example.com/live", {
  responseType: "stream",
  headers: { Accept: "text/event-stream" }
})

if (!res.ok || !res.isStream) {
  Bot.sendMessage(chat.id, "Feed unavailable.")
  return
}

try {
  for await (let chunk of res.stream) {
    // Chunks may split mid-line — buffer incomplete lines yourself
    for (let line of chunk.split("\n")) {
      if (line.startsWith("data: ")) {
        Bot.inspect(line.slice(6))
      }
    }
  }
} catch (err) {
  Bot.sendMessage(chat.id, "Stream ended: " + err.message)
}
```

### NDJSON — collect then parse

Only works if the full body is under 2 MB:

```js
let res = await HTTP.get("https://api.example.com/export.ndjson", {
  responseType: "stream"
})

let raw = await res.stream.collect()
let records = raw.split("\n").filter(Boolean).map(JSON.parse)

Bot.sendMessage(chat.id, "Loaded " + records.length + " records.")
```

### Read until enough, then cancel

```js
let res = await HTTP.get(url, { responseType: "stream" })
let found = false

for await (let chunk of res.stream) {
  if (chunk.includes("target_value")) {
    found = true
    res.stream.cancel()
    break
  }
}
```

### Non-2xx error body

```js
let res = await HTTP.get("https://api.example.com/missing", {
  responseType: "stream"
})

if (!res.ok) {
  let errorBody = await res.stream.collect()
  Bot.sendMessage(chat.id, "Error " + res.status + ": " + errorBody)
}
```

---

## With fallback commands

Streaming works with `success` / `error`, but timers **start when the HTTP response is parsed** — before your callback command executes. Start reading immediately inside the callback.

```js
HTTP.get({
  url: "https://api.example.com/feed",
  responseType: "stream",
  success: "/processFeed"
})
```

```js
// /processFeed — read immediately, don't do slow work first
if (!response.isStream) return

try {
  for await (let chunk of response.stream) {
    Bot.inspect(chunk)
  }
} catch (err) {
  Bot.inspect("Stream error: " + err.message)
}
```

In callbacks: `response.stream`, `response.isStream`, `response.contentType` via the `response` global. See [Fallback Commands](fallback-commands.md).

---

## Error reference

All stream errors are **thrown** during `read()`, `for await`, or `collect()` — wrap in try/catch.

| Error message | Cause |
| --- | --- |
| `Stream lifetime limit of 30s exceeded` | Plan lifetime timer fired (30/60/120s) |
| `Stream idle timeout of 15s exceeded (no data received)` | No chunk for 15 seconds |
| `Chunk size exceeds 1MB limit` | Server sent a single chunk > 1 MB |
| `Stream cumulative size exceeded maximum limit of N bytes` | Total read exceeds 2 MB default |
| `Stream exceeded size limit of N bytes` | `collect(maxSize)` limit hit |
| `Stream cancelled by user` | You called `stream.cancel()` |
| `Stream has been closed or aborted` | Read attempted after abort |

---

## Streaming vs regular response

| | `"auto"` / `"json"` / `"text"` | `"stream"` |
| --- | --- | --- |
| Body loaded | All at once before return | On demand, chunk by chunk |
| `res.data` / `res.content` | Yes | No — use `stream` |
| `Content-Length` pre-check | Yes | No — checked during read |
| Chunk format | N/A | UTF-8 string only |
| Duration limit | `timeout` option | Lifetime + idle timers |
| Best for | JSON APIs, small bodies | SSE, chunked text, early cancel |

See [Limits & Timeouts](limits.md) for the full caps table.
