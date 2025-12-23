# The `tbl_options` Variable

In TBL, `tbl_options` contains **exactly what you pass to a callback command**.

It is not wrapped or modified.

## How `tbl_options` Is Used

The `tbl_options` variable is used when:

- A command is executed as a callback
- A value is explicitly passed for the next command

It is **not available** in normal command execution.

## Example Value

If this value is passed:

\`\`\`json
{
  "key": "value"
}
\`\`\`

Then `tbl_options` will be that exact value.

You can access it directly:

tbl_options.key

## Notes

- `tbl_options` exists only in callback commands
- It can be any type (object, string, number, etc.)
- If nothing is passed, it will be `undefined`