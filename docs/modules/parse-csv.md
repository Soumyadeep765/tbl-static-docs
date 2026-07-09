# ParseCSV

Comma-separated values, row by row — without hand-splitting strings and crying.

## What is it?

**ParseCSV** turns CSV text into an array of row objects. Feed it a string like `"name,age\nAlice,25"`, get back `[{ name: "Alice", age: "25" }]`. The first row becomes column headers by default.

Access it as `modules.ParseCSV`.

Built on [csv-parse](https://www.npmjs.com/package/csv-parse).

---

## How to use

**`parse()` returns a Promise — you must use `await`:**

```js
let rows = await modules.ParseCSV.parse("name,age\nAlice,25\nBob,30")
// [{ name: "Alice", age: "25" }, { name: "Bob", age: "30" }]
```

!!! warning "Async — don't skip await"
    `parse()` is **async**. Without `await`, you get a Promise instead of rows. Your `for` loop will be very confused.

---

## Methods

| Method | Returns | Description |
| --- | --- | --- |
| `parse(csvString, options?)` | `Promise<array>` | Parse CSV into row objects |

Pass any [csv-parse options](https://csv.js.org/parse/options/) as the second argument.

Common options:

| Option | Description |
| --- | --- |
| `columns: true` | Use first row as headers (default behaviour) |
| `columns: ["id", "name"]` | Manual column names (no header row) |
| `delimiter: "\t"` | Tab-separated instead of comma |
| `skip_empty_lines: true` | Ignore blank lines |
| `trim: true` | Trim whitespace from values |

---

## Try it

### Loop through parsed rows

[Bot](../bot-instance/index.md) sends each row to [chat](../globals/chat.md):

```js
let csv = "id,name,score\n1,Alice,95\n2,Bob,87"
let rows = await modules.ParseCSV.parse(csv)

for (let row of rows) {
  Bot.sendMessage(chat.id, row.name + " scored " + row.score)
}
```

### Import a user list from ENV

Read CSV text from [`process.env`](../globals/process.md), validate emails, save to [db](../db-instance/index.md):

```js
let csv = process.env.USER_CSV

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

## Limits

| Limit | Value |
| --- | --- |
| Total input size | Plan buffer size (512 KB – 10 MB) |
| Max record size | 256 KB per row |
| Method | Async — returns Promise |

Exceeding input size throws: `CSV input exceeds plan limit (N bytes)`.

---

## Notes

- Always **`await`** — `parse()` returns a Promise
- Column values are **strings** by default — convert numbers yourself if needed
- Column names come from the header row unless you set `columns` manually
- For YAML data, use [ParseYML](parse-yml.md)
- For query strings, use [qs](qs.md)
