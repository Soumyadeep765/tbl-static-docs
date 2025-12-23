## ParseYML

ParseYML is used to **parse YAML strings into JSON objects**.

It is useful when working with YAML configuration files or structured data written in YAML format.

ParseYML functionality is available through the `modules` object.

## Parsing a YAML String

```js
const result = modules.ParseYML.parse(
  "name: Alice\nage: 25"
)
```

This converts YAML content into a JavaScript object.

## Example Output

```
result → {
  name: "Alice",
  age: 25
}
```

Unlike CSV parsing, numeric values are automatically converted to numbers.

## Notes

- YAML indentation is respected
- Supports standard YAML syntax
- Useful for configuration files and structured settings

## Official Documentation

[js-yaml Docs]

[js-yaml Docs]: https://www.npmjs.com/package/js-yaml