from __future__ import annotations

import subprocess
from pathlib import Path

import streamlit as st

from shared.app_registry import get_app_by_module_path


def run_app(module_path: str) -> None:
    app = get_app_by_module_path(module_path)
    if not app:
        st.error(f"App not found for module_path: {module_path}")
        return

    source_path = app['source_path']
    # Try different possible main file names
    possible_files = [
        app['id'] + '.py',
        app['id'].replace('ai_', '') + '.py',
        app['id'].replace('ai_', '') + '_agent.py',
        app['id'] + '_agent.py',
        'app.py'  # fallback
    ]

    # Determine main file
    main_file = app.get("main_file")
    if not main_file:
        # Fallback to common patterns
        for file in possible_files:
            if file:  # simple check
                main_file = file
                break
        if not main_file:
            main_file = "app.py"  # default

    run_command = f"cd {source_path} && streamlit run {main_file}"

    deployed_url = app.get('deployed_url', '').strip()
    if deployed_url:
        # Open deployed URL in new tab
        st.markdown(f'<a href="{deployed_url}" target="_blank"><button style="background-color:#FF4B4B;color:white;border:none;padding:10px 20px;text-align:center;text-decoration:none;display:inline-block;font-size:16px;margin:4px 2px;cursor:pointer;border-radius:12px;">Launch {app["name"]}</button></a>', unsafe_allow_html=True)
        st.success(f"Opening {app['name']} in new tab")
    else:
        # Launch app (local execution)
        try:
            root_dir = Path(__file__).resolve().parent.parent.parent
            full_source_path = root_dir / source_path
            full_path = full_source_path / main_file
            subprocess.Popen(['streamlit', 'run', str(full_path)], cwd=str(full_source_path))
            st.success(f"✅ Launched {app['name']} in new window/tab!")
        except Exception as e:
            # Fallback: show run command with helpful message
            st.warning(f"❌ Could not launch automatically. Please run this command in your terminal:\n\n```\n{run_command}\n```")
            st.info("💡 Make sure you're running the hub locally and the repository is fully cloned")
    # Clear active app and go back to list
    from shared.session_state import clear_active_app
    clear_active_app()
    st.rerun()