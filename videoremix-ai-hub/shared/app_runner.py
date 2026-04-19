from __future__ import annotations

import importlib

import streamlit as st

from shared.app_registry import get_app_by_module_path


def run_app(module_path: str) -> None:
    try:
        full_module_path = f"app_modules.{module_path}"
        module = importlib.import_module(full_module_path)

        if not hasattr(module, "main"):
            st.error(f"Module '{full_module_path}' does not expose a main() function.")
            return

        module.main()
    except ModuleNotFoundError as exc:
        # Show a placeholder UI for unembedded apps
        app = get_app_by_module_path(module_path)
        if app:
            st.write(f"## {app['name']}")
            st.info("🚧 This app is registered but the module is not yet implemented.")
            st.caption(f"Source: `{app.get('source_path','unknown')}`")
            st.write(f"**Status:** {app.get('status','advanced')}")
            if app.get("external"):
                st.warning("This app is marked as external and may be hosted elsewhere.")
            st.write(
                "The implementation will be placed in `app_modules/{}` with a `main()` function.".format(
                    module_path.replace(".", "/")
                )
            )
        else:
            st.error(f"Module not found: {module_path}")
            st.exception(exc)
    except Exception as exc:
        st.error(f"Could not launch app: {module_path}")
        st.exception(exc)