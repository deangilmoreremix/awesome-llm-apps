from __future__ import annotations

import streamlit as st
from typing import Dict


def render_app_card(app: Dict[str, str]) -> bool:
    """
    Returns True when launch button is clicked.
    """
    with st.container(border=True):
        st.markdown(f"### {app['name']}")
        if app.get("badge"):
            st.caption(app["badge"])
        st.write(app["description"])
        st.caption(f"Status: {app['status']}")
        return st.button("Launch App", key=f"launch_{app['id']}", use_container_width=True)