# qs

Everything after the `?` in a URL — parsed, stringified, and tamed.

## What is it?

**qs** handles query strings: turn `"a=1&b=2"` into `{ a: "1", b: "2" }`, or go the other way. Essential for webhook params, API URLs, and anywhere URL encoding gets messy.

Access it as `modules.qs`.

---

## How to use

Parse a query string:

```js
let obj = modules.qs.parse("a=1&b=2")
// { a: "1", b: "2" }
```

Stringify an object back:

```js
let str = modules.qs.stringify({ a: 1, b: 2 })
// "a=1&b=2"
```

Both methods are **synchronous** — no `await`.

---

## Methods

| Method | Returns | Description |
| --- | --- | --- |
| `parse(str, options?)` | `object` | Parse a query string into an object |
| `stringify(obj, options?)` | `string` | Convert an object to a query string |

Common `parse` options:

| Option | Description |
| --- | --- |
| `ignoreQueryPrefix: true` | Strip leading `?` before parsing |
| `delimiter` | Custom separator (default `&`) |
| `arrayLimit` | Max array size when parsing |

---

## Try it

### Read webhook query params

[Bot](../bot-instance/index.md) replies in [chat](../globals/chat.md). Query params are often in [`params`](../globals/params.md) or the request URL:

```js
let query = modules.qs.parse(params, { ignoreQueryPrefix: true })

if (query.token) {
  Bot.sendMessage("Token received: " + query.token.slice(0, 8) + "...")
} else {
  Bot.sendMessage("No token in query string.")
}
```

### Build an API URL

Store your base URL in [`process.env`](../globals/process.md):

```js
let query = modules.qs.stringify({
  api_key: process.env.API_KEY,
  limit: 10,
  format: "json"
})

let url = process.env.API_BASE + "?" + query
Bot.sendMessage("Request URL built. Ready to fetch.")
```

### Parse nested params

```js
let obj = modules.qs.parse("user[name]=Alice&user[age]=25")
// { user: { name: "Alice", age: "25" } }
```

---

## Limits

| Limit | Value |
| --- | --- |
| Input size (`parse`) | Plan buffer size (512 KB – 10 MB) |
| Max parameters | 1000 |
| Array limit | 100 items per array key |

---

## Notes

- **Sync** — no `await` needed
- `parse()` returns string values by default — convert types yourself
- For full CSV/YAML parsing, see [ParseCSV](parse-csv.md) and [ParseYML](parse-yml.md)
- Official package: [qs on npm](https://www.npmjs.com/package/qs)
