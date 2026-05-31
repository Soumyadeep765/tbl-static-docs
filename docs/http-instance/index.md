# HTTP

Your bot lives on Telegram, but it doesn't have to stay there.

The **HTTP instance** sends requests to the outside world — your backend, a payment API, a weather service, anything with a URL. GET, POST, headers, JSON bodies: the usual fetch-style workflow, inside a command.

```js
let res = await HTTP.get("https://api.example.com/status")
```

Use it when Telegram doesn't have the data you need, or when another system needs to know something happened in the bot.

## When HTTP fits

- Pulling live data (prices, scores, inventory) into a reply  
- POSTing form submissions to your server  
- Verifying a token against an auth API  
- Anything that isn't a Telegram method  

For talking *to* Telegram, use [Api](../api-instance/index.md). For talking *out* to the rest of the internet, use HTTP.

## Pages here

| Page | Covers |
| --- | --- |
| [Making Requests](making-requests.md) | GET, POST, options, reading responses |
| [Fallback Commands](fallback-commands.md) | Route success or failure to different commands |

Responses from HTTP callbacks land in [`http_response`](../globals/http_response.md) and related globals when you use the fallback pattern.
