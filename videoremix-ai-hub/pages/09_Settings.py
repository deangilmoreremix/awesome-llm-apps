import streamlit as st

from shared.app_registry import get_all_apps
from shared.constants import STATUS_META
from shared.session_state import init_session_state
from shared.ui_components import render_css, render_page_header

init_session_state()
render_css()

apps = get_all_apps()

render_page_header(
    "Settings",
    "Review app totals, setup guidance, and Streamlit secret requirements.",
    icon="⚙️",
)

status_counts = {}
for app in apps:
    status = app["status"]
    status_counts[status] = status_counts.get(status, 0) + 1

cols = st.columns(max(1, len(status_counts)))
for idx, (status, count) in enumerate(sorted(status_counts.items())):
    meta = STATUS_META.get(status, {"emoji": "•", "label": status.title()})
    with cols[idx]:
        st.metric(f"{meta['emoji']} {meta['label']}", count)

st.divider()
st.subheader("Recommended secrets")

st.code(
    """
# .streamlit/secrets.toml

OPENAI_API_KEY = "your-openai-key"
GOOGLE_API_KEY = "your-google-key"
ANTHROPIC_API_KEY = "your-anthropic-key"
SERPAPI_API_KEY = "your-serpapi-key"
GITHUB_TOKEN = "your-github-token"
NOTION_TOKEN = "your-notion-token"
""".strip(),
    language="toml",
)

st.divider()
st.subheader("Setup notes")
st.write("Use 'ready' for modules that can run now.")
st.write("Use 'advanced' for modules that need extra services, packages, or local setup.")
st.write("Use 'external' for apps you want to expose in the hub before fully embedding them.")