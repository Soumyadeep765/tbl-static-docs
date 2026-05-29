## Using HTTP with Fallback Commands

TBL allows you to define **success** and **error fallback commands** when making HTTP requests.

These commands are executed automatically based on the result of the request.

If the **error command is missing**, the **success command will run instead**.

This makes HTTP workflows simple, safe, and predictable.

## Basic HTTP Request with Fallback Commands

You can attach `success` and `error` commands directly to an HTTP request.

Example:
```js
HTTP.get({
  url: "https://jsonplaceholder.typicode.com/todos/1",
  success: "onSuccess",
  error: "onError",
  tbl_options: { key: value }
})
```
### tbl_options

- `tbl_options` is optional
- Used to pass **custom data** to the next command
- Available directly as `tbl_options` in the success or error command

Example access:

tbl_options.key

## How Command Execution Works

- If the HTTP request succeeds:
  - The `success` command is executed
  - `options` contains the HTTP response
- If the HTTP request fails:
  - The `error` command is executed
  - `options` contains the HTTP error
- If the `error` command is **not defined**:
  - The `success` command will be executed instead

!!! note
    The error command runs only on **real HTTP failures**  
    such as invalid URLs, network errors, or server errors (e.g. 500).

## Example Success Command

The success command receives HTTP response data.

Example:
```js
/*command: onSuccess*/
Bot.sendMessage("Fetched title: " + content)
```
On success, the following variables are available:

- `http_response`
- `response`
- `content` (raw response body string)
- `headers`
- `cookies`

## Example Error Command

The error command receives HTTP error details.

Example:
```js
/*command: onError*/
Bot.sendMessage("HTTP request failed: " + error.status)
```
On error, the following are available:

- `error`
- `options` (error-related response data)
- `tbl_options` (if provided)

## Available Response Data

On successful requests, detailed response information is available.

See full documentation here: [HTTP Response]

[HTTP Response]: ../globals/http_response.md

## Important Notes

!!! tip
    Use fallback commands to keep HTTP logic separate from message logic.

!!! warning
    HTTP fallback commands do not catch TBL runtime errors.
    Those must be handled using the `!` command.

This approach makes external API integration clean, modular, and easy to debug.
