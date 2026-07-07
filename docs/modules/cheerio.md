# cheerio

jQuery for HTML strings — no browser, no guilt.

## What is it?

**cheerio** parses HTML and lets you query it with a familiar `$()` syntax. Scrape a page title, pull links from a snippet, read table cells — all from a string, no DOM required.

Access it as `modules.cheerio`.

---

## How to use

Load HTML, then query it:

```js
let $ = modules.cheerio.load("<p>Hello</p>")
let text = $("p").text()
// "Hello"
```

`load()` returns a cheerio instance. Use CSS selectors like you would in jQuery: `$("a")`, `$(".price")`, `$("#main")`.

---

## API reference

| Method | Description |
| --- | --- |
| `load(html, options?)` | Parse HTML and return a cheerio `$` function |
| `$("selector")` | Query elements (standard cheerio/jQuery API) |
| `.text()` | Get combined text content |
| `.html()` | Get inner HTML |
| `.attr(name)` | Get an attribute value |
| `.each(fn)` | Loop over matched elements |

The full cheerio API applies — see the [official docs](https://cheerio.js.org/) for selectors, traversal, and manipulation.

---

## Try it

### Extract a page title from HTML

[`params`](../globals/params.md) might hold a URL's HTML from an HTTP callback, or a snippet the user pasted. [Bot](../bot-instance/index.md) sends the result to [chat](../globals/chat.md):

```js
let html = params
let $ = modules.cheerio.load(html)

let title = $("title").text() || "No title found"
Bot.sendMessage(chat.id, "Page title: " + title)
```

### List all links

```js
let $ = modules.cheerio.load(html)
let links = []

$("a").each((i, el) => {
  let href = $(el).attr("href")
  if (href) links.push(href)
})

Bot.sendMessage(chat.id, "Found " + links.length + " links:\n" + links.slice(0, 10).join("\n"))
```

---

## Notes

- **Sync** — no `await` needed
- Input size is limited by your plan's buffer size (512 KB – 10 MB). Go over and you'll see: `Input exceeds plan limit (N bytes)`
- cheerio works on HTML strings, not live URLs — fetch the page first (e.g. via HTTP), then parse
- Official package: [cheerio on npm](https://www.npmjs.com/package/cheerio)
