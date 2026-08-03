# TeleBotHost TBL Documentation

Official documentation for [TeleBotHost](https://telebothost.com), built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

**Live site:** [https://docs.telebothost.com](https://docs.telebothost.com)

## Local development

```bash
pip install -r requirements.txt
mkdocs serve
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to preview changes.

## SEO system

Per-page meta tags (description, keywords, Open Graph, Twitter Card, JSON-LD) are managed in:

- `hooks/seo_pages.yaml` — edit descriptions and keywords per page
- `hooks/seo.py` — MkDocs hook that injects meta and builds `sitemap.xml`

After deploy, verify:

- `https://docs.telebothost.com/sitemap.xml`
- `https://docs.telebothost.com/robots.txt`
- `https://docs.telebothost.com/llms.txt` — plain-text URL index for AI agents (from `docs/llms.txt`)
- `https://docs.telebothost.com/for-agents/` — intent → page map for agents

## AI / agent docs

| File | Served as | Purpose |
|------|-----------|---------|
| `docs/llms.txt` | `/llms.txt` | Machine-readable URL list (MkDocs copies non-md files as-is) |
| `docs/for-agents.md` | `/for-agents/` | Human + agent “what is what” router |

Keep both in sync when you add major doc sections. Agents should open **one** page per task — not crawl the whole site.

To add SEO for a new page, add an entry under `pages:` in `hooks/seo_pages.yaml` using the docs-relative path (e.g. `api-instance/new-page.md`).
