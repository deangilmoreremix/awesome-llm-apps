from __future__ import annotations

from typing import Any


def _matches_text(app: dict[str, Any], query: str) -> bool:
    if not query.strip():
        return True

    q = query.strip().lower()
    haystack = " ".join(
        [
            app.get("name", ""),
            app.get("description", ""),
            app.get("hub", ""),
            " ".join(app.get("tags", [])),
            app.get("status", ""),
        ]
    ).lower()
    return q in haystack


def _matches_status(app: dict[str, Any], statuses: list[str]) -> bool:
    if not statuses:
        return True
    return app.get("status", "") in statuses


def _matches_tags(app: dict[str, Any], tags: list[str]) -> bool:
    if not tags:
        return True
    app_tags = set(app.get("tags", []))
    return any(tag in app_tags for tag in tags)


def _matches_featured(app: dict[str, Any], featured_only: bool) -> bool:
    if not featured_only:
        return True
    return bool(app.get("featured", False))


def filter_apps(
    apps: list[dict[str, Any]],
    query: str = "",
    statuses: list[str] | None = None,
    tags: list[str] | None = None,
    featured_only: bool = False,
) -> list[dict[str, Any]]:
    statuses = statuses or []
    tags = tags or []

    filtered = []
    for app in apps:
        if not _matches_text(app, query):
            continue
        if not _matches_status(app, statuses):
            continue
        if not _matches_tags(app, tags):
            continue
        if not _matches_featured(app, featured_only):
            continue
        filtered.append(app)
    return filtered