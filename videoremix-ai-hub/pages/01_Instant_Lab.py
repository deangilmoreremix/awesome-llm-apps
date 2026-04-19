import streamlit as st
from shared.app_registry import get_apps_by_hub
from shared.app_runner import run_app
from shared.ui_components import render_app_card


st.title("⚡ Instant Lab")
st.write("Quick-launch AI tools that are fast to use and easy to test.")

apps = get_apps_by_hub("Instant Lab")

selected_app_id = st.session_state.get("selected_instant_lab_app")

if selected_app_id:
    current_app = next((app for app in apps if app["id"] == selected_app_id), None)
    if current_app:
        col1, col2 = st.columns([1, 5])
        with col1:
            if st.button("← Back to Lab", use_container_width=True):
                st.session_state["selected_instant_lab_app"] = None
                st.rerun()
        with col2:
            st.subheader(current_app["name"])

        run_app(current_app["path"])
else:
    cols = st.columns(3)

    for i, app in enumerate(apps):
        with cols[i % 3]:
            clicked = render_app_card(app)
            if clicked:
                st.session_state["selected_instant_lab_app"] = app["id"]
                st.rerun()