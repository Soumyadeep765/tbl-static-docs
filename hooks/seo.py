"""
MkDocs hook: per-page SEO meta tags, JSON-LD, and enhanced sitemap.xml.

Edit unique descriptions and keywords in hooks/seo_pages.yaml.
"""

from __future__ import annotations

import html
import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from xml.dom import minidom

import yaml

HOOK_DIR = Path(__file__).parent
SEO_FILE = HOOK_DIR / "seo_pages.yaml"
SITE_NAME_SUFFIX = " | TBL Docs"

_seo_config: dict[str, Any] | None = None


def _load_config() -> dict[str, Any]:
    global _seo_config
    if _seo_config is None:
        with SEO_FILE.open(encoding="utf-8") as fh:
            _seo_config = yaml.safe_load(fh) or {}
    return _seo_config


def _page_key(page) -> str:
    return page.file.src_path.replace("\\", "/")


def _get_page_seo(page) -> dict[str, Any]:
    config = _load_config()
    defaults = config.get("defaults", {})
    pages = config.get("pages", {})
    key = _page_key(page)

    if key in pages:
        return {**defaults, **pages[key]}

    title = page.title or "TBL Documentation"
    return {
        **defaults,
        "description": (
            f"{title} — reference for Tele Bot Language (TBL) on TeleBotHost. "
            "Build and host Telegram bots without managing servers."
        ),
        "keywords": f"TBL, TeleBotHost, Telegram bot, {title}, Tele Bot Language",
    }


def _canonical_url(page, config) -> str:
    base = (config.site_url or "").rstrip("/")
    path = page.url or ""
    if not path.startswith("/"):
        path = "/" + path
    return f"{base}{path}"


def _meta_title(page, seo: dict[str, Any]) -> str:
    if seo.get("title"):
        return seo["title"]
    title = page.title or "TBL Documentation"
    return f"{title}{SITE_NAME_SUFFIX}"


def _meta_tag(attrs: dict[str, str]) -> str:
    parts = " ".join(f'{k}="{html.escape(v, quote=True)}"' for k, v in attrs.items())
    return f"<meta {parts}>"


def _build_head_injection(page, config) -> str:
    seo = _get_page_seo(page)
    description = seo.get("description", "")
    keywords = seo.get("keywords", "")
    meta_title = _meta_title(page, seo)
    canonical = _canonical_url(page, config)

    tags = [
        _meta_tag({"name": "description", "content": description}),
        _meta_tag({"name": "keywords", "content": keywords}),
        _meta_tag({"name": "author", "content": config.site_author or "TeleBotHost"}),
        _meta_tag(
            {
                "name": "robots",
                "content": seo.get(
                    "robots",
                    "index, follow, max-snippet:-1, max-image-preview:large",
                ),
            }
        ),
        _meta_tag({"property": "og:type", "content": seo.get("og_type", "article")}),
        _meta_tag({"property": "og:site_name", "content": "TeleBotHost Docs"}),
        _meta_tag({"property": "og:title", "content": meta_title}),
        _meta_tag({"property": "og:description", "content": description}),
        _meta_tag({"property": "og:url", "content": canonical}),
        _meta_tag({"property": "og:locale", "content": "en_US"}),
        _meta_tag({"name": "twitter:card", "content": seo.get("twitter_card", "summary_large_image")}),
        _meta_tag({"name": "twitter:title", "content": meta_title}),
        _meta_tag({"name": "twitter:description", "content": description}),
    ]

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "TechArticle",
                "headline": page.title or "TBL Documentation",
                "description": description,
                "keywords": keywords,
                "url": canonical,
                "author": {"@type": "Organization", "name": config.site_author or "TeleBotHost"},
                "publisher": {
                    "@type": "Organization",
                    "name": "TeleBotHost",
                    "url": "https://telebothost.com",
                },
                "isPartOf": {
                    "@type": "WebSite",
                    "name": config.site_name or "TBL Documentation",
                    "url": (config.site_url or "").rstrip("/"),
                },
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": (config.site_url or "").rstrip("/") + "/",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": page.title or "Documentation",
                        "item": canonical,
                    },
                ],
            },
        ],
    }

    script = (
        f'<script type="application/ld+json">'
        f"{json.dumps(json_ld, ensure_ascii=False)}"
        f"</script>"
    )

    return "\n".join(tags) + "\n" + script + "\n"


def on_post_page(html, page, config, **kwargs):
    """Replace generic meta description and inject page-specific SEO tags."""
    injection = _build_head_injection(page, config)

    # Remove default description / duplicate og tags Material may have added
    html = re.sub(r'<meta name=description content="[^"]*"\s*>', "", html, count=1)
    html = re.sub(r'<meta property="og:description" content="[^"]*"\s*>', "", html)
    html = re.sub(r'<meta property="og:title" content="[^"]*"\s*>', "", html)
    html = re.sub(r'<meta property="og:url" content="[^"]*"\s*>', "", html)

    marker = "</head>"
    if marker in html:
        return html.replace(marker, injection + marker, 1)
    return html


def _prettify_xml(element: ET.Element) -> str:
    rough = ET.tostring(element, encoding="unicode")
    return minidom.parseString(rough).toprettyxml(indent="  ")


def _md_to_url(src_key: str) -> str:
    if src_key == "index.md":
        return "/"
    path = src_key
    if path.endswith("/index.md"):
        path = path[: -len("index.md")]
    elif path.endswith(".md"):
        path = path[: -len(".md")]
    if not path.endswith("/"):
        path = path + "/"
    if not path.startswith("/"):
        path = "/" + path
    return path


def on_post_build(config, **kwargs):
    """Generate sitemap.xml with per-page priority and changefreq."""
    if not config.site_url:
        return

    site_dir = Path(config.site_dir)
    docs_dir = Path(config.docs_dir)
    config_data = _load_config()
    defaults = config_data.get("defaults", {})
    pages_seo = config_data.get("pages", {})
    base_url = config.site_url.rstrip("/")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    seen_urls: set[str] = set()

    for md_file in sorted(docs_dir.rglob("*.md")):
        src_key = md_file.relative_to(docs_dir).as_posix()
        url_path = _md_to_url(src_key)
        page_url = f"{base_url}{url_path if url_path != '/' else '/'}"
        if page_url in seen_urls:
            continue
        seen_urls.add(page_url)

        seo = {**defaults, **pages_seo.get(src_key, {})}
        url_el = ET.SubElement(urlset, "url")
        ET.SubElement(url_el, "loc").text = page_url
        ET.SubElement(url_el, "lastmod").text = today
        ET.SubElement(url_el, "changefreq").text = seo.get(
            "changefreq", defaults.get("changefreq", "monthly")
        )
        ET.SubElement(url_el, "priority").text = str(
            seo.get("priority", defaults.get("priority", 0.65))
        )

    (site_dir / "sitemap.xml").write_text(_prettify_xml(urlset), encoding="utf-8")

    sitemap_index = ET.Element("sitemapindex", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    entry = ET.SubElement(sitemap_index, "sitemap")
    ET.SubElement(entry, "loc").text = f"{base_url}/sitemap.xml"
    ET.SubElement(entry, "lastmod").text = today
    (site_dir / "sitemap_index.xml").write_text(_prettify_xml(sitemap_index), encoding="utf-8")
