import streamlit as st

from shared.app_registry import get_all_apps, get_featured_apps
from shared.constants import HUB_META, HUB_ORDER
from shared.filters import filter_apps
from shared.session_state import init_session_state
from shared.ui_components import (
    render_app_card,
    render_css,
    render_empty_state,
    render_hub_summary_cards,
    render_page_header,
)

init_session_state()
render_css()

all_apps = get_all_apps()
featured_apps = get_featured_apps(limit=8)

render_page_header(
    "VideoRemix AI Hub",
    "Launch, search, and organize all of your AI apps from one Streamlit dashboard.",
    icon="🚀",
)

left, right = st.columns([2.2, 1])

with left:
    global_search = st.text_input(
        "Search everything",
        value=st.session_state.get("global_search", ""),
        placeholder="Search by app name, description, hub, or tag...",
    )
    st.session_state["global_search"] = global_search

with right:
    show_featured_only = st.checkbox(
        "Show featured only",
        value=st.session_state.get("show_featured_only", False),
    )
    st.session_state["show_featured_only"] = show_featured_only

hub_counts = []
for hub_name in HUB_ORDER:
    hub_count = len([app for app in all_apps if app["hub"] == hub_name])
    hub_counts.append((hub_name, hub_count))

render_hub_summary_cards(hub_counts)

st.divider()
st.subheader("Featured Apps")

if featured_apps:
    featured_cols = st.columns(4)
    for idx, app in enumerate(featured_apps):
        with featured_cols[idx % 4]:
            render_app_card(app, button_prefix="home_featured")
else:
    render_empty_state("No featured apps have been marked yet.")

st.divider()
st.subheader("Browse by Hub")

for hub_name in HUB_ORDER:
    hub_apps = [app for app in all_apps if app["hub"] == hub_name]
    filtered = filter_apps(
        hub_apps,
        query=global_search,
        featured_only=show_featured_only,
    )

    with st.container(border=True):
        meta = HUB_META[hub_name]
        st.markdown(f"### {meta['icon']} {hub_name}")
        st.write(meta["description"])
        st.caption(f"{len(filtered)} of {len(hub_apps)} apps visible")

        if not filtered:
            st.caption("No apps matched the current search.")
            continue

        preview_cols = st.columns(3)
        for idx, app in enumerate(filtered[:3]):
            with preview_cols[idx % 3]:
                render_app_card(app, button_prefix=f"home_{hub_name.lower().replace(' ', '_')}")