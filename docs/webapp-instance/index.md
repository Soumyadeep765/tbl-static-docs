# Webapp Instance

The **Webapp instance** is used to generate clean and global URLs for your bot web integrations, such as dashboards, pages, and lightweight APIs.

Unlike **Webhook**, Webapp URLs are **not cryptographically signed**, so they are ideal for public or embed-style resources.

!!! info "Public URL Behavior"
    **Webapp URLs** are public and do not contain user authentication data.
    Use them for pages that do not require secure user verification.

## When to Use

Use the `Webapp` class when you need static or semi-dynamic links for:

- Landing pages or info dashboards
- Public web components or previews
- Lightweight APIs or micro webviews
- Embedded pages that do not require signed user context

!!! warning "Security Note"
    Webapp URLs are public and are not signed.
    For sensitive or user-specific actions, use **Webhook** URLs.
