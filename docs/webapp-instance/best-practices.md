# Webapp Best Practices

Follow these practices when building public webapp endpoints:

- Use `Webapp` only for public or semi-public resources.
- Use `params` for readable URL parameters (example: `?ref=home&lang=en`).
- Use `options` for app-level configuration.
- Keep sensitive values out of URL query strings.
- For secure or user-specific links, use **Webhook**.

!!! warning "Security Reminder"
    Webapp URLs are public and are not cryptographically signed.
    Use **Webhook** for any sensitive or authenticated flow.
