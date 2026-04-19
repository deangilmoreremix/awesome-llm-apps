from __future__ import annotations

from typing import Dict, List, Optional


APP_CATALOG: List[Dict[str, str]] = [
    {
        "id": "ai_meme_generator",
        "name": "AI Meme Generator",
        "hub": "Instant Lab",
        "path": "instant_lab.ai_meme_generator.app",
        "description": "Generate meme concepts and captions.",
        "status": "ready",
        "badge": "Popular",
    },
    {
        "id": "ai_blog_to_podcast",
        "name": "AI Blog to Podcast",
        "hub": "Instant Lab",
        "path": "instant_lab.ai_blog_to_podcast.app",
        "description": "Turn blog content into podcast-style output.",
        "status": "ready",
        "badge": "New",
    },
    {
        "id": "ai_travel_agent",
        "name": "AI Travel Agent",
        "hub": "Instant Lab",
        "path": "instant_lab.ai_travel_agent.app",
        "description": "Plan trips and generate travel suggestions.",
        "status": "ready",
        "badge": "Fast",
    },
]


def get_apps_by_hub(hub_name: str) -> List[Dict[str, str]]:
    return [app for app in APP_CATALOG if app["hub"] == hub_name]


def get_app_by_id(app_id: str) -> Optional[Dict[str, str]]:
    for app in APP_CATALOG:
        if app["id"] == app_id:
            return app
    return None