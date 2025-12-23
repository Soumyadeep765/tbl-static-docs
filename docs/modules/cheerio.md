## cheerio

cheerio is used to **parse and manipulate HTML** in Node.js, similar to jQuery.

It is useful for scraping and DOM manipulation.

## Load and Read HTML

```js
const $ = modules.cheerio.load("<p>Hello</p>")
const text = $("p").text()
```

## Example Output

```
text → "Hello"
```

## Official Documentation

[cheerio Docs]

[cheerio Docs]: https://www.npmjs.com/package/cheerio