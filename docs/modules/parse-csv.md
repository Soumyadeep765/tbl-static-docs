# ParseCSV

`modules.ParseCSV` parses **CSV strings** into arrays of row objects. Returns a **Promise** — use `await`.

```js
let rows = await modules.ParseCSV.parse("name,age\nAlice,25\nBob,30")
// [{ name: "Alice", age: "25" }, { name: "Bob", age: "30" }]
```

Built on [csv-parse](https://www.npmjs.com/package/csv-parse).

---

## Basic usage

```js
let csv = "id,name,score\n1,Alice,95\n2,Bob,87"
let rows = await modules.ParseCSV.parse(csv)

for (let row of rows) {
  Bot.inspect(row.id + ": " + row.name + " = " + row.score)
}
```

By default, the first row is treated as column headers and values are **strings**.

---

## With options

Pass any [csv-parse options](https://csv.js.org/parse/options/) as the second argument:

```js
// Tab-separated, no header row
let rows = await modules.ParseCSV.parse(tsvData, {
  delimiter: "\t",
  columns: ["id", "name", "value"]
})

// Skip empty lines
let rows = await modules.ParseCSV.parse(csv, {
  skip_empty_lines: true
})
```

---

## Limits

| Limit | Value |
| --- | --- |
| Total input size | Plan buffer size (512 KB – 10 MB) |
| Max record size | 256 KB per row |
| Method | Async — returns Promise |

Exceeding input size throws: `CSV input exceeds plan limit (N bytes)`.

---

## Example — import user list

```js
let csv = process.env.USER_CSV  // from ENV or HTTP response

let rows = await modules.ParseCSV.parse(csv, {
  columns: true,
  skip_empty_lines: true,
  trim: true
})

let imported = 0
for (let row of rows) {
  if (modules.validator.isEmail(row.email)) {
    db.bot.set("users/" + row.email, { name: row.name })
    imported++
  }
}

Bot.sendMessage(chat.id, "Imported " + imported + " users.")
```

---

## Notes

- Always `await` — `parse()` returns a Promise
- Column names come from the header row unless you set `columns` manually
- For YAML data, use [ParseYML](parse-yml.md)
- For query strings, use [qs](qs.md)
