from __future__ import annotations

import importlib

import streamlit as st


def run_app(module_path: str) -> None:
    try:
        full_module_path = f"app_modules.{module_path}"
        module = importlib.import_module(full_module_path)

        if not hasattr(module, "main"):
            st.error(f"Module '{full_module_path}' does not expose a main() function.")
            return

        module.main()
    except ModuleNotFoundError as exc:
        st.error("This app module has not been added yet.")
        st.caption(f"Missing module: {module_path}")
        st.exception(exc)
    except Exception as exc:
        st.error(f"Could not launch app: {module_path}")
        st.exception(exc)