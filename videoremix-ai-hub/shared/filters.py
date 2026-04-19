from __future__ import annotations

from typing import List, Dict


def filter_apps_by_search(apps: List[Dict[str, str]], search_term: str) -> List[Dict[str, str]]:
    """
    Filter apps based on search term matching name, description, or hub.
    """
    if not search_term:
        return apps
    search_lower = search_term.lower()
    return [
        app for app in apps
        if search_lower in app["name"].lower()
        or search_lower in app["description"].lower()
        or search_lower in app["hub"].lower()
    ]