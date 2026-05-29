## Using the HTTP Instance

The HTTP instance allows your bot to make **external API requests**.

You can call any HTTP method using:

`HTTP.method(...)`

All common HTTP methods are supported, such as **GET**, **POST**, **PUT**, **PATCH**, and **DELETE**.

## Simple Request

The simplest form sends a request using only a URL.

Example:
```js
//Pass url as String 
HTTP.get("https://example.com")
```

## Using await to Get Response Data

To access the response data, use `await`.

Example:
```js
let res = await HTTP.get("https://example.com")
```
The returned value contains full information about the HTTP response.

!!! tip
    Use `await` when you need to read the response body, status, or headers.

## Flexible Request Options

For more control, you can pass an options object.

Example:
```js
HTTP.get({
  url: "https://example.com",
  body: null,
  headers: {
    Authorization: "Bearer TOKEN"
  },
  params: {key: 1},
  timeout: 5000, //max 15s/15,000ms
  redirect: true,
  maxRedirect: 3
})

//Or 
HTTP.get("https://example.com", { options }) 
```


### Available Options

- `url` – Request URL  
- `body` – Request body (used in POST, PUT, etc.)  
- `headers` – Custom request headers  
- `timeout` – Request timeout in milliseconds  
- `redirect` – Enable or disable redirects  
- `maxRedirect` – Maximum redirect count (up to 3)

!!! note
    Redirects are limited to avoid infinite loops.

## Demo HTTP Response

Example response object returned by an HTTP request:

```json
{
  "ok": true,
  "status": 200,
  "statusText": "",
  "content": "OK",
  "data": "OK",
  "isJson": false,
  "headers": {
    "server": "nginx/1.24.0 (Ubuntu)",
    "date": "Mon, 22 Dec 2025 17:03:56 GMT",
    "content-type": "text/html; charset=utf-8",
    "content-length": "2",
    "connection": "keep-alive",
    "x-powered-by": "Express",
    "etag": "W/\"2-nOO9QiTIwXgNtWtBJezz8kv3SLc\""
  },
  "cookies": [],
  "url": "https://example.com",
  "redirected": false,
  "redirectCount": 0
}
```

## Understanding the Response

- `ok` – Whether the request succeeded  
- `status` – HTTP status code  
- `content` – Raw response body (string)  
- `data` – Parsed data (if JSON)  
- `headers` – Response headers  
- `cookies` – Cookies returned by the server  

!!! info
    When `isJson` is true, `data` contains the parsed JSON response.

## Learn More

For a full breakdown of response fields, see : [HTTP Response]

## Important Notes

!!! warning
    External API failures do not crash your bot.
    Always check `res.ok` before using the response data.

The HTTP instance is best used for **external integrations**, **data fetching**, and **service communication**.

[HTTP Response]: ../globals/http_response.md#the-response-variable