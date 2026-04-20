from __future__ import annotations

import streamlit as st


def init_session_state() -> None:
    defaults = {
        "active_app_id": None,
        "global_search": "",
        "selected_statuses": [],
        "selected_tags": [],
        "show_featured_only": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def set_active_app(app_id: str | None) -> None:
    st.session_state["active_app_id"] = app_id


def get_active_app() -> str | None:
    return st.session_state.get("active_app_id")


def clear_active_app() -> None:
    st.session_state["active_app_id"] = None