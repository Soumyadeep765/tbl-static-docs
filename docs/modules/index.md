# modules Object

The **modules** object provides access to **preloaded utility libraries** inside TBL.

It allows you to perform common tasks such as data processing, validation, formatting, and other helper operations without importing or installing anything.

Modules are accessed using:

modules.moduleName.method()

All modules are sandboxed and safe to use within TBL.

## Notes

- `modules` is available globally
- No setup or imports are required
- Only approved libraries are exposed
- Designed for convenience and security
