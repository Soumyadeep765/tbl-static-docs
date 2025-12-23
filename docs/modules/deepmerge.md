## deepmerge

deepmerge is used to **deeply merge objects**.

It is useful for combining configurations or nested data.

## Merge Two Objects

```js
const merged = modules.deepmerge(
  { a: 1, b: { x: 1 } },
  { b: { y: 2 }, c: 3 }
)
```

## Example Output

```
merged → { a: 1, b: { x: 1, y: 2 }, c: 3 }
```

## Official Documentation

[deepmerge Docs]

[deepmerge Docs]: https://www.npmjs.com/package/deepmerge