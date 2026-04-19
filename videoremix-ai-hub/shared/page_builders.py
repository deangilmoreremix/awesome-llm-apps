from __future__ import annotations

from typing import Any

import streamlit as st

from shared.app_registry import get_all_tags, get_app_by_id, get_apps_by_hub
from shared.app_runner import run_app
from shared.constants import HUB_META
from shared.filters import filter_apps
from shared.session_state import clear_active_app, get_active_app, set_active_app
from shared.ui_components import render_app_card, render_empty_state, render_page_header


def render_filter_bar(apps: list[dict[str, Any]], key_prefix: str) -> tuple[str, list[str], list[str], bool]:
    available_tags = get_all_tags(apps)

    col1, col2, col3, col4 = st.columns([2.2, 1.4, 1.7, 1.1])

    with col1:
        query = st.text_input(
            "Search apps",
            key=f"{key_prefix}_search",
            placeholder="Search by name, description, tag, or status...",
        )

    with col2:
        statuses = st.multiselect(
            "Status",
            options=["ready", "advanced", "external", "blocked", "wip"],
            default=[],
            key=f"{key_prefix}_statuses",
        )

    with col3:
        tags = st.multiselect(
            "Tags",
            options=available_tags,
            default=[],
            key=f"{key_prefix}_tags",
        )

    with col4:
        featured_only = st.checkbox("Featured only", value=False, key=f"{key_prefix}_featured")

    return query, statuses, tags, featured_only


def render_app_grid(apps: list[dict[str, Any]], button_prefix: str) -> None:
    if not apps:
        render_empty_state("No apps matched your filters.")
        return

    cols = st.columns(3)
    for index, app in enumerate(apps):
        with cols[index % 3]:
            clicked = render_app_card(app, button_prefix=button_prefix)
            if clicked:
                set_active_app(app["id"])
                st.rerun()


def render_active_app_view(app: dict[str, Any]) -> None:
    top_left, top_right = st.columns([1, 6])

    with top_left:
        if st.button("← Back", use_container_width=True):
            clear_active_app()
            st.rerun()

    with top_right:
        st.subheader(app["name"])
        st.caption(f"{app['hub']} • {app['status']} • {app['source_path']}")

    st.divider()
    run_app(app["module_path"])


def render_hub_page(hub_name: str) -> None:
    meta = HUB_META[hub_name]
    apps = get_apps_by_hub(hub_name)

    render_page_header(hub_name, meta["description"], icon=meta["icon"])

    active_app_id = get_active_app()
    if active_app_id:
        active_app = get_app_by_id(active_app_id)
        if active_app and active_app["hub"] == hub_name:
            render_active_app_view(active_app)
            return

    query, statuses, tags, featured_only = render_filter_bar(apps, key_prefix=hub_name.lower().replace(" ", "_"))
    filtered_apps = filter_apps(
        apps,
        query=query,
        statuses=statuses,
        tags=tags,
        featured_only=featured_only,
    )

    ready_count = len([a for a in filtered_apps if a["status"] == "ready"])
    advanced_count = len([a for a in filtered_apps if a["status"] == "advanced"])
    featured_count = len([a for a in filtered_apps if a.get("featured")])

    c1, c2, c3 = st.columns(3)
    c1.metric("Visible Apps", len(filtered_apps))
    c2.metric("Ready", ready_count)
    c3.metric("Featured", featured_count if featured_count else 0)

    if advanced_count:
        st.caption(f"Advanced setup apps currently visible: {advanced_count}")

    st.divider()
    render_app_grid(filtered_apps, button_prefix=hub_name.lower().replace(" ", "_"))