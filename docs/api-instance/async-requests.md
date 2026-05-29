# Using await with Api Calls

In TBL, some `Api` methods return a response.  
You can use **`await`** to get that response **immediately** and continue logic in the same command.

This is useful when your next step depends on the result of an Api call.

## How await Works in TBL

When you use `await`:

- Execution pauses at that line
- The Api call finishes
- The response is returned
- Execution continues with the result

This allows **step-by-step logic** inside one command.

## Basic Example

Get bot information and use it right away:

```js
let me = await Api.getMe()

if (me.ok) {
  Api.sendMessage({
    text: "My bot id is " + me.result.id
  })
}
```

Here:

- `Api.getMe()` is called
- The result is stored in `me`
- The response is checked
- A message is sent using the returned data

## Another Example

Send a message and store the response:

```js
let sent = await Api.sendMessage({
  text: "Hello again!"
})
```

The `sent` variable now contains information about the message that was sent.

This is useful when you need:

- Message IDs
- Status confirmation
- Result-based logic

## When to Use await

Use `await` when:

- You need the Api response immediately
- Logic depends on the result
- You want everything in one command

If you don’t need the response, you can call `Api.xxx()` without `await`.

## Important Notes

- Only supported Api calls can be awaited
- Code still runs safely inside TBL
- Avoid unnecessary awaits to keep commands fast

## Summary

- `await` lets you get Api responses inline
- Results are stored in variables
- Logic stays simple and readable
- Best for sequential, result-based flows
