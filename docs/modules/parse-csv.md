## ParseCSV

ParseCSV is used to **parse CSV strings into JSON objects**.

It is useful when working with CSV data in bots or scripts, such as importing lists, reports, or external data sources.

ParseCSV functionality is available through the `modules` object.

## Parsing a CSV String

```js
const result = modules.ParseCSV.parse(
  "name,age\nAlice,25\nBob,30"
)
```

This converts CSV rows into an array of objects.

## Example Output

```
result → [
  { name: "Alice", age: "25" },
  { name: "Bob", age: "30" }
]
```

Values are returned as **strings** by default.

## Notes

- The first row is treated as column headers
- Each row becomes one object
- Useful for quick CSV imports and transformations

## Official Documentation

[csv-parse Docs]

[csv-parse Docs]: https://www.npmjs.com/package/csv-parse
