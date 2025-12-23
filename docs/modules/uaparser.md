## uaParser

uaParser is used to **parse user-agent strings** and extract information about the browser, operating system, and device.

It is useful for:

- Analytics
- Logging
- Device detection
- Customizing content based on client environment

uaParser functionality is available through the `modules` object.

## Parsing a User-Agent String

```js
const ua = modules.uaParser.parse(
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
)
```

This returns a structured object describing the client.

## Example Output

```
ua → {
  browser: { name: "Firefox", version: "xx" },
  os: { name: "Windows", version: "10" },
  device: { model: "", type: "", vendor: "" }
}
```

## Notes

- Browser, OS, and device details are extracted automatically
- Device fields may be empty for desktop browsers
- Useful for environment-aware logic

## Official Documentation

[ua-parser-js Docs]

[ua-parser-js Docs]: https://www.npmjs.com/package/ua-parser-js