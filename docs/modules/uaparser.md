# uaParser

"Mozilla/5.0 (Windows NT..." — let's find out what that actually means.

## What is it?

**uaParser** decodes User-Agent strings into structured info: browser name, OS, device type. Useful for analytics, logging, or tailoring responses based on whether someone's on mobile or desktop.

Access it as `modules.uaParser`.

---

## How to use

Pass a User-Agent string, get a structured object:

```js
let ua = modules.uaParser.parse(
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
)
// {
//   browser: { name: "Chrome", version: "120.0.0.0", major: "120" },
//   os: { name: "Windows", version: "10" },
//   device: { model: "", type: "", vendor: "" }
// }
```

**Sync** — no `await` needed.

---

## Methods

| Method | Returns | Description |
| --- | --- | --- |
| `parse(uaString)` | `object` | Parse a User-Agent into browser, OS, and device |
| `setUA(uaString)` | `UAParser` | Set UA on an instance (advanced usage) |

### Parsed object shape

| Field | Description |
| --- | --- |
| `browser.name` | Browser name (Chrome, Firefox, Safari, …) |
| `browser.version` | Full version string |
| `browser.major` | Major version number |
| `os.name` | Operating system (Windows, macOS, Android, …) |
| `os.version` | OS version |
| `device.model` | Device model (often empty on desktop) |
| `device.type` | `"mobile"`, `"tablet"`, or `""` for desktop |
| `device.vendor` | Device manufacturer |

---

## Try it

### Log visitor info from a webhook

[Bot](../bot-instance/index.md) replies in [chat](../globals/chat.md). The User-Agent is often in the [request](../globals/request.md) headers:

```js
let uaString = request.headers["user-agent"] || ""
let ua = modules.uaParser.parse(uaString)

let summary = [
  "Browser: " + (ua.browser.name || "Unknown"),
  "OS: " + (ua.os.name || "Unknown"),
  "Device: " + (ua.device.type || "desktop")
].join("\n")

Bot.sendMessage("Visitor info:\n" + summary)
```

### Customize message for mobile users

```js
let ua = modules.uaParser.parse(request.headers["user-agent"] || "")

if (ua.device.type === "mobile") {
  Bot.sendMessage("Tip: open our mini-app for the best mobile experience.")
} else {
  Bot.sendMessage("Welcome! Use /help to get started.")
}
```

### Store analytics in db

```js
let ua = modules.uaParser.parse(request.headers["user-agent"] || "")

db.bot.set("analytics/last_visit", {
  browser: ua.browser.name,
  os: ua.os.name,
  device: ua.device.type || "desktop",
  user: user.id,
  at: Date.now()
})
```

---

## Notes

- **Sync** — no `await` needed
- Device fields are often empty for desktop browsers — that's normal
- User-Agent strings can be spoofed; don't rely on them for security decisions
- Official package: [ua-parser-js on npm](https://www.npmjs.com/package/ua-parser-js)
