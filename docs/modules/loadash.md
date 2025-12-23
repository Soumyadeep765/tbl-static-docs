## lodash

lodash is a utility library for **array, object, and function operations**.

It is very useful for:

- Filtering data
- Mapping and transforming arrays
- Working with objects
- Simplifying common logic

lodash functionality is available through the `modules` object.

## Filtering an Array

```js
const result = modules.lodash.filter(
  [1, 2, 3, 4],
  n => n > 2
)
```

This filters the array and returns only values greater than `2`.

## Example Output

```
result → [3, 4]
```

## Notes

- Works with arrays, objects, and collections
- Helps reduce boilerplate code
- Methods follow standard lodash behavior

## Official Documentation

[lodash Docs]

[lodash Docs]: https://www.npmjs.com/package/lodash