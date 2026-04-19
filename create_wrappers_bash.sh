#!/bin/bash

echo "=== Creating instant_lab wrappers for all apps ==="

# Get all app directories
./find_apps.sh | while read app_dir; do
    # Clean app name for directory
    app_name=$(basename "$app_dir" | sed 's/[^a-zA-Z0-9_]/_/g' | sed 's/__*/_/g' | sed 's/^_//;s/_$//')
    wrapper_dir="app_modules/instant_lab/${app_name}"
    
    if [ -d "$wrapper_dir" ]; then
        echo "SKIP: $app_name (already exists)"
        continue
    fi
    
    echo "CREATE: $app_name from $app_dir"
    
    # Create directory structure
    mkdir -p "$wrapper_dir/app/.streamlit"
    
    # Find the main Python file
    main_script=""
    if [ -f "$app_dir/app.py" ]; then
        main_script="app.py"
    elif [ -f "$app_dir/main.py" ]; then
        main_script="main.py"
    elif [ -f "$app_dir/${app_name}.py" ]; then
        main_script="${app_name}.py"
    else
        # Find first Python file
        main_script=$(find "$app_dir" -maxdepth 1 -name "*.py" | head -1 | xargs basename 2>/dev/null)
    fi
    
    if [ -z "$main_script" ]; then
        echo "ERROR: No main script found for $app_name in $app_dir"
        continue
    fi
    
    echo "  Using main script: $main_script"
    
    # Create __init__.py
    cat > "$wrapper_dir/__init__.py" << INIT_EOF
"""
$app_name - Instant Lab App Module
Auto-generated wrapper for app.
"""

import sys
import os

# Add path to original agent
module_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(module_dir)))
agent_path = os.path.join(project_root, '$app_dir')
sys.path.insert(0, agent_path)

__all__ = ['main']
INIT_EOF
    
    # Create main.py
    cat > "$wrapper_dir/app/main.py" << MAIN_EOF
"""
Main entry point for $app_name - Instant Lab App
This module is loaded by the hosting platform to run the agent.
"""

import sys
import os

# Ensure proper path resolution
module_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(module_dir))))

# Add the original agent directory to path
agent_path = os.path.join(project_root, '$app_dir')


def main():
    """Entry point that runs the Streamlit application."""
    import subprocess
    
    # Get the agent script path
    agent_script = os.path.join(agent_path, '$main_script')
    
    # Run the Streamlit app
    subprocess.run(['streamlit', 'run', agent_script])


if __name__ == '__main__':
    main()
MAIN_EOF
    
    # Create config.toml
    cat > "$wrapper_dir/app/.streamlit/config.toml" << CONFIG_EOF
[theme]
primaryColor = "#4B8BBE"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
CONFIG_EOF
    
    echo "✓ Created wrapper for $app_name"
done

echo "=== Wrapper creation complete ==="
