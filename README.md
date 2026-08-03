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
| `docs/llms.txt` | `/llms.txt` | **Complete** machine-readable URL list (every page + subpath) |
| `docs/for-agents.md` | `/for-agents/` | What-is-what + full section/subpath map |

Regenerate the complete URL list after adding/removing docs pages:

```bash
node scripts/generate_llms_txt.js
# or: python scripts/generate_llms_txt.py
```

Agents should open **one** page per task — `llms.txt` lists everything so they can find the right URL, not so they fetch all of them.

To add SEO for a new page, add an entry under `pages:` in `hooks/seo_pages.yaml` using the docs-relative path (e.g. `api-instance/new-page.md`).
