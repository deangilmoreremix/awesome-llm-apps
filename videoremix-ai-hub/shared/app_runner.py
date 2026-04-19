from __future__ import annotations

import importlib
import streamlit as st


def run_app(module_path: str) -> None:
    """
    Dynamically imports and runs an app module.
    Expected module layout:
        app_modules/<hub>/<tool>/app.py
    Expected callable:
        main()
    """
    try:
        full_module_path = f"app_modules.{module_path}"
        module = importlib.import_module(full_module_path)

        if hasattr(module, "main"):
            module.main()
        else:
            st.error(f"Module '{full_module_path}' does not expose a main() function.")
    except Exception as exc:
        st.error(f"Could not launch app: {module_path}")
        st.exception(exc)