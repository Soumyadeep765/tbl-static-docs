## Dynamic Methods in Api.xxx

Sometimes a specific **Telegram Bot API method** may not yet exist as a built-in method inside TBL’s `Api` instance.

In such cases, you don’t need to wait for a platform update.

TBL allows you to call **any official Telegram Bot API method dynamically** using:

Api.call("methodName", { ...parameters })

## Why Dynamic Methods Exist

Telegram frequently adds new API methods and features.

Dynamic methods ensure that:

- You can use new Telegram features immediately
- You are not blocked by missing built-in methods
- TBL stays compatible with the latest Telegram API

As long as Telegram supports a method, you can use it.

## Basic Usage

Calling a Telegram method dynamically:

```js
Api.call("methodName", {
  /* parameters */
})
```

!!! note
    `"methodName"` must exactly match the official Telegram API method name.

## Example: Calling getChat Dynamically

Suppose `getChat` is not available as a built-in method.

You can still call it like this:

```js
Api.call("getChat", {
  chat_id: 4444443444
})
```

## How It Works

- `"getChat"` is the official Telegram method name
- The second argument is an object of parameters
- TBL sends the request directly to Telegram
- Telegram returns the response

The response behaves exactly like any normal Api call.

!!! tip
    If a built-in Api method exists, always prefer using it first.  
    Use `Api.call()` only when the method is missing.

## Using the Response

Dynamic method responses:

- Can be awaited
- Contain `ok` and `result`
- Can be used in further logic

!!! info
    Dynamic calls fully support async behavior and error handling.

## Important Warning

!!! warning
    TBL does not validate parameters for dynamic methods.  
    Make sure parameters exactly match Telegram’s API specification.

Incorrect parameters may result in Telegram API errors.

## Official Telegram Reference

To see all available Telegram methods and their parameters, refer to the official documentation:

https://core.telegram.org/bots/api

Any method listed there can be used with `Api.call()`.

## Summary

- `Api.call()` enables dynamic Telegram API access
- Works with any official Telegram method
- Keeps bots future-proof
- Best used only when built-in methods are unavailable