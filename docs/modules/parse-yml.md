# ParseYML

YAML configs without the "why won't this indent" headache.

## What is it?

**ParseYML** parses YAML strings into JavaScript objects (and stringifies objects back to YAML). Handy for config files, structured settings, or any time someone hands you YAML and expects you to make sense of it.

Access it as `modules.ParseYML`.

---

## How to use

Parse a YAML string — **sync, no `await`**:

```js
let result = modules.ParseYML.parse("name: Alice\nage: 25")
// { name: "Alice", age: "25" }
```

Stringify an object back to YAML:

```js
let yaml = modules.ParseYML.stringify({ name: "Alice", age: 25 })
// "name: Alice\nage: 25\n"
```

---

## Methods

| Method | Returns | Description |
| --- | --- | --- |
| `parse(yamlString, options?)` | `object` | Parse YAML into a JavaScript object |
| `stringify(object, options?)` | `string` | Convert an object to YAML text |

---

## Try it

### Load bot config from YAML

[Bot](../bot-instance/index.md) sends to [chat](../globals/chat.md). Store config in [db](../db-instance/index.md) as a YAML string, parse on read:

```js
let raw = db.bot.get("config_yaml") || "theme: dark\nlang: en"
let config = modules.ParseYML.parse(raw)

Bot.sendMessage(chat.id, "Theme: " + config.theme + ", Language: " + config.lang)
```

### Parse user-submitted YAML

[`params`](../globals/params.md) might contain YAML the user pasted:

```js
try {
  let data = modules.ParseYML.parse(params)
  Bot.sendMessage(chat.id, "Parsed " + Object.keys(data).length + " top-level keys.")
} catch (err) {
  Bot.sendMessage(chat.id, "Invalid YAML: " + err.message)
}
```

### Save settings as YAML

```js
let settings = { notifications: true, theme: "dark", lang: "en" }
let yaml = modules.ParseYML.stringify(settings)
db.user.set("settings_yaml", yaml)
Bot.sendMessage(chat.id, "Settings saved.")
```

---

## Limits

| Limit | Value |
| --- | --- |
| Input size | Plan buffer size (512 KB – 10 MB) |
| Schema | `FAILSAFE_SCHEMA` — **all values are strings** |
| Method | Sync |

`parse()` uses `FAILSAFE_SCHEMA` for safety — numbers and booleans in YAML become strings (`"25"`, not `25`). Convert types yourself after parsing.

Exceeding input size throws: `Input exceeds plan limit (N bytes)`.

---

## Notes

- **Sync** — no `await` needed
- YAML indentation matters — spaces, not tabs (YAML's eternal rule)
- All parsed values are strings under `FAILSAFE_SCHEMA`
- For tabular data, use [ParseCSV](parse-csv.md)
- Official package: [js-yaml on npm](https://www.npmjs.com/package/js-yaml)
