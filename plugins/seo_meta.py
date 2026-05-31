"""Inject per-page SEO metadata from seo/pages.yaml into MkDocs pages."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin


class SeoMetaPlugin(BasePlugin):
    config_scheme = (
        ("config_file", config_options.Type(str, default="seo/pages.yaml")),
        ("site_name_suffix", config_options.Type(str, default=" | TeleBotHost Docs")),
    )

    def __init__(self) -> None:
        self._seo: dict[str, dict[str, Any]] = {}

    def on_config(self, config, **kwargs):
        config_path = Path(config["docs_dir"]).parent / self.config["config_file"]
        if config_path.is_file():
            with config_path.open(encoding="utf-8") as handle:
                loaded = yaml.safe_load(handle) or {}
            self._seo = {str(key): value for key, value in loaded.items()}
        else:
            log = getattr(self, "log", None)
            if log:
                log.warning(f"SEO config not found: {config_path}")
        return config

    def on_nav(self, nav, config, **kwargs):
        suffix = self.config["site_name_suffix"]
        site_name = config["site_name"]

        for page in nav.pages:
            src = page.file.src_path.replace("\\", "/")
            entry = self._seo.get(src, {})

            if entry.get("title"):
                page.title = entry["title"]
            elif entry.get("append_site_name", True):
                page.title = f"{page.title}{suffix}"

            page.meta.setdefault("description", entry.get("description", _fallback_description(page, site_name)))
            page.meta["keywords"] = entry.get("keywords", _fallback_keywords(page))
            page.meta["robots"] = entry.get("robots", "index, follow")

            if entry.get("og_type"):
                page.meta["og_type"] = entry["og_type"]
            if entry.get("og_image"):
                page.meta["og_image"] = entry["og_image"]

            page.meta["priority"] = entry.get("priority", _default_priority(src))
            page.meta["changefreq"] = entry.get("changefreq", _default_changefreq(src))

            if entry.get("canonical"):
                page.meta["canonical"] = entry["canonical"]

        return nav


def _fallback_description(page, site_name: str) -> str:
    title = page.title.split(" | ")[0]
    return (
        f"{title} — official {site_name} reference for TeleBotHost TBL "
        f"(Tele Bot Language) Telegram bot development."
    )[:160]


def _fallback_keywords(page) -> str:
    title = page.title.lower()
    base = "TeleBotHost, TBL, Telegram bot, Tele Bot Language, bot documentation"
    return f"{title}, {base}"


def _default_priority(src: str) -> float:
    if src == "index.md":
        return 1.0
    if src.endswith("/index.md") or src in {
        "getting-started.md",
        "about-tbl.md",
        "tutorials/index.md",
        "guides/bot-vs-api.md",
        "api-instance/index.md",
        "bot-instance/index.md",
    }:
        return 0.9
    if "getting-started-with-tbl/" in src or src.startswith("guides/"):
        return 0.85
    return 0.7


def _default_changefreq(src: str) -> str:
    if src == "index.md":
        return "daily"
    if "modules/" in src or "libs/" in src:
        return "monthly"
    return "weekly"
