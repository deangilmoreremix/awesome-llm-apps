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

    root_dir = Path(__file__).resolve().parent.parent.parent
    full_source_path = root_dir / source_path
    if not full_source_path.exists():
        st.error(f"Source directory does not exist: {full_source_path}")
        return

    main_file = app.get("main_file")
    if main_file and (full_source_path / main_file).exists():
        pass  # use it
    else:
        main_file = None
        for file in possible_files:
            if (full_source_path / file).exists():
                main_file = file
                break

    if not main_file:
        st.error(f"Main file not found for app {app['name']} in {full_source_path}")
        return

    full_path = full_source_path / main_file

    run_command = f"cd {source_path} && streamlit run {main_file}"
    try:
        # Attempt to launch in new process (works locally)
        subprocess.Popen(['streamlit', 'run', str(full_path)], cwd=str(full_source_path))
        st.success(f"Launched {app['name']} in new window/tab")
    except Exception as e:
        # Fallback for hosted environments: show run command
        st.info(f"**Unable to launch automatically. Run {app['name']} locally with:**\n\n```\n{run_command}\n```")
    # Clear active app and go back to list
    from shared.session_state import clear_active_app
    clear_active_app()
    st.rerun()