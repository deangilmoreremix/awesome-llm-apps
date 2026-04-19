from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT_DIR / "data" / "app_catalog.json"


@st.cache_data(show_spinner=False)
def load_catalog() -> list[dict[str, Any]]:
    if not CATALOG_PATH.exists():
        raise FileNotFoundError(f"Missing catalog file: {CATALOG_PATH}")

    with CATALOG_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("app_catalog.json must contain a list of app records.")

    normalized: list[dict[str, Any]] = []
    for item in data:
        record = {
            "id": item.get("id", "").strip(),
            "name": item.get("name", "").strip(),
            "hub": item.get("hub", "").strip(),
            "module_path": item.get("module_path", "").strip(),
            "source_path": item.get("source_path", "").strip(),
            "description": item.get("description", "").strip(),
            "status": item.get("status", "ready").strip().lower(),
            "tags": item.get("tags", []),
            "featured": bool(item.get("featured", False)),
        }
        normalized.append(record)
    return normalized


def get_all_apps() -> list[dict[str, Any]]:
    return load_catalog()


def get_apps_by_hub(hub_name: str) -> list[dict[str, Any]]:
    return [app for app in load_catalog() if app["hub"] == hub_name]


def get_app_by_id(app_id: str) -> dict[str, Any] | None:
    for app in load_catalog():
        if app["id"] == app_id:
            return app
    return None


def get_featured_apps(limit: int | None = None) -> list[dict[str, Any]]:
    featured = [app for app in load_catalog() if app.get("featured")]
    return featured[:limit] if limit else featured


def get_all_tags(apps: list[dict[str, Any]] | None = None) -> list[str]:
    source = apps if apps is not None else load_catalog()
    tags: set[str] = set()
    for app in source:
        for tag in app.get("tags", []):
            if isinstance(tag, str) and tag.strip():
                tags.add(tag.strip())
    return sorted(tags)