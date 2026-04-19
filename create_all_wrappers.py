#!/usr/bin/env python3

import os
import sys

def find_main_script(app_dir):
    """Find the main Python script in an app directory."""
    candidates = ['app.py', 'main.py']
    
    # Check for common main files
    for candidate in candidates:
        if os.path.isfile(os.path.join(app_dir, candidate)):
            return candidate
    
    # Check for file with same name as directory
    dir_name = os.path.basename(app_dir)
    script_name = f"{dir_name}.py"
    if os.path.isfile(os.path.join(app_dir, script_name)):
        return script_name
    
    # Find first Python file
    for file in os.listdir(app_dir):
        if file.endswith('.py'):
            return file
    
    return None

def create_wrapper(app_dir):
    """Create instant_lab wrapper for an app directory."""
    app_name = os.path.basename(app_dir).replace('-', '_').replace(' ', '_')
    wrapper_dir = f"app_modules/instant_lab/{app_name}"
    
    if os.path.exists(wrapper_dir):
        print(f"SKIP: {app_name} (already exists)")
        return
    
    print(f"CREATE: {app_name} from {app_dir}")
    
    # Create directory structure
    os.makedirs(f"{wrapper_dir}/app/.streamlit", exist_ok=True)
    
    # Find main script
    main_script = find_main_script(app_dir)
    if not main_script:
        print(f"ERROR: No main script found for {app_name}")
        return
    
    # Create __init__.py
    with open(f"{wrapper_dir}/__init__.py", 'w') as f:
        f.write(f'''"""
{app_name} - Instant Lab App Module
Auto-generated wrapper for app.
"""

import sys
import os

# Add path to original agent
module_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(module_dir)))
agent_path = os.path.join(project_root, '{app_dir}')
sys.path.insert(0, agent_path)

__all__ = ['main']
''')
    
    # Create main.py
    with open(f"{wrapper_dir}/app/main.py", 'w') as f:
        f.write(f'''"""
Main entry point for {app_name} - Instant Lab App
This module is loaded by the hosting platform to run the agent.
"""

import sys
import os

# Ensure proper path resolution
module_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(module_dir))))

# Add the original agent directory to path
agent_path = os.path.join(project_root, '{app_dir}')
sys.path.insert(0, agent_path)


def main():
    """Entry point that runs the Streamlit application."""
    import subprocess
    
    # Get the agent script path
    agent_script = os.path.join(agent_path, '{main_script}')
    
    # Run the Streamlit app
    subprocess.run(['streamlit', 'run', agent_script])


if __name__ == '__main__':
    main()
''')
    
    # Create config.toml
    with open(f"{wrapper_dir}/app/.streamlit/config.toml", 'w') as f:
        f.write('''[theme]
primaryColor = "#4B8BBE"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
''')

def main():
    """Main function to create wrappers for all apps."""
    # Get all app directories
    import subprocess
    result = subprocess.run(['./find_apps.sh'], capture_output=True, text=True, cwd='.')
    app_dirs = result.stdout.strip().split('\n')
    
    print(f"Found {len(app_dirs)} app directories")
    
    for app_dir in app_dirs:
        if app_dir.strip():
            create_wrapper(app_dir.strip())
    
    print("Wrapper creation complete!")

if __name__ == '__main__':
    main()
