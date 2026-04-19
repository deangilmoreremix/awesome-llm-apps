from __future__ import annotations

from typing import Any

import streamlit as st

from shared.constants import HUB_META, STATUS_META


def render_css() -> None:
    st.markdown(
        """
        <style>
        .hub-hero {
            padding: 1.1rem 1.2rem;
            border: 1px solid rgba(255,255,255,0.10);
            border-radius: 18px;
            background: linear-gradient(135deg, rgba(34,34,34,0.85), rgba(18,18,18,0.95));
            margin-bottom: 1rem;
        }
        .hub-subtle {
            color: rgba(255,255,255,0.75);
            font-size: 0.95rem;
        }
        .stat-chip {
            display: inline-block;
            padding: 0.25rem 0.55rem;
            border-radius: 999px;
            border: 1px solid rgba(255,255,255,0.12);
            margin-right: 0.35rem;
            margin-bottom: 0.35rem;
            font-size: 0.8rem;
        }
        .card-title {
            font-weight: 700;
            font-size: 1.05rem;
            margin-bottom: 0.25rem;
        }
        .card-body {
            min-height: 68px;
            color: rgba(255,255,255,0.78);
            font-size: 0.93rem;
        }
        .section-divider {
            margin-top: 0.5rem;
            margin-bottom: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_page_header(title: str, description: str, icon: str = "🚀") -> None:
    st.markdown(
        f"""
        <div class="hub-hero">
            <div style="font-size:1.8rem; font-weight:800;">{icon} {title}</div>
            <div class="hub-subtle">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_status_badge(status: str) -> str:
    meta = STATUS_META.get(status, {"emoji": "•", "label": status.title()})
    return f"{meta['emoji']} {meta['label']}"


def render_tag_chips(tags: list[str]) -> None:
    if not tags:
        return
    chips = "".join([f"<span class='stat-chip'>{tag}</span>" for tag in tags[:5]])
    st.markdown(chips, unsafe_allow_html=True)


def render_app_card(app: dict[str, Any], button_prefix: str = "launch") -> bool:
    with st.container(border=True):
        st.markdown(f"<div class='card-title'>{app['name']}</div>", unsafe_allow_html=True)

        sub_bits = [render_status_badge(app.get("status", "ready"))]
        if app.get("featured"):
            sub_bits.append("⭐ Featured")
        st.caption(" • ".join(sub_bits))

        st.markdown(
            f"<div class='card-body'>{app.get('description', '')}</div>",
            unsafe_allow_html=True,
        )
        render_tag_chips(app.get("tags", []))
        return st.button(
            "Launch App",
            key=f"{button_prefix}_{app['id']}",
            use_container_width=True,
        )


def render_hub_summary_cards(hub_counts: list[tuple[str, int]]) -> None:
    cols = st.columns(4)
    for index, (hub_name, count) in enumerate(hub_counts):
        meta = HUB_META.get(hub_name, {})
        with cols[index % 4]:
            with st.container(border=True):
                st.markdown(f"### {meta.get('icon', '📦')} {hub_name}")
                st.write(meta.get("description", ""))
                st.caption(f"{count} apps")


def render_empty_state(message: str) -> None:
    with st.container(border=True):
        st.info(message)